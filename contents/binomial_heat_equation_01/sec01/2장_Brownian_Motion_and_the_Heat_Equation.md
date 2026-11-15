# 제2장. 브라운 운동과 열방정식
**(Chapter 2. Brownian Motion and the Heat Equation)**

---

## §2.1. 브라운 운동 (Brownian motion)

이 절에서는 **브라운 운동(Brownian motion)**을 소개한다. 브라운 운동은 시간과 공간의 증분(increments)이 0으로 갈 때 랜덤 워크의 극한(limit)으로 간주될 수 있다. 그러한 극한을 취하는 방법이나 "극한"이라는 단어의 의미 자체가 무엇인지는 명확하지 않다. 따라서 그러한 세부 사항에 대해 당장 걱정하기보다는, 단순 랜덤 워크의 극한 형태가 존재한다고 가정하고 그 극한이 가져야 할 몇 가지 성질들을 나열할 것이다. 우리는 1차원 경우부터 시작할 것이다. 이 과정은 연속 시간과 연속 공간에서 정의될 것이다. $W_t$를 시간 $t$에서의 브라운 운동(연속적인 무작위 이동자)의 위치라 하자.

> **♦ 정리: 브라운 운동과 위너 과정(Wiener Process)**
> 수학자들에게 "브라운 운동"과 "위너 과정"은 동의어이다. 과학 문헌에서 "브라운 운동"이라는 용어는 종종 물리적 과정을 지칭하기 위해 사용되는데, 이에 대해서는 여러 가지 수학적 모델이 존재하며 그중 하나가 바로 우리가 여기서 논의하는 모델이다. "위너 과정"이라는 용어는 항상 우리가 여기서 기술하는 과정을 지칭한다.

브라운 운동은 **연속 확률 과정(continuous stochastic process)**의 예이다. 확률 과정은 시간에 의해 인덱스된 확률 변수들의 모임 $\{W_t\}$이다. 우리의 경우 시간은 음이 아닌 실수를 가로질러 흐른다. (단순 랜덤 워크는 시간이 음이 아닌 정수로 인덱스된 확률 과정이다.) 이 확률 변수들의 모임은 무작위 함수 $t \mapsto W_t$로도 볼 수 있다.

### 2.1.1. 이산 근사로부터의 유도 (Derivation from discrete approximation)

우리는 이산 근사를 고려함으로써 브라운 운동의 정의에 다가갈 것이다. 시간과 공간에서 작은 단계가 있어서 시간 $\Delta t$ 동안 공간에서의 전형적인 변화는 $\Delta x$ 차원이라고 가정하자. 정수 격자 $\mathbb{Z}$ 상의 단순 랜덤 워크 $S_n$은 $\Delta t = 1, \Delta x = 1$인 과정이다. 즉, 각 정수 시간 단계마다 과정은 거리 1만큼 이동한다. 이제 랜덤 워크 경로를 가지고 시간과 공간의 증분을 변경해 보자.

시간 증분이 $\Delta t = \delta = 1/N$ ($N$은 큰 정수)이라고 가정하자. 공간 증분 $\Delta x$를 어떻게 변경해야 하는지 살펴보자. 큰 $N$에 대해 극한 과정은 다음과 같이 보여야 한다:

$$W_{k\delta} \approx \Delta x S_k$$

여기서 $\Delta x$는 공간 스케일링 인자를 나타낸다. 과정이 올바르게 스케일링되도록 하기 위해 $\delta$에 관하여 $\Delta x$가 무엇이어야 하는지 알아내야 한다. 극한 과정을 $\mathbb{E}[W_1^2] = 1$이 되도록 정규화하자. $S_N$은 $N$번의 단계 후의 랜덤 워크 위치이므로 $\mathbb{E}[S_N^2] = N$이다. 따라서,

$$\mathbb{E}[(\Delta x S_N)^2] = (\Delta x)^2 \mathbb{E}[S_N^2] = (\Delta x)^2 N$$

우리는 이것이 1이 되기를 원하므로, 올바른 스케일링은 $\Delta x = 1/\sqrt{N} = \sqrt{\delta}$ 이다. 따라서 $t = j\delta = j/N$ 이면, 우리는 다음과 같이 쓸 수 있다:

$$W_t = W_{j/N} \approx \frac{S_j}{\sqrt{N}}$$

> **♦ 정리: 직관적인 이해**
> 위의 내용은 처음에는 조금 이상하게 보일 수 있다. $1/N$ 크기의 시간 단계 $N$번 동안, 이 과정은 $1/\sqrt{N}$ 크기의 공간 단계를 $N$번 거친다. 언뜻 보기에 이 과정이 총 $\sqrt{N}$만큼의 거리를 이동할 것처럼 보일 수 있다. 그러나 단계 중 절반은 양의 방향으로, 나머지 절반은 음의 방향으로 이동하므로 최종 이동 거리는 1차원적인 차수가 된다.

### 2.1.2. 중심극한정리와 브라운 운동의 성질 (Central Limit Theorem and Properties)

> **♦ 정리: 중심극한정리 (Central Limit Theorem)**
> $X_1, X_2, \dots$가 평균 $\mu$, 분산 $\sigma^2$을 갖는 독립 확률 변수들일 때, 중심극한정리에 따르면 큰 $n$에 대해 다음 확률 변수의 분포는
>
> $$Z_n = \frac{(X_1 + \cdots + X_n) - n\mu}{\sqrt{\sigma^2 n}}$$
>
> 평균 0, 분산 1을 갖는 정규분포에 근사한다. 더 정확하게는, 모든 $a < b$에 대해 다음이 성립한다:
>
> $$\lim_{n\to\infty} \mathbb{P}\{a \le Z_n \le b\} = \int_a^b \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, dx$$

다음과 같이 써보자:

$$W_t = W_{j\delta} \approx \frac{S_j}{\sqrt{N}} = \frac{S_j}{\sqrt{j}} \sqrt{\frac{j}{N}} = \frac{S_j}{\sqrt{j}} \sqrt{t}$$

중심극한정리에 의해 $j \to \infty$에 따라 $S_j/\sqrt{j}$의 분포는 평균 0, 분산 1인 정규분포로 접근한다. 따라서 $\sqrt{t} \, S_j/\sqrt{j}$는 평균 0, 분산 $t$인 정규분포로 접근한다. 이러한 확률 변수는 다음과 같은 밀도 함수를 가짐을 상기하자:

$$\frac{1}{\sqrt{2\pi t}} e^{-\frac{x^2}{2t}}, \quad -\infty < x < \infty$$

($Y$가 분산 1인 정규분포를 가질 때 $\sigma Y$가 평균 0, 분산 $\sigma^2$인 정규분포를 가짐은 쉽게 확인할 수 있다.)

이것을 동기로 삼아, 우리는 브라운 운동의 정의를 위한 첫 번째 성질을 얻는다:

* **성질 1 (정규분포 위치):** 각 $t$에 대해, 확률 변수 $W_t$는 평균 0, 분산 $t$인 정규분포를 가진다.

사실 $W_t - W_s$에 대해서도 동일한 논증을 적용할 수 있으며, 이는 때로 **동일 분포 정규 증분(identically distributed normal increments)**이라 불리는 다음 성질로 이어진다:

* **성질 2 (정규 증분):** $0 \le s < t < \infty$에 대해, 확률 변수 $W_t - W_s$는 평균 0, 분산 $t - s$인 정규분포를 가진다.

다음 성질은 **독립 증분(independent increments)**이라 불린다. $S_n$이 단순 랜덤 워크이고 $n < m$이면, 확률 변수 $S_m - S_n$은 시간 $n$까지의 랜덤 워크와 독립이다. 우리는 이 성질이 극한에서도 성립할 것으로 기대한다.

* **성질 3 (독립 증분):** 모든 $s < t$에 대해, 확률 변수 $W_t - W_s$는 모든 확률 변수 $\{W_r : r \le s\}$와 독립이다.

> **♦ 정리: 위치와 증분의 독립성**
> $s < t$에 대해 위치 $W_s$와 $W_t$가 독립이라고 말하는 것이 아님에 유의하라. 실제로 $s$와 $t$가 가까우면 $W_s$와 $W_t$도 가까울 것으로 예상된다. 독립인 것은 바로 위치 자체가 아니라 증분인 $W_s$와 $W_t - W_s$이다.

### 2.1.3. 이진 유리수 상에서의 브라운 운동 정의 (Definition on Dyadic Rationals)

$W_t$와 같은 확률 과정을 정의할 때 부딪히는 주요 기술적 문제는 양의 실수 $t$가 비가산(uncountably many)이라는 점이다. 가산 집합(countable set) 상에서만 정의된 과정을 고려하는 것이 더 쉽다. 모든 시간의 집합에서 조밀한(dense) 가산 집합을 선택한다면 이것으로 충분하기를 기대할 수 있다. 당장은 유리수 시간으로 한정할 수 있으며, 나아가 이들의 부분집합인 **이진 유리수(dyadic rationals)**로 더 한정할 수 있다.

$\mathcal{D}_n$을 분모가 $2^n$인 음이 아닌 유리수의 집합이라 하자 (기약분수 형태일 필요는 없음):

$$\mathcal{D}_n = \left\{ \frac{k}{2^n} : k = 0, 1, 2, \dots \right\}$$

그러면 $\mathcal{D}_0 \subset \mathcal{D}_1 \subset \mathcal{D}_2 \subset \cdots$ 이다. (음이 아닌) 이진 유리수의 집합은 $\mathcal{D} = \bigcup_{n} \mathcal{D}_n$ 이다.

이러한 가정들을 모아서 정의로 구성한다.

> **정의 2.1 (Definition 2.1)**  
> 이진 유리수 상에서의 (표준 1차원) 브라운 운동은 다음을 만족하는 확률 변수들의 모임 $\{W_t : t \in \mathcal{D}\}$이다:
>
> * 각 $n$에 대해, 확률 변수들
>
>   $$W_{k/2^n} - W_{(k-1)/2^n}, \quad k = 1, 2, \dots$$
>
>   은 평균 0, 분산 $2^{-n}$을 갖는 독립 정규 확률 변수들이다.

시간 $1/2^n, 2/2^n, 3/2^n, \dots$에서의 브라운 운동의 위치에만 관심이 있다면, 이를 크기 $2^{-n}$의 시간 증분을 갖는 랜덤 워크로 간주할 수 있다. 공간 증분은 단순 랜덤 워크처럼 두 가지 값만 가지는 것이 아니라 정규분포를 가질 것이다.

다음과 같이 써보자:

$$(2.1) \quad J(k, n) = 2^{n/2} \left[ W_{k/2^n} - W_{(k-1)/2^n} \right]$$

그러면 조건의 또 다른 표현 방식은 각 $n$에 대해 확률 변수들

$$J(1, n), J(2, n), J(3, n), \dots$$

이 각각 평균 0, 분산 1을 갖는 독립 정규 확률 변수라는 것이다.

우리는 $W_t, t \in \mathcal{D}$가 브라운 운동이 되기 위한 요구사항을 기술하였다. 정의가 유용하기 위해서는 이러한 과정이 실제로 존재함을 보여야 한다. 우리는 이를 절 2.7.1에서 증명한다. 이러한 확률 변수를 찾을 수 있음을 받아들인다면 절 2.7.1은 건너뛸 수 있다. 정의를 사용하면 다음을 보일 수 있다:

* $0 \le s \le t$인 $s, t \in \mathcal{D}$에 대해, $W_t - W_s$는 $\{W_r : r \le s\}$와 독립이며 평균 0, 분산 $t - s$인 정규분포를 가진다.

이진 유리수 $\mathcal{D}$는 정수 $j$에 대해 다음 성질을 갖는다:

$$2^j \mathcal{D} := \{ 2^j q : q \in \mathcal{D} \} = \mathcal{D}$$

$W_t$가 브라운 운동이고 시간을 $2^j$만큼 스케일링할 때, 공간을 $1/\sqrt{2^j}$만큼 스케일링하면 또 다른 브라운 운동을 얻는다. 더 정확하게는: $W_q, q \in \mathcal{D}$가 표준 브라운 운동이고 $j \in \mathbb{Z}$이며,

$$\tilde{W}_q = 2^{-j/2} W_{2^j q}$$

이면, $\tilde{W}_q$ 역시 표준 브라운 운동이다. 이는 $\tilde{W}_q$가 브라운 운동을 정의하는 성질들을 만족함을 확인함으로써 검증된다 (연습문제 2.1).

시간 집합 $\mathcal{D}$는 양의 실수에 조밀(dense)하다. 조밀한 부분집합의 모든 시간 $t$에서 함수 $W_t$의 값을 알면 모든 시간에서 $W_t$를 알 수 있는가? $W_t$가 $t$의 연속 함수라면 대답은 '예'이다. $W_t$가 연속 함수임을 보이기 위해서는 $\mathcal{D}$로 제한된 $W_t$가 각 콤팩트 구간(compact interval)에서 균등 연속(uniformly continuous)임을 보이면 충분하다.

### 2.1.4. 균등 연속성과 브라운 운동의 연속 확장 (Theorem 2.2)

> **♦ 정리: 조밀 부분집합에서의 균등 연속 확장**
> $f : \mathcal{D} \to \mathbb{R}$이 함수이고 모든 유계 구간 $[a, b]$ 상에서 $f$가 균등 연속이라고 하자. 이는 모든 $\epsilon > 0$에 대해 $\delta > 0$가 존재하여 $|s - t| < \delta$이고 $s, t \in \mathcal{D}$이면 $|f(s) - f(t)| < \epsilon$임을 의미한다. $\mathcal{D}$는 $[0, \infty)$의 조밀 부분집합이므로, $a \le t \le b$이면 $t_n \to t$인 $t_n \in \mathcal{D} \cap [a, b]$ 수열을 찾을 수 있다. $f$가 $[a, b]$에서 균등 연속이므로 $\{f(t_n)\}$이 코시 수열(Cauchy sequence)이고 따라서 유일한 극한을 가짐을 쉽게 확인할 수 있다. $f(t), t \in \mathbb{R}$을 이 극한으로 정의하면, $f$가 $[a, b]$에서 균등 연속임을 쉽게 알 수 있다. 요약하면: $\mathcal{D}$ 상의 함수 $f$가 각 유계 구간 $[a, b]$에서 균등 연속이면, $\mathbb{R}$로의 유일한 연속 확장이 존재한다.

이진 유리수 상의 브라운 운동에 대해, 확률 1로 균등 연속성이 성립한다.

