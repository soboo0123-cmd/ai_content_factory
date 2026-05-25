[CONTENT]
# 1.16 옵션 가격 책정(Pricing)의 본질과 문제 제기: 미래를 오늘로 가져오는 수학

## 1. 도입: 만기일이라는 '확신'에서 오늘이라는 '안개'로

지난 1.15절에서 우리는 옵션이라는 파생상품이 만기일($T$)에 도달했을 때 보여주는 '비대칭적 가치의 마법'을 수학적으로 확인했습니다. 기초자산의 가격이 아무리 하락하더라도 손실은 오직 매수할 때 지불한 프리미엄으로 한정하여 $0$원 밑으로 떨어지지 않게 묶고, 반대로 주가가 오르는 만큼 이익을 무제한으로 열어두는 우아한 수식인 콜옵션 만기 페이오프 $C_T = \max(S_T - K, 0)$를 설계했습니다. 그리고 이 설계도가 위험중립평가 엔진의 심장부에 주입될 핵심 연료라는 사실도 배웠습니다.

하지만 여기에서 금융공학 역사상 가장 정교하고 뜨거운 질문이 싹틉니다. **"만약 오늘이 만기일이 아니라면 어떨까요?"**

만기일 당일에는 주가 $S_T$가 우리 눈앞에 완전히 확정되어 있으므로, 옵션의 실질적 가치를 계산하는 것은 초등학생도 할 수 있을 만큼 직관적이고 간단합니다. 그러나 만기까지 3달, 혹은 1년이라는 긴 시간이 남아있고, 당장 내일 주가가 오를지 내릴지조차 알 수 없는 **'오늘($t$)'** 시점에서 우리는 이 비대칭적인 권리 증서에 정확히 얼마의 가격표를 붙여야 할까요?

단순히 "앞으로 오를 것 같으니 대충 비싸게 판다"는 식의 주관적인 감정이나 직관은 시장에서 통용될 수 없습니다. 시장 참여자 모두가 이성적이고 합리적으로 납득할 수 있는 '공정 가치(Fair Value)'를 정의하고, 보이지 않는 미래의 가치 흐름을 오늘날의 단 하나의 숫자로 정밀하게 당겨오는 과정—이것이 바로 **옵션 가격 책정(Option Pricing)**의 본질적인 원리이자 금융공학이 해결해야 할 궁극적인 과제입니다.

이 장에서는 시간과 변동성이 어떻게 만기 이전 옵션의 몸값을 구성하는지 패턴을 통해 살펴보고, 불확실성이라는 안개 속에서 오늘날의 가치를 도출해 내는 수학적 이정표를 하나씩 정밀하게 짚어보겠습니다.

---

## 2. 본론

### 2.1 만기 이전의 가치: 시간과 변동성이 만드는 패턴

만기 시점의 페이오프 공식인 $\max(S_T - K, 0)$는 만기 당일의 주가($S_T$)와 사전에 약정된 행사가격($K$) 두 가지만으로 결정되는 2차원적인 수식입니다. 그러나 만기 이전인 오늘($t$) 옵션의 가치는 단순히 오늘 주가($S_t$)와 행사가격($K$)의 차이만으로 설명되지 않습니다. 아직 만기까지 시간이 남아있다는 사실 그 자체가 옵션에 독특한 추가 가치를 부여하기 때문입니다.

이해를 돕기 위해, 행사가격 $K = 1,000$원인 콜옵션의 '만기 이전 실제 거래 가격'이 현재 주가 수준에 따라 어떻게 형성되는지 구체적인 수치 패턴을 귀납적으로 나열해 보겠습니다.

#### [표 1] 만기를 3개월 앞둔 콜옵션($K=1,000$)의 시장 가격 패턴 (예시)

| 현재 주가 ($S_t$) | 800원 | 900원 | 1,000원 | 1,100원 | 1,200원 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **(A) 즉시 행사 가치 (내재 가치)**<br>$\max(S_t - K, 0)$ | 0원 | 0원 | 0원 | 100원 | 200원 |
| **(B) 실제 옵션 가격 (시장 가치)** | **15원** | **45원** | **95원** | **165원** | **250원** |
| **(B - A) 시간 가치 (시간 프리미엄)** | **15원** | **45원** | **95원** | **65원** | **50원** |

이 표를 세밀하게 뜯어보면 대단히 흥미롭고 일관된 세 가지 패턴이 발견됩니다.

