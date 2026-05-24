import os
import sys
import json
import time
import re
from datetime import datetime
from google import genai

# 환경 변수 로드 및 정제
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = 'gemini-3.1-flash-lite'

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
    generate_sidebar(index_data)

def generate_sidebar(index_data):
    """index.json 상태를 기반으로 각 도서별 contents/[book_id]/_sidebar.md 파일을 최상위 루트 경로 기준으로 자동 생성합니다."""
    for book in index_data.get("books", []):
        book_id = sanitize_id(book['book_id'])
        book_dir = os.path.join(CONTENTS_DIR, book_id)
        ensure_dir(book_dir)
        
        sidebar_path = os.path.join(book_dir, "_sidebar.md")
        lines = [f"* [🏠 {book['book_title']}](home.md)", ""]
        
        for section in book.get("sections", []):
            lines.append(f"* **{section['section_title']}**")
            for sub in section.get("sub_sections", []):
                # 최신 파일 경로 찾기
                target_path = None
                if sub.get("final_file_path"):
                    target_path = sub["final_file_path"]
                elif sub.get("history", {}).get("v3", {}).get("file_path"):
                    target_path = sub["history"]["v3"]["file_path"]
                elif sub.get("history", {}).get("v1", {}).get("file_path"):
                    target_path = sub["history"]["v1"]["file_path"]
                
                if target_path:
                    # 404 방지를 위해 사이드바 링크는 책 폴더 기준이 아닌, 전체 루트 경로(contents/[book_id]/...) 형태로 유지합니다.
                    web_path = target_path.replace("\\", "/")
                    lines.append(f"  * [{sub['sub_title']}]({web_path})")
                else:
                    # 파일이 없는 경우 링크 없이 텍스트만 렌더링
                    lines.append(f"  * {sub['sub_title']}")
            lines.append("")
            
        with open(sidebar_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"   [사이드바 갱신] {book['book_title']} (_sidebar.md) 생성 완료.", flush=True)