> **정리 2.2 (Theorem 2.2)**  
> $W_q, q \in \mathcal{D}$가 표준 1차원 브라운 운동이면, 확률 1로 모든 구간 $[a, b]$에 대해 함수 $W_q$는 균등 연속이다.
>
> 특히 $W_t, t \in [0, \infty)$는 연속성에 의해 정의될 수 있으며 다음 성질들을 갖는다:
>
> * $W_0 = 0$.
> * 모든 $0 \le s \le t$에 대해, $W_t - W_s$는 평균 0, 분산 $t - s$인 정규분포를 갖는다. 또한 $W_t - W_s$는 $\{W_r : r \le s\}$와 독립이다.
> * 확률 1로, 함수 $t \mapsto W_t$는 연속 함수이다.

> **♦ 정리: 연속성에 대한 직관적 이유**
> $W_t$가 연속이어야 하는 간단한 직관적 이유가 있다. $W_{t+\delta} - W_t$를 고려해 보자. 이 확률 변수는 평균 0, 분산 $\delta$를 가지므로 $\mathbb{E}[(W_{t+\delta} - W_t)^2] = \delta$이다. 즉, 다음을 기대할 수 있다:
>
> $$(W_{t+\delta} - W_t)^2 \approx \delta, \quad |W_{t+\delta} - W_t| \approx \sqrt{\delta}$$
>
> $\delta \to 0$에 따라 $\sqrt{\delta} \to 0$이 되므로 연속성을 기대할 수 있다. 이 직관적 논증은 훌륭하지만, 엄밀하게 만들기 위해서는 $(W_{t+\delta} - W_t)^2$의 평균값이 $\delta$ 차원일 뿐만 아니라 어떤 의미에서는 항상 그 차원(또는 너무 크지 않은 차원)임을 보여야 한다.

이 정리의 증명에서 가장 어려운 부분은 균등 연속성을 확립하는 것이다. 이를 위해서는 몇 가지 추정(estimates)을 수행해야 한다. 구간 $[0, 1]$에 대해 증명을 진행할 것이며, 다른 구간들도 유사하게 다룰 수 있다.

$$(2.2) \quad K^*_n = \sup \left\{ |W_s - W_t| : 0 \le s, t \le 1, \, |s - t| \le 2^{-n}, \, s, t \in \mathcal{D} \right\}$$

라 하자. 그러면 함수 $t \mapsto W_t$의 균등 연속성은 $n \to \infty$일 때 $K^*_n \to 0$이라는 명제와 동치이다. (이것이 즉시 명확하지 않다면 직접 검증해 보라.) 추정하기 더 쉬운 약간 다른 양을 정의하자:

$$(2.3) \quad K_n = \max_{k=1,\dots,2^n} \sup \left\{ |W_q - W_{(k-1)/2^n}| : q \in \mathcal{D}, \, \frac{k-1}{2^n} \le q \le \frac{k}{2^n} \right\}$$

차이점은 두 시간 중 하나(둘 다는 아님)가 $\mathcal{D}_n$에 속해야 한다는 점이다. 삼각부등식을 사용하면 다음을 볼 수 있다:

$$K_n \le K^*_n \le 3 K_n$$

따라서 $K_n \to 0$임을 보이는 것과 동치이다. 절 2.7.2에서 $K_n$이 클 확률에 대한 정밀한 추정을 제공한다. 특히, 다음을 보인다:

$$(2.4) \quad \sum_{n=1}^\infty \mathbb{P}\left\{ K_n \ge 2 \sqrt{n} \, 2^{-n/2} \right\} < \infty$$

보렐-칸텔리 보조정리(Borel-Cantelli lemma, 보조정리 1.3)에 의해 확률 1로 충분히 큰 모든 $n$에 대해 다음 추정이 성립한다:

$$K_n < 2 \sqrt{n} \, 2^{-n/2}$$

특히, $K_n \to 0$이다.

### 2.1.5. 어디서도 미분 불가능성 (Nowhere Differentiability - Theorem 2.3)

브라운 운동은 무작위 함수 $t \mapsto W_t$를 정의한다. 우리는 질문할 수 있다: 이 함수는 얼마나 매끄러운가(smooth)? 한 점 $t$에서 도함수를 취하려고 시도해 보자. 도함수의 정의는 극한이 존재할 때 다음과 같다:

$$\frac{d W_t}{dt} = \lim_{\delta \to 0} \frac{W_{t+\delta} - W_t}{\delta}$$

우변 분자의 전형적인 크기는 $|W_{t+\delta} - W_t| \approx \sqrt{\delta}$이며, 이는 $\delta$가 작을 때 $\delta$보다 훨씬 크다. 이로부터 도함수가 존재하는 경우가 매우 드물 것으로 예상할 수 있으며, 실제로 도함수는 어디에서도 존재하지 않는다.

> **정리 2.3 (Theorem 2.3)**  
> 확률 1로, 함수 $t \mapsto W_t$는 어디에서도 미분 가능하지 않다 (nowhere differentiable).

연속이지만 어디에서도 미분 가능하지 않은 함수를 하나 작성하는 것도 쉽지 않지만, 브라운 운동의 경우 이것이 항상 참임을 보여준다. 직관은 이미 설명하였으며, 증명의 상세한 내용은 연습문제 2.26으로 남긴다.

> **♦ 정리: 미분 불가능성에 대한 추가 직관**
> 미분 불가능한 함수를 얻는다는 것이 놀라워 보일 수 있지만, 사실 우리의 초기 가정이 미분 불가능한 함수를 내포하고 있음을 볼 수 있다. $W_t$가 $t_0$에서 미분 가능하고 도함수가 $m$이라고 가정하자. 그러면 $t \le t_0$인 $W_t$를 살펴봄으로써 $m$을 결정할 수 있을 것이다. 작은 $t > t_0$에 대해 $W_t - W_{t_0} \approx m (t - t_0)$임을 알게 된다. 그러나 우리의 가정 중 하나는 증분 $W_t - W_{t_0}$가 시간 $t_0$ 이전의 브라운 운동의 값들과 독립이라는 점이다.

### 2.1.6. 고차원 브라운 운동과 정지 시간 (High-dimensional Brownian Motion and Stopping Time - Proposition 2.4)

$\mathbb{R}^d$에서 브라운 운동을 정의하기 위해, $d$개의 독립인 브라운 운동 $W^1_t, \dots, W^d_t$를 취하고 $W_t = (W^1_t, \dots, W^d_t)$라 놓는다. $W_t$의 밀도 함수는 다음과 같다:

$$(2\pi t)^{-d/2} \exp\left\{ -\frac{x_1^2 + \cdots + x_d^2}{2t} \right\}$$

$W_t$의 밀도가 방사 대칭(radially symmetric)임에 유의하라. (각 좌표에서의 독립 변수들이 방사 대칭인 결과를 준다는 사실은 놀라울 수 있다. 실제로 정규분포는 어떤 의미에서 이러한 성질을 갖는 유일한 분포이다, 연습문제 2.4 참조.) 우리는 $d$차원 브라운 운동이 회전 불변(invariant under rotations)이라는 사실을 사용할 것이다.

$W_t$가 $W_0 = x$에서 시작하는 브라운 운동이고 $U$가 $\mathbb{R}^d$의 열린 부분집합이라고 하자. 그러면 $\mathbb{E}[W_t] = x$이다. 우리는 이 결과의 "정지된(stopped)" 버전이 필요하다.

$$T = T_U = \inf \{ t \ge 0 : W_t \notin U \}$$

라 놓자. 확률 변수 $T$는 **정지 시간(stopping time)**의 한 예이다. 이 경우 $U$를 벗어날 때 정지한다. "정지 시간"이라는 용어는 특정 시간에 정지할지 여부에 대한 결정이 미래를 내다보지 않고 그 순간까지 이용 가능한 정보만을 사용하여 내려짐을 의미한다. $t \wedge T = \min \{ t, T \}$임을 상기하자.

> **명제 2.4 (Proposition 2.4)**  
> 모든 $t \ge 0$에 대해,
>
> $$(2.5) \quad \mathbb{E}[W_{t \wedge T} \mid W_0 = x] = x$$

**증명.** $t = 1$ 및 $x = 0$에 대해 증명하겠다. 다른 $t, x$ 값에 대한 증명도 유사하다. 각 양의 정수 $n$에 대해

$$T_n = \min \{ q \in \mathcal{D}_n : q \ge T \}$$

라 하자. 즉, $(k-1)/2^n \le T < k/2^n$이면 $T_n = k/2^n$이다. 우리는 먼저 각 $n$에 대해 다음을 보일 것이다:

$$(2.6) \quad \mathbb{E}[W_{1 \wedge T_n}] = 0$$

실제로, 지시 함수(indicator function) 표기법을 사용하여 다음과 같이 쓸 수 있다:

$$W_{1 \wedge T_n} = \sum_{k=1}^{2^n} 1\left\{ T > \frac{k-1}{2^n} \right\} \left[ W_{k/2^n} - W_{(k-1)/2^n} \right]$$

따라서,

$$\mathbb{E}[W_{1 \wedge T_n}] = \sum_{k=1}^{2^n} \mathbb{E}\left[ 1\left\{ T > \frac{k-1}{2^n} \right\} \left[ W_{k/2^n} - W_{(k-1)/2^n} \right] \right]$$

사건 $T > (k-1)/2^n$은 $t \le (k-1)/2^n$에 대해 $W_t$를 관찰함으로써 결정될 수 있다. 따라서 $W_{k/2^n} - W_{(k-1)/2^n}$은 이 사건과 독립이며,

$$\mathbb{E}\left[ 1\left\{ T > \frac{k-1}{2^n} \right\} \left[ W_{k/2^n} - W_{(k-1)/2^n} \right] \right] = \mathbb{P}\left\{ T > \frac{k-1}{2^n} \right\} \mathbb{E}\left[ W_{k/2^n} - W_{(k-1)/2^n} \right] = 0$$

합산함으로써 (2.6)을 얻는다. 마지막으로 다음이 성립함에 유의하라:

$$|W_{1 \wedge T_n} - W_{1 \wedge T}| \le K_n \to 0$$

여기서 $K_n$은 (2.3)에서 정의된 바와 같다. 이것을 사용하면 명제를 얻는다. $\quad \blacksquare$

---

#### 📐 주요 수식 및 개념 정리 (LaTeX)

1. **이산 근사의 스케일링 규칙:**
   - 시간 증분 $\Delta t = \delta = 1/N$, 공간 증분 $\Delta x = \sqrt{\delta} = 1/\sqrt{N}$
   - 근사 식: $W_t = W_{j/N} \approx \frac{S_j}{\sqrt{N}}$

2. **브라운 운동의 3가지 핵심 성질:**
   - **정규 위치 및 초기값:** $W_0 = 0$, $W_t \sim \mathcal{N}(0, t)$ 밀도 함수 $f(x) = \frac{1}{\sqrt{2\pi t}} e^{-x^2/(2t)}$
   - **정규 증분 (Normal Increments):** $W_t - W_s \sim \mathcal{N}(0, t-s) \quad (0 \le s < t)$
   - **독립 증분 (Independent Increments):** $W_t - W_s$는 $\{W_r : r \le s\}$와 독립

3. **이진 유리수 (Dyadic Rationals)와 스케일링 변환:**
   - $\mathcal{D}_n = \{k/2^n : k = 0, 1, 2, \dots\}$, $\mathcal{D} = \bigcup_{n=0}^\infty \mathcal{D}_n$
   - 표준화된 증분 변수: $J(k, n) = 2^{n/2} [W_{k/2^n} - W_{(k-1)/2^n}] \sim \mathcal{N}(0, 1)$ 독립
   - 공간-시간 재스케일링 (Self-similarity): $\tilde{W}_q = 2^{-j/2} W_{2^j q} \quad (q \in \mathcal{D}, j \in \mathbb{Z})$ 도 표준 브라운 운동

4. **연속성 및 미분 불가능성:**
   - **경로 연속성 (Theorem 2.2):** 확률 1로 $t \mapsto W_t$는 연속이며, $K_n = \max_{k} \sup_{q} |W_q - W_{(k-1)/2^n}| < 2\sqrt{n}2^{-n/2} \to 0$ (Borel-Cantelli)
   - **어디서도 미분 불가능성 (Theorem 2.3):** 증분 크기 $|W_{t+\delta} - W_t| \approx \sqrt{\delta} \gg \delta \implies \frac{dW_t}{dt}$ 존재하지 않음

5. **$d$차원 브라운 운동 및 정지 시간 (Stopping Time):**
   - $d$차원 밀도 함수: $(2\pi t)^{-d/2} \exp\left( -\frac{\|x\|^2}{2t} \right)$ (회전 불변성)
   - 정지 시간 $T_U = \inf\{t \ge 0 : W_t \notin U\}$에 대해 마팅게일 성질: $\mathbb{E}[W_{t \wedge T} \mid W_0 = x] = x$ (Proposition 2.4)

---

## §2.2. 조화함수 (Harmonic functions)

$\mathbb{Z}^d$ 상의 함수 $f$가 $x$에서 조화적(harmonic)이라는 것은 $f(x)$가 가장 가까운 이웃점들에서의 $f$의 평균과 같다는 것을 의미함을 상기하자. $U$가 $\mathbb{R}^d$의 열린 부분집합일 때, $f$가 연속이고 다음의 **평균값 성질(mean value property)**을 만족할 때 그리고 오직 그때만 $f$가 $U$에서 조화적이라고 말한다: 모든 $x \in U$ 및 모든 $0 < \epsilon < \text{dist}(x, \partial U)$에 대해,

$$(2.7) \quad f(x) = \text{MV}(f; x, \epsilon) = \int_{|y-x|=\epsilon} f(y) \, ds(y)$$

이 정의에는 정의되지 않은 몇 가지 양이 포함되어 있으므로 이제 이들을 정의할 것이다. 먼저 $\text{dist}(x, \partial U)$는 $x$에서 $U$의 경계까지의 거리를 나타내며, $\inf\{|x - y| : y \notin U\}$로 정의될 수 있다. 적분에서 $s$는 $x$를 중심으로 하는 반지름 $\epsilon$인 구(sphere) 상의 곡면 측도(surface measure)를 나타내며, 다음을 만족하도록 정규화(normalize)되어 있다:

$$\int_{|y-x|=\epsilon} 1 \, ds(y) = 1$$

여기서 $\text{MV}(f; x, \epsilon)$는 $x$를 중심으로 하는 반지름 $\epsilon$인 구 상에서의 $f$의 평균값을 나타낸다.