1. **외가격(OTM) 영역에서의 시간 가치**: 현재 주가가 행사가격보다 훨씬 낮은 $800$원일 때, 당장 권리를 행사하면 가치는 당연히 $0$원입니다. 하지만 시장에서 이 옵션은 **15원**이라는 가치를 인정받아 거래됩니다. 만기까지 남은 3개월 동안 주가가 1,000원을 돌파하여 가치가 살아날 '일말의 가능성(확률적 기대감)'이 존재하기 때문입니다.
2. **등가격(ATM) 영역에서 극대화되는 시간 가치**: 현재 주가가 정확히 행사가격인 $1,000$원일 때, 즉시 행사 가치는 여전히 $0$원입니다. 그러나 실제 옵션 가격은 무려 **95원**에 달하며, 이 시점에서 시간 가치는 최대치를 기록합니다. 향후 주가가 위로 튈지 아래로 튈지 모르는 방향성의 불확실성이 극대화되는 경계점이기 때문에, 상승 시의 무제한 이익 가능성을 품은 이 권리의 몸값이 가장 매력적으로 평가받는 것입니다.
3. **내가격(ITM) 영역에서의 시간 가치**: 주가가 $1,200$원으로 크게 오르면 당장 권리를 행사해 수취할 수 있는 내재 가치만 해도 $200$원입니다. 하지만 실제 옵션 가격은 그보다 50원 더 비싼 **250원**입니다. 이미 이익 구간에 깊이 들어와 있어 안전마진을 확보한 상태이지만, 남은 기간 주가가 한층 더 상승할 여지가 열려 있기 때문입니다.

결국 만기 이전의 옵션 가치는 아래 그림과 같이 철저하게 두 가지 차원의 결합으로 구성됩니다.

![옵션 가치의 구조: 내재 가치와 시간 가치의 유기적 결합](assets/diagrams/sub_01_16_diagram1.svg)

* **내재 가치(Intrinsic Value)**: 현재 시점에서 옵션을 즉시 행사한다고 가정했을 때 얻을 수 있는 물리적인 가치로, 오직 기초자산 가격($S_t$)과 행사가격($K$)의 차이로만 결정됩니다.
* **시간 가치(Time Value)**: 만기일 전까지 자산 가격이 옵션 매수자에게 보다 유리한 방향으로 변동하여 발생할 수 있는 추가적인 기대수익의 가치입니다. 이 시간 가치를 결정짓는 양대 핵심 변수가 바로 **만기까지의 잔존 기간($T-t$)**과 자산 가격의 춤폭을 결정하는 **변동성($\sigma$)**입니다.

---

### 2.2 가격 결정의 대원칙: 할인된 위험중립 기댓값

우리가 앞서 확립한 위험중립평가법(Risk-Neutral Valuation)의 패러다임은 이 복잡한 불확실성을 단 하나의 일관된 수학적 질서 속으로 융합해 줍니다. 미래 만기 시점($T$)에 얻게 될 비선형적 페이오프의 수학적 기댓값을 구하되, 주관적인 기대수익률이 아닌 객관적인 '위험중립 확률 $Q$'를 사용하여 산출한 뒤, 이를 무위험 이자율 $r$을 적용해 현재 가치로 귀환(할인)시키는 것입니다.

이를 콜옵션의 현재 가격($C_t$)을 구하는 수식으로 선언하면 다음과 같습니다.

$$C_t = \text{할인계수} \times \mathbb{E}^Q [ \text{만기 시점 콜옵션 페이오프} ]$$

$$C_t = e^{-r(T-t)} \mathbb{E}^Q [ \max(S_T - K, 0) ]$$

* **$\mathbb{E}^Q [ \cdot ]$**: 위험중립 세계(Risk-neutral World) 하에서 계산한 만기 페이오프의 기댓값입니다.
* **$e^{-r(T-t)}$**: 만기 시점($T$)의 통화 가치를 오늘 시점($t$)의 현재 가치로 변환해 주는 **연속복리 할인계수(Continuous Discount Factor)**입니다.

아래의 실시간 인터랙티브 시뮬레이터를 통해 시간의 흐름이 옵션 가격에 미치는 가혹한 영향력을 직접 체험해 보십시오. 만기 잔존 기간($T-t$) 슬라이더를 왼쪽으로 당겨 만기가 임박해올수록, 곡선 형태를 그리던 부드러운 오늘날의 옵션 가치 그래프가 시간 가치를 모두 소실하고 결국 V자 형태의 뾰족한 '만기 페이오프 꺾인 선'으로 완전히 밀착하는 **시간 가치 잠식(Time Decay)** 현상을 직관적으로 관찰할 수 있습니다.

<iframe src="contents/black_scholes_equation_01/sec_01/assets/diagrams/sub_01_16_visual1.html" width="100%" height="520px" frameborder="0" scrolling="no"></iframe>

---

### 2.3 [수학적 깊이 더하기] 왜 $e^{-r(T-t)}$가 할인계수가 되는가?

우리는 일상적인 은행 거래나 고전적인 경제학 문제를 풀 때 이산적인(Discrete) 단리 혹은 복리 할인 계산법을 자주 사용합니다. 예를 들어 1년 뒤에 받게 될 $1$원을 연 이자율 $r$로 매년 한 번씩 복리 할인하면 현재 가치는 $\frac{1}{1+r}$이 됩니다. 

