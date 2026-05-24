# AI Content Factory 🚀

AI를 활용하여 고품질 교육 콘텐츠를 자동으로 생성하고 관리하는 시스템입니다.

## 사용방법
- 목차를 index.json에 추가한다.(ready부터 v3의 user feedback: nul까지(zip파일에 기초 양식 있다)
- 목차뿐 아니라 참고할 원고와 코드를 넘길 수 있다.(00_00_direction.md 등 파일명을 맞춰 source폴더에 두기)
- 작성하고 나면 polishing 절차가 있지만 따로 assets폴더에 html파일을 넣고 본문에 링크를 추가하면 된다.
- 초안이 작성되면 reveiw_arena.html을 통해 수정사항을 전달하고 v3을 만든다.
- v3에 polishing단게를 거치면 final버전이 된다. 

## 🛠 실행 방법 (uv 사용 권장)

`uv`가 설치되어 있다면 의존성 설치 없이 바로 실행 가능합니다.

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
uv run ai_content_factory/orchestrator.py
```

일반 `pip`를 사용한다면:

```powershell
pip install -r ai_content_factory/requirements.txt
python ai_content_factory/orchestrator.py
```

## 🔄 주요 프로세스
1. **v1 (Drafting_V1)**: 기본 지침을 준수한 초안 생성
2. **v2 (Drafting_V2)**: 제로베이스에서의 새로운 관점 재집필
3. **v3 (Review_Pending)**: v1, v2 및 사용자 피드백 통합본 생성
4. **Polishing**: 시각화 및 수식 보강

## 📂 폴더 구조
- `index.json`: 공정 상태 및 버전 관리
- `orchestrator.py`: 메인 실행 엔진
- `instructions/`: 집필 지침 및 프롬프트 템플릿
- `contents/`: 생성된 마크다운 콘텐츠
  -`source/`: 초고작성 때 참고할 원고와 코드
  -`assets/`: polishing단계에서 생성하는 interactive한 시각자료(html, svg 등)