def load_guidelines():
    if os.path.exists(GUIDELINES_FILE):
        with open(GUIDELINES_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "기본 집필 지침을 따르세요."

def call_gemini_with_retry(client, model_name, contents, max_retries=3):
    """API 호출 실패 시 재시도 및 할당량 관리"""
    for attempt in range(max_retries + 1):
        try:
            print("   [진행] AI에게 원고 작성을 요청했습니다. (약 10~30초 소요, 대기해주세요...)", flush=True)
            response = client.models.generate_content(model=model_name, contents=contents)
            print("   [완료] AI 원고 작성이 완료되었습니다!", flush=True)
            return response
        except Exception as e:
            error_str = str(e).lower()
            if "429" in error_str or "rate limit" in error_str or "resource exhausted" in error_str:
                if attempt < max_retries:
                    wait = 60 * (attempt + 1)
                    print(f"\n[대기] Rate Limit 발생. {wait}초 후 재시도 ({attempt+1}/{max_retries})...")
                    time.sleep(wait)
                    continue
                else:
                    print(f"\n[실패] Rate Limit 최대 재시도 횟수 초과.")
                    raise e
            elif "quota" in error_str or "limit exceeded" in error_str:
                print(f"\n[종료] 할당량 초과. 상태 저장 후 종료합니다.")
                sys.exit(0)
            else:
                if attempt < max_retries:
                    print(f"\n[대기] 오류 발생. 10초 후 재시도 ({attempt+1}/{max_retries}): {e}")
                    time.sleep(10)
                else:
                    print(f"\n[실패] 치명적 오류로 재시도 포기: {e}")
                    raise e

def get_previous_sub_section(section, current_sub_id):
    """동일 섹션 내에서 현재 소목차의 인덱스를 찾아 바로 직전 소목차를 반환"""
    sub_sections = section.get("sub_sections", [])
    for idx, sub in enumerate(sub_sections):
        if sanitize_id(sub['sub_id']) == sanitize_id(current_sub_id):
            if idx > 0:
                return sub_sections[idx - 1]
            break
    return None

def is_task_held(book, section, sub, prev_sub):
    """직전 목차의 집필 상태에 따라 현재 목차의 진행을 홀드(Hold)할지 여부를 판별"""
    if not prev_sub:
        return False
        
    current_status = sub.get("status")
    
    if current_status in ["Ready", "Drafting_V1"]:
        v1_info = prev_sub.get("history", {}).get("v1", {})
        if v1_info.get("status") != "Completed" or not v1_info.get("file_path"):
            return True
            
    elif current_status == "Drafting_V2":
        v2_info = prev_sub.get("history", {}).get("v2", {})
        if v2_info.get("status") != "Completed" or not v2_info.get("file_path"):
            return True
            
    elif current_status == "Review_Pending":
        v3_info = prev_sub.get("history", {}).get("v3", {})
        if v3_info.get("status") != "Completed" or not v3_info.get("file_path"):
            return True
            
    elif current_status == "Polishing":
        if prev_sub.get("status") != "Published" or not prev_sub.get("final_file_path"):
            return True
            
    return False

def get_next_task(index_data, exclude_ids=None):
    if exclude_ids is None: exclude_ids = []
    priority_order = ["Review_Pending", "Drafting_V1", "Drafting_V2", "Polishing", "Ready"]
    
    for status in priority_order:
        for book in index_data.get("books", []):
            for section in book.get("sections", []):
                for sub in section.get("sub_sections", []):
                    sub_id = sanitize_id(sub['sub_id'])
                    if sub_id in exclude_ids:
                        continue
                        
                    if sub.get("status") == status:
                        if status == "Review_Pending" and not sub['history']['v3'].get('user_feedback'):
                            continue
                            
                        prev_sub = get_previous_sub_section(section, sub_id)
                        if is_task_held(book, section, sub, prev_sub):
                            continue
                            
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

def read_prev_file_content(prev_sub, step_key):
    if not prev_sub:
        return ""
    
    file_path = None
    if step_key == "final":
        file_path = prev_sub.get("final_file_path")
    else:
        file_path = prev_sub.get("history", {}).get(step_key, {}).get("file_path")
        
    if file_path:
        return read_file_content(file_path)
    return ""

def load_ipynb_code(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            notebook = json.load(f)
        code_lines = []
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                source = cell.get("source", [])
                if isinstance(source, list):
                    code_lines.append("".join(source))
                else:
                    code_lines.append(source)
        return "\n\n".join(code_lines)
    except Exception as e:
        print(f"   [오류] ipynb 파싱 실패 ({filepath}): {e}", flush=True)
        return ""

def load_manual_inputs(book_id, sub_id):
    book_id_san = sanitize_id(book_id)
    sub_id_san = sanitize_id(sub_id)
    source_dir = os.path.join(CONTENTS_DIR, book_id_san, "source")
    
    direction = ""
    code = ""
    
    txt_path = os.path.join(source_dir, f"{sub_id_san}_direction.txt")
    md_path = os.path.join(source_dir, f"{sub_id_san}_direction.md")
    
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            direction = f.read()
    elif os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            direction = f.read()
            
    py_path = os.path.join(source_dir, f"{sub_id_san}_code.py")
    ipynb_path = os.path.join(source_dir, f"{sub_id_san}_code.ipynb")
    
    if os.path.exists(py_path):
        with open(py_path, "r", encoding="utf-8") as f:
            code = f.read()
    elif os.path.exists(ipynb_path):
        code = load_ipynb_code(ipynb_path)
        
    return direction.strip(), code.strip()

def execute_v1_draft(client, book, section, sub, guidelines):
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v1.md"
    print(f"--- [v1 작성] {sub['sub_title']} ({file_name}) ---")
    
    direction, code = load_manual_inputs(book['book_id'], sub['sub_id'])
    prev_sub = get_previous_sub_section(section, sub['sub_id'])
    prev_v1 = read_prev_file_content(prev_sub, "v1")
    
    prompt = f"[집필 지침]\n{guidelines}\n\n"
    
    if prev_v1:
        prompt += f"[직전 목차 v1 원고 흐름 (참고하여 내용 연결)]\n소제목: {prev_sub['sub_title']}\n\n{prev_v1}\n\n"
        
    prompt += f"[작성 대상]\n도서: {book['book_title']}\n섹션: {section['section_title']}\n소제목: {sub['sub_title']}\n\n"
    
    if direction:
        prompt += f"[수동 세부 작성 방향]\n{direction}\n\n"
    if code:
        prompt += f"[본문에 포함/설명할 파이썬 실습 코드]\n```python\n{code}\n```\n\n"
        
    prompt += "위 정보를 바탕으로 'v1 초안'을 작성하세요."
    if prev_v1:
        prompt += " 특히 직전 목차 원고의 서사 흐름, 논리 전개, 용어 사용을 자연스럽게 이어받아야 합니다."
    
    response = call_gemini_with_retry(client, GEMINI_MODEL, prompt)
    
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
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v2.md"
    print(f"--- [v2 재집필] {sub['sub_title']} ({file_name}) ---")
    
    direction, code = load_manual_inputs(book['book_id'], sub['sub_id'])
    prev_sub = get_previous_sub_section(section, sub['sub_id'])
    prev_v2 = read_prev_file_content(prev_sub, "v2")
    
    prompt = f"[집필 지침]\n{guidelines}\n\n"
    
    if prev_v2:
        prompt += f"[직전 목차 v2 원고 흐름 (참고하여 내용 연결)]\n소제목: {prev_sub['sub_title']}\n\n{prev_v2}\n\n"
        
    prompt += f"[작성 대상]\n소제목: {sub['sub_title']}\n\n"
    
    if direction:
        prompt += f"[수동 세부 작성 방향]\n{direction}\n\n"
    if code:
        prompt += f"[본문에 포함/설명할 파이썬 실습 코드]\n```python\n{code}\n```\n\n"
        
    prompt += "이전에 쓴 v1은 잊고 완전히 새로운 관점에서 v2를 작성하세요."
    if prev_v2:
        prompt += " 특히 직전 목차 원고의 서사 흐름, 논리 전개, 용어 사용을 자연스럽게 이어받아야 합니다."
        
    response = call_gemini_with_retry(client, GEMINI_MODEL, prompt)
    
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
    feedback = sub['history']['v3'].get('user_feedback')
    if not feedback:
        print(f"   [대기] {sub['sub_title']}: 사용자 피드백이 입력될 때까지 대기.")
        return False

    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_v3.md"
    print(f"--- [v3 통합] {sub['sub_title']} ({file_name}) ---")
    
    direction, code = load_manual_inputs(book['book_id'], sub['sub_id'])
    prev_sub = get_previous_sub_section(section, sub['sub_id'])
    prev_v3 = read_prev_file_content(prev_sub, "v3")
    
    v1_content = read_file_content(sub['history']['v1']['file_path'])
    v2_content = read_file_content(sub['history']['v2']['file_path'])
    
    prompt = f"""
    [집필 지침]
    {guidelines}
    """
    
    if prev_v3:
        prompt += f"""
    [직전 목차 v3 원고 흐름 (참고하여 내용 연결)]
    소제목: {prev_sub['sub_title']}
    
    {prev_v3}
        """
        
    prompt += f"""
    [통합 대상]
    소제목: {sub['sub_title']}
    
    [v1 초안]
    {v1_content}
    
    [v2 재집필]
    {v2_content}
    """
    
    if code:
        prompt += f"""
    [통합에 반드시 반영해야 하는 사용자 제공 파이썬 코드]
    ```python
    {code}
    ```
        """
        
    prompt += f"""
    [사용자 피드백]
    {feedback}
    
    위 내용을 바탕으로 v3 통합본을 작성하고, 이번 과정에서 얻은 공통 노하우를 추출하세요.
    """
    
    if prev_v3:
        prompt += "\n특히 직전 목차 v3 원고의 서사 흐름, 논리 전개, 용어 사용을 자연스럽게 이어받아야 합니다."
        
    prompt += """
    응답 형식:
    [CONTENT]
    (통합된 마크다운 본문)
    [/CONTENT]
    
    [TIP]
    (이번 통합을 통해 발견한, 다른 주제에도 적용 가능한 보편적인 집필 노하우 한 문장)
    [/TIP]
    """
    
    response = call_gemini_with_retry(client, GEMINI_MODEL, prompt)
    full_text = response.text
    
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
    """5단계: 시각화(HTML/JS 인터랙티브 위젯 및 정적 SVG 자가 변환 포함) 및 수식 보강 (Polishing) 및 에셋 추출"""
    sub_id = sanitize_id(sub['sub_id'])
    file_name = f"{sub_id}_final.md"
    print(f"--- [Polishing] {sub['sub_title']} ({file_name}) ---")
    
    prev_sub = get_previous_sub_section(section, sub['sub_id'])
    prev_final = read_prev_file_content(prev_sub, "final")
    
    v3_content = read_file_content(sub['history']['v3']['file_path'])
    
    b_id = sanitize_id(book['book_id'])
    s_id = sanitize_id(section['section_id'])
    
    prompt = f"""[집필 지침]
{guidelines}

[직전 목차 최종 완성본 흐름 (참고용)]
소제목: {prev_sub['sub_title'] if prev_sub else '없음'}
{prev_final if prev_final else '없음'}

[대상 원고]
{v3_content}

위 원고를 바탕으로 최종 'Polishing' 작업을 수행하세요.

1. 시각화 보강: 원고에 포함된 [시각화: ...] 등의 마크다운 주석이나 텍스트를 분석하여, 독자가 웹 화면 상에서 직접 클릭하고 조작할 수 있는 완성도 높은 반응형 인터랙티브 웹 위젯(HTML/CSS/JS 단일 파일) 코드를 작성해 주세요.
2. 에셋 추출 규격 (HTML 위젯): 작성된 HTML 위젯 파일은 반드시 다음 형식을 준수하여 별도로 출력해 주세요.
   [ASSET:에셋파일명.html] 
   (<!DOCTYPE html>로 시작하며, 가독성 높은 모던 스타일링 CSS 및 상호작용 가능한 JavaScript가 완벽히 내장된 HTML 웹코드) 
   [/ASSET]
   * 파일명은 '{sub_id}_visual1.html', '{sub_id}_visual2.html'과 같이 유니크하게 작명해 주세요.
   * 필요에 따라 Tailwind CSS 라이브러리나 외부 모던 테마(CDN 링크)를 내부에 포함하여 사용해도 좋습니다.
3. 본문 연결 (HTML 위젯): 마크다운 본문의 시각화 주석 위치에는 이미지가 아닌, 생성한 HTML 파일을 즉시 가져와 보여줄 수 있는 iframe 태그를 다음과 같이 조화롭게 배치해 주세요.
   `<iframe src="contents/{b_id}/{s_id}/assets/diagrams/에셋파일명.html" width="100%" height="450px" frameborder="0" scrolling="no"></iframe>`
   * 주의: 뷰어 상의 404 에러 방지를 위해, iframe의 src 주소는 반드시 'contents/{b_id}/{s_id}/assets/diagrams/'로 시작하는 최상위 루트 기준의 물리 경로를 사용해야 합니다.
4. 다이어그램 및 도식화 (SVG 그래픽): 마크다운 주석 내용 중 단순 흐름도, 순서도, 구조도 등은 XML 형태의 정적 SVG 그래픽 코드로 직접 변환하여 별도로 추출해 주세요.
   [ASSET:다이어그램파일명.svg]
   (<svg ...>로 시작하여 적절한 viewBox, 깔끔한 폰트 및 컬러 스타일을 내장한 완성된 정적 SVG 드로잉 코드)
   [/ASSET]
   * 다이어그램 파일명은 '{sub_id}_diagram1.svg'와 같이 작명해 주세요.
   * 본문에는 마크다운 이미지 링크 형식을 사용하여 연결해 주세요: `![설명](assets/diagrams/다이어그램파일명.svg)`
   * SVG는 브라우저 이미지 태그를 통해 렌더링되므로, 올바른 XML 형식과 xmlns 속성이 선언되어 있어야 합니다.

응답 형식:
[CONTENT]
(최종 보강된 마크다운 본문)
[/CONTENT]
"""

    response = call_gemini_with_retry(client, GEMINI_MODEL, prompt)
    full_text = response.text
    
    # 본문 추출
    content_match = re.search(r'\[CONTENT\](.*?)\[/CONTENT\]', full_text, re.DOTALL)
    final_content = content_match.group(1).strip() if content_match else full_text
    
    # 경로 설정
    section_dir = os.path.join(CONTENTS_DIR, b_id, s_id)
    assets_dir = os.path.join(section_dir, "assets")
    diagrams_dir = os.path.join(assets_dir, "diagrams")
    
    ensure_dir(diagrams_dir)
    
    # 다이어그램 및 HTML 에셋(Mermaid, SVG, HTML) 추출 및 저장
    asset_matches = re.finditer(r'\[ASSET:(.*?)\](.*?)\[/ASSET\]', full_text, re.DOTALL)
    for match in asset_matches:
        a_filename = match.group(1).strip()
        a_content = match.group(2).strip()
        a_path = os.path.join(diagrams_dir, a_filename)
        with open(a_path, "w", encoding="utf-8") as af:
            af.write(a_content)
        print(f"   [에셋 생성] 시각화 에셋 {a_filename} 저장 완료.", flush=True)
    
    # 최종 마크다운 저장
    file_path = os.path.join(section_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    sub['status'] = "Published"
    sub['final_file_path'] = os.path.relpath(file_path, BASE_DIR)
    print(f"   [발행] {sub['sub_title']} 최종본 및 인터랙티브 위젯 연동 완료.", flush=True)
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
            has_unfinished = False
            for b in index_data.get("books", []):
                for s in b.get("sections", []):
                    for sb in s.get("sub_sections", []):
                        if sb.get("status") != "Published":
                            has_unfinished = True
                            break
            if has_unfinished:
                print("더 이상 진행 가능한 작업이 없거나, 이전 목차가 완성될 때까지 대기(Hold) 중입니다. 또는 사용자 피드백을 기다리고 있습니다.", flush=True)
            else:
                print("모든 작업이 완료되었습니다.", flush=True)
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
                print(f"현재 {status} 단계 로직은 개발 중입니다.", flush=True)
                break
                
            save_index(index_data)
            time.sleep(30)

        except Exception as e:
            print(f"오류 발생: {e}", flush=True)
            break

if __name__ == "__main__":
    main()
