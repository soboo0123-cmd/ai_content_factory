import os
import sys
import json
import time
import re
from datetime import datetime
from google import genai

# 환경 변수 로드
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.json")
GUIDELINES_FILE = os.path.join(BASE_DIR, "instructions", "writing_guidelines.md")
CONTENTS_DIR = os.path.join(BASE_DIR, "contents")

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
    """참고자료의 성공 사례를 반영한 안정적인 호출 함수"""
    for attempt in range(max_retries + 1):
        try:
            return client.models.generate_content(model=model_name, contents=contents)
        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "limit exceeded" in error_str:
                print(f"\n[종료] 할당량 초과. 상태 저장 후 종료: {e}")
                sys.exit(0)
            elif "429" in error_str or "rate limit" in error_str:
                if attempt < max_retries:
                    wait = 60 * (attempt + 1)
                    print(f"[대기] Rate Limit. {wait}초 후 재시도...")
                    time.sleep(wait)
                else: raise e
            else:
                if attempt < max_retries:
                    time.sleep(10)
                else: raise e

def get_next_task(index_data):
    """우선순위에 따른 작업 추출: Review_Pending -> In_Progress -> Ready"""
    priority_order = ["Review_Pending", "Drafting_V1", "Drafting_V2", "Integrating_V3", "Ready"]
    
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

def execute_v1_draft(client, book, section, sub, guidelines):
    """1단계: v1 초안 작성"""
    print(f"--- [v1 작성] {sub['sub_title']} ---")
    
    prompt = f"""
    [집필 지침]
    {guidelines}
    
    [작성 대상]
    도서: {book['book_title']}
    섹션: {section['section_title']}
    소제목: {sub['sub_title']}
    
    위 정보를 바탕으로 'v1 초안'을 작성하세요. 
    가이드라인의 도입-본론-요약 구조를 지키고, 상세하고 친절하게 서술하세요.
    나중에 시각화할 요소는 [시각화: ...] 주석으로 포함하세요.
    응답은 마크다운 본문만 출력하세요.
    """
    
    response = call_gemini_with_retry(client, "gemini-2.0-flash", prompt)
    content = response.text
    
    # 파일 저장
    target_dir = os.path.join(CONTENTS_DIR, book['book_id'], section['section_id'])
    ensure_dir(target_dir)
    file_name = f"{sub['sub_id']}_v1.md"
    file_path = os.path.join(target_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # 상태 업데이트
    sub['status'] = "Drafting_V2" # v1 완료 후 다음 단계로
    sub['current_version_code'] = "v1"
    sub['history']['v1'] = {
        "status": "Completed",
        "file_path": os.path.relpath(file_path, BASE_DIR),
        "created_at": datetime.now().isoformat()
    }
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
            current_status = sub['status']
            
            if current_status == "Ready" or current_status == "Drafting_V1":
                execute_v1_draft(client, book, section, sub, guidelines)
                save_index(index_data) # 매 단계 성공 시 즉시 저장 (Atomic)
                time.sleep(10) # 속도 조절
            
            # TODO: Drafting_V2, Review_Pending, Integrating_V3 로직 추가 예정
            else:
                print(f"현재 {current_status} 단계 로직은 개발 중입니다. 다음 항목으로...")
                break # 루프 방지용 (개발 중)

        except Exception as e:
            print(f"작업 중 오류 발생 ({sub['sub_title']}): {e}")
            break

if __name__ == "__main__":
    main()