만약 1년 동안 이자를 단순히 한 번에 지급하지 않고, 이자 지급 주기를 1년에 $m$번으로 더 쪼개어 지급하는 복리(Compounding) 계약을 맺었다면, $t$년 뒤의 $1$원을 오늘 시점으로 끌어당긴 현재 가치는 다음과 같이 정의됩니다.

$$\text{현재 가치} = \frac{1}{\left(1 + \frac{r}{m}\right)^{m \cdot t}} = \left(1 + \frac{r}{m}\right)^{-m \cdot t}$$

여기서 금융공학자들은 수학적인 완결성과 현실 모사를 위해 극단적인 질문을 던졌습니다. **"만약 이자를 나누어 지급하는 횟수인 $m$을 무한대($\infty$)로 극한 청구한다면 어떻게 될까? 즉 매 분, 매 초, 눈 깜짝할 찰나의 순간에도 이자가 연속적으로 미세하게 굴러가는 '연속복리(Continuous Compounding)'를 적용한다면 이 할인식은 어떻게 수렴할 것인가?"**

이 질문을 정식화하기 위해 식의 이자 지급 횟수 $m$을 무한대로 보내는 극한 연산을 수행해 보겠습니다. 계산의 편의를 위해 $n = \frac{m}{r}$이라고 치환하면, $m = n \cdot r$이 성립하며 $m \to \infty$ 일 때 $n \to \infty$가 됩니다. 이를 대입해 식을 재정리해 봅니다.

$$\lim_{m \to \infty} \left(1 + \frac{r}{m}\right)^{-m \cdot t} = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{-n \cdot r \cdot t} = \left[ \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \right]^{-rt}$$

