api 수정 필요

~~다음은 수정 필요함~~

~~$\hat{{\sigma}}_{\textcolor{#e53935}{n}}^{2} {=} \text{{V}{a}{r}}{(}{R}_{{t}{o}{t}{a}{l}}{)} {=} {\textcolor{#e53935}{n}} {\cdot} \hat{{\sigma}}^{2} {=} {\textcolor{#e53935}{n}} {\cdot} \left\{ {q}{(}{1}{-}{q}{)} \left[ \ln\left(\frac{{u}}{{d}}\right) \right]^{2} \right\}$~~

- 다음은 수정 필요함
  - re_index_builder2.html이 책 한 권을 기준으로 구성되어 있음. (index.json에 책이 두 권있는데 첫번째만 인식하는 문제)
  - 그리고 book id는 수기 변경 필요


# AI Content Factory 🚀

AI를 활용하여 고품질 교육 콘텐츠를 자동으로 생성하고 관리하는 시스템입니다.

## 사용방법
- 목차를 index.json에 추가한다.(ready부터 v3의 user feedback: nul까지(zip파일에 기초 양식 있다)
- 목차뿐 아니라 참고할 원고와 코드를 넘길 수 있다.(00_00_direction.md 등 파일명을 맞춰 source폴더에 두기. 그러면 프롬프트 넘길 때 같이 넘김)
  - **위 과정을 자동화해주는 re_index_builder2.html이 있다.** index.json이 있는 로컬 폴더를 지정하고 작성 시작. 참고할 원고를 선택하면 파일명을 변경해줌
- 작성하고 나면 polishing 절차가 있다. 따로 추가하는 html파일은 assets폴더에 넣고 본문에 링크를 추가하면 된다.
  - 링크 예시) <iframe src="contents/black_scholes_equation_01/sec_01/assets/diagrams/sub_01_01_visual1.html" width="100%" height="450px" frameborder="0" scrolling="no"></iframe>
- 초안이 작성되면 reveiw_arena.html을 통해 수정사항을 전달하고 v3을 만든다.
- v3에 polishing단게를 거치면 final버전이 된다.
- (참고) 목차인 _sidebar.md는 루트(책 제목)와 책 폴더(책 목차)에 각각 위치시킨다.
  - docsify.md에 새로운 책의 링크를 추가

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
index.html 코드에는 메인 화면 문서로 homepage: 'docsify.md를 불러오도록 설정되어 있습니다.
(home.md으로 하면 404에러 발생) 

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
  - `source/`: 초고작성 때 참고할 원고와 코드
  - `assets/`: polishing단계에서 생성하는 interactive한 시각자료(html, svg 등)
