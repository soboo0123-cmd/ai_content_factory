import os
import sys
import json
import time
import re
from datetime import datetime
from google import genai

# 환경 변수 로드 및 정제 (눈에 보이지 않는 탭/공백 제거)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.json")
GUIDELINES_FILE = os.path.join(BASE_DIR, "instructions", "writing_guidelines.md")
CONTENTS_DIR = os.path.join(BASE_DIR, "contents")

def sanitize_id(text):
    """ID 값에서 공백, 탭, 특수문자 제거하여 안전한 파일명/경로 생성"""
    return re.sub(r'[\s\t\n\r]', '', str(text))

def load_index():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_index(index_data):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

def load_guidelines():
    if os.path.exists(GUIDELINES_FILE):
        with open(GUIDELINES_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "기본 집필 지침을 따르세요."

def call_gemini_with_retry(client, model_name, contents, max_retries=3):
    """API 호출 실패 시 재시도 및 할당량 관리"""
    for attempt in range(max_retries + 1):
        try:
            return client.models.generate_content(model=model_name, contents=contents)
        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "limit exceeded" in error_str:
                print(f"\n[종료] 할당량 초과. 상태 저장 후 종료합니다.")
                sys.exit(0)
            elif "429" in error_str or "rate limit" in error_str:
                if attempt < max_retries:
                    wait = 60 * (attempt + 1)
                    print(f"[대기] Rate Limit 발생. {wait}초 후 재시도 ({attempt+1}/{max_retries})...")
                    time.sleep(wait)
                else: raise e
            else:
                if attempt < max_retries:
                    time.sleep(10)
                else: raise e

def get_next_task(index_data):
    """우선순위: Review_Pending -> Drafting_V1 -> Drafting_V2 -> Integrating_V3 -> Polishing -> Ready"""
    priority_order = ["Review_Pending", "Drafting_V1", "Drafting_V2", "Integrating_V3", "Polishing", "Ready"]
    
    for status in priority_order:
        for book in index_data.get("books", []):
            for section in book.get("sections", []):
                for sub in section.get("sub_sections", []):
                    if sub.get("status") == status:
                        return book, section, sub
    return None, None, None

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_file_content(relative_path):
    full_path = os.path.join(BASE_DIR, relative_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def execute_v1_draft(client, book, section, sub, guidelines):
    """1단계: v1 초안 작성"""
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v1.md"
    print(f"--- [v1 작성] {sub['sub_title']} ({file_name}) ---")
    
    prompt = f"[집필 지침]\n{guidelines}\n\n[작성 대상]\n도서: {book['book_title']}\n섹션: {section['section_title']}\n소제목: {sub['sub_title']}\n\n위 정보를 바탕으로 'v1 초안'을 작성하세요."
    
    response = call_gemini_with_retry(client, "gemini-2.0-flash", prompt)
    
    target_dir = os.path.join(CONTENTS_DIR, sanitize_id(book['book_id']), sanitize_id(section['section_id']))
    ensure_dir(target_dir)
    file_path = os.path.join(target_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    sub['status'] = "Drafting_V2"
    sub['current_version_code'] = "v1"
    sub['history']['v1'] = {
        "status": "Completed",
        "file_path": os.path.relpath(file_path, BASE_DIR),
        "created_at": datetime.now().isoformat()
    }
    return True

def execute_v2_zerobase(client, book, section, sub, guidelines):
    """2단계: v2 재집필 (Zero-base)"""
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v2.md"
    print(f"--- [v2 재집필] {sub['sub_title']} ({file_name}) ---")
    
    prompt = f"[집필 지침]\n{guidelines}\n\n[작성 대상]\n소제목: {sub['sub_title']}\n\n이전에 쓴 v1은 잊고 완전히 새로운 관점에서 v2를 작성하세요."
    
    response = call_gemini_with_retry(client, "gemini-2.0-flash", prompt)
    
    target_dir = os.path.join(CONTENTS_DIR, sanitize_id(book['book_id']), sanitize_id(section['section_id']))
    ensure_dir(target_dir)
    file_path = os.path.join(target_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    sub['status'] = "Review_Pending"
    sub['current_version_code'] = "v2"
    sub['history']['v2'] = {
        "status": "Completed",
        "file_path": os.path.relpath(file_path, BASE_DIR),
        "created_at": datetime.now().isoformat()
    }
    return True

def update_guidelines(tip):
    """새로운 집필 노하우를 writing_guidelines.md에 추가"""
    header = "\n\n## 6. 누적된 집필 노하우 (자동 업데이트)\n"
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"- [{date_str}] {tip}\n"
    
    content = ""
    if os.path.exists(GUIDELINES_FILE):
        with open(GUIDELINES_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    
    if "## 6. 누적된 집필 노하우" not in content:
        content += header
    
    content += new_entry
    
    with open(GUIDELINES_FILE, "w", encoding="utf-8") as f:
        f.write(content)

def execute_v3_integration(client, book, section, sub, guidelines):
    """3단계: v3 통합본 작성 및 지침 자가 추출"""
    feedback = sub['history']['v3'].get('user_feedback')
    if not feedback:
        print(f"   [대기] {sub['sub_title']}: 사용자 피드백이 입력될 때까지 대기.")
        return False

    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v3.md"
    print(f"--- [v3 통합] {sub['sub_title']} ({file_name}) ---")
    
    v1_content = read_file_content(sub['history']['v1']['file_path'])
    v2_content = read_file_content(sub['history']['v2']['file_path'])
    
    prompt = f"""
    [집필 지침]
    {guidelines}
    
    [통합 대상]
    소제목: {sub['sub_title']}
    
    [v1 초안]
    {v1_content}
    
    [v2 재집필]
    {v2_content}
    
    [사용자 피드백]
    {feedback}
    
    위 내용을 바탕으로 v3 통합본을 작성하고, 이번 과정에서 얻은 공통 노하우를 추출하세요.
    
    응답 형식:
    [CONTENT]
    (통합된 마크다운 본문)
    [/CONTENT]
    
    [TIP]
    (이번 통합을 통해 발견한, 다른 주제에도 적용 가능한 보편적인 집필 노하우 한 문장)
    [/TIP]
    """
    
    response = call_gemini_with_retry(client, "gemini-2.0-flash", prompt)
    full_text = response.text
    
    # 본문과 팁 추출
    content_match = re.search(r'\[CONTENT\](.*?)\[/CONTENT\]', full_text, re.DOTALL)
    tip_match = re.search(r'\[TIP\](.*?)\[/TIP\]', full_text, re.DOTALL)
    
    final_content = content_match.group(1).strip() if content_match else full_text
    tip = tip_match.group(1).strip() if tip_match else None
    
    target_dir = os.path.join(CONTENTS_DIR, sanitize_id(book['book_id']), sanitize_id(section['section_id']))
    file_path = os.path.join(target_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    if tip:
        update_guidelines(tip)
        print(f"   [학습] 새로운 노하우 반영: {tip}")
        
    sub['status'] = "Polishing"
    sub['current_version_code'] = "v3"
    sub['history']['v3']['status'] = "Completed"
    sub['history']['v3']['file_path'] = os.path.relpath(file_path, BASE_DIR)
    sub['history']['v3']['created_at'] = datetime.now().isoformat()
    return True

def execute_polishing(client, book, section, sub, guidelines):
    """5단계: 시각화 및 수식 보강 (Polishing) 및 에셋 추출"""
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_final.md"
    print(f"--- [Polishing] {sub['sub_title']} ({file_name}) ---")
    
    v3_content = read_file_content(sub['history']['v3']['file_path'])
    
    prompt = f"""
    [집필 지침]
    {guidelines}
    
    [대상 원고]
    {v3_content}
    
    위 원고를 바탕으로 최종 'Polishing' 작업을 수행하세요.
    
    1. 시각화 보강: [시각화: ...] 주석을 상세한 Mermaid 다이어그램이나 SVG로 변환하세요.
    2. 에셋 분리: 다이어그램이나 복잡한 도식은 반드시 아래 태그 형식을 사용하여 별도로 출력하세요.
       [ASSET:파일명.mmd] (Mermaid 코드) [/ASSET] 또는 [ASSET:파일명.svg] (SVG 코드) [/ASSET]
    3. 본문 연결: 본문에는 해당 에셋을 불러오는 마크다운 링크를 넣으세요. 예: ![설명](assets/diagrams/파일명.mmd)
    
    응답 형식:
    [CONTENT]
    (최종 마크다운 본문)
    [/CONTENT]
    """
    
    response = call_gemini_with_retry(client, "gemini-2.0-flash", prompt)
    full_text = response.text
    
    # 본문 추출
    content_match = re.search(r'\[CONTENT\](.*?)\[/CONTENT\]', full_text, re.DOTALL)
    final_content = content_match.group(1).strip() if content_match else full_text
    
    # 경로 설정
    b_id = sanitize_id(book['book_id'])
    s_id = sanitize_id(section['section_id'])
    section_dir = os.path.join(CONTENTS_DIR, b_id, s_id)
    assets_dir = os.path.join(section_dir, "assets", "diagrams")
    ensure_dir(assets_dir)
    
    # 에셋 추출 및 저장
    asset_matches = re.finditer(r'\[ASSET:(.*?)\](.*?)\[/ASSET\]', full_text, re.DOTALL)
    for match in asset_matches:
        a_filename = match.group(1).strip()
        a_content = match.group(2).strip()
        a_path = os.path.join(assets_dir, a_filename)
        with open(a_path, "w", encoding="utf-8") as af:
            af.write(a_content)
        print(f"   [에셋 생성] {a_filename} 저장 완료.")
    
    # 최종 마크다운 저장
    file_path = os.path.join(section_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    sub['status'] = "Published"
    sub['final_file_path'] = os.path.relpath(file_path, BASE_DIR)
    print(f"   [발행] {sub['sub_title']} 최종본 및 에셋 생성 완료.")
    return True

def main():
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY가 설정되지 않았습니다.")
        return

    client = genai.Client(api_key=GEMINI_API_KEY)
    index_data = load_index()
    guidelines = load_guidelines()
    
    while True:
        book, section, sub = get_next_task(index_data)
        if not sub:
            print("모든 작업이 완료되었습니다.")
            break
            
        try:
            status = sub['status']
            if status in ["Ready", "Drafting_V1"]:
                execute_v1_draft(client, book, section, sub, guidelines)
            elif status == "Drafting_V2":
                execute_v2_zerobase(client, book, section, sub, guidelines)
            elif status == "Review_Pending":
                if not execute_v3_integration(client, book, section, sub, guidelines):
                    break
            elif status == "Polishing":
                execute_polishing(client, book, section, sub, guidelines)
            else:
                print(f"현재 {status} 단계 로직은 개발 중입니다.")
                break
                
            save_index(index_data)
            time.sleep(5)

        except Exception as e:
            print(f"오류 발생: {e}")
            break

if __name__ == "__main__":
    main()