이때 대괄호 안을 가만히 살펴보면, 고등학교 미적분학에서 배우는 자연상수(Euler's Number) $e$의 엄밀한 정의식과 완벽하게 일치함을 발견할 수 있습니다.

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2.71828$$

따라서 이 복리 할인식의 극한값은 다음과 같이 극도로 단순하고 아름다운 지수함수 형태로 수렴하게 됩니다.

$$\lim_{m \to \infty} \left(1 + \frac{r}{m}\right)^{-m \cdot t} = e^{-rt}$$

우리가 다루는 금융 옵션 계약에서 오늘 시점을 $t$, 만기 시점을 $T$라고 정의하면, 만기까지 남아있는 실질적 잔존 기간은 $(T-t)$가 됩니다. 따라서 미래의 만기 가치를 오늘날의 가치 저울 위로 복원시키는 연속복리 할인계수는 필연적으로 **$e^{-r(T-t)}$**가 되는 것입니다.

#### 왜 금융공학에서는 일반 복리를 버리고 '연속복리'를 지향할까?

일반 시중은행의 상품들이 직관적인 연 복리나 월 복리를 사용함에도 불구하고, 현대 금융공학의 복잡한 방정식들이 하나같이 연속복리 구조를 기본 뼈대로 채택한 데에는 타당한 수학적 및 실무적 이유가 뒷받침되어 있습니다.

1. **수학적 미분의 독보적 우아함**: 일반적인 이산 복리 할인식인 $(1+r)^{-t}$을 시간에 대해 미분하면 지저분한 로그 항($\ln$)들이 번잡하게 튀어나와 수식을 극도로 왜곡시킵니다. 반면 자연지수함수인 $e^{-rt}$는 시간 $t$에 대해 미분을 가하더라도 자기 자신의 형태를 고스란히 보존하며 오직 상수 $-r$만을 앞으로 뱉어냅니다($\frac{d}{dt} e^{-rt} = -r e^{-rt}$). 이 간결한 성질 덕분에 향후 우리가 풀어내야 할 편미분방정식의 해법이 상상을 초월할 정도로 단순해집니다.
2. **현대 금융시장의 시간적 연속성**: 실제 현대 금융시장의 가격 변동과 차익 거래 기회는 하루 혹은 한 달 단위로 불연속하게 끊겨서 작동하지 않습니다. 컴퓨터 알고리즘과 초단타 매매(HFT)를 통해 자금은 매 밀리초(ms) 단위로 끊임없이 이동하고 가치가 평가됩니다. 이 연속적인 흐름을 빈틈없이 묘사하고 차익 거래가 원천적으로 불가능한 '무차익 정합성'을 확보하기 위해서는 연속복리 구조가 논리적으로 완벽한 완결성을 갖춘 확률계(Probability System)를 제공하게 됩니다.

---

### 2.4 문제 제기: 무한한 미래 경로라는 장벽

우리가 앞서 연속복리 할인계수 $e^{-r(T-t)}$를 아주 깔끔하게 유도해 냈고 가격 책정의 기본 뼈대를 수립했음에도 불구하고, 여전히 거대하고 거친 수학적 장벽이 우리 앞을 가로막고 있습니다. 바로 기댓값 기호 내부에 도사리고 있는 **$S_T$(만기 주가)의 제어하기 힘든 확률적 무작위성**입니다.

오늘 시점 $t$로부터 먼 미래인 만기일 $T$까지 기초자산의 가격이 움직여갈 수 있는 궤적(Trajectory)은 이론상 무한히 존재합니다.

* 매일 눈에 보이지 않을 만큼 미세하게 연속 우상향하여 만기에 부드럽게 도달하는 경로
* 숨이 막힐 듯한 극심한 롤러코스터 장세를 반복하다가 결국 오늘 가격 부근으로 회귀하는 경로
* 감당할 수 없는 파멸적 악재를 만나 일직선으로 대폭락을 겪으며 최종적으로 $0$원에 달라붙는 경로

이처럼 사방으로 뻗어 나가는 무수히 많은 미래 주가 경로들의 끝에는, 각기 다른 만기 주가 $S_T$가 기다리고 있으며, 그에 대응하는 옵션의 페이오프 또한 천차만별로 벌어집니다. 아래의 몬테카를로 시뮬레이션 위젯을 실행하여, 현재 주가에서 뻗어 나가는 수많은 주가 경로와 만기 시점에 형성되는 페이오프 분포의 복잡성을 직접 눈으로 확인해 보십시오.

<iframe src="contents/black_scholes_equation_01/sec_01/assets/diagrams/sub_01_16_visual2.html" width="100%" height="520px" frameborder="0" scrolling="no"></iframe>

우리가 오늘 콜옵션의 공정 가치 $C_t = e^{-r(T-t)} \mathbb{E}^Q [ \max(S_T - K, 0) ]$를 단 하나의 완벽한 정답으로 계산해 내기 위해서는, 위 시뮬레이션에서 펼쳐진 무수히 많은 만기 주가들의 확률적 분포 지도를 수학적으로 단 한 치의 오차도 없이 그려내고 완벽히 제어할 수 있어야 합니다.

* 주가는 과연 어떤 확률분포의 통제 하에 움직이는가? (주가는 마이너스가 될 수 없다는 물리적 한계가 존재하므로, 단순 좌우대칭의 정규분포를 그대로 적용할 수는 없습니다.)
* 자산의 춤폭을 뜻하는 변동성($\sigma$)은 시간이 흘러 만기에 도달하는 내내 일정한 상수로 유지되는가?
* 시장의 대원칙인 무차익 거래(No-Arbitrage) 논리를 깨뜨리지 않으면서, 이 복잡한 미래 경로 전체를 깔끔한 하나의 격자망(Lattice)이나 미분방정식의 틀 안에 가두어 단 하나의 현재 가격으로 벼려낼 수 있는가?

이것이 바로 피셔 블랙(Fischer Black), 마이런 숄즈(Myron Scholes), 로버트 머턴(Robert Merton)을 비롯하여 현대 금융공학의 기틀을 닦은 위대한 천재들이 평생을 바쳐 매달렸던 궁극적인 숙제였습니다.

---

## 3. 요약

* **시간 가치의 본질**: 만기 이전의 옵션 가격은 당장 권리를 행사했을 때 챙길 수 있는 '내재 가치'에, 미래에 주가가 더 유리하게 변해줄 가능성의 몸값인 '시간 가치'가 유기적으로 덧붙여져 결정됩니다.
* **연속복리 할인의 필연성**: 금융공학에서 미래의 기댓값을 오늘날의 가치로 되돌려놓는 할인계수 $e^{-r(T-t)}$는 이산 복리 할인의 주기를 무한대($m \to \infty$)로 극한 청구하는 과정에서 자연스럽게 유도되는 수학적 결정체입니다. 이는 미분 연산의 편의성과 초 단위로 움직이는 현대 시장의 연속성을 대변합니다.
* **풀어야 할 숙제**: 옵션의 공정한 가격을 완성하기 위해서는 할인계수 뒤에 곱해진 무작위 기댓값 $\mathbb{E}^Q [\max(S_T - K, 0)]$을 명확하게 풀어내야 하며, 이를 위해서는 한 치 앞을 내다볼 수 없는 주가의 무한한 미래 변동 경로를 완벽하게 정형화할 구체적인 모델링 프레임워크가 절실히 요구됩니다.

---
*우리는 이제 미래의 불확실성을 오늘날의 단일 가치로 환산해 줄 완벽한 '마법의 저울(할인계수)'과 계산해야 할 '기댓값의 수학적 골격'을 모두 갖추었습니다. 다음 장부터는 주가의 갈가리 찢어지는 미래 경로를 통제 가능한 단순한 영역으로 끌어내리기 위해, 주가가 단 두 방향(상승과 하락)으로만 계단식으로 움직인다고 가정하는 직관적이면서도 대단히 강력한 도구인 **'이항 트리 가격결정 모형(Binomial Tree Model)'**의 수학적 모험을 함께 시작해 보겠습니다.*

---

[ASSET:sub_01_16_diagram1.svg]
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" width="100%" height="100%">
  <!-- Background -->
  <rect width="600" height="320" fill="#0f172a" rx="12" />
  
  <!-- Outer Box: Option Value -->
  <rect x="30" y="30" width="540" height="260" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4" rx="8" />
  <text x="300" y="24" fill="#38bdf8" font-family="'Inter', system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">만기 이전의 총 옵션 가치 (Option Market Value)</text>

  <!-- Left Box: Intrinsic Value -->
  <rect x="50" y="70" width="230" height="180" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="8" />
  <text x="165" y="100" fill="#f43f5e" font-family="'Inter', system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">내재 가치 (Intrinsic Value)</text>
  <text x="165" y="130" fill="#94a3b8" font-family="'Inter', system-ui, sans-serif" font-size="12" text-anchor="middle">즉시 권리를 행사할 때의 가치</text>
  <rect x="70" y="155" width="190" height="40" fill="#2d1520" rx="6" />
  <text x="165" y="180" fill="#fda4af" font-family="'Consolas', 'Courier New', monospace" font-size="14" font-weight="bold" text-anchor="middle">max(S_t - K, 0)</text>
  <text x="165" y="225" fill="#64748b" font-family="'Inter', system-ui, sans-serif" font-size="11" text-anchor="middle">변수: 현재 주가(S_t), 행사가격(K)</text>

  <!-- Plus Sign -->
  <circle cx="300" cy="160" r="18" fill="#334155" />
  <text x="300" y="166" fill="#f8fafc" font-family="'Inter', system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">+</text>

  <!-- Right Box: Time Value -->
  <rect x="320" y="70" width="230" height="180" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8" />
  <text x="435" y="100" fill="#10b981" font-family="'Inter', system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">시간 가치 (Time Value)</text>
  <text x="435" y="130" fill="#94a3b8" font-family="'Inter', system-ui, sans-serif" font-size="12" text-anchor="middle">미래 가치 상승에 대한 기대감</text>
  <rect x="340" y="155" width="190" height="40" fill="#062f22" rx="6" />
  <text x="435" y="180" fill="#6ee7b7" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">시간 프리미엄 (Time Premium)</text>
  <text x="435" y="225" fill="#64748b" font-family="'Inter', system-ui, sans-serif" font-size="11" text-anchor="middle">변수: 잔존기간(T-t), 변동성(σ)</text>
</svg>
[/ASSET]

---

[ASSET:sub_01_16_visual1.html]
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Time Decay & Option Value Curves</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {
      background-color: #0f172a;
      color: #f8fafc;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    input[type="range"] {
      accent-color: #38bdf8;
    }
  </style>
</head>
<body class="p-4 flex flex-col items-center justify-center min-h-[500px]">

  <div class="w-full max-w-4xl bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-2xl">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 border-b border-slate-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-sky-400">옵션의 시간 가치 소멸 (Time Decay) 시뮬레이터</h2>
        <p class="text-xs text-slate-400">만기 잔존 기간이 줄어듦에 따라 실제 옵션 가치가 만기 페이오프(꺾인 선)에 완벽하게 수렴하는 양상을 관찰하세요.</p>
      </div>
      <div class="mt-2 md:mt-0 bg-slate-950 px-3 py-1.5 rounded-lg border border-slate-800 text-xs text-slate-300">
        모델: 블랙-숄즈 콜옵션 식 기준
      </div>
    </div>

    <!-- Main Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <!-- Left: Interactive Controls -->
      <div class="space-y-4 bg-slate-950 p-4 rounded-lg border border-slate-800 flex flex-col justify-center">
        <div>
          <div class="flex justify-between text-xs font-semibold mb-1">
            <span>만기 잔존 기간 (<span class="italic">T - t</span>)</span>
            <span class="text-sky-400 font-bold" id="val-time">0.50 년</span>
          </div>
          <input id="slider-time" type="range" min="0.001" max="1.0" step="0.01" value="0.5" class="w-full bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-500 mt-1">
            <span>0 (만기 당일)</span>
            <span>1년 (장기)</span>
          </div>
        </div>

        <div>
          <div class="flex justify-between text-xs font-semibold mb-1">
            <span>행사 가격 (<span class="italic">K</span>)</span>
            <span class="text-rose-400 font-bold" id="val-strike">1,000 원</span>
          </div>
          <input id="slider-strike" type="range" min="800" max="1200" step="10" value="1000" class="w-full bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-500 mt-1">
            <span>800원</span>
            <span>1,200원</span>
          </div>
        </div>

        <div>
          <div class="flex justify-between text-xs font-semibold mb-1">
            <span>기초자산 변동성 (<span class="italic">σ</span>)</span>
            <span class="text-emerald-400 font-bold" id="val-vol">30 %</span>
          </div>
          <input id="slider-vol" type="range" min="5" max="80" step="5" value="30" class="w-full bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-500 mt-1">
            <span>5% (안정적)</span>
            <span>80% (극심함)</span>
          </div>
        </div>

        <div>
          <div class="flex justify-between text-xs font-semibold mb-1">
            <span>무위험 이자율 (<span class="italic">r</span>)</span>
            <span class="text-indigo-400 font-bold" id="val-rate">5 %</span>
          </div>
          <input id="slider-rate" type="range" min="0" max="15" step="1" value="5" class="w-full bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-500 mt-1">
            <span>0%</span>
            <span>15%</span>
          </div>
        </div>
      </div>

      <!-- Center & Right: Chart Display -->
      <div class="lg:col-span-2 flex flex-col justify-between">
        <div class="h-64 w-full relative">
          <canvas id="decayChart"></canvas>
        </div>

        <!-- Real-time dynamic stats -->
        <div class="grid grid-cols-3 gap-2 mt-4 text-center">
          <div class="bg-slate-950 p-2.5 rounded border border-slate-800">
            <div class="text-[10px] text-slate-400">현재 주가 1,000원 기준</div>
            <div class="text-sm font-extrabold text-sky-400" id="stat-total">-- 원</div>
            <div class="text-[8px] text-slate-500">총 시장 가치</div>
          </div>
          <div class="bg-slate-950 p-2.5 rounded border border-slate-800">
            <div class="text-[10px] text-slate-400">현재 주가 1,000원 기준</div>
            <div class="text-sm font-extrabold text-rose-400" id="stat-intrinsic">-- 원</div>
            <div class="text-[8px] text-slate-500">내재 가치 (즉시행사)</div>
          </div>
          <div class="bg-slate-950 p-2.5 rounded border border-slate-800">
            <div class="text-[10px] text-slate-400">현재 주가 1,000원 기준</div>
            <div class="text-sm font-extrabold text-emerald-400" id="stat-timeval">-- 원</div>
            <div class="text-[8px] text-slate-500">시간 가치 (Premium)</div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <script>
    // Standard Normal Cumulative Distribution Function
    function stdNormalCDF(x) {
      const b1 =  0.319381530;
      const b2 = -0.356563782;
      const b3 =  1.781477937;
      const b4 = -1.821255978;
      const b5 =  1.330274429;
      const p  =  0.2316419;
      const c  =  0.39894228;

      if (x >= 0) {
        let t = 1.0 / (1.0 + p * x);
        return (1.0 - c * Math.exp(-x * x / 2.0) * t *
          (t * (t * (t * (t * b5 + b4) + b3) + b2) + b1));
      } else {
        let t = 1.0 / (1.0 - p * x);
        return (c * Math.exp(-x * x / 2.0) * t *
          (t * (t * (t * (t * b5 + b4) + b3) + b2) + b1));
      }
    }

    // Black-Scholes Call Pricing Formula
    function blackScholesCall(S, K, T, r, sigma) {
      if (T <= 0.002) {
        return Math.max(S - K, 0);
      }
      const d1 = (Math.log(S / K) + (r + (sigma * sigma) / 2) * T) / (sigma * Math.sqrt(T));
      const d2 = d1 - sigma * Math.sqrt(T);
      return S * stdNormalCDF(d1) - K * Math.exp(-r * T) * stdNormalCDF(d2);
    }

    // Elements
    const sliderTime = document.getElementById('slider-time');
    const sliderStrike = document.getElementById('slider-strike');
    const sliderVol = document.getElementById('slider-vol');
    const sliderRate = document.getElementById('slider-rate');

    const valTime = document.getElementById('val-time');
    const valStrike = document.getElementById('val-strike');
    const valVol = document.getElementById('val-vol');
    const valRate = document.getElementById('val-rate');

    const statTotal = document.getElementById('stat-total');
    const statIntrinsic = document.getElementById('stat-intrinsic');
    const statTimeval = document.getElementById('stat-timeval');

    // Chart Setup
    const ctx = document.getElementById('decayChart').getContext('2d');
    
    // Generate Stock Price Axis Data
    const generateLabels = () => {
      const labels = [];
      for (let s = 600; s <= 1400; s += 20) {
        labels.push(s);
      }
      return labels;
    };

    const labels = generateLabels();

    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: '현재 옵션 가치',
            data: [],
            borderColor: '#38bdf8',
            borderWidth: 3,
            pointRadius: 0,
            fill: false,
            tension: 0.1
          },
          {
            label: '만기 페이오프',
            data: [],
            borderColor: '#f43f5e',
            borderWidth: 2,
            borderDash: [5, 5],
            pointRadius: 0,
            fill: false,
            tension: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            labels: {
              color: '#94a3b8',
              font: { size: 11 }
            }
          }
        },
        scales: {
          x: {
            title: { display: true, text: '주가 (S)', color: '#94a3b8', font: { size: 10 } },
            grid: { color: '#334155' },
            ticks: { color: '#64748b', font: { size: 9 } }
          },
          y: {
            title: { display: true, text: '옵션 가치 (C)', color: '#94a3b8', font: { size: 10 } },
            grid: { color: '#334155' },
            ticks: { color: '#64748b', font: { size: 9 } },
            min: 0,
            max: 500
          }
        }
      }
    });

    function updateChart() {
      const T = parseFloat(sliderTime.value);
      const K = parseFloat(sliderStrike.value);
      const sigma = parseFloat(sliderVol.value) / 100;
      const r = parseFloat(sliderRate.value) / 100;

      // Update Slider Label Displays
      valTime.innerText = `${T.toFixed(2)} 년`;
      valStrike.innerText = `${K.toLocaleString()} 원`;
      valVol.innerText = `${Math.round(sigma * 100)} %`;
      valRate.innerText = `${Math.round(r * 100)} %`;

      const currentPrices = [];
      const payoffPrices = [];

      labels.forEach(S => {
        currentPrices.push(blackScholesCall(S, K, T, r, sigma));
        payoffPrices.push(Math.max(S - K, 0));
      });

      chart.data.datasets[0].data = currentPrices;
      chart.data.datasets[1].data = payoffPrices;
      chart.update('none'); // silent update

      // Update Stats (for standard spot price S = 1000)
      const testS = 1000;
      const totalVal = blackScholesCall(testS, K, T, r, sigma);
      const intrinsicVal = Math.max(testS - K, 0);
      const timeVal = totalVal - intrinsicVal;

      statTotal.innerText = `${totalVal.toFixed(1)} 원`;
      statIntrinsic.innerText = `${intrinsicVal.toFixed(1)} 원`;
      statTimeval.innerText = `${timeVal.toFixed(1)} 원`;
    }

    // Event listeners
    [sliderTime, sliderStrike, sliderVol, sliderRate].forEach(slider => {
      slider.addEventListener('input', updateChart);
    });

    // Initial Trigger
    updateChart();
  </script>