> **♦ 정리: 곡면 측도 (Surface Measure)**
> $d = 3$인 경우, $s$는 통상적인 표면적에 상수를 곱한 것이다. $d > 3$인 경우, 이는 그에 대응하는 $(d-1)$차원 "부피(volume)"이다.

$d = 1$인 경우, $f$가 연속이고 $a < x - \epsilon < x < x + \epsilon < b$인 각 $x, \epsilon$에 대해 다음을 만족하면 $f$는 $(a, b)$에서 조화적이다:

$$(2.8) \quad f(x) = \frac{1}{2} [f(x + \epsilon) + f(x - \epsilon)]$$

선형 함수 $f(x) = mx + r$은 이 방정식을 만족한다. 다음 명제는 이들이 $\mathbb{R}$에서의 유일한 조화함수임을 보여준다.

> **명제 2.5 (Proposition 2.5)**  
> $f : (a, b) \to \mathbb{R}$이 조화적이면, 어떤 $m, r$에 대해 다음이 성립한다:
>
> $$f(x) = mx + r$$

**증명.** $a < 0, b > 1$ 및 $f(0) = 0, f(1) = 1$이라고 가정하겠다. 우리는 $0 \le x \le 1$에 대해 $f(x) = x$임을 보일 것이다. 일반적인 증명도 유사하게 작동한다. $\epsilon = 1/2$로 하여 (2.8)을 사용하면 다음을 얻는다:

$$f\left(\frac{1}{2}\right) = \frac{f(0) + f(1)}{2} = \frac{1}{2}$$

유사하게, $\epsilon$을 이진 유리수 $\mathcal{D} \cap [0, 1]$ 전체에 걸쳐 변하게 하면서 (2.8)을 반복 적용하면, 모든 이진 유리수에 대해 $f(j/2^n) = j/2^n$임을 볼 수 있다. $f$가 연속이므로, 모든 $t$에 대해 $f(t) = t$이어야 한다. $\quad \blacksquare$

### 2.2.1. 1차원 조화함수와 미적분학적 접근 (1-D Harmonic Functions and Calculus)

방금 전 증명이 간단했음에도 불구하고, 이 명제의 또 다른 증명을 제시하고자 한다. $f$가 $x$의 이웃에서 두 번 연속 미분 가능하다고 가정하자. 그러면 테일러 정리(Taylor's theorem)에 의해 다음을 얻는다:

$$f(x + \epsilon) = f(x) + \epsilon f'(x) + \frac{\epsilon^2}{2} f''(x) + o(\epsilon^2)$$

$$f(x - \epsilon) = f(x) - \epsilon f'(x) + \frac{\epsilon^2}{2} f''(x) + o(\epsilon^2)$$

여기서 $o(\epsilon^2)$는 $\epsilon \to 0$일 때 $o(\epsilon^2)/\epsilon^2 \to 0$을 만족하는 ($x$에 의존하는) 함수를 나타낸다. 두 식을 더하고 $\epsilon \to 0$으로 보내면 다음을 얻는다:

$$(2.9) \quad f''(x) = \lim_{\epsilon \to 0} \frac{f(x + \epsilon) + f(x - \epsilon) - 2f(x)}{\epsilon^2}$$

$f$가 조화적이면 우변은 모든 $x$에 대해 0과 같으므로 $f'' \equiv 0$이다. 미적분학으로부터 이것이 $f$가 선형 함수임을 내포함을 알고 있다.

(2.9)의 우변을 다음과 같이 다시 쓸 수 있다:

$$\lim_{\epsilon \to 0} \frac{1}{\epsilon} \left[ \frac{f(x + \epsilon) - f(x)}{\epsilon} - \frac{f(x) - f(x - \epsilon)}{\epsilon} \right]$$

대괄호 안의 분수들은 $f'$의 근사치이며, 이로부터 $f'$의 도함수처럼 보이는 표현식을 얻게 된다.

### 2.2.2. $d$차원 라플라시안과 평균값 표현 (Laplacian in $d$-dimensions)

(2.9)를 $d$차원으로 확장할 수 있다. 다음과 같이 정의하자:

$$\Delta f(x) = \lim_{\epsilon \to 0} \frac{1}{\epsilon^2} \sum_{y \in \mathbb{Z}^d, |y|=1} [f(x + \epsilon y) - f(x)]$$

> **♦ 정리: $C^k$ 함수의 정의**
> 함수 $f : \mathbb{R}^d \to \mathbb{R}$가 $C^k$라는 것은 $k$차의 모든 편도함수(partial derivatives)가 존재하고 연속함수임을 의미한다.

> **명제 2.6 (Proposition 2.6)**  
> $f$가 $\mathbb{R}^d$의 $x$의 이웃에서 $C^2$ 함수라고 하자. 그러면 $x$에서 $\Delta f(x)$가 존재하며 다음이 성립한다:
>
> $$(2.10) \quad \Delta f(x) = \sum_{j=1}^d \partial_{jj} f(x)$$

**증명.** $y_j$를 $j$번째 성분이 1인 $\mathbb{Z}^d$ (또는 $\mathbb{R}^d$)의 단위 벡터라 하면, $y_j$ 방향으로 1차원 테일러 정리를 사용하여 다음을 얻을 수 있다:

$$f(x \pm \epsilon y_j) = f(x) \pm \epsilon \partial_j f(x) + \frac{\epsilon^2}{2} \partial_{jj} f(x) + o(\epsilon^2)$$

따라서,

$$\sum_{y \in \mathbb{Z}^d, |y|=1} [f(x + \epsilon y) - f(x)] = \epsilon^2 \sum_{j=1}^d \partial_{jj} f(x) + o(\epsilon^2) \quad \blacksquare$$

$\Delta$의 정의를 다음과 같이 다시 쓸 수 있다:

$$\frac{1}{2d} \Delta f(x) = \lim_{\epsilon \to 0} \frac{1}{\epsilon^2} \left[ \left( \frac{1}{2d} \sum_{y \in \mathbb{Z}^d, |y|=1} f(x + \epsilon y) \right) - f(x) \right]$$

안쪽 괄호의 항은 평균값이 좌표축 방향으로만 취해진 $f$의 일종의 평균값으로 볼 수 있다. 이 평균값은 좌표축 선택에 의존한다. 다음 명제는 구 상에서 평균을 취할 수도 있으며, 따라서 정의가 좌표축 선택에 의존하지 않음을 보여준다.

> **명제 2.7 (Proposition 2.7)**  
> $f$가 $x$의 이웃에서 $C^2$이면, 다음이 성립한다:
>
> $$(2.11) \quad \frac{1}{2d} \Delta f(x) = \lim_{\epsilon \to 0} \frac{\text{MV}(f; x, \epsilon) - f(x)}{\epsilon^2}$$
>
> 여기서 $\text{MV}(f; x, \epsilon)$는 (2.7)에서와 같이 $x$를 중심으로 하는 반지름 $\epsilon$인 구 상에서의 $f$의 평균값을 나타낸다.

**증명.** 표기의 편의를 위해 $x = 0$ 및 $f(x) = f(0) = 0$이라 가정하자. $f$가 0의 이웃에서 $C^2$이면 다음과 같이 쓸 수 있다:

$$(2.12) \quad f(y) = P_2(y) + o(|y|^2)$$

여기서 $P_2$는 0 근방에서 $f$의 2차 테일러 다항식을 나타낸다:

$$P_2(y) = y \cdot \nabla f(0) + \frac{1}{2} \sum_{1 \le k, l \le d} a_{kl} y_k y_l$$

여기서 $y = (y_1, \dots, y_d)$ 및 $a_{kl} = \partial_{kl} f(0)$이다. 대칭성에 의해 $\text{MV}(y_k; 0, \epsilon) = 0$임에 유의하라. 유사하게 $k \neq l$이면 $\text{MV}(y_k y_l; 0, \epsilon) = 0$이다. 따라서,

$$\text{MV}(P_2; 0, \epsilon) = \frac{1}{2} \sum_{k=1}^d a_{kk} \text{MV}(y_k^2; 0, \epsilon)$$

적분을 계산하여 $\beta_k := \text{MV}(y_k^2; 0, \epsilon)$를 계산할 수도 있지만, 이 계산을 피하기 위해 기교를 사용할 것이다. 대칭성에 의해 $\beta_k$는 모든 $k$에 대해 동일하며,

$$\beta_1 + \cdots + \beta_d = \text{MV}(y_1^2 + \cdots + y_d^2; 0, \epsilon) = \text{MV}(\epsilon^2; 0, \epsilon) = \epsilon^2$$

이다. 따라서 $\text{MV}(y_k^2; 0, \epsilon) = \epsilon^2 / d$이다. 마지막으로 (2.12)의 오차항이 $o(|y|^2)$이므로,

$$\lim_{\epsilon \to 0^+} \epsilon^{-2} \text{MV}(f; 0, \epsilon) = \lim_{\epsilon \to 0^+} \epsilon^{-2} \text{MV}(P_2; 0, \epsilon) = \frac{1}{2} \sum_{k=1}^d a_{kk} = \frac{1}{2d} \Delta f(0) \quad \blacksquare$$

### 2.2.3. 라플라시안 연산자 (The Laplacian Operator)

연산자 $\Delta$를 **라플라시안(Laplacian)**이라 부른다. 돌이켜보면 $\frac{1}{2}\Delta$를 라플라시안이라 부르는 것이 더 편리했을 수도 있지만, 용어가 고정되어 있다. 대부분의 서적은 (2.10)에 의해 라플라시안을 정의하지만($1/2$이 나타나지 않는 이유이다), 평균값 성질에 의해 라플라시안이 정의된다고 생각하는 것이 더 자연스럽다. $\Delta f(x) = \text{div}[\nabla f(x)]$임에 유의하라. 라플라시안의 또 다른 표준 표기법은 $\nabla^2$이다. 이는 다음과 같이 생각할 수 있다:

$$\nabla^2 = \nabla \cdot \nabla = \left( \frac{\partial}{\partial x_1}, \dots, \frac{\partial}{\partial x_d} \right) \cdot \left( \frac{\partial}{\partial x_1}, \dots, \frac{\partial}{\partial x_d} \right)$$

혼란을 더하자면, 많은 해석학자들은 라플라시안을 $-\Delta$로 정의하기로 선택한다. 이렇게 하면 이 연산자가 "양의 연산자(positive operator)"가 된다는 장점이 있다 (식 (2.46) 참조). $1/2$을 곱하든 마이너스 부호를 붙이든, 조건 $\Delta f(x) = 0$은 동일한 의미를 갖는다.

### 2.2.4. 조화함수와 라플라스 방정식의 동치성 (Theorem 2.8)

> **정리 2.8 (Theorem 2.8)**  
> 영역 $U$에서의 함수가 조화적일 필요충분조건은 $f$가 $C^2$이고 $U$의 모든 $x$에 대해 $\Delta f(x) = 0$인 것이다.

이 정리의 증명은 이 절의 나머지 부분에서 논의할 것이다. 대부분의 서적에서는 $\Delta f(x) = 0$인 경우 $f$가 $U$에서 조화적이라고 정의하기 때문에 이 정리를 찾을 수 없다. 그러나 그들은 이러한 함수가 평균값 성질을 만족함을 보일 것이므로 어느 쪽이든 정리를 증명해야 한다.

> **♦ 정리: 적분 변수 표기법**
> $z = (z_1, \dots, z_d) \in \mathbb{R}^d$일 때, $ddz$는 $dz_1 \cdots dz_d$를 의미한다. 해석학자들은 공간 차원으로 보통 $n$을 선호하는 반면, 확률론자들은 $d$를 사용하는 경향이 있으며 $n$은 수열의 인덱스로 남겨둔다. 차원으로 $d$를 사용하는 바람에 생기는 부작용 중 하나는 두 $d$가 서로 다른 의미를 가지는 $ddz$를 써야 한다는 점이다.

사실 우리는 $f$가 조화적이면 모든 $x$에 대해 $\Delta f(x) = 0$임을 거의 보였다. 우리가 보여준 것은 함수 $f$가 평균값 성질을 만족하고 $C^2$이면 $\Delta f = 0$을 만족한다는 것이다. 증명을 마치기 위해, $f$가 연속이고 평균값 성질을 만족하면 자동으로 $C^\infty$임을 보일 것이다! 이를 보이기 위해 다음을 만족하는 $\mathbb{R}^d$ 상의 $C^\infty$ 함수 $\phi$가 존재한다는 사실(연습문제 2.6 참조)이 필요하다: $\phi$는 방사 대칭(radially symmetric)이고, $|x| \ge 1$에 대해 $\phi(x) = 0$이며, $|x| < 1$에 대해 $\phi(x) > 0$이고,

$$\int_{\mathbb{R}^d} \phi(z) \, ddz = 1$$

$\phi$를 그러한 함수라 하고 $\phi_\epsilon(x) = \epsilon^{-d} \phi(x/\epsilon)$이라 하자. 그러면 $\phi_\epsilon$은 $|x| < \epsilon$일 때 그리고 오직 그때만 양수이며,

$$\int_{\mathbb{R}^d} \phi_\epsilon(z) \, ddz = 1$$

이다. $\text{dist}(x, \partial U) \ge 2\epsilon$이라고 가정하자. $f$가 $U$에서 연속이고 평균값 성질을 만족하면, 구면 좌표계와 $\phi_\epsilon$의 방사 대칭성을 사용하여 $|y - x| < \epsilon$에 대해 다음을 볼 수 있다:

$$f(y) = \int_{\mathbb{R}^d} \phi_\epsilon(z) f(y + z) \, ddz = \int_{\mathbb{R}^d} \phi_\epsilon(z - y) f(z) \, ddz$$

이제 우변을 미분함으로써 $y$에 대한 $f$의 도함수를 취할 수 있다. 적분과 미분의 순서 교환을 정당화하기 위해 $f$의 연속성이 사용된다.

### 2.2.5. 적분과 미분의 순서 교환 정당화 (Interchanging Integral and Derivative)

> **♦ 정리: 적분과 미분의 순서 교환 정당화**
> 종종 적분과 미분의 순서를 교환하고 싶으므로, 이것이 언제 정당화될 수 있는지 논의해 보자. $g(t, x), t \in \mathbb{R}, x \in \mathbb{R}^d$가 편도함수 $\partial_t g(t, x)$가 존재하고 연속인 $\mathbb{R}^{d+1}$ 상의 연속 함수라고 하자. $V$가 $\mathbb{R}^d$의 부분집합일 때, 우리는 다음을 쓰고 싶다:
>
> $$(2.13) \quad \partial_t \int_V g(t, x) \, ddx = \int_V \partial_t g(t, x) \, ddx$$
>
> $g_\epsilon(t, x) = \epsilon^{-1} [g(t + \epsilon, x) - g(t, x)]$라 놓으면, $\partial_t g(t, x) = \lim_{\epsilon \to 0} g_\epsilon(t, x)$이다. 미분의 정의를 사용하면
>
> $$\partial_t \int_V g(t, x) \, ddx = \lim_{\epsilon \to 0} \frac{1}{\epsilon} \left[ \int_V g(t + \epsilon, x) \, ddx - \int_V g(t, x) \, ddx \right] = \lim_{\epsilon \to 0} \int_V g_\epsilon(t, x) \, ddx$$
>
> 이며, 미분은 우변의 극한이 존재할 때만 존재한다. 다음을 보이기 위해:
>
> $$\lim_{\epsilon \to 0} \int_V g_\epsilon(t, x) \, ddx = \int_V \partial_t g(t, x) \, ddx$$
>
> 다음을 보이면 충분하다:
>
> $$\lim_{\epsilon \to 0} \int_V [g_\epsilon(t, x) - \partial_t g(t, x)] \, ddx = 0$$
>
> 이는 다시 다음을 보일 수 있으면 성립한다:
>
> $$(2.14) \quad \lim_{\epsilon \to 0} \int_V |g_\epsilon(t, x) - \partial_t g(t, x)| \, ddx = 0$$
>
> 따라서 (2.14)는 (2.13)을 정당화하기 위한 충분조건을 제공한다. $g$가 $t$에 대해 두 번 연속 미분 가능하면, 잔여항이 있는 테일러 정리에 의해
>
> $$|g_\epsilon(t, x) - \partial_t g(t, x)| \le \frac{\epsilon}{2} K_\epsilon(t, x)$$
>
> 여기서 $K_\epsilon(t, x) = \max \{ |\partial_{tt} g(s, x)| : |s - t| \le \epsilon \}$이다. 따라서 (2.13)을 정당화하는 충분조건은 다음을 만족하는 $\epsilon > 0$이 존재하는 것이다:
>
> $$(2.15) \quad \int_V K_\epsilon(t, x) \, ddx < \infty$$
>
> 적분과 미분의 순서 교환을 정당화해야 하는 모든 경우에 대해 (2.15)를 증명할 수 있다. 그러나 항상 세부 사항을 다 포함하지는 않는다.

### 2.2.6. 조화함수의 평균값 성질 역증명과 그린 정리 (Proof of Mean Value Property)

증명을 마치기 위해, $f$가 영역 $U$에서 모든 $x$에 대해 $\Delta f(x) = 0$인 $C^2$ 함수이고 $\text{dist}(x, \partial U) > \epsilon$인 $x \in U$이면 $\text{MV}(f; x, \epsilon) = f(x)$임을 보여야 한다. 즉, $f$가 평균값 성질을 만족함을 보여야 한다. ((2.11)에 의해 $f$가 "$\epsilon$이 0으로 가는 극한에서" 평균값 성질을 만족함을 알고 있지만, 실제 평균값 성질을 보여주고자 한다.) 편의상 $f$가 콤팩트 지지(compact support)를 가진다고 가정하겠다. 일반적인 경우를 도출하려면 연습문제 2.7을 사용하라. 일반성을 잃지 않고 $x = 0, f(0) = 0$이라 가정할 수 있다.

> **♦ 정리: 콤팩트 지지 (Compact Support)**
> 함수 $f : \mathbb{R}^d \to \mathbb{R}$가 콤팩트 지지(compact support)를 가진다는 것은 $|x| > K$일 때 $f(x) = 0$이 되는 $K < \infty$가 존재함을 의미한다.

계산을 확립하는 가장 쉬운 방법은 직접 계산에 의해서이다. 다음과 같이 써보자:

$$\text{MV}(\epsilon) = \text{MV}(f; 0, \epsilon) = \int_{|x|=1} f(\epsilon x) \, ds(x)$$

여기서 $s$는 반지름 1인 구 상의 정규화된 곡면 측도를 나타낸다. $\text{MV}(0) = 0$임을 알고 있다. 모든 $\epsilon$에 대해 $\text{MV}(\epsilon) = 0$임을 보이기 위해서는 $\text{MV}'(\epsilon) = 0$임을 보이면 충분하다. 미분하면 다음을 얻는다:

$$\text{MV}'(\epsilon) = \int_{|x|=1} \frac{d}{d\epsilon} f(\epsilon x) \, ds(x) = \int_{|x|=1} \partial_r f(\epsilon x) \, ds(x)$$

여기서 $\partial_r$은 지름(반지름) 방향으로의 미분을 나타낸다. 그린 정리(Green's theorem, 연습문제 2.11)를 사용하면 $f$가 조화적일 때 다음을 보일 수 있다:

$$(2.16) \quad \int_{|x|=1} \partial_r f(\epsilon x) \, ds(x) = 0$$

> **♦ 정리: 그린 정리 / 스토크스 정리 (Green's / Stokes' Theorem)**
> $d$차원에서 미적분학의 기본 정리의 다양한 버전들이 스토크스(Stokes) 또는 그린(Green) 정리라는 이름으로 불린다. 여기서는 다음 버전이 필요하다. $U \subset \mathbb{R}^d$가 매끄러운 경계를 갖는 유계 연결 열린집합이고 $F$가 매끄러운 벡터장(vector field)이면,
>
> $$\int_{\partial U} (F \cdot n)(y) \, ds(y) = \int_U (\text{div} F)(x) \, ddx$$
>
> 여기서 $s$는 $\partial U$ 상의 (정규화되지 않은) 곡면 측도를 나타내고 $n$은 외향 단위 법선 벡터(outward unit normal)를 나타낸다. 함수 $f$에 대해 $\partial U$ 상의 (외향) 법선 도함수(normal derivative)는 $\nabla f \cdot n$으로 주어진다.

### 2.2.7. 브라운 운동을 통한 확률론적 접근과 이토 적분 (Probabilistic Approach via Brownian Motion and Itô Integral)

이제 구 이외의 집합 상에서의 평균값으로 일반화되는 장점을 가진 이 관계를 바라보는 확률론적 방법을 논의한다. $W_t$를 원점에서 시작하는 브라운 운동이라 하고,

$$T = T_\epsilon = \inf \{ t \ge 0 : |W_t| = \epsilon \}$$

을 $W_t$가 $x$ 주변의 반지름 $\epsilon$인 구에 도달하는 최초 시간이라 하자. ($W_t$가 연속 함수이므로 하한(infimum)이라는 단어를 최솟값(minimum)이라는 단어로 대체할 수 있음에 유의하라.) 그러면 브라운 운동의 방사 대칭성은 $W_T$의 분포가 반지름 $\epsilon$인 구 상에서 균일 분포(uniformly distributed)임을 내포하며, 따라서

$$\text{MV}(f; 0, \epsilon) = \mathbb{E}[f(W_T)]$$

이다. 우리는 다음을 보여야 한다:

$$(2.17) \quad \mathbb{E}[f(W_T)] = 0$$

이것은 다음 마팅게일 성질(martingale property)로부터 도출될 것이다: 모든 $t < \infty$에 대해,

$$(2.18) \quad \mathbb{E}[f(W_{T \wedge t})] = 0$$

(2.18)에서 (2.17)로 가는 논증은 이산 디리클레 문제에서와 본질적으로 동일하므로 세부 사항은 생략한다. 우리는 (2.18)을 도출하는 데 집중할 것이다. 더 쉬운 관계인 $\mathbb{E}[f(W_t)] = 0$을 도출하는 것부터 시작할 것이며, 편의상 $f(W_0) = 0$이라 가정하고 $t = 1$을 선택한다.

$P_2(y; x)$를 $x$ 근방에서 $f$의 2차 테일러 다항식이라 하고,

$$e(x, y) = f(y) - P_2(y; x)$$

라 하자. $f$가 콤팩트 지지를 갖는 $C^2$ 함수이므로, 모든 $x, y$에 대해 $\epsilon(0^+) = 0$을 만족하는 함수 $\epsilon(\delta)$가 존재하여 다음을 만족한다:

$$|e(x, y)| \le \epsilon(|x - y|) |x - y|^2$$

(연습문제 2.5 참조.)

각 $n$에 대해 다음과 같이 쓴다:

$$f(W_1) = \sum_{m=1}^n \left[ f(W_{m/n}) - f(W_{(m-1)/n}) \right]$$

$P_2(y; x)$를 다음과 같이 쓸 수 있다:

$$P_2(y; x) = f(x) + (y - x) \cdot \nabla f(x) + \sum_{1 \le j \le k \le d} a_{jk}(x) (y_j - x_j) (y_k - x_k)$$

여기서 $a_{jk}(x) = \partial_{jk} f(x) = \partial_{kj} f(x)$이다. $\Delta f \equiv 0$이고 $f$가 $C^2$이므로 다음을 볼 수 있다:

$$\sum_{j=1}^d a_{jj}(x) (y_j - x_j) (y_k - x_k) = o(|y|^2)$$

따라서 $o(|y|^2)$ 오차 범위 내에서 $f(W_1)$은 다음 세 항의 합이다:

$$\sum_{m=1}^n \nabla f(W_{(m-1)/n}) \cdot \left[ W_{m/n} - W_{(m-1)/n} \right]$$

$$\sum_{m=1}^n \sum_{1 \le j < k \le d} a_{jk}(W_{(m-1)/n}) \left[ W^j_{m/n} - W^j_{(m-1)/n} \right] \left[ W^k_{m/n} - W^k_{(m-1)/n} \right]$$

$$\sum_{m=1}^n e(W_{(m-1)/n}, W_{m/n})$$

여기서 $d$차원 브라운 운동을 $W_t = (W^1_t, \dots, W^d_t)$로 표기한다. $\nabla f(W_{(m-1)/n})$은 시간 $(m-1)/n$까지의 브라운 운동에만 의존하고 $W_{m/n} - W_{(m-1)/n}$은 이것과 독립이며 평균이 0이므로, 다음을 볼 수 있다:

$$\mathbb{E}\left[ \nabla f(W_{(m-1)/n}) \cdot \left[ W_{m/n} - W_{(m-1)/n} \right] \right] = 0$$

유사하게 $j < k$이면 $a_{jk}(W_{(m-1)/n})$, $W^j_{m/n} - W^j_{(m-1)/n}$, $W^k_{m/n} - W^k_{(m-1)/n}$은 독립이며 마지막 두 개는 평균이 0이다. 따라서,

$$\mathbb{E}\left[ a_{jk}(W_{(m-1)/n}) \left[ W^j_{m/n} - W^j_{(m-1)/n} \right] \left[ W^k_{m/n} - W^k_{(m-1)/n} \right] \right] = 0$$

마지막 항에 대해서는 다음을 유의하자:

$$\left| \sum_{m=1}^n e(W_{(m-1)/n}, W_{m/n}) \right| \le \epsilon(R_n) Q_n$$

여기서

$$Q_n = \sum_{j=1}^d \sum_{m=1}^n \left[ W^j_{m/n} - W^j_{(m-1)/n} \right]^2$$

이고 $R_n = \max \{ |W_{m/n} - W_{(m-1)/n}| : m = 1, \dots, n \}$이다. 우리는 확률 1로 우변이 0으로 수렴함을 주장한다. 브라운 운동의 연속성은 $R_n \to 0$을 내포한다. 또한 $\epsilon(R_n)$은 유계이며 (왜 그런가?) 따라서 $\mathbb{E}[\epsilon(R_n)^2] \to 0$이다. 연습문제(연습문제 2.23 참조)에서 $Q_n$을 연구하는데, 특히 $\mathbb{E}[Q_n^2]$은 $n$에 대해 유계이다. 따라서 코시-슈바르츠 부등식(Cauchy-Schwarz inequality)을 사용하면,

$$\mathbb{E}[\epsilon(R_n) Q_n]^2 \le \mathbb{E}[\epsilon(R_n)^2] \mathbb{E}[Q_n^2] \to 0$$

을 얻는다. 특히 $\mathbb{E}[f(W_1)] = 0$이다.

이 논증은 독자로 하여금 다음 식을 쓰고 싶게 만들 수 있다:

$$f(W_1) - f(W_0) = \lim_{n\to\infty} \sum_{k=1}^n \nabla f(W_{T_{k-1}}) \cdot [W_{T_k} - W_{T_{k-1}}] = \int_0^1 \nabla f(W_t) \cdot dW_t$$

실제로 이것은 엄밀하게 만들어질 수 있다. 이것이 바로 **이토 확률 적분(Itô stochastic integral)**의 한 예이다.

---

#### 📐 주요 수식 및 개념 정리 (LaTeX)

1. **조화함수의 평균값 성질 (Mean Value Property):**
   - 구 상의 평균: $f(x) = \text{MV}(f; x, \epsilon) = \int_{|y-x|=\epsilon} f(y) \, ds(y) \quad (0 < \epsilon < \text{dist}(x, \partial U))$
   - 1차원 조화함수: $f(x) = \frac{1}{2}[f(x+\epsilon) + f(x-\epsilon)] \implies f(x) = mx + r$ (유일한 1차원 조화함수는 선형함수)

2. **라플라시안 연산자 (Laplacian Operator):**
   - 정의식: $\Delta f(x) = \sum_{j=1}^d \partial_{jj} f(x) = \text{div}[\nabla f(x)] = \nabla^2 f(x)$
   - 평균값 극한표현: $\frac{1}{2d} \Delta f(x) = \lim_{\epsilon \to 0} \frac{\text{MV}(f; x, \epsilon) - f(x)}{\epsilon^2}$

3. **조화함수의 동치 정리 (Theorem 2.8):**
   - $f$가 영역 $U$에서 조화적 $\iff f \in C^2(U)$ 이며 $\Delta f(x) = 0 \quad (\forall x \in U)$
   - 평균값 성질을 만족하는 연속함수는 자동으로 $C^\infty$ 매끄러움을 가짐 (Mollifier $\phi_\epsilon$ 콘볼루션 활용)

4. **그린 정리와 미분/적분 교환 조건:**
   - 그린 정리: $\int_{\partial U} (\nabla f \cdot n)(y) \, ds(y) = \int_U \Delta f(x) \, ddx = 0$
   - 적분-미분 순서 교환 조건: $\int_V K_\epsilon(t, x) \, ddx < \infty$ ($K_\epsilon = \max_{|s-t|\le \epsilon} |\partial_{tt} g(s, x)|$)

5. **브라운 운동을 통한 확률론적 표상 및 이토 적분:**
   - 정지 시간 $T = T_\epsilon = \inf\{t \ge 0 : |W_t| = \epsilon\}$에 대해 구 상의 일양 분포: $\text{MV}(f; 0, \epsilon) = \mathbb{E}[f(W_T)] = 0$
   - 이토 확률 적분(Itô Integral): $f(W_1) - f(W_0) = \int_0^1 \nabla f(W_t) \cdot dW_t \quad (\Delta f \equiv 0 \implies \mathbb{E}[f(W_1)] = 0)$

---

## §2.3. 디리클레 문제 (Dirichlet problem)

우리는 미리 정해진 경계값을 갖는 조화함수를 찾는 문제를 고려할 것이다. 유계 영역과 연속적인 경계값에 논의를 한정할 것이다.

> **정의: 조화함수에 대한 디리클레 문제**  
> 유계 영역 $U \subset \mathbb{R}^d$와 연속 함수 $F : \partial U \to \mathbb{R}$가 주어졌을 때, 다음을 만족하는 $U$ 전체로의 $F$의 확장(extension)을 찾아라:
>
> (2.19) $F : U \to \mathbb{R}$은 연속이다.  
> (2.20) $\Delta F(x) = 0, \quad x \in U$.

> **♦ 정리: 물리적 의미**
> $F$가 온도를 나타낸다면, 이는 경계에서 온도가 고정되고 알려져 있을 때 내부에서의 평형 온도 분포를 제공한다.

### 2.3.1. 해의 유일성과 최대 원리 (Uniqueness and Maximum Principle)

우리는 먼저 디리클레 문제의 해가 존재한다면 유일함을 보일 것이다. 이를 위해 다음을 말하는 **최대 원리(maximum principle)**를 사용한다: $U$가 유계 영역이고 $F$가 (2.19)와 (2.20)을 만족하면, $F$의 최댓값은 경계 어딘가에서 얻어진다. 이는 연속성과 평균값 성질로부터 따르며, 이제 이를 증명한다. $U$라는 콤팩트 집합 위의 연속 함수 $F$이므로, $F$는 어딘가에서 최댓값을 갖는다. 최댓값이 내부 점 $x$에서 얻어진다고 가정하자. $x$를 둘러싼 $U$ 내의 모든 구에 대한 평균값이 $F(x)$이므로, 연속성은 함수가 이러한 각 구 위에서 상수값 $F(x)$를 취해야 함을 시사한다. 구들을 키워나감으로써, 값이 $F(x)$인 경계상의 점을 찾을 수 있다. 최대 원리(그리고 이에 대응하는 최소 원리)가 주어지면, $F_1, F_2$가 $\partial U$ 위에서 $F_1 \equiv F_2$인 (2.19), (2.20)의 두 해라면, $F = F_1 - F_2$는 $\partial U$ 위에서 $F \equiv 0$인 해가 되고 따라서 $U$ 위에서 $F \equiv 0$이 됨을 알 수 있다.

> **♦ 정리: 선형성과 비선형성**
> 조화함수의 선형성 성질을 여기서 사용한다: $f, g$가 조화적이고 $a, b$가 상수이면 $af+bg$도 조화적이다. (2.20)이나 우리가 아래에서 논의할 열방정식과 같은 수리물리학의 고전 방정식들 중 다수는 선형 편미분 방정식이다. 오늘날 미분 방정식 분야의 대부분의 연구는 비선형 방정식을 포함한다.

> **♦ 정리: 연결 영역과 최대 원리**
> 위의 논증은 $U$가 연결(connected)되어 있고 $F$가 내부 점 최댓값을 가지면 상수라는 더 강한 사실을 증명한다.

### 2.3.2. 존재성 증명 (Existence Proof)

존재성을 보이기 위해, 이산적인 아날로그에 기초하여 좋은 추측을 한다. $W_t$가 $x \in U$에서 시작하는 $d$차원 브라운 운동이라 하고,

$$T_U = \inf \{ t \ge 0 : W_t \notin U \} = \min \{ t \ge 0 : W_t \in \partial U \}$$

라 하자. $\partial U$ 위에서의 함수 $F$가 주어졌을 때, $x \in U$에 대해 다음과 같이 정의한다:

$$(2.21) \quad F(x) = \mathbb{E} [F(W_{T_U}) \mid W_0 = x]$$

즉, 우리는 $x$에서 브라운 운동을 시작하여 경계에 도달할 때까지 움직이게 한 다음 경계 온도를 관찰한다. $x$에서의 온도는 이 온도의 평균값이며, 모든 브라운 경로에 대해 평균한 것이다. 브라운 운동의 회전 불변성은 (2.21)로 정의된 $F$가 평균값 성질을 만족함을 보여준다. $F$가 $U$에서 연속임( $U$에서의 연속성은 더 까다로우므로 아래에서 논의함)을 보이면, $x \in U$에 대해 $\Delta F(x) = 0$임을 보일 수 있다.

> **♦ 정리: 강 마르코프 성질 (Strong Markov Property)**
> 사실 여기서는 강 마르코프 성질이라 불리는 브라운 운동에 관한 미묘한 사실이 사용되고 있다. 이는 매우 미묘하여 이 문제에 대한 논의는 생략하고, 독자가 브라운 운동에 관한 고급 서적을 읽어 이 의미를 찾도록 한다.

### 2.3.3. 디리클레 문제 예제 및 브라운 운동의 성질 (Examples and Properties)

> **예제 2.9 (Example 2.9)**  
> $d = 1$이고 $U = (0, R)$이라 하자. 그러면 $\partial U = \{0, R\}$이다.
>
> $$F(x) = \mathbb{P}\{W_{T_U} = R \mid W_0 = x\}$$
>
> 라 하면, 이는 브라운 운동이 0에 도달하기 전에 $R$에 도달할 확률이다. 그러면 $F$는 다음을 만족한다:
>
> $$F(0) = 0, \quad F(R) = 1, \quad F''(x) = 0 \quad (0 < x < R)$$
>
> 이것의 유일한 해는 $F(x) = x/R$이다. 더 일반적으로, 경계값 $F(0), F(R)$을 갖는 $U$ 상의 조화함수는 다음과 같다:
>
> $$F(x) = F(0) + \frac{x}{R} [F(R) - F(0)]$$

> **예제 2.10 (Example 2.10)**  
> $d \ge 2$, $0 < r < R < \infty$라 하고, $U$를 다음 환형 영역(annular region)이라 하자:
>
> $$U = \{x \in \mathbb{R}^d : r < |x| < R\}, \quad \partial U = \{|x| = r\} \cup \{|x| = R\}$$
>
> $F(x) = \mathbb{P}\{|W_{T_U}| = R \mid W_0 = x\}$라 하자. 회전 대칭성에 의해 일변수 함수 $\phi$에 대해 $F(x) = \phi(|x|)$라 쓸 수 있으며, $\phi$는 $\phi(r) = 0, \phi(R) = 1$을 만족한다. 또한,
>
> $$\Delta F(x) = \sum_{j=1}^d \partial_{jj} F(x) = 0, \quad x \in U$$
>
> $F(x_1, \dots, x_d) = \phi(|x|) = \phi(\sqrt{x_1^2 + \cdots + x_d^2})$라 쓰면, 연쇄 법칙 계산(연습문제 2.16)에 의해 다음을 얻는다:
>
> $$(2.22) \quad \Delta F(x) = \sum_{j=1}^d \partial_{jj} \phi(|x|) = \phi''(|x|) + \frac{d-1}{|x|} \phi'(|x|)$$
>
> 따라서 미분방정식 $s \phi''(s) + (d-1) \phi'(s) = 0$의 해를 찾아야 한다. 이는 $\phi'$에 대한 1계 선형 미분방정식이며, 표준적인 방법에 의해 $\phi'(s) = c s^{1-d}$를 얻고, 적분하면 다음을 얻는다:
>
> $$\phi(s) = c_1 \log s + c_2 \quad (d = 2)$$
>
> $$\phi(s) = c_1 s^{2-d} + c_2 \quad (d \ge 3)$$
>
> 경계 조건 $\phi(r) = 0, \phi(R) = 1$을 대입하면 다음을 얻는다:
>
> $$\phi(|x|) = \frac{\log |x| - \log r}{\log R - \log r} \quad (d = 2)$$
>
> $$\phi(|x|) = \frac{r^{2-d} - |x|^{2-d}}{r^{2-d} - R^{2-d}} \quad (d \ge 3)$$

마지막 예제로부터 $d$차원 브라운 운동에 관한 흥미로운 사실들을 결론지을 수 있다.

먼저 $d \ge 3$을 고려하자. $r < |x|$이고 $x \in \mathbb{R}^d$에서 브라운 운동을 시작할 때, 브라운 운동이 원점 근방의 반지름 $r$인 구에 도달할 확률은 다음과 같이 주어진다:

$$\lim_{R \to \infty} \mathbb{P}\{|W_{T_U}| = r \mid W_0 = x\} = \lim_{R \to \infty} \frac{|x|^{2-d} - R^{2-d}}{r^{2-d} - R^{2-d}} = \left( \frac{r}{|x|} \right)^{d-2} < 1$$

특히, 브라운 운동이 그 구로 결코 돌아가지 않을 양의 확률이 존재한다. 이로부터 (연습문제 2.8) 확률 1로 다음이 성립함을 볼 수 있다:

$$(2.23) \quad \lim_{t \to \infty} |W_t| = \infty \quad (d \ge 3)$$

우리는 $d \ge 3$에 대한 브라운 운동이 **추이적(transient)**이라고 말한다.

이제 $d = 2$를 고려하자. 첫 번째 질문: $|x| > r$인 $x$에서 시작할 때, 원점 근방 반지름 $r$인 구에 도달할 확률은 얼마인가? 이는 다음과 같이 주어진다:

$$\lim_{R \to \infty} \mathbb{P}\{|W_{T_U}| = r \mid W_0 = x\} = \lim_{R \to \infty} \frac{\log R - \log |x|}{\log R - \log r} = 1$$

즉, 고정된 임의의 양수 $r$에 대해 브라운 운동은 원점 근방 반지름 $r$인 구로 계속해서 돌아온다.
두 번째 질문: $x \neq 0$에서 시작하는 브라운 운동이 원점에 도달할 확률은 얼마인가? 잠시 그 확률이 양수라고 가정하자. 그러면 원점으로부터 거리 $R$만큼 떨어지기 전에 원점에 도달할 확률이 양수가 되는 $R$이 존재할 것이다. 그러나,

$$\mathbb{P}\{\text{거리 } R \text{에 도달하기 전 } 0 \text{에 도달}\} \le \lim_{r \to 0} \mathbb{P}\{|W_{T_U}| = r \mid W_0 = x\} = \lim_{r \to 0} \frac{\log R - \log |x|}{\log R - \log r} = 0$$

따라서 확률 1로 브라운 운동은 결코 원점에 도달하지 않는다. 우리는 $d = 2$에 대한 브라운 운동이 **점 재귀적(point recurrent)이지는 않지만 이웃 재귀적(neighborhood recurrent)**이라고 말한다.

논증에서 점 0에 특별한 점은 없다. 동일한 논증은 모든 $x \in \mathbb{R}^2$에 대해, 시간 0 이후로 브라운 운동이 $x$를 결코 방문하지 않음을 보여준다. (반면에 모든 $x \in \mathbb{R}^2$에 대해 $x$가 방문되지 않는다는 것은 당연히 참이 아니다. 한정기(quantifier)의 순서가 중요하다!)

> **♦ 정리: 복소수 표기법**
> 다음 예제는 $\mathbb{R}^2$ 상의 조화함수에 관한 것이다. 우리는 $\mathbb{R}^2$를 복소수 집합 $\mathbb{C}$와 동일시한다. 이는 단순한 표기상의 편의 때문이 아니다. 복소함수론은 $\mathbb{R}^2$ 상의 실수값 조화함수 연구에서 매우 중요하다.

> **예제 2.11 (Example 2.11 - 2차원 포아송 커널)**  
> $U = \{x \in \mathbb{R}^2 : |x| < 1\} = \{r e^{i\theta} \in \mathbb{C} : 0 \le r < 1, 0 \le \theta < 2\pi\}$를 단위원 $\partial U = \{e^{i\theta} : 0 \le \theta < 2\pi\}$를 경계로 갖는 2차원 단위 원판이라 하자. 연속 함수 $F : \partial U \to \mathbb{R}$은 모든 $\theta$에 대해 $F(\theta) = F(\theta + 2\pi)$를 만족하는 $\mathbb{R}$ 상의 연속 함수로 볼 수 있다. 경계값 $F$를 갖는 조화함수는 다음과 같다:
>
> $$F(x) = \mathbb{E}[F(W_{\tau_U}) \mid W_0 = x]$$
>
> 각 $x \in U$에 대해, $x$에서 시작한 브라운 운동이 $\partial U$를 처음 방문하는 분포에 대응하는 확률분포가 $\partial U$ 상에 존재한다. 이 분포는 길이에 대한 밀도 함수 $H(x, e^{i\theta})$를 가짐이 밝혀졌다. 즉, $\theta_1 < \theta_2 < \theta_1 + 2\pi$일 때, $x$에서 시작한 브라운 운동이 각도 $\theta_1$과 $\theta_2$ 사이에서 $\partial U$에 부딪힐 확률은 다음과 같이 주어진다:
>
> $$\int_{\theta_1}^{\theta_2} H(x, e^{i\theta}) \, d\theta$$
>
> 함수 $H(x, e^{i\theta})$는 명시적으로 알려져 있으며 **포아송 커널(Poisson kernel)**이라 불린다:
>
> $$H(x, z) = \frac{1 - |x|^2}{2\pi |z - x|^2}, \quad |x| < 1, \, |z| = 1$$
>
> 따라서,
>
> $$(2.24) \quad F(x) = \int_0^{2\pi} F(e^{i\theta}) \frac{1 - |x|^2}{2\pi |e^{i\theta} - x|^2} \, d\theta$$
>
> 우리는 모자에서 커널 $H(x, z)$를 꺼낸 것처럼 제시했지만, 공식이 주어지면 (2.24)와 같이 정의된 $F$가 $U$에서 조화적이고 $U$ 상에서 연속임을 직접 검증할 수 있다 (연습문제 2.9 참조).

> **예제 2.12 (Example 2.12 - $d$차원 포아송 커널)**  
> $d \ge 3, U = \{x \in \mathbb{R}^d : |x| < 1\}$인 경우에도 유사한 포아송 커널이 존재한다. $s$를 구 $\{|x| = 1\}$의 곡면 측도라 하자. 그러면 이 측도에 대해 포아송 커널은 다음과 같다:
>
> $$(2.25) \quad H(x, z) = \frac{1 - |x|^2}{C_d |z - x|^d}, \quad |x| < 1, \, |z| = 1$$
>
> 여기서 $C_d$는 $\partial U$의 $(d-1)$차원 곡면적(측도)을 나타낸다. 즉, 주어진 함수 $F$에 대한 디리클레 문제의 해는 다음과 같다:
>
> $$F(x) = \int_{|z|=1} F(z) H(x, z) \, ds(z)$$
>
> 위에 정의된 $F$가 $U$에서 조화적이고 $\partial U$에서 연속임을 검증하는 것은 미적분학 연습문제이다 (연습문제 2.18).

---

#### 📐 주요 수식 및 개념 정리 (LaTeX)

1. **디리클레 문제 (Dirichlet problem):**
   - 정의: $\Delta F = 0$ in $U$, $F|_{\partial U} = \Phi$
   - 확률론적 해 (Probabilistic solution): $F(x) = \mathbb{E} [F(W_{T_U}) \mid W_0 = x]$
   - 최대 원리: 유계 영역 $U$에서 조화함수의 최댓값/최솟값은 경계 $\partial U$에서 취함 (해의 유일성 보장)

2. **브라운 운동을 이용한 해 존재성 및 포아송 커널:**
   - 정지 시간 (Hitting time): $T_U = \inf \{ t \ge 0 : W_t \notin U \}$
   - 포아송 적분 공식: $F(x) = \int_{|z|=1} F(z) H(x, z) \, ds(z)$
   - $d$차원 포아송 커널: $H(x, z) = \frac{1 - |x|^2}{C_d |z - x|^d} \quad (|x| < 1, |z| = 1)$

3. **1차원/2차원/고차원 예제:**
   - 1차원 $U=(0, R)$: $F(x) = F(0) + \frac{x}{R}[F(R)-F(0)]$
   - $d$차원 환형 영역 $U=\{x: r < |x| < R\}$: $\Delta F(x) = \phi''(|x|) + \frac{d-1}{|x|}\phi'(|x|) = 0$
   - 2차원(d=2): $\phi(|x|) = \frac{\log |x| - \log r}{\log R - \log r}$
   - $d \ge 3$차원: $\phi(|x|) = \frac{r^{2-d} - |x|^{2-d}}{r^{2-d} - R^{2-d}}$

4. **브라운 운동의 재귀성 및 추이성:**
   - $d \ge 3$ (Transient): $\mathbb{P}\{T_r < \infty\} = (r/|x|)^{d-2} < 1 \implies \lim_{t\to\infty} |W_t| = \infty$ (확률 1)
   - $d = 2$ (Neighborhood recurrent): $\mathbb{P}\{T_r < \infty\} = 1$, 단 $\mathbb{P}\{W_t = 0 \text{ for some } t > 0\} = 0$ (점 재귀적이지 않음)

5. **정칙 경계 (Regular Boundary):**
   - 구멍 뚫린 원판 등 경계 불연속 예제 존재 $\implies$ 브라운 운동이 $y \in \partial U$ 부근에서 출발 시 높은 확률로 $y$ 부근에서 탈출하는 정칙 경계 조건 필요

---

## §2.4. 열방정식 (Heat equation)

이제 열방정식의 연속 아날로그(continuous analogue)를 고려한다. 먼저 $\mathbb{R}^d$ 전체에서의 방정식을 고려하는 것부터 시작한다. 초기 온도가 $f(x), x \in \mathbb{R}^d$로 주어졌다고 가정하며, $f$는 유계 연속 함수라고 가정한다. 이산적인 경우와 유사하게, 우리는 온도가 브라운 운동을 하는 매우 많은 수의 열 입자에 의해 결정되는 것으로 상상한다.

$u(t, x), t \ge 0, x \in \mathbb{R}^d$를 시간 $t$에 점 $x$에서의 온도라 하자. 이는 (대략) 시간 $t$에 점 $x$에서의 열 입자의 밀도로 생각할 수 있다. 매우 직관적인 수준에서, 점 $y$에서 시작하는 $f(y)$개의 점이 있고 그들 중 시간 $t$에 $x$에 있는 비율은 $y$에 있던 입자가 $x$로 이동했을 확률이라고 상상한다. 우리는 이 확률이 시간 $t$ 동안 입자가 $x$에서 $y$로 이동할 확률과 동일할 것으로 기대한다. 가능한 모든 $y$에 대해 평균을 취하면 다음을 얻는다:

$$(2.27) \quad u(t, x) = \mathbb{E} [f(W_t) \mid W_0 = x]$$

### 2.4.1. 열 핵(Heat Kernel)과 공간 밀도 적분

이를 조금 더 엄밀하게 만들어 보자. $W_t$가 $x$에서 시작하는 $\mathbb{R}^d$ 상의 브라운 운동이면, 고정된 $t$에 대해 $W_t$는 다음 (확률) 밀도 (함수)를 갖는 확률 변수이다:

$$p(t, x, y) = \frac{1}{(2\pi t)^{d/2}} e^{-\frac{|y-x|^2}{2t}}$$

여기서 $t, x$는 고정되어 있으며 $p(t, x, y)$는 $y$의 함수로 간주된다. 다시 말해 $W_t - x$의 성분들은 평균 0, 분산 $t$인 독립 정규 확률 변수들이다. 대칭성은 $p(t, x, y) = p(t, y, x)$임을 확인함으로써 알 수 있다. (2.27)을 다음과 같이 쓸 수 있다:

$$(2.28) \quad u(t, x) = \int_{\mathbb{R}^d} f(y) p(t, x, y) \, ddy = \int_{\mathbb{R}^d} f(y) p(t, y, x) \, ddy$$

첫 번째 등식은 (2.27)의 재서술이며, 두 번째 등식은 열 흐름에 대한 우리의 해석 — 즉 $y$에서 시작하여 시간 $t$에 $x$에 존재하는 열 입자의 밀도가 $f(y) p(t, y, x)$라는 점 — 을 더 잘 반영한다.

$u(0, x) = f(x)$로 정의하고 $t > 0$에 대해 $u(t, x)$를 (2.27)로 정의한다. 다음이 성립함을 보이는 것은 어렵지 않다 (연습문제 2.13):

$$(2.29) \quad u(0, x) = u(0^+, x) := \lim_{t \to 0^+} u(t, x)$$

### 2.4.2. 근사 델타 함수 (Approximate Delta Function)

> **♦ 정리: 근사 델타 함수 (Approximate Delta Function)**
> 수학자들은 때로 $\{p(t, 0, y) : t > 0\}$를 근사 $\delta$-함수(approximate $\delta$-function)라고 부른다. 직관적으로 $\mathbb{R}^d$ 상의 델타 함수는 다음을 만족하는 함수 $\delta$이다:
>
> $$\delta(0) = \infty, \quad \delta(x) = 0 \; (x \neq 0), \quad \int_{\mathbb{R}^d} \delta(y) \, ddy = 1$$
>
> 특히 $f$가 유계 연속 함수이면 다음이 성립한다:
>
> $$(2.30) \quad \int_{\mathbb{R}^d} f(y) \delta(y - x) \, ddy = f(x)$$
>
> 기술된 그대로는 수학적 의미를 갖지 않지만, 이를 엄밀하게 만드는 여러 가지 방법이 있다. 한 가지 방법은 델타 함수를 $p(0^+, 0, y)$로 생각하는 것이며, 그러면 (2.30)은 (2.29)가 된다.

### 2.4.3. 편미분방정식의 유도 (Derivation of the Heat Equation)

이제 $u(t, x)$가 만족하는 편미분방정식을 찾을 것이다.

먼저 $d = 1$이라 가정하고 시간에 대한 우도함수(right derivative)를 고려하자. (우도함수를 계산하는 것으로 충분함을 보려면 연습문제 2.15를 참조하라.) 편의상 $t = 0, x = 0, f(0) = 0$이라 가정하자. 그러면,

$$\lim_{s \to 0^+} \frac{u(s, 0) - f(0)}{s} = \lim_{s \to 0^+} \frac{\mathbb{E}[f(W_s) \mid W_0 = 0]}{s}$$

$f$가 $C^2$이라 가정하고 2차 테일러 다항식에 의한 근사를 쓰면,

$$f(x) = f'(0) x + \frac{1}{2} f''(0) x^2 + o(x^2), \quad x \to 0$$

그러면

$$\mathbb{E}[f(W_s)] = f'(0) \mathbb{E}[W_s] + \frac{1}{2} f''(0) \mathbb{E}[W_s^2] + o(W_s^2)$$

그러나 $\mathbb{E}[W_s] = 0$, $\mathbb{E}[W_s^2] = s$ 및 $o(W_s^2) = o(s)$이다. 따라서 $s$로 나누고 $s \to 0$으로 보내면 극한이 $f''(0)/2$가 될 것으로 기대한다. $t > 0$에 대한 유사한 논증은 다음 예측을 제공한다:

$$(2.31) \quad \partial_t u(t, x) = \frac{1}{2} \partial_{xx} u(t, x)$$

이 논증의 엄밀함의 수준에 만족하지 않는 사람이 있을 수 있지만, 일단 방정식을 추측하고 나면 다음 식:

$$(2.32) \quad u(t, x) = \int_{-\infty}^\infty f(y) \frac{1}{\sqrt{2\pi t}} e^{-\frac{(y-x)^2}{2t}} \, dy$$

가 적어도 $t > 0$에 대해 (2.31)을 만족함을 직접 확인함으로써 검증할 수 있으므로 문제가 되지 않는다. 이는 도함수와 적분의 순서 교환을 정당화하기만 하면 (절 2.2의 주의사항 참조) 간단한 계산이다. $f$가 $C^2$이면 $t = 0$에서도 우도함수에 대해 이것이 성립하지만, $f$가 연속이기만 하다면 (2.29)에 만족해야 한다.

### 2.4.4. $d$차원으로의 확장 및 유일성

$d$차원에 대한 계산도 유사하므로 서술하기만 하겠다. $f$가 $\mathbb{R}^d$ 상의 유계 연속 함수라고 하자. 그러면 (2.28)에서 정의된 $u(t, x)$는 다음 열방정식을 만족한다:

$$(2.33) \quad \partial_t u(t, x) = \frac{1}{2} \Delta_x u(t, x), \quad t > 0$$

초기 조건은 다음과 같다:

$$(2.34) \quad u(0, x) = u(0^+, x) = f(x)$$

여기서 라플라시안이 $x$ 변수에 대해서만 취해짐을 나타내기 위해 $\Delta_x$라 쓴다. 직접 미분함으로써 $u$가 (2.33)을 만족함을 검증할 수 있다. 실제로 여기서 증명하지는 않겠지만, 이것은 초기 조건 (2.34)를 갖는 (2.33)의 유일한 해이다.

---

#### 📐 주요 수식 및 개념 정리 (LaTeX)

1. **전체 공간 $\mathbb{R}^d$에서의 열방정식 해 (Solution to Heat Equation):**
   - 열입자 브라운 운동 기댓값 표상: $u(t, x) = \mathbb{E}[f(W_t) \mid W_0 = x]$
   - 적분 표상: $u(t, x) = \int_{\mathbb{R}^d} f(y) p(t, x, y) \, ddy$
   - 초기 조건: $u(0, x) = \lim_{t\to 0^+} u(t, x) = f(x)$

2. **열 핵 (Heat Kernel / Transition Density):**
   - 식: $p(t, x, y) = \frac{1}{(2\pi t)^{d/2}} \exp\left( -\frac{\|y-x\|^2}{2t} \right)$
   - 대칭성: $p(t, x, y) = p(t, y, x)$
   - 근사 델타 함수: $t \to 0^+$일 때 $p(t, 0, y) \to \delta(y)$

3. **열방정식 편미분방정식 (Heat Equation PDE):**
   - $d=1$ 차원: $\partial_t u(t, x) = \frac{1}{2} \partial_{xx} u(t, x)$ (테일러 2차 전개 $\mathbb{E}[W_s^2]=s$ 활용)
   - $d$ 차원: $\partial_t u(t, x) = \frac{1}{2} \Delta_x u(t, x) \quad (t > 0)$

---

## §2.5. 유계 영역 (Bounded domain)

$\mathbb{R}^d$ 전체에서의 열방정식 해는 쉽게 구할 수 있었으며, 실제로 (2.32)와 같은 해를 직접 유도하고 검증할 수 있었습니다. 그러나 유계 영역(bounded domain)으로 제한하면 해를 제시하는 것이 더 어려울 수 있으며, 이를 위해 확률론적 해석이 유용합니다.

$U \subset \mathbb{R}^d$를 유계 영역이라 합시다. 초기 온도 $f(x), x \in U$가 주어졌고, 모든 시간에서 경계에서의 온도를 0으로 고정한다고 가정합시다. 경계가 절 2.3에서 설명한 바와 같이 정칙(regular)하다고 가정합니다. $u(t, x) = u(t, x; U)$를 시간 $t$, 점 $x$에서의 온도라고 하면, $u(t, x)$는 다음을 만족합니다:

$$u(0, x) = u(0^+, x) = f(x), \quad x \in U$$
$$(2.35) \quad u(t, x) = 0, \quad x \in \partial U$$
$$x \mapsto u(t, x) \text{는 } t > 0 \text{일 때 } U \text{에서 연속임}$$
$$(2.36) \quad \partial_t u(t, x) = \frac{1}{2} \Delta_x u(t, x), \quad t > 0, \, x \in U$$

열방정식 (2.36)의 유도는 $\mathbb{R}^d$의 경우와 유사합니다. 본질적으로 $x \in U$이고 $t$가 매우 작으면, $x$ 주변의 열 흐름에 미치는 경계의 효과는 최소입니다(그리고 $t$가 0으로 갈수록 효과는 0으로 갑니다). 따라서 비유계 경우와 동일한 미분 방정식을 얻습니다. (2.35)와 (2.36)을 만족하는 함수의 집합은 벡터 공간을 이룸에 유의하십시오.

여전히 열은 브라운 운동을 하는 열 입자들에 의해 주어진다는 해석을 유지하지만, 이러한 입자들은 경계에 도달하면 소멸(destroyed)됩니다. $W_t$를 그러한 브라운 운동이라 하고, $T = T_U = \inf \{ t : W_t \notin U \}$라 하며, $p(t, x, y, U)$를 $W_0 = x$이고 시간 $t$까지 입자가 경계에서 소멸되지 않았다고 가정할 때 $y$에서의 밀도라 합시다. 더 정확하게는, $V \subset U$이면 다음이 성립합니다:

$$\mathbb{P}\{W_t \in V, T > t \mid W_0 = x\} = \int_V p(t, x, y, U) \, ddy$$

식 (2.27)은 다음과 같이 됩니다:

$$u(t, x; U) = \mathbb{E} [f(W_t) 1_{\{T > t\}} \mid W_0 = x] = \int_U f(y) p(t, x, y, U) \, ddy$$

이 방정식의 유도는 $p(t, x, y, U) = p(t, y, x, U)$를 사용합니다. 이 등식은 전체 평면의 경우만큼 명확하지 않지만, $U$ 내부에 머무르는 $x$에서 $y$로 가는 임의의 "경로(path)"에 대해, 역방향으로 탐색하여 얻은 $U$ 내부에 머무르는 $y$에서 $x$로 가는 대응하는 경로가 존재합니다.

### 2.5.1. 1차원 (One dimension)

$d = 1, U = (0, \pi)$라 가정합시다. 함수의 무한급수(infinite series of functions) 형태로 열방정식을 정확하게 풀 수 있습니다. (2.35)와 (2.36)을 만족하는 다음 형태의 해를 찾는 것으로 시작합니다:

$$u(t, x) = e^{-\lambda t} \phi(x)$$

이 함수는 다음을 만족할 때 (2.36)을 만족합니다:

$$\phi''(x) = -2\lambda \phi(x)$$

이는 일반해 $\phi(x) = c_1 \sin(\sqrt{2\lambda} x) + c_2 \cos(\sqrt{2\lambda} x)$를 가집니다. 경계 조건 $u(t, 0) = u(t, \pi) = 0$을 부과하면 다음 해들을 얻습니다:

$$\phi_k(x) = \sin(kx), \quad \lambda_k = \frac{k^2}{2}, \quad k = 1, 2, \dots$$

해의 선형 결합(linear combinations)도 해이므로, 다음 형태의 해들의 가족을 얻습니다:

$$(2.37) \quad u(t, x) = \sum_{k=1}^\infty a_k e^{-k^2 t / 2} \sin(kx)$$

이 시점에서, 약간 주의할 필요가 있습니다. $a_k$ 중 유한 개를 제외한 나머지가 모두 0이면, 이것은 유한합이며 해를 제공합니다. 그렇지 않으면 급수의 수렴(convergence)과 이 무한합이 열방정식을 만족하는지 걱정해야 합니다. 현재는 그 문제를 무시하고 형식적인 계산을 수행합시다. $t = 0$을 대입하면

$$u(0, x) = \sum_{k=1}^\infty a_k \sin(kx)$$

를 얻습니다. 이것이 $f$와 같기를 원한다면, 이를 만족하는 계수 $a_k$를 찾아야 합니다. 이것은 푸리에 급수(Fourier series)의 한 예입니다. 형식적인 계산을 계속하여, 다음이 성립한다고 가정하면

$$(2.38) \quad f(x) = \sum_{k=1}^\infty a_k \sin(kx)$$

계수 $a_k$를 계산합니다. 간단한 계산을 통해 다음을 얻습니다:

$$\int_0^\pi \sin(jx) \sin(kx) \, dx = \begin{cases} 0, & j \neq k \\ \pi/2, & j = k \end{cases}$$

적분에 대한 합 법칙을 사용하면(무한합이라는 사실은 일단 무시합니다!),

$$\int_0^\pi f(x) \sin(kx) \, dx = \sum_{j=1}^\infty \int_0^\pi a_j \sin(jx) \sin(kx) \, dx = \frac{\pi}{2} a_k$$

이것은 다음을 제공합니다:

$$(2.39) \quad a_k = \frac{2}{\pi} \int_0^\pi f(x) \sin(kx) \, dx$$

이제 수렴 문제로 돌아옵시다. 연속 함수 $f$로 시작하여 위와 같이 $a_k$를 정의합시다. (2.38)은 어떤 의미에서 참일까요? 즉,

$$(2.40) \quad f_n(x) = \sum_{k=1}^n a_k \sin(kx)$$

라 할 때, 함수 $f_n$이 $f$로 수렴할까요? 불행히도 모든 연속 함수 $f$와 모든 $x$에 대해 $f_n(x) \to f(x)$인 것은 아닙니다. 그러나 수렴의 정의를 변경하면, 항상 수렴을 얻을 수 있습니다.

> **♦ 정리: 수렴의 정의**
> 함수 수렴에 대한 많은 비동치적(nonequivalent) 정의가 존재합니다. 이는 단순히 수학자들이 많은 정의를 가지길 원해서가 아닙니다! 여기서 함수에 대한 점별 수렴(pointwise convergence) 개념은 매우 자연스럽지만 모든 함수에 대해 수렴이 유지되지는 않습니다. 다른 수렴 개념을 선택하면 모든 함수가 수렴하도록 할 수 있습니다.

모든 연속 함수 $f$에 대해, (2.40)으로 정의된 $f_n$은 평균 제곱(mean-square) 또는 $L^2$ 의미에서 $f$로 수렴합니다; 즉,

$$\lim_{n\to\infty} \int_0^\pi [f(x) - f_n(x)]^2 \, dx = 0$$

이 정리의 전체 증명은 생략하겠지만, 증명 과정에서 파르세발의 항등식(Parseval’s identity, 피타고라스 정리의 또 다른 형태!)을 다음 계산을 정당화함으로써 유도합니다:

$$\int_0^\pi f(x)^2 \, dx = \int_0^\pi \left[ \sum_{k=1}^\infty a_k \sin(kx) \right]^2 \, dx$$
$$= \sum_{j=1}^\infty \sum_{k=1}^\infty a_j a_k \int_0^\pi \sin(jx) \sin(kx) \, dx = \sum_{k=1}^\infty \frac{\pi}{2} a_k^2$$

특히 $\sum a_k^2 < \infty$입니다. 이것이 $\sum |a_k| < \infty$임을 내포하지는 않습니다. 그러나 이것은 $t > 0$이면 각 $x$에 대해 (2.37)의 합이 절대 수렴함을 내포합니다.

우리는 열방정식을 유도하기 위해 브라운 운동으로부터의 직관을 사용할 수 있습니다. 반대로, 브라운 운동을 연구하기 위해 열방정식의 해를 사용할 수 있습니다. $U = (0, \pi)$에서 경계점에 도달하면 소멸되는 브라운 운동을 고려해 봅시다. 살아남았다고 가정하고 $y$에서 시작하는 브라운 입자의 밀도를 계산할 수 있습니다.

이는 형식적인 초기 조건 $f(x) = \delta(y - x)$에 대응합니다. 이 초기 조건을 갖는 열방정식의 해는 밀도 $p(t, y, x, U)$가 되어야 합니다. 델타 함수의 형식적인 성질을 사용하면 다음을 얻습니다:

$$\int_0^\pi \delta(y - x) \sin(kx) \, dx = \sin(ky)$$

(2.39)에 대입하면 $a_k = (2/\pi) \sin(ky)$를 얻고, 따라서 다음을 얻습니다:

$$p(t, y, x, U) = \frac{2}{\pi} \sum_{k=1}^\infty e^{-k^2 t / 2} \sin(kx) \sin(ky)$$

다음이 성립함에 유의하십시오:

$$\left| \sum_{k=2}^\infty e^{-k^2 t / 2} \sin(kx) \sin(ky) \right| \le \sum_{k=2}^\infty e^{-kt} = \frac{e^{-2t}}{1 - e^{-t}}$$

따라서 $t \to \infty$에 따라 우변의 합은 $k = 1$ 항에 의해 지배됩니다:

$$p(t, y, x, U) \sim \frac{2}{\pi} e^{-t/2} \sin(x) \sin(y), \quad t \to \infty$$

다음이 성립함에 유의하십시오:

$$\int_0^\pi \frac{2}{\pi} e^{-t/2} \sin(x) \sin(y) \, dx = \frac{4}{\pi} e^{-t/2} \sin y$$

이를 해석해 봅시다. $y$에서 브라운 운동을 시작하면, 매우 큰 시간 $t$에서 입자가 (0, \pi)를 떠나지 않았을 확률은 약 $(4/\pi) e^{-t/2} \sin y$입니다. 도메인을 떠나지 않았다고 가정할 때 입자가 있을 것으로 예상되는 확률 밀도는 $(1/2) \sin x$입니다. 이 마지막 밀도는 $y$에 의존하지 않음에 유의하십시오 — 매우 긴 시간에서, 도메인에 머무른다는 조건 하에 입자의 위치는 시작점과 독립적입니다. 즉, 입자는 시작점을 잊어버립니다. 랜덤 워크의 경우와 유사한 결과를 얻었지만, 랜덤 워커가 잊지 못하는 것(시작점이 짝수인지 홀수인지)이 있습니다.

### 2.5.2. 고차원 (Many dimensions)

변수 분리법(separation of variables)이라는 동일한 아이디어를 사용하여 $\mathbb{R}^d$ 내의 유계 영역 $U$에서 열방정식을 풀 수 있습니다. 다시, $u_j(t, x) = e^{-\lambda_j t} \phi_j(x)$ 형태의 해를 찾습니다. 이는 다음을 만족할 때 경계 조건을 만족하는 해를 제공합니다:

$$(2.41) \quad \frac{1}{2} \Delta \phi_j(x) = -\lambda_j \phi_j(x), \quad \phi_j \equiv 0 \text{ on } \partial U$$

함수 $\phi_j$를 디리클레 경계 조건을 갖는 라플라시안의 고유함수(eigenfunction)라 부르며, 고유값은 $-\lambda_j$입니다. 이는 각 영역에 대해 다음 문제로 이어집니다: (2.41)을 만족하는 완벽한 고유함수의 가족(complete family of eigenfunctions)을 찾을 수 있을까요? 즉, 모든 초기 조건 $f$를 다음과 같이 쓸 수 있을 만큼 충분히 많은 그러한 함수를 찾을 수 있을까요?

$$(2.42) \quad f(x) = \sum_{k=1}^\infty a_k \phi_k(x)$$

경계에서 열이 소실되므로 시간이 지남에 따라 증가하는 해는 없을 것으로 예상합니다 — 따라서 $\lambda_j > 0$을 예상합니다. 마이너스 부호를 넣었으므로, $\lambda_j$는 $-\frac{1}{2}\Delta$에 대한 고유값입니다. 매우 일반적인 조건 하에서 그러한 함수를 찾을 수 있으며 고유값은 다음과 같이 정렬될 수 있습니다:

$$\lambda_1 < \lambda_2 \le \lambda_3 \le \cdots$$

그리고 고유함수 $\phi_j$는 정규 직교(orthonormal)가 되도록 선택될 수 있습니다:

$$\langle \phi_j, \phi_k \rangle := \int_U \phi_j(x) \phi_k(x) \, ddx = \begin{cases} 0, & j \neq k \\ 1, & j = k \end{cases}$$

(1차원의 경우 정규 직교 고유함수는 $\phi_j(x) = \sqrt{2/\pi} \sin(jx)$였습니다.) $U$ 위의 모든 연속 함수 $f$는 다음을 만족하는 일반화된 푸리에 급수 (2.42)로 작성될 수 있습니다:

$$\sum_{k=1}^\infty a_k^2 < \infty$$

여기서 합은 평균 제곱 또는 $L^2$ 의미에서의 수렴입니다. 계수는 다음과 같이 주어집니다:

$$a_k = \langle f, \phi_k \rangle = \int_U f(x) \phi_k(x) \, ddx$$

초기 조건 $f$를 갖는 열방정식의 해는 다음과 같습니다:

$$u(t, x) = \sum_{k=1}^\infty a_k e^{-\lambda_k t} \phi_k(x)$$

초기 조건이 $y$에서의 "델타 함수"인 해를 원한다면, $a_k = \int_U \delta(y - x) \phi_k(x) \, ddx = \phi_k(y)$를 선택하고 다음을 얻습니다:

$$p(t, y, x; U) = p(t, x, y; U) = \sum_{k=1}^\infty e^{-\lambda_k t} \phi_k(x) \phi_k(y)$$

첫 번째 등식은 $U$ 내부에 머무르는 $x$에서 $y$로 가는 각 경로에 대해 $y$에서 $x$로 가는 대응하는 경로가 존재한다는 사실을 이용합니다. $y$에서 브라운 운동을 시작하면, $U$ 안에 여전히 존재할 확률은 점근적으로 $c e^{-\lambda_1 t} \phi_1(y)$이며, $U$에 머물러 있다고 조건부될 때 입자가 있을 확률 밀도는 약 $c^{-1} \phi_1(x)$입니다. 여기서 $c = \int_U \phi_1(x) \, ddx$입니다. 이 마지막 밀도는 $y$에 의존하지 않습니다 — 매우 긴 시간에서, 도메인에 머무른다는 조건 하에 입자의 위치는 시작점과 독립적입니다. 즉, 입자는 시작점을 잊어버립니다.

> **예제 2.13 (Example 2.13 - 원판 위의 라플라시안)**  
> 물리학에서 발생하는 많은 특수 함수들은 영역 위의 라플라시안의 고유함수들입니다. $U = \{x \in \mathbb{R}^2 : |x| < 1\}$이라 합시다. 우리는 다음 방정식의 해를 찾을 것입니다:
>
> $$\frac{1}{2} \Delta \phi(x) = -\lambda \phi(x), \quad \phi \equiv 0 \text{ on } \partial U$$
>
> 변수 분리법을 사용하여 $\phi(r, \theta) = h(r) g(\theta)$ 형태의 해를 찾습니다. 그러면,
>
> $$\Delta \phi(r, \theta) = \left( h''(r) + r^{-1} h'(r) \right) g(\theta) + r^{-2} h(r) g''(\theta)$$
>
> 이것이 $-2\lambda h(r) g(\theta)$와 같기를 원한다면,
>
> $$(2.43) \quad \frac{r^2 h''(r) + r h'(r) + 2 r^2 \lambda h(r)}{h(r)} = -\frac{g''(\theta)}{g(\theta)} = \beta$$
>
> 좌변은 $r$의 함수이고 우변은 $\theta$의 함수입니다. 이들이 같기 위해서는 상수 $\beta$와 같아야 합니다. $g$는 주기 $2\pi$를 가지므로 가능한 선택은 $\beta_j = j^2$이고 $\phi_j(\theta) = \sin(j\theta), \psi_j(\theta) = \cos(j\theta)$입니다. (j = 0인 경우 코사인 함수만 0이 아닙니다.) 그러면 $h$는 다음을 만족합니다:
>
> $$h''(r) + \frac{1}{r} h'(r) + \left( 2\lambda - \frac{j^2}{r^2} \right) h(r) = 0$$
>
> 경계값 $h(1) = 0$을 만족하는 이 방정식을 풀어야 합니다. $v(s) = h(s/\sqrt{2\lambda})$라 쓰면 이 방정식은 다음이 됩니다:
>
> $$v''(s) + \frac{1}{s} v'(s) + \left( 1 - \frac{j^2}{s^2} \right) v(s) = 0$$
>
> $s \to 0^+$일 때 유계(bounded)를 유지하는 이 방정식의 해(상수를 곱한 것 제외)는 하나뿐입니다. 이를 $j$차 베셀 함수(Bessel function)라고 합니다.
>
> 초기 함수 $f$가 방사 대칭(radially symmetric)이라고 가정하는 특수한 경우를 고려합시다. 우리는 $\phi(r, \theta) = h(r)$ 형태의 함수를 찾습니다. 이는 (2.43)에서 상수 $\beta = j^2 = 0$임을 요구하며, 따라서 $v(s) = h(s/\sqrt{2\lambda})$는 0차 베셀 방정식을 만족합니다:
>
> $$(2.44) \quad v''(s) + \frac{1}{s} v'(s) + v(s) = 0$$
>
> 이는 두 개의 선형 독립해를 갖는 2계 미분방정식입니다. 해를 닫힌 형식(closed form)으로 제공할 수는 없습니다. 0에서 유계이고 연속인 해는 (상수를 곱한 것 제외) 하나뿐입니다; $v(0) = 1$로 지정하면 유일하며 다음으로 주어질 수 있습니다 (연습문제 2.20):
>
> $$(2.45) \quad v(x) = J_0(x) := \frac{2}{\pi} \int_0^{\pi/2} \cos(x \cos \theta) \, d\theta$$
>
> 이것은 제1종 0차 베셀 함수입니다. (2.45)를 분석하면(연습문제 2.21), $J_0$의 근(roots)들이 증가 수열을 형성함을 알 수 있습니다:
>
> $$0 < r_1 < r_2 < r_3 < \cdots$$
>
> 따라서 $h_k(x) = J_0(r_k x)$인 함수들이 다음을 만족합니다:
>
> $$h_k''(x) + \frac{1}{x} h_k'(x) + r_k^2 h_k(x) = 0, \quad h_k(1) = 0$$
>
> 사실, 이 함수들은 직교합니다:
>
> $$\int_0^1 h_j(x) h_k(x) \, dx = 0, \quad j \neq k$$
>
> $\phi_k(x) = h_k(|x|)$라 설정하면 다음을 얻습니다:
>
> $$\Delta \phi_k(x) = -r_k^2 \phi_k(x), \quad \phi_k \equiv 0 \text{ on } \partial U$$
>
> 이는 방사 대칭인 고유함수의 완전한 집합(complete set)을 제공합니다.

> **♦ 정리: 베셀 함수의 역할**
> 베셀 함수 $J_0(x)$는 통상적인 푸리에 급수에서 $J(x) = \sin x$가 하는 역할과 유사한 역할을 합니다. $J$의 근은 양의 정수이므로 $h_k(x) = J(kx) = \sin(kx)$가 됩니다.

> **♦ 정리: 도메인의 조화성**
> 영역 위의 라플라시안에 대한 고유함수와 고유값은 때때로 해당 도메인의 조화(harmonics of the domain)라고 불립니다. 마지막 예제는 도메인에 대한 조화를 찾는 것이 미분 방정식을 연구하는 것으로 이어짐을 보여줍니다. 베셀 함수는 도메인 위의 라플라시안 및 기타 연산자를 연구할 때 발생하는 수학과 물리학의 많은 "특수 함수" 중 일부일 뿐입니다. 이러한 함수들에 대해서는 많이 알려져 있습니다 — 자세한 내용은 특수 함수에 관한 서적을 참조하십시오.

도메인 $U$에서 열방정식을 풀기 위해서는 고유함수와 고유값을 찾아야 합니다. 특히 절대값이 가장 작은 고유값 $-\lambda_1$이 중요합니다. 사실 $\lambda_1$은 항상 양수입니다(따라서 모든 고유값은 음수이며 다른 고유값들은 더 큰 절대값을 갖습니다). $t \to \infty$에 따라,

$$p(t, x, y; U) \sim e^{-\lambda_1 t} \phi_1(x) \phi_1(y)$$

좌변은 양수이므로, 고유함수 $\phi_1$은 엄밀하게 양수(또는 엄밀하게 음수)로 선택될 수 있는 것이 좋습니다. 이를 다른 관점에서 살펴봅시다; 편의상 $U$가 매끄러운 경계를 갖는다고 가정합시다. 그러면 그린 항등식(Green's identities)을 사용하여, $\partial U$에서 $f \equiv 0$을 만족하는 임의의 함수 $f$에 대해 다음을 볼 수 있습니다:

$$(2.46) \quad \langle -\Delta f, f \rangle = - \int_U f(x) \Delta f(x) \, dx = \int_U |\nabla f(x)|^2 \, dx > 0$$

---

## §2.6. 조화함수에 관한 추가 논의 (More on harmonic functions)

이 절에서는 조화함수(harmonic function)에 대한 추가적인 성질을 살펴봅니다. 특히 조화함수 공간의 구조와 도함수의 경계(bounds)에 대해 논의합니다.

그린 항등식(2.46)은 $f \equiv 0$ on $\partial U$인 임의의 함수 $f$에 대해 다음을 성립함을 보여줍니다:

$$\langle -\Delta f, f \rangle = - \int_U f(x) \Delta f(x) \, dx = \int_U |\nabla f(x)|^2 \, dx > 0$$

(이러한 이유로 $-\Delta$는 때때로 **양의 연산자(positive operator)**라고 불립니다.) 우리는 다음을 얻습니다:

$$2 \lambda_1 = \min \frac{\langle -\Delta f, f \rangle}{\langle f, f \rangle}$$

여기서 최소값은 $\partial U$ 위에서 0과 같은 모든 매끄러운 함수 $f$에 대해 계산됩니다. 이것은 정리 1.8의 연속적인 아날로그입니다. 이를 보이기 위해, $\lambda_1$에 연관된 고유함수인 $\phi_1$을 대입하면 우변의 최소값이 $\lambda_1$보다 크지 않음을 알 수 있습니다. 그러나 일반적인 $f$에 대해, 우리는

$$f(x) = \sum_{j=1}^\infty a_j \phi_j$$

라 쓸 수 있으며, 여기서 실제로 등식이 성립함을 알 수 있습니다.

> **♦ 정리: 그린 항등식 (Green's identity)**
> 사용된 그린 항등식은 다음과 같습니다:
>
> $$\int_U f \Delta g(x) \, ddx = \int_{\partial U} f (\nabla g \cdot n)(y) \, ds(y) - \int_U (\nabla f \cdot \nabla g)(x) \, ddx$$

### 2.6.1. 조화함수의 성질

$d \ge 2$이고 $U$가 $\mathbb{R}^d$의 열린 부분집합일 때, $U$ 상의 조화함수 $F$들의 집합은 무한 차원 벡터 공간(infinite dimensional vector space)입니다. $U$ 상에서 연속적으로 확장될 수 있는 이러한 함수 $F$들의 집합 또한 무한 차원 부분공간입니다. 조화함수는 몇 가지 멋진 성질들을 가지고 있습니다. 예를 들어, 다음 명제는 도함수들이 함수 값의 최대치(maximum)로 경계 지어질 수 있음을 보여줍니다.

> **명제 2.14 (Proposition 2.14)**  
> $U$가 $\mathbb{R}^d$의 열린 부분집합이고, $f$는 $U$ 상의 조화함수라고 합시다. $x \in U$에 대해,
>
> $$\rho(x) = \text{dist}(x, \partial U) = \inf \{ |x - y| : y \notin U \}$$
>
> 라 합시다. 그러면 다음이 성립합니다:
>
> $$|\nabla f(x)| \le \frac{d}{\rho} \sup_{x \in U} |f(x)|$$

**증명.** $M = \sup_{x \in U} |f(x)|$라 하고 $M < \infty$라고 가정합시다 (결과는 $M = \infty$인 경우 자명합니다). 먼저 $U$가 열린 단위 볼(open unit ball)이고, $x = 0$이며, $f$가 $\bar{U}$ 상의 연속 함수로 확장되는 경우를 고려합시다. 그러면 $M = \max_{x \in \bar{U}} |f(x)|$입니다. 우리는 다음을 알고 있습니다:

$$f(x) = \int_{\partial U} f(z) H(x, z) \, ds(z)$$

계산(연습문제 2.18)은 $|\nabla H(0, z)| = d/C_d$임을 보여줍니다. (여기서 $\nabla$는 첫 번째 성분에 대한 기울기를 나타냅니다.) 따라서,

$$|\nabla f(0)| = \left| \left( \nabla \int_{\partial U} f(y) H(x, z) \, ds(z) \right)_{x=0} \right|$$
$$\le \int_{\partial U} |f(z)| |\nabla H(0, z)| \, ds(z)$$
$$\le \int_{\partial U} M \frac{d}{C_d} \, ds(z) = M d$$

더 일반적으로, $r < \rho(x)$라 하고 $g(y) = f(x + ry)$라 합시다. 그러면 $g$는 $U$ 상에서 조화적인 연속 함수입니다. 또한 $\max_{y \in U} |g(y)| \le M$입니다. 따라서,

$$|\nabla g(0)| \le d M$$

그러나 $\nabla f(x) = r \nabla g(0)$입니다. 따라서,

$$r |\nabla f(x)| \le M$$

모든 $r < \rho(x)$에 대해 이것이 성립하므로, 명제가 증명되었습니다. $\quad \square$

우리는 이 명제를 이산 조화함수에 대해 증명했던 정리의 연속적 아날로그를 확립하는 데 사용합니다.

> **명제 2.15 (Proposition 2.15)**  
> $\mathbb{R}^d$ 상의 유계 조화함수는 상수 함수(constant functions)뿐이다.

**증명.** $f : \mathbb{R}^d \to \mathbb{R}$이 $\sup_x |f(x)| = M < \infty$를 만족한다고 합시다. 그러면 도메인 $U = \{x : |x| < 2R\}$에 이전 명제를 적용하면, 모든 $R < \infty$와 모든 $|x| < R$에 대해 다음을 알 수 있습니다:

$$|\nabla f(x)| \le \frac{M d}{R}$$

따라서 모든 $x$에 대해 $\nabla f(x) = 0$이고, 그러므로 $f$는 상수입니다. $\quad \square$

단위 원판에 대한 포아송 커널이 명시적으로 주어지기 때문에 많은 계산을 수행할 수 있습니다. 대부분의 도메인에 대해서는 커널의 명시적인 형태를 제공하는 것이 불가능합니다. 그러나 일부 도메인의 경우 변수 분리법(separation of variables)을 효과적으로 사용할 수 있습니다.

> **예제 2.16 (Example 2.16)**  
> $U = \{(x, y) \in \mathbb{R}^2 : 0 < x < 1, 0 < y < \pi\}$인 직사각형이라 합시다. $U$의 경계는 4개의 선분으로 구성됩니다. 우리는 세 개의 선분에서는 경계값이 0이고, $\partial^* = \{(1, y) : 0 \le y \le \pi\}$에서는 0이 아닐 수 있는 조화함수 $F$를 고려할 것입니다. 간단한 계산은 다음 함수가 $U$에서 조화적(사실 $\mathbb{R}^2$에서 조화적)임을 보여줍니다:
>
> $$\phi_j(x, y) = \sinh(jx) \sin(jy)$$
>
> 더 나아가, $j$가 양의 정수이면 $\phi_j \equiv 0$은 $\partial^*$를 제외한 3개의 경계 선분 위에서 만족됩니다. $F$가 $\partial^*$ 상에서 $F(1, y) = g(y)$ (여기서 $g : [0, \pi] \to \mathbb{R}$)로 정의된다고 합시다. 그러면 다음 형태의 함수를 원합니다:
>
> $$F(x, y) = \sum_{j=1}^\infty a_j \sinh(jx) \sin(jy)$$
>
> 여기서 상수 $a_j$는 다음을 만족하도록 선택됩니다:
>
> $$g(y) = \sum_{j=1}^\infty a_j \sinh(j) \sin(jy)$$
>
> 이것은 $g$에 대한 푸리에 급수이며, 따라서 $a_j \sinh(j) = \frac{2}{\pi} \int_0^\pi g(z) \sin(jz) \, dz$로 선택해야 함을 확인했습니다.

---

#### 📐 주요 수식 및 개념 정리 (LaTeX)

1. **라플라시안의 성질과 양의 연산자:**
   - 그린 항등식: $\langle -\Delta f, f \rangle = \int_U |\nabla f(x)|^2 \, dx > 0$ ($\partial U$에서 $f=0$일 때)
   - 최소 고유값 $\lambda_1$: $2 \lambda_1 = \min \frac{\langle -\Delta f, f \rangle}{\langle f, f \rangle}$

2. **조화함수의 미분 경계 (Proposition 2.14):**
   - $|\nabla f(x)| \le \frac{d}{\rho} \sup_{x \in U} |f(x)|$
   - $\rho = \text{dist}(x, \partial U)$

3. **리우빌 정리의 조화함수 버전 (Proposition 2.15):**
   - $\mathbb{R}^d$ 상의 유계 조화함수는 상수 함수뿐이다. (경계가 무한히 확장될 때 도함수 $\nabla f$가 0으로 수렴함에 기인)

4. **직사각형 도메인의 조화함수 예제 (Example 2.16):**
   - 해의 형태: $F(x, y) = \sum_{j=1}^\infty a_j \sinh(jx) \sin(jy)$
   - 경계 조건 및 푸리에 계수: $a_j \sinh(j) = \frac{2}{\pi} \int_0^\pi F(1, z) \sin(jz) \, dz$