</body>
</html>
[/ASSET]

---

[ASSET:sub_01_16_visual2.html]
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Walk Path & Payoff Distribution</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {
      background-color: #0f172a;
      color: #f8fafc;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
  </style>
</head>
<body class="p-4 flex flex-col items-center justify-center min-h-[500px]">

  <div class="w-full max-w-4xl bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-2xl">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 border-b border-slate-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-sky-400">무작위 주가 경로와 만기 페이오프 분포</h2>
        <p class="text-xs text-slate-400">몬테카를로 기법을 사용해 주가의 무수한 변동 경로를 실시간으로 그리고, 만기($T$)에서의 옵션 보상 분포를 도식화합니다.</p>
      </div>
      <button id="btn-simulate" class="mt-2 md:mt-0 bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs py-2 px-4 rounded-lg transition-all shadow-md active:scale-95">
        시뮬레이션 재생 실행
      </button>
    </div>

    <!-- Parameter Dashboard -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 bg-slate-950 p-3 rounded-lg border border-slate-800 mb-4 text-xs">
      <div>
        <span class="text-slate-400 block">현재 주가 (<span class="italic">S₀</span>)</span>
        <strong class="text-slate-200 text-sm">1,000 원</strong>
      </div>
      <div>
        <span class="text-slate-400 block">행사 가격 (<span class="italic">K</span>)</span>
        <strong class="text-rose-400 text-sm">1,000 원</strong>
      </div>
      <div>
        <span class="text-slate-400 block">무위험 이자율 (<span class="italic">r</span>)</span>
        <strong class="text-indigo-400 text-sm">5.0 % (무위험 표류)</strong>
      </div>
      <div>
        <span class="text-slate-400 block">자산 변동성 (<span class="italic">σ</span>)</span>
        <strong class="text-emerald-400 text-sm">35.0 %</strong>
      </div>
    </div>

    <!-- Multi-Chart Canvas -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- Path Chart -->
      <div class="md:col-span-2 h-64 bg-slate-950 p-2 rounded-lg border border-slate-800 relative">
        <div class="absolute top-2 left-2 text-[10px] text-slate-500 z-10 font-bold">시간 흐름과 무작위 주가 경로 (30 Paths)</div>
        <canvas id="pathChart"></canvas>
      </div>

      <!-- Histogram Payoff Chart -->
      <div class="h-64 bg-slate-950 p-2 rounded-lg border border-slate-800 relative">
        <div class="absolute top-2 left-2 text-[10px] text-rose-400 z-10 font-bold">만기 페이오프 분포 [Max(S_T - K, 0)]</div>
        <canvas id="distributionChart"></canvas>
      </div>
    </div>

    <!-- Analytical Note -->
    <div class="mt-4 bg-slate-950 p-3 rounded border border-slate-800 text-[11px] text-slate-400 leading-relaxed">
      💡 <strong class="text-slate-300">금융공학적 통찰:</strong> 주가는 기하 브라운 운동(GBM)을 따라 확률적으로 분산됩니다. 우측 분포에서 확인되듯, 하방 가격은 <span class="text-rose-400 font-bold">0원</span>에서 조밀하게 차단(하방 경직성)되는 반면, 상방 영역은 길게 늘어지며 비선형적 비대칭성을 창출합니다. 이 무수히 넓게 퍼진 페이오프 분포의 평균(기댓값)을 구한 뒤 무위험 금리로 할인한 값이 바로 오늘의 공정 가격입니다.
    </div>

  </div>

  <script>
    const S0 = 1000;
    const K = 1000;
    const r = 0.05;
    const sigma = 0.35;
    const T = 1.0; // 1 year
    const steps = 50; // daily resolution
    const dt = T / steps;

    // Normal Random Box-Muller Transform
    function randomNormal() {
      let u = 0, v = 0;
      while(u === 0) u = Math.random(); 
      while(v === 0) v = Math.random();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }

    // Charts Setup
    const ctxPath = document.getElementById('pathChart').getContext('2d');
    const ctxDist = document.getElementById('distributionChart').getContext('2d');

    let pathChart, distChart;

    function initCharts() {
      // Setup Path Chart
      const timeLabels = Array.from({length: steps + 1}, (_, i) => (i * dt).toFixed(2));
      
      pathChart = new Chart(ctxPath, {
        type: 'line',
        data: {
          labels: timeLabels,
          datasets: []
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { 
              grid: { color: '#1e293b' }, 
              ticks: { color: '#64748b', font: { size: 9 } },
              title: { display: true, text: '시간 (t)', color: '#94a3b8', font: { size: 10 } }
            },
            y: { 
              grid: { color: '#1e293b' }, 
              ticks: { color: '#64748b', font: { size: 9 } },
              title: { display: true, text: '주가 (S)', color: '#94a3b8', font: { size: 10 } }
            }
          }
        }
      });

      // Setup Distribution Chart
      distChart = new Chart(ctxDist, {
        type: 'bar',
        data: {
          labels: ['0원 (행사포기)', '0-50원', '50-150원', '150-300원', '300원 이상'],
          datasets: [{
            data: [0, 0, 0, 0, 0],
            backgroundColor: ['#f43f5e', '#38bdf8', '#0ea5e9', '#0284c7', '#0369a1'],
            borderWidth: 0,
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { 
              grid: { display: false }, 
              ticks: { color: '#64748b', font: { size: 9 } } 
            },
            y: { 
              grid: { color: '#1e293b' }, 
              ticks: { color: '#64748b', font: { size: 9 } },
              title: { display: true, text: '도달 경로 횟수', color: '#94a3b8', font: { size: 10 } }
            }
          }
        }
      });
    }

    function runSimulation() {
      const numPaths = 30;
      const paths = [];
      const finalPayoffs = [];

      // Calculate GBM Paths
      for (let p = 0; p < numPaths; p++) {
        const path = [S0];
        let S = S0;
        for (let t = 1; t <= steps; t++) {
          const drift = (r - 0.5 * sigma * sigma) * dt;
          const diffusion = sigma * Math.sqrt(dt) * randomNormal();
          S = S * Math.exp(drift + diffusion);
          path.push(S);
        }
        paths.push(path);
        
        // Option Payoff at Maturity T
        const payoff = Math.max(S - K, 0);
        finalPayoffs.push(payoff);
      }

      // Update Path Datasets
      pathChart.data.datasets = paths.map((path, index) => ({
        data: path,
        borderColor: index === 0 ? '#38bdf8' : 'rgba(56, 189, 248, 0.15)',
        borderWidth: index === 0 ? 2.5 : 1,
        pointRadius: 0,
        fill: false,
        tension: 0.1
      }));
      pathChart.update();

      // Bin the payoffs for the distribution chart
      let binZero = 0;
      let binLow = 0;
      let binMid = 0;
      let binHigh = 0;
      let binMax = 0;

      finalPayoffs.forEach(payoff => {
        if (payoff === 0) binZero++;
        else if (payoff <= 50) binLow++;
        else if (payoff <= 150) binMid++;
        else if (payoff <= 300) binHigh++;
        else binMax++;
      });

      distChart.data.datasets[0].data = [binZero, binLow, binMid, binHigh, binMax];
      distChart.update();
    }

    // Initialize & Execute
    initCharts();
    runSimulation();

    document.getElementById('btn-simulate').addEventListener('click', () => {
      runSimulation();
    });
  </script>
</body>
</html>
[/ASSET]