# 제1장. 랜덤 워크와 이산 열방정식
**(Chapter 1. Random Walk and Discrete Heat Equation)**

---

## §1.1. 단순 랜덤 워크 (Simple random walk)

우리는 랜덤 워크의 가장 기본적인 모델 중 하나인 정수 격자 $\mathbb{Z}^d$ 상에서의 **단순 랜덤 워크(simple random walk)**를 고려한다. 각 시간 단계마다, 무작위 이동자(random walker)는 격자 방향 중 하나로 길이가 1인 무작위 이동을 수행한다.

---

### 1.1.1. 1차원 (One dimension)

우리는 정수 집합($\mathbb{Z}$) 위에서의 단순 랜덤 워크를 연구하는 것부터 시작한다. 각 시간 단위(time unit)마다, 워커는 공정한 동전(fair coin)을 던져 동전의 앞면 또는 뒷면이 나오느냐에 따라 오른쪽으로 1단계 또는 왼쪽으로 1단계 이동한다. 

시간 $n$에서의 워커의 위치를 $S_n$이라고 하자. 워커가 위치 $x$에서 출발한다고 가정하면, 다음과 같이 나타낼 수 있다:

$$S_n = x + X_1 + \cdots + X_n$$

여기서 $X_j$는 $\pm 1$의 값을 가지며, 시간 $j - 1$과 시간 $j$ 사이의 위치 변화(증분, increment)를 나타낸다. 더 정확히 말하면, 증분들 $X_1, X_2, \ldots$는 다음 확률 분포를 만족하는 **독립 확률 변수(independent random variables)**이다:

$$\mathbb{P}\{X_j = 1\} = \mathbb{P}\{X_j = -1\} = \frac{1}{2}$$

워커가 원점($x = 0$)에서 출발한다고 가정하자. 이때 자연스럽게 던지게 되는 질문은 다음과 같다:

* **평균적으로, 워커는 시작점으로부터 얼마나 멀리 떨어져 있는가?**

---


                       S_n
                     3 |
                       |
                     2 |        •       •
                       |       / \     / \
                     1 |      •   •---•   •
                       |     /             \
                     0 |----•---------------•-------•---> n
                       |   0  1   2   3   4   5   6 \ 7 / 8
                    -1 |                             •
                       |
                    -2 |
                       |
                    -3 |

---
**그림 1. $x=0$에서의 1차원 랜덤 워크 (Figure 1. One dimensional random walk with $x = 0$)**

* **추가적인 자연스러운 질문들:**
  * 특정 시점에 워커가 원점에 위치할 확률은 얼마인가? (*What is the probability that at a particular time the walker is at the origin?*)
  * 더 일반적으로, 워커의 위치에 대한 확률 분포는 어떻게 되는가? (*More generally, what is the probability distribution for the position of the walker?*)
  * 무작위 이동자는 계속해서 원점으로 돌아오는가, 아니면 결국 영원히 떠나버리는가? (*Does the random walker keep returning to the origin or does the walker eventually leave forever?*)

---

확률론자들은 이산 확률 변수(discrete random variables)에 대해 정의되는 **기댓값**(expectation, 기대값/평균값/expected value, mean, average value)을 표기하기 위해 $\mathbb{E}$ 기호를 사용한다:

$$\mathbb{E}[X] = \sum_{z} z \, \mathbb{P}\{X = z\}$$

$+1$과 $-1$의 이동 단계가 동일한 확률로 발생하기 때문에, 랜덤 워크는 다음을 만족한다:

$$\mathbb{E}[S_n] = 0$$

평균 거리(average distance)를 계산하기 위해, 누군가는 $\mathbb{E}[|S_n|]$을 계산하려고 시도할 수 있다. 하지만 $\mathbb{E}[S_n^2]$을 계산하는 것이 훨씬 쉽다는 것이 밝혀졌다:

$$\mathbb{E}[S_n^2] = \mathbb{E}\left[ \left( \sum_{j=1}^n X_j \right)^2 \right] = \mathbb{E}\left[ \sum_{j=1}^n \sum_{k=1}^n X_j X_k \right] = \sum_{j=1}^n \sum_{k=1}^n \mathbb{E}[X_j X_k] = n + \sum_{j \neq k} \mathbb{E}[X_j X_k]$$

> **♦ 정리: 기댓값의 합 규칙 (Linearity of Expectation)**
> 이 계산은 평균값의 중요한 성질인 다음을 사용합니다:
> $$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$
> 확률 변수들이 서로 종속(dependent)적이더라도 합의 평균이 평균의 합과 같다는 사실은 증명하기는 쉽지만 놀라울 수 있습니다. 예를 들어 $n$개의 일반적인 6면체 주사위를 굴릴 때, 주사위 하나를 던져 그 나온 눈을 $n$번 사용하든, $n$개의 다른 주사위를 굴려 더하든 합의 기댓값은 항상 $(7/2)n$입니다. 첫 번째 경우 합은 $n, 2n, \ldots, 6n$의 6가지 가능성을 각각 $1/6$ 확률로 가지지만, 두 번째 경우 합의 확률 분포는 명시적으로 작성하기 어렵습니다.

$j \neq k$인 경우, $(X_j, X_k)$의 가능성은 4가지입니다. 그 중 두 경우 $X_j X_k = 1$이고 두 경우 $X_j X_k = -1$입니다. 따라서 $j \neq k$일 때 $\mathbb{E}[X_j X_k] = 0$이며, 다음을 얻습니다:

$$\text{Var}[S_n] = \mathbb{E}[S_n^2] = n$$

여기서 $\text{Var}$는 확률 변수의 **분산(variance)**을 나타내며 다음과 같이 정의됩니다:

$$\text{Var}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

(간단한 계산으로 두 번째 등식이 성립함을 알 수 있습니다). 우리의 계산은 합의 분산에 대한 중요한 사실을 보여줍니다: 만약 $X_1, \ldots, X_n$이 독립이라면, 다음이 성립합니다:

$$\text{Var}[X_1 + \cdots + X_n] = \text{Var}[X_1] + \cdots + \text{Var}[X_n]$$

> **♦ 정리: 피타고라스 정리와의 기하학적 유추**
> 기댓값의 합 규칙과 교차 항 $\mathbb{E}[X_j X_k]$가 사라지는(vanish) 사실은 확률 변수 제곱의 평균을 다른 거듭제곱보다 훨씬 쉽게 계산하게 해줍니다. 여러 면에서 이는 기하학의 피타고라스 정리와 유추됩니다. 확률 변수들이 독립이고 평균이 0이라는 사실에서 유도되는 $\mathbb{E}[X_j X_k] = 0$ 성질은 벡터의 수직성(perpendicularity) 또는 직교성(orthogonality)의 대응물(analogue)입니다.

$n$ 단계 후 워커가 원점에 있을 확률을 찾는 것은 $\mathbb{E}[S_n^2]$을 계산하는 것보다 어렵습니다. 하지만 우리의 계산을 통해 확률의 크기를 추측할 수 있습니다. $\mathbb{E}[S_n^2] = n$이므로 원점으로부터의 일반적인(typical) 거리는 $O(\sqrt{n})$ 차원입니다. 시작점으로부터 거리가 최대 $\sqrt{n}$ 이내인 정수가 약 $\sqrt{n}$개 존재하므로, 특정 지점에 있을 확률은 상수 곱하기 $n^{-1/2}$ 형태로 감쇠할 것이라 추측할 수 있습니다. 이는 우리가 확률을 정확히 계산함으로써 실제로 그러함을 증명하게 됩니다.

홀수 번의 단계 후 워커는 홀수 정수에, 짝수 번의 단계 후에는 짝수 정수에 위치함을 쉽게 알 수 있습니다. 따라서 $n + x$가 홀수이면 $\mathbb{P}\{S_n = x\} = 0$입니다. 워커가 $2n$이라는 짝수 번의 단계를 거쳤다고 가정합시다. 시간 $2n$에 원점으로 돌아오려면 워커는 $n$번의 "+1" 단계와 $n$번의 "-1" 단계를 거쳐야 합니다. 어느 $n$번의 단계가 +1인지 선택하는 방법의 수는 $\binom{2n}{n}$이며, +1과 -1들의 각 특정 선택이 일어날 확률은 $2^{-2n}$입니다. 따라서:

$$\mathbb{P}\{S_{2n} = 0\} = \binom{2n}{n} 2^{-2n} = \frac{(2n)!}{n! n!} 2^{-2n}$$

더 일반적으로, 워커가 $2j$에 위치하려면 $(n + j)$번의 +1 단계와 $(n - j)$번의 -1 단계가 있어야 합니다. +1 단계의 개수에 대한 확률은 매개변수 $2n$과 $1/2$을 갖는 이항 분포(binomial distribution)에 의해 주어집니다:

$$\mathbb{P}\{S_{2n} = 2j\} = \binom{2n}{n + j} 2^{-2n} = \frac{(2n)!}{(n + j)!(n - j)!} 2^{-2n}$$

이 식들은 정확하지만, 매우 큰 수들의 비율을 포함하고 있어 어떻게 활용해야 할지 직관적으로 명확하지 않습니다. 우변의 표현을 이해하는 것은 $n$이 커질 때 $n!$의 행동을 연구하는 것으로 이어지며, 이것이 다음 절의 목표입니다.

---

### 1.1.2. 스털링 공식 (Stirling's formula)

**스털링 공식(Stirling's formula)**은 $n \to \infty$일 때 다음이 성립함을 나타냅니다:

$$n! \sim \sqrt{2\pi} \, n^{n+\frac{1}{2}} \, e^{-n}$$

여기서 $\sim$ 기호는 양변의 비율이 1로 수렴함을 의미합니다. 우리는 다음 두 소절에 걸쳐 이를 증명할 것입니다. 이 소절에서는 다음을 만족하는 양의 상수 $C_0$가 존재함을 증명합니다:

$$(1.1) \quad \lim_{n \to \infty} b_n = C_0, \quad \text{단, } b_n = \frac{n!}{n^{n+\frac{1}{2}} e^{-n}}$$

그리고 1.1.3절에서 $C_0 = \sqrt{2\pi}$임을 보일 것입니다.

> **♦ 정리: 수열의 무한곱 수렴 조건**
> $a_n$이 무한대로 발산하는 양의 수열이라 하고, $a_n / f(n)$이 양의 상수 $L$로 수렴하도록 하는 양의 함수 $f(n)$을 찾으려 한다고 합시다. $b_n = a_n / f(n)$이라 놓으면:
> $$b_n = b_1 \prod_{j=2}^n \frac{b_j}{b_{j-1}} = b_1 \prod_{j=2}^n [1 + \delta_j], \quad \text{단, } \delta_j = \frac{b_j}{b_{j-1}} - 1$$
> 합이 수렴한다는 전제 하에 로그를 취하면 다음과 같습니다:
> $$\lim_{n \to \infty} \log b_n = \log b_1 + \lim_{n \to \infty} \sum_{j=2}^n \log[1 + \delta_j] = \log b_1 + \sum_{j=2}^\infty \log[1 + \delta_j]$$
> 수렴을 위한 필요조건은 $\delta_n \to 0$입니다. 로그의 테일러 급수는 $|\delta_n| \le 1/2$일 때 $|\log[1 + \delta_n]| \le c |\delta_n|$임을 보여주므로, 급수가 균등 수렴하기 위한 충분조건은 다음과 같습니다:
> $$\sum_{n=2}^\infty |\delta_n| < \infty$$
> 비록 이 논증이 극한이 존재함을 증명하지만, 극한의 값 자체를 결정해주지는 않습니다.

우선 $b_1 = e$임을 쉽게 확인할 수 있으며, $n \ge 2$일 때 다음과 같습니다:

$$(1.2) \quad \frac{b_n}{b_{n-1}} = e \left( \frac{n-1}{n} \right)^{n - \frac{1}{2}} = e \left( 1 - \frac{1}{n} \right)^n \left( 1 - \frac{1}{n} \right)^{-1/2}$$

$\delta_n = (b_n / b_{n-1}) - 1$이라 놓았을 때, 우리는 $\sum |\delta_n| < \infty$임을 보일 것입니다.

> **♦ 정리: 나머지 항을 가진 테일러 정리 (Taylor's Theorem with Remainder)**
> 극한을 결정하는 가장 중요한 도구 중 하나는 나머지 항을 포함한 테일러 정리입니다. $f$가 $C^{k+1}$ 함수, 즉 $k+1$개의 도함수가 모두 연속인 함수라고 합시다. $P_k(x)$를 원점 근처에서 $f$의 $k$차 테일러 다항식이라 하면, $x > 0$에 대해:
> $$|f(x) - P_k(x)| \le a_k x^{k+1}, \quad a_k = \frac{1}{(k+1)!} \max_{0 \le t \le x} |f^{(k+1)}(t)|$$
> 음수 $x$에 대해서도 $\tilde{f}(x) = f(-x)$를 고려하여 유사한 추정치를 얻습니다. 로그의 테일러 급수는 $|u| < 1$에 대해 다음과 같습니다:
> $$\log(1 + u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \cdots$$
> 나머지 항을 포함한 테일러 정리에 의해 모든 양의 정수 $k$에 대해:
> $$(1.3) \quad \log(1 + u) = P_k(u) + O(|u|^{k+1})$$
> 여기서 $P_k(u) = u - (u^2/2) + \cdots + (-1)^{k+1}(u^k/k)$ 입니다. $O(|u|^{k+1})$은 작은 $u$에 대해 상수 곱하기 $|u|^{k+1}$로 상한이 설정되는 항을 의미합니다. 예를 들어 $|u| \le 1/2$인 모든 $u$에 대해 다음을 만족하는 상수 $c_k$가 존재합니다:
> $$(1.4) \quad |\log(1 + u) - P_k(u)| \le c_k |u|^{k+1}$$
> 우리는 점근 분석 시 (1.3)과 같은 $O(\cdot)$ 표기법을 사용할 것이며, 이는 항상 (1.4)와 같은 엄밀한 명제의 축약 표현입니다.

우리는 $\delta_n = O(n^{-2})$, 즉 $|\delta_n| \le \frac{c}{n^2}$을 만족하는 상수 $c$가 존재함을 보일 것입니다.
이를 위해 $n$이 커짐에 따라 $e^{-1}$로 접근하는 $(1 - 1/n)^n$을 고려합니다. 테일러 급수를 사용하여 수렴 속도를 추정하면:

$$\log \left( 1 - \frac{1}{n} \right)^n = n \log \left( 1 - \frac{1}{n} \right) = n \left[ -\frac{1}{n} - \frac{1}{2n^2} + O(n^{-3}) \right] = -1 - \frac{1}{2n} + O(n^{-2})$$

그리고,

$$\log \left( 1 - \frac{1}{n} \right)^{-1/2} = \frac{1}{2n} + O(n^{-2})$$

(1.2)식에 로그를 취하고 항들을 더함으로써 (1.1)의 증명을 완료합니다. 실제로 다음을 보일 수 있습니다:

$$(1.5) \quad n! = C_0 \, n^{n+\frac{1}{2}} \, e^{-n} \left[ 1 + O(n^{-1}) \right]$$

---

### 1.1.3. 중심 극한 정리 (Central limit theorem)

이제 스털링 공식을 사용하여 랜덤 워커가 특정 위치에 있을 확률을 추정합니다. $S_0 = 0$이라 가정하고 정수 상의 단순 랜덤 워커 위치를 $S_n$이라 합시다. 모든 정수 $j$에 대해 이항 분포로부터 다음을 얻었습니다:

$$\mathbb{P}\{S_{2n} = 2j\} = \binom{2n}{n + j} 2^{-2n} = \frac{(2n)!}{(n + j)!(n - j)!} 2^{-2n}$$

$|j| \le n/2$라고 가정합시다. 스털링 공식을 대입하고 정리하면:

$$(1.6) \quad \mathbb{P}\{S_{2n} = 2j\} \sim \frac{\sqrt{2}}{C_0} \left( 1 - \frac{j^2}{n^2} \right)^{-n} \left( 1 + \frac{j}{n} \right)^{-j} \left( 1 - \frac{j}{n} \right)^j \left( \frac{n}{n^2 - j^2} \right)^{1/2}$$

실제로 (1.5)를 사용하면 양변의 비율이 1로부터 $c/n$ 이내의 거리에 있게 하는 상수 $c$가 존재합니다 ($|j| \le n/2$ 가정 하에).

$n \to \infty$ 일 때 이 식은 어떻게 될까요? 먼저 $j = 0$인 경우를 생각하면:

$$\mathbb{P}\{S_{2n} = 0\} \sim \frac{\sqrt{2}}{C_0 n^{1/2}}$$

이제 $j$가 $\sqrt{n}$ 차원인 경우를 고려합니다. 전형적인 거리가 $\sqrt{n}$ 차원이므로 확률이 상수 곱하기 $n^{-1/2}$ 형태여야 한다는 이전의 경험적 논증이 확증됩니다.

$S_{2n}$이 $\sqrt{n}$ 차원일 것으로 예상되므로 정수 $j$를 $j = r\sqrt{n}$으로 놓아봅시다. 그러면 (1.6)의 우변은 다음과 같이 변형됩니다:

$$\frac{\sqrt{2}}{C_0 \sqrt{n}} \left( 1 - \frac{r^2}{n} \right)^{-n} \left[ \left( 1 + \frac{r}{\sqrt{n}} \right)^{-\sqrt{n}} \right]^r \left[ \left( 1 - \frac{r}{\sqrt{n}} \right)^{-\sqrt{n}} \right]^{-r} \left( \frac{1}{1 - (r^2/n)} \right)^{1/2}$$

> **♦ 정리: 잘 알려진 지수 극한 공식**
> 우리는 $n \to \infty$ 일 때 다음의 잘 알려진 극한을 사용합니다:
> $$\left( 1 + \frac{a}{n} \right)^n \longrightarrow e^a$$
> 실제로 로그의 테일러 급수를 사용하면 $n \ge 2a^2$일 때 다음을 얻습니다:
> $$\log \left( 1 + \frac{a}{n} \right)^n = a + O\left(\frac{a^2}{n}\right) \implies \left( 1 + \frac{a}{n} \right)^n = e^a \left[ 1 + O\left(\frac{a^2}{n}\right) \right]$$

$n \to \infty$ 일 때, (1.6)의 우변은 다음으로 점근합니다:

$$\frac{\sqrt{2}}{C_0 \sqrt{n}} e^{r^2} e^{-r^2} e^{-r^2} = \frac{\sqrt{2}}{C_0 \sqrt{n}} e^{-j^2/n}$$

모든 $a < b$에 대해:

$$(1.7) \quad \lim_{n \to \infty} \mathbb{P}\{a\sqrt{2n} \le S_{2n} \le b\sqrt{2n}\} = \lim_{n \to \infty} \sum \frac{\sqrt{2}}{C_0 \sqrt{n}} e^{-j^2/n}$$

여기서 합은 $a\sqrt{2n} \le 2j \le b\sqrt{2n}$을 만족하는 모든 $j$에 대해 수행됩니다. 우변은 합의 간격 길이가 $\sqrt{2/n}$인 적분의 **리만 합 근사(Riemann sum approximation)**입니다. 따라서 극한은 다음과 같습니다:

$$\int_a^b \frac{1}{C_0} e^{-x^2/2} \, dx$$

이 극한 분포는 확률 분포여야 하므로 전체 구간에서의 적분값은 1이어야 합니다:

$$\int_{-\infty}^\infty \frac{1}{C_0} e^{-x^2/2} \, dx = 1$$

이로부터 상수 $C_0 = \sqrt{2\pi}$ 값을 얻게 되며, 따라서 스털링 공식은 다음과 같이 최종 완성됩니다:

$$n! = \sqrt{2\pi} \, n^{n+\frac{1}{2}} \, e^{-n} \left[ 1 + O(n^{-1}) \right]$$

---

### 1.1.4. 원점으로의 귀환 (Returns to the origin)

> **♦ 정리: p-급수의 수렴 조건**
> 다음 무한급수를 상기합시다:
> $$\sum_{n=1}^\infty n^{-a}$$
> 이 급수는 $a > 1$일 때 수렴하고, $a \le 1$일 때 발산합니다.

우리는 이제 무작위 이동자가 원점으로 돌아오는 횟수(number of times)를 고려합니다. $J_n = \mathbf{1}\{S_n = 0\}$이라 놓읍시다. 여기서 지시 함수(indicator function) 표기법을 사용합니다. 사건(event) $E$에 대해, $\mathbf{1}_E$ 또는 $\mathbf{1}(E)$는 사건이 발생하면 1의 값을 갖고, 발생하지 않으면 0의 값을 갖는 확률 변수입니다. 랜덤 워커가 원점을 방문한 총 횟수 $V$는 다음과 같습니다:

$$V = \sum_{n=0}^\infty J_{2n}$$

다음 기댓값을 살펴봅시다:

$$\mathbb{E}[V] = \sum_{n=0}^\infty \mathbb{E}[J_{2n}] = \sum_{n=0}^\infty \mathbb{P}\{S_{2n} = 0\}$$

우리는 $n \to \infty$ 일 때 $\mathbb{P}\{S_{2n} = 0\} \sim c/\sqrt{n}$임을 알고 있습니다. 따라서:

$$\mathbb{E}[V] = \infty$$

하지만 확률 변수가 유한한 값(finite)을 가지면서도 무한한 기댓값(infinite expectation)을 갖는 것은 가능하므로, $V$가 실제로 무한하다는 것을 증명하기 위해서는 추가적인 작업이 필요합니다.

> **♦ 정리: 상트페테르부르크의 역설 (St. Petersburg's Paradox)**
> 무한한 기댓값을 갖는 잘 알려진 확률 변수는 상트페테르부르크의 역설에서 얻어집니다. 뒷면(tails)이 나올 때까지 동전을 던지는 게임을 한다고 합시다. 뒷면이 나오기 전까지 $k$번의 앞면(heads)이 나왔다면, 당첨금(payoff)은 $2^k$입니다. 정확히 $k$번의 앞면이 나올 확률은 $k$번 연속 앞면이 나온 후 뒷면이 나올 확률이므로 $2^{-(k+1)}$입니다. 따라서 이 게임에서 기대 당첨금은 다음과 같습니다:
> $$2^0 \cdot \frac{1}{2} + 2^1 \cdot \frac{1}{2^2} + 2^2 \cdot \frac{1}{2^3} + \cdots = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \cdots = \infty$$
> 기댓값이 무한대이므로, 이 게임을 한 번 하기 위해 얼마든지 많은 돈을 지불해야 할 것처럼 보입니다. 그러나 이것은 분명 현실적이지 않으며, 여기에 역설이 존재합니다.

시간 0 이후 무작위 이동자가 원점으로 단 한 번이라도 재귀환(return)할 확률을 $q$라 합시다. 우리는 먼저 $q < 1$이라 가정하고 모순을 유도함으로써 $q = 1$임을 보일 것입니다.

$q < 1$이라고 가정합시다. 그러면 $V$의 확률 분포를 구할 수 있습니다. 예를 들어, $\mathbb{P}\{V = 1\} = (1 - q)$ 입니다. 왜냐하면 $V = 1$이라는 것은 워커가 시간 0 이후 다시는 원점으로 돌아오지 않는 것과 동치이기 때문입니다. 더 일반적으로, $k = 1, 2, \ldots$에 대해:

$$\mathbb{P}\{V = k\} = q^{k-1} (1 - q)$$

이는 기하분포(geometric distribution) 형태이며, $V$의 기댓값을 다음과 같이 계산할 수 있게 해줍니다:

$$\mathbb{E}[V] = \sum_{k=1}^\infty k \, \mathbb{P}\{V = k\} = \sum_{k=1}^\infty k \, q^{k-1} (1 - q) = \frac{1}{1 - q} < \infty$$

그러나 우리는 이미 $\mathbb{E}[V] = \infty$임을 알고 있습니다. 따라서 $q = 1$일 수밖에 없습니다.

이로써 다음 정리가 확립되었습니다.

**정리 1.1 (Theorem 1.1).**
(1차원) 단순 랜덤 워커가 원점으로 무한히 많이(infinitely often) 재귀환할 확률은 1이다.

이 정리는 워커가 $x \neq 0$에서 출발하더라도 원점에 도달할 확률이 1임을 의미한다는 점에 유의합시다.

> **♦ 정리: 재귀환 확률 $q$를 이용한 $\mathbb{E}[V]$의 대수적 계산**
> $q$를 이용하여 $\mathbb{E}[V]$를 계산하는 또 다른 방법은 다음과 같은 관계식을 사용하는 것입니다:
> $$\mathbb{E}[V] = 1 + q \, \mathbb{E}[V]$$
> 여기서 $1$은 첫 번째 방문(시간 0에서의 시작)을 나타내고, $q$는 원점으로 재귀환할 확률입니다. 핵심 관찰은 두 번째 방문이 존재한다는 조건 하에 첫 번째 방문 이후의 예상 방문 횟수가 정확히 원점에서 출발할 때의 예상 방문 횟수와 같다는 것입니다. 이 간단한 방정식을 풀면 $\mathbb{E}[V] = (1 - q)^{-1}$을 얻게 됩니다.

---

### 1.1.5. 다차원에서의 랜덤 워크 (Several dimensions)

우리는 이제 $d$차원 정수 격자(integer grid) 상에서의 무작위 이동자를 고려합니다:

$$\mathbb{Z}^d = \{(x_1, \dots, x_d) \mid x_j \in \mathbb{Z}\}$$

각 시간 단계마다, 랜덤 워커는 $2d$개의 가장 가까운 이웃(nearest neighbors) 중 하나를 각각 $1/(2d)$의 동일한 확률로 선택하여 해당 위치로 이동합니다. 입자의 위치를 다시 다음과 같이 표기합니다:

$$S_n = x + X_1 + \cdots + X_n$$

여기서 $x, X_1, \ldots, X_n, S_n$은 $\mathbb{Z}^d$ 상의 점들, 즉 정수 성분을 갖는 $d$차원 벡터(d-dimensional vectors)입니다. 증분 $X_1, X_2, \ldots$는 하나의 성분만 절댓값이 1이고 나머지 성분은 0인 단위 벡터(unit vectors)입니다.

내적(dot product)을 살펴보면, $X_j \cdot X_j = 1$입니다. $j \neq k$일 때, $X_j \cdot X_k$는 확률 $1/(2d)$로 $1$, 확률 $1/(2d)$로 $-1$, 나머지 확률로 $0$의 값을 갖습니다. 특히 기댓값을 취하면:

$$\mathbb{E}[X_j \cdot X_j] = 1, \quad \mathbb{E}[X_j \cdot X_k] = 0 \quad (j \neq k)$$

$S_0 = 0$이라 가정합시다. 그러면 $\mathbb{E}[S_n] = 0$ 이며, 1차원의 경우와 동일한 계산에 의해 다음을 얻습니다:

$$\mathbb{E}[|S_n|^2] = \mathbb{E}[S_n \cdot S_n] = \mathbb{E}\left[ \left(\sum_{j=1}^n X_j\right) \cdot \left(\sum_{j=1}^n X_j\right) \right] = n$$

```
   y
   |
  •---•---•
   |  |  |
--•---•---•-- x
   |  |  |
  •---•---•
   |
```
**그림 2. 정수 격자 $\mathbb{Z}^2$ (Figure 2. The integer lattice $\mathbb{Z}^2$)**

---

$S_0 = 0$이라 가정할 때, $n$ 단계 후 원점에 있을 확률은 얼마일까요? $n$이 홀수이면 이 확률은 0입니다. $n$이 짝수일 때, 경험적 논증(heuristic argument)을 제시해 보겠습니다.

1. 원점으로부터 $S_n$까지의 전형적인(typical) 거리는 $O(\sqrt{n})$ 차원입니다.
2. $d$차원 공간에서 거리가 $\sqrt{n}$ 이내인 격자점의 개수는 $(\sqrt{n})^d = n^{d/2}$에 비례하여 증가합니다.
3. 따라서 특정 지점을 선택할 확률은 상수 곱하기 $n^{-d/2}$ 형태로 감쇠할 것입니다.

이 직관을 조합론적으로 엄밀히 정당화하는 것은 1차원보다 다소 복잡하지만, 올바른 행동을 파악하기 위해 다음과 같이 설명할 수 있습니다: $2n$ 단계 동안 $d$개의 각 가능한 방향으로 약 $2n/d$번씩 이동할 것으로 기대됩니다 (예: $d=2$이면 약 $n$번의 수평 이동과 $n$번의 수직 이동). 원점에 위치하려면 $d$개의 각 방향 모두에서 짝수 번의 이동을 해야 합니다. 이 사건의 확률은 $2^{-(d-1)}$입니다. 각 방향의 이동 횟수가 짝수라는 조건 하에, 각 성분이 원점에 위치할 확률은 1차원 랜덤 워크가 시간 $2n/d$에 원점에 위치할 확률과 같습니다. 이 아이디어를 사용하면 다음 점근식(asymptotics)을 얻습니다:

$$\mathbb{P}\{S_{2n} = 0\} \sim \frac{c_d}{n^{d/2}}, \quad c_d = \frac{d^{d/2}}{\pi^{d/2} 2^{d-1}}$$

상수 $c_d$의 구체적인 값 자체는 중요하지 않지만, $n$의 지수가 $d/2$라는 사실은 매우 중요합니다.

원점으로의 예상 귀환 횟수를 고려해 봅시다. $V$가 원점 방문 횟수라면, $d=1$인 경우와 마찬가지로:

$$\mathbb{E}[V] = \sum_{n=0}^\infty \mathbb{P}\{S_{2n} = 0\} = \frac{1}{1 - q}$$

여기서 $q = q_d$는 $d$차원 워크가 원점으로 재귀환할 확률입니다. $\mathbb{P}\{S_{2n} = 0\} \sim c/n^{d/2}$이므로 무한급수의 수렴성(p-급수 판정법)에 의해:

$$\mathbb{E}[V] = \sum_{n=0}^\infty \mathbb{P}\{S_{2n} = 0\} = \begin{cases} < \infty, & d \ge 3 \text{ 일 때} \\ = \infty, & d = 1, 2 \text{ 일 때} \end{cases}$$

이로부터 폴리아(Pólya)의 유명한 정리가 도출됩니다.

**정리 1.2 (Theorem 1.2 - Polya's Theorem).**
$S_n$을 $S_0 = 0$인 $\mathbb{Z}^d$ 상의 단순 랜덤 워크라 하자.
1. $d = 1, 2$인 경우, 랜덤 워크는 **재귀적(recurrent)**이다. 즉, 확률 1로 원점으로 무한히 많이 재귀환한다 ($q_1 = q_2 = 1$).
2. $d \ge 3$인 경우, 랜덤 워크는 **비재귀적/일시적(transient)**이다. 즉, 확률 1로 원점으로 오직 유한 번만 귀환한다 ($q_d < 1$). 또한 $d \ge 3$일 때 다음이 성립합니다:
$$\mathbb{P}\{S_n \neq 0 \text{ for all } n > 0\} > 0$$

---

### 1.1.6. 확률에 관한 유의사항 (Notes about probability)

우리는 이미 확률에 대한 몇 가지 사실들을 암묵적으로 사용했습니다. 확률의 규칙 중 일부에 대해 보다 명시적으로 다루어 보겠습니다.

**표본 공간(sample space)** 또는 **확률 공간(probability space)**은 하나의 집합 $\Omega$이며, **사건(event)**들은 공집합 $\emptyset$과 전체집합 $\Omega$를 포함하는 $\Omega$의 부분집합들의 모임입니다. **확률 $\mathbb{P}$**는 사건에서 $[0, 1]$ 구간으로 가는 함수로서 $\mathbb{P}(\Omega) = 1$ 및 다음 **가산 가법성 규칙(countable additivity rule)**을 만족합니다:

* $E_1, E_2, \ldots$가 서로소인(disjoint, mutually exclusive) 사건들이라면, 다음이 성립한다:
$$\mathbb{P}\left( \bigcup_{n=1}^\infty E_n \right) = \sum_{n=1}^\infty \mathbb{P}(E_n)$$

우리는 $\mathbb{P}$가 $\Omega$의 모든 부분집합에 대해 정의된다고 가정하지는 않지만, 사건들의 모임이 가산 합집합(countable union)과 "여집합 연산(complementation)"에 대해 닫혀 있다고 가정합니다. 즉, $E_1, E_2, \ldots$가 사건들이면 $\bigcup E_j$ 와 $\Omega \setminus E_j$ 역시 사건입니다.

> **♦ 정리: 측도론(Measure Theory)과의 연관성**
> 확률에 관한 이러한 가정들은 측도론(measure theory)에서 측도를 정의할 때 사용하는 가정과 정확히 일치합니다. 우리는 이러한 확률의 존재성을 증명하는 데 수반되는 어려움에 대해서는 논의하지 않을 것입니다. 확률론의 많은 내용을 엄밀하게 다루기 위해서는 르베그 적분론(Lebesgue integration theory)을 사용할 필요가 있지만, 이 책에서는 이에 대해 걱정하지 않을 것입니다.

우리는 확률론자들이 항상 사용하는 한 가지 중요한 보조정리(lemma)에 대해 다루고자 합니다. 매우 쉽지만 고유한 이름을 가지고 있습니다. (수학자들은 아주 간단하더라도 자주 사용되는 보조정리에 이름을 붙여 쉽게 참조할 수 있도록 하는 경우가 매우 흔합니다.)

**보조정리 1.3 (Lemma 1.3 - 보렐-캉텔리 보조정리 / Borel-Cantelli Lemma).**
$E_1, E_2, \ldots$가 다음을 만족하는 사건들의 모임이라고 하자:

$$\sum_{n=1}^\infty \mathbb{P}(E_n) < \infty$$

그러면 확률 1로 이 사건들 중 오직 유한개(at most finitely many)만 발생한다.

**증명 (Proof).**
$E_1, E_2, \ldots$ 중 무한히 많은 사건이 발생하는 사건을 $A$라 하자.
각 정수 $N$에 대해, $A \subset A_N$이다. 여기서 $A_N$은 사건 $E_N, E_{N+1}, \ldots$ 중 적어도 하나가 발생하는 사건이다.
따라서,

$$\mathbb{P}(A) \le \mathbb{P}(A_N) = \mathbb{P}\left( \bigcup_{n=N}^\infty E_n \right) \le \sum_{n=N}^\infty \mathbb{P}(E_n)$$

그런데 $\sum_{n=1}^\infty \mathbb{P}(E_n) < \infty$ 조건에 의해 다음이 성립한다:

$$\lim_{N \to \infty} \sum_{n=N}^\infty \mathbb{P}(E_n) = 0$$

따라서 $\mathbb{P}(A) = 0$ 이다. $\blacksquare$

---

**적용 예시 (Application Example):**
$d \ge 3$인 경우의 $\mathbb{Z}^d$ 상의 단순 랜덤 워크를 고려하고, $E_n$을 $S_n = 0$인 사건이라 하자. 그러면 이전 절의 추정치에 의해 다음이 성립합니다:

$$\sum_{n=1}^\infty \mathbb{P}(E_n) < \infty$$

따라서 보렐-캉텔리 보조정리에 의해 확률 1로 사건 $E_n$ 중 오직 유한개만 발생합니다. 이는 확률 1로 랜덤 워크가 원점을 오직 유한 번만 방문한다는 사실(일시성, transience)을 재확인해 줍니다.

---

## §1.2. 경계값 문제 (Boundary value problems)

### 1.2.1. 1차원: 도박꾼의 파산 문제 (One dimension: gambler's ruin)

양의 정수 $N$이 주어지고, 무작위 이동자(random walker)가 $x \in \{0, 1, \ldots, N\}$에서 출발한다고 합시다. 시간 $n$에서의 이동자의 위치를 $S_n$이라 합시다. 이동자가 $0$ 또는 $N$에 도달하면 멈춘다고 가정합니다. 이를 보다 정밀하게 표현하기 위해 다음과 같이 정지 시간(stopping time) $T$를 정의합니다:

$$T = \min \{ n : S_n = 0 \text{ 또는 } N \}$$

그러면 시간 $n$에서의 이동자의 위치는 $\hat{S}_n = S_{n \wedge T}$ 로 주어집니다. 여기서 $n \wedge T$는 $n$과 $T$ 중 최솟값($\min(n, T)$)을 의미합니다. 확률 1로 $T < \infty$임을 쉽게 볼 수 있습니다. 즉, 결국 이동자는 $0$ 또는 $N$에 도달하여 정지합니다. 우리의 목표는 이동자가 어느 점에서 멈추는지 알아내는 것입니다.

함수 $F : \{0, \ldots, N\} \to [0, 1]$을 다음과 같이 정의합니다:

$$F(x) = \mathbb{P}\{S_T = N \mid S_0 = x\}$$

> **♦ 정리: 조건부 확률의 정의**
> $V_1, V_2$가 사건이고 $\mathbb{P}(V_2) > 0$일 때, $V_2$가 주어졌을 때 $V_1$의 조건부 확률 $\mathbb{P}(V_1 \mid V_2)$는 다음과 같이 정의됩니다:
> $$\mathbb{P}(V_1 \mid V_2) = \frac{\mathbb{P}(V_1 \cap V_2)}{\mathbb{P}(V_2)}$$

이 문제에 도박적 해석(gambling interpretation)을 제공할 수 있습니다: $S_n$을 매 판마다 칩 1개를 얻거나 잃는 공정한 게임을 하는 도박꾼이 현재 보유한 칩의 개수로 보는 것입니다. 도박꾼은 $x$개의 칩으로 시작하여 $N$개의 칩을 얻거나 파산($0$)할 때까지 게임을 지속합니다. 도박꾼이 파산하기 전에 $N$개의 칩을 달성할 확률이 $F(x)$입니다. 자명하게 다음과 같은 경계 조건(boundary conditions)이 성립합니다:

$$F(0) = 0, \quad F(N) = 1$$

$0 < x < N$이라 가정합시다. 첫 번째 게임 후, 도박꾼은 각각 $1/2$의 동일한 확률로 $x - 1$개 또는 $x + 1$개의 칩을 갖게 됩니다. 따라서 다음 차분 방정식(difference equation)이 성립합니다:

$$(1.8) \quad F(x) = \frac{1}{2} F(x + 1) + \frac{1}{2} F(x - 1), \quad x = 1, \ldots, N - 1$$

경계 조건 $F(0) = 0, F(N) = 1$과 (1.8)을 만족하는 하나의 함수 $F$는 선형 함수(linear function) $F(x) = x/N$입니다. 실제로 이것이 유일한 해(unique solution)임을 보일 것입니다.

**정리 1.4 (Theorem 1.4).**
실수 $a, b$와 양의 정수 $N$이 주어졌다고 하자. 경계 조건 $F(0) = a, F(N) = b$와 (1.8)을 만족하는 유일한 함수 $F : \{0, \ldots, N\} \to \mathbb{R}$은 다음과 같은 선형 함수이다:

$$F_0(x) = a + \frac{x(b - a)}{N}$$

이 정리는 증명하기 비교적 쉽지만, 우리는 **4가지 서로 다른 증명 방식**을 제시할 것입니다. 이는 단순히 얼마나 많은 증명을 보여줄 수 있는지 자랑하기 위함이 아닙니다! 동일한 정리에 대해 서로 다른 증명을 제공하는 것은 추후 일반화(generalizations)를 증명하려 할 때 사용할 수 있는 다양한 접근 방식을 제공해주므로 매우 유용합니다. $F_0$가 조건을 만족함은 즉시 확인할 수 있으므로, 진짜 핵심 질문은 **유일성(uniqueness)**입니다. $F_0$가 유일한 그러한 함수임을 증명해야 합니다.

---

#### 유일성 증명 1 (Proof 1 - 벡터 공간의 차원 구조)
(1.8)을 만족하는 모든 함수 $F : \{0, \ldots, N\} \to \mathbb{R}$의 집합 $V$를 고려하자. $V$가 벡터 공간(vector space)임을 쉽게 확인할 수 있습니다. 즉, $f, g \in V$이고 $c_1, c_2 \in \mathbb{R}$이면 $c_1 f + c_2 g \in V$입니다.

실제로 이 벡터 공간의 차원이 2임을 주장합니다. 이를 위해 기저(basis)를 제시하겠습니다. $f_1(0) = 0, f_1(1) = 1$로 정의되고, (1.8)을 만족하도록 유일한 방식으로 연장되는 함수 $f_1$을 고려합시다. 즉, $x > 1$에 대해:

$$f_1(x) = 2f_1(x - 1) - f_1(x - 2)$$

로 정의합니다. $f_1$이 $f_1(0) = 0, f_1(1) = 1$을 만족하는 (1.8)의 유일한 해임을 쉽게 알 수 있습니다. 마찬가지로 초깃값 $f_2(0) = 1, f_2(1) = 0$으로 $f_2$를 정의합니다. 그러면 $c_1 f_1 + c_2 f_2$는 $f(0) = c_2, f(1) = c_1$을 만족하는 (1.8)의 유일한 해입니다. $a, b$가 변함에 따라 $F_0$ 형태의 함수들이 이루는 집합은 $V$의 2차원 부분 공간을 형성하므로, $V$ 전체와 정확히 일치해야 합니다.

> **♦ 정리: 함수 공간과 벡터 공간의 동형**
> 모든 함수 $f : \{0, \ldots, N\} \to \mathbb{R}$의 집합은 본질적으로 $\mathbb{R}^{N+1}$과 동일합니다. 이는 함수 $f$에 벡터 $(f(0), f(1), \ldots, f(N))$을 대응시킴으로써 볼 수 있습니다. 집합 $V$는 이 벡터 공간의 부분 공간(subspace)입니다. 부분 공간의 차원이 $k$임을 보이기 위해서는 $k$개의 원소 $v_1, \ldots, v_k$로 구성된 기저를 찾으면 됩니다. 이들이 기저를 형성함을 보이기 위해서는 이들이 선형 독립(linearly independent)이고 부분 공간의 모든 벡터가 이들의 선형 결합(linear combination)임을 보이면 됩니다.

#### 유일성 증명 2 (Proof 2 - 최대 및 최소 원리 / Maximum & Minimum Principle)
$F$가 (1.8)의 해라고 하자. 그러면 각 $0 < x < N$에 대해 다음이 성립합니다:

$$F(x) \le \max \{ F(x - 1), F(x + 1) \}$$

이를 이용하면 $F$의 최댓값은 경계점인 $0$ 또는 $N$에서 달성됨을 알 수 있습니다. 마찬가지로 $F$의 최솟값도 경계 $\{0, N\}$에서 달성됩니다.

만약 $F(0) = 0, F(N) = 0$이라면, 함수의 최솟값과 최댓값이 모두 0이므로 $F \equiv 0$ (모든 위치에서 0)입니다.
이제 $F(0) = a, F(N) = b$라 하고 $F_0$를 동일한 경계값을 갖는 선형 함수라 합시다. 그러면 차이 함수 $F - F_0$ 역시 (1.8)을 만족하고 경계값이 0이 되므로, 모든 곳에서 0입니다 ($F - F_0 \equiv 0$). 이는 $F = F_0$임을 의미합니다.

#### 유일성 증명 3 (Proof 3 - 선형 연립방정식과 행렬 가역성)
방정식 (1.8)을 $N - 1$개의 미지수 $F(1), \ldots, F(N - 1)$에 대한 $N - 1$개의 선형 방정식으로 봅시다. 이를 $A v = w$ 형태의 행렬 방정식으로 쓸 수 있습니다:

$$A = \begin{bmatrix}
-1 & 1/2 & 0 & 0 & \cdots & 0 & 0 \\
1/2 & -1 & 1/2 & 0 & \cdots & 0 & 0 \\
0 & 1/2 & -1 & 1/2 & \cdots & 0 & 0 \\
\vdots & & & \ddots & & & \vdots \\
0 & 0 & 0 & \cdots & 1/2 & -1 & 1/2 \\
0 & 0 & 0 & \cdots & 0 & 1/2 & -1
\end{bmatrix}, \quad
w = \begin{bmatrix}
-F(0)/2 \\
0 \\
0 \\
\vdots \\
0 \\
-F(N)/2
\end{bmatrix}$$

만약 행렬 $A$가 가역(invertible)임을 증명한다면, 유일한 해는 $v = A^{-1} w$로 주어집니다. 가역성을 증명하기 위해서는 $A v = 0$이 유일한 해 $v = 0$만을 가짐을 보이면 충분하며, 이는 증명 2에서의 논증(최대 원리)으로 수행할 수 있습니다.

#### 유일성 증명 4 (Proof 4 - 마팅게일 성질 및 조건부 기댓값 논증)
$F$가 (1.8)의 해라 하자. $x$에서 출발하는 랜덤 워크를 $S_n$이라 합시다.
우리는 모든 $n$에 대해 다음이 성립함을 주장합니다:

$$\mathbb{E}[F(S_{n \wedge T})] = F(x)$$

이를 수학적 귀납법(induction)으로 증명합시다.
$n = 0$일 때, $F(S_0) = F(x)$ 이므로 $\mathbb{E}[F(S_0)] = F(x)$입니다.
귀납 단계를 위해 조건부 기댓값을 이용한 기댓값 법칙을 사용합니다:

$$\mathbb{E}[F(S_{(n+1) \wedge T})] = \sum_{y=0}^N \mathbb{P}\{S_{n \wedge T} = y\} \, \mathbb{E}[F(S_{(n+1) \wedge T}) \mid S_{n \wedge T} = y]$$

- 만약 $y = 0$ 또는 $y = N$ 이고 $S_{n \wedge T} = y$ 이면, 이미 정지했으므로 $S_{(n+1) \wedge T} = y$ 이고 $\mathbb{E}[F(S_{(n+1) \wedge T}) \mid S_{n \wedge T} = y] = F(y)$ 입니다.
- 만약 $0 < y < N$ 이고 $S_{n \wedge T} = y$ 이면, 다음 단계에서 $y + 1$ 또는 $y - 1$로 각각 $1/2$ 확률로 이동하므로:
$$\mathbb{E}[F(S_{(n+1) \wedge T}) \mid S_{n \wedge T} = y] = \frac{1}{2} F(y + 1) + \frac{1}{2} F(y - 1) = F(y)$$

따라서:

$$\mathbb{E}[F(S_{(n+1) \wedge T})] = \sum_{y=0}^N \mathbb{P}\{S_{n \wedge T} = y\} F(y) = \mathbb{E}[F(S_{n \wedge T})] = F(x)$$

귀납 가설에 의해 마지막 등식이 성립합니다. 따라서:

$$\begin{aligned}
F(x) &= \lim_{n \to \infty} \mathbb{E}[F(S_{n \wedge T})] \\
&= \lim_{n \to \infty} \sum_{y=0}^N \mathbb{P}\{S_{n \wedge T} = y\} F(y) \\
&= \mathbb{P}\{S_T = 0\} F(0) + \mathbb{P}\{S_T = N\} F(N) \\
&= [1 - \mathbb{P}\{S_T = N\}] F(0) + \mathbb{P}\{S_T = N\} F(N)
\end{aligned}$$

$F(0) = 0, F(N) = 1$인 경우를 고려하면 다음을 직접 얻게 됩니다:

$$\mathbb{P}\{S_T = N \mid S_0 = x\} = \frac{x}{N}$$

그리고 더 일반적인 경계 조건에 대해서는:

$$F(x) = F(0) + \frac{x}{N} [F(N) - F(0)]$$

> **이 증명의 뛰어난 점:**
> 마지막 증명의 근사한 점은 선형 함수 해를 미리 추측할 필요가 없었다는 것입니다. 증명 과정 자체가 해를 구성적으로 도출해 냅니다!

---

### 1.2.2. 고차원에서의 경계값 문제 (Higher dimensions)

우리는 이 결과를 고차원으로 일반화할 것입니다.
구간 $\{1, \ldots, N\}$을 $\mathbb{Z}^d$의 임의의 유한 부분집합(finite subset) $A$로 대체합니다. $A$의 (외곽) 경계 $\partial A$를 다음과 같이 정의합니다:

$$\partial A = \{z \in \mathbb{Z}^d \setminus A \mid \text{dist}(z, A) = 1\}$$

그리고 $A$의 "폐포(closure)" $\bar{A}$를 $\bar{A} = A \cup \partial A$ 로 정의합니다.

```
   o   o   o
 o •   •   • o
 o •   •   • o
   o   o   o
```
**그림 3. 흰색 점은 $A$, 검은색 점은 $\partial A$ (Figure 3. The white dots are $A$ and the black dots are $\partial A$)**

> **♦ 정리: 폐포(closure) 용어에 대하여**
> "폐포"라는 용어가 생소해 보일 수 있지만, 연속 공간에서의 유사한 개념에서 $A$는 열린 집합(open set), $\partial A$는 위상적 경계(topological boundary), $\bar{A} = A \cup \partial A$는 위상적 폐포(topological closure)가 됩니다.

함수들에 작용하는 선형 연산자(linear operators) $Q$와 $L$을 다음과 같이 정의합니다:

$$Q F(x) = \frac{1}{2d} \sum_{y \in \mathbb{Z}^d, |x-y|=1} F(y)$$

$$L F(x) = (Q - I) F(x) = \frac{1}{2d} \sum_{y \in \mathbb{Z}^d, |x-y|=1} [F(y) - F(x)]$$

연산자 $L$은 흔히 **(이산) 라플라시안((discrete) Laplacian)**이라 불립니다. $S_n$을 $\mathbb{Z}^d$ 상의 단순 랜덤 워크라 하면, 다음과 같이 쓸 수 있습니다:

$$L F(x) = \mathbb{E}[F(S_1) - F(S_0) \mid S_0 = x]$$

$L F(x) = 0$일 때 함수 $F$가 $x$에서 **(이산) 조화적((discrete) harmonic)**이라고 말합니다. 이는 평균값 성질(mean-value property)의 한 예입니다. 이에 대응하는 경계값 문제를 흔히 **조화함수에 대한 디리클레 문제(Dirichlet problem for harmonic functions)**라 부릅니다.

> **♦ 정리: 선형 연산자의 행렬 표현과 전이 확률**
> 선형 연산자라는 용어는 정역(domain)이 함수 공간인 선형 함수에 대해 자주 사용됩니다. 우리의 경우, 정역은 유한 집합 $A$ 상의 함수 공간이며, 이는 $K = \#(A)$일 때 $\mathbb{R}^K$와 동형(isomorphic)입니다. 이 경우 선형 연산자는 선형대수학의 선형 변환과 동일합니다. 우리는 $Q$와 $L$을 $K \times K$ 행렬로 생각할 수 있습니다. $|x-y|=1$일 때 $Q(x, y) = 1/(2d)$이고 그렇지 않으면 $Q(x, y) = 0$인 $Q = [Q(x, y)]_{x, y \in A}$를 작성할 수 있습니다. $Q^n = [Q^n(x, y)]$을 정의하면, $Q^n(x, y)$는 랜덤 워크가 $x$에서 출발하여 시간 $n$에 $y$ 위치에 존재하고, 시간 $n$까지 집합 $A$를 벗어나지 않았을 확률입니다.

**조화함수에 대한 디리클레 문제 (Dirichlet problem for harmonic functions)**
집합 $A \subset \mathbb{Z}^d$와 함수 $F : \partial A \to \mathbb{R}$이 주어졌을 때, $F$의 $A$로의 연장(extension)으로서 $A$ 내부에서 조화적인 함수, 즉 다음을 만족하는 함수를 찾는 문제:

$$(1.9) \quad L F(x) = 0 \quad \text{for all } x \in A$$

$d = 1$ 및 $A = \{1, \ldots, N-1\}$인 경우, 우리는 해를 추측한 뒤 그것이 맞음을 검증할 수 있었습니다. 고차원에서는 해의 공식을 제시하는 것이 그다지 명확하지 않습니다. 우리는 $d = 1$에서의 마지막 증명 방식(마팅게일 증명)이 $d > 1$에서도 자연스럽게 일반화됨을 보일 것입니다. 정지 시간을 $T_A = \min \{ n \ge 0 : S_n \notin A \}$ 로 놓읍시다.

**정리 1.5 (Theorem 1.5).**
$A \subset \mathbb{Z}^d$가 유한 집합이면, 모든 $F : \partial A \to \mathbb{R}$에 대해 (1.9)를 만족하는 $A$로의 유일한 연장이 존재한다. 그 해는 다음과 같이 주어진다:

$$F_0(x) = \mathbb{E}[F(S_{T_A}) \mid S_0 = x] = \sum_{y \in \partial A} \mathbb{P}\{S_{T_A} = y \mid S_0 = x\} \, F(y)$$

**증명 및 유일성 유도 (Proof & Uniqueness):**
위에서 정의된 $F_0$가 디리클레 문제의 해임을 검증하는 것은 어렵지 않습니다. 관건은 **유일성**을 보여주는 것입니다. $F$가 $A$에서 조화적이고, $S_0 = x \in A$라 합시다. 프로세스를 $M_n = F(S_{n \wedge T_A})$로 정의합니다. 그러면 (1.9)는 다음과 같이 재작성될 수 있습니다:

$$(1.10) \quad \mathbb{E}[M_{n+1} \mid S_0, \ldots, S_n] = F(S_{n \wedge T_A}) = M_n$$

$\mathbb{E}[M_{n+1} \mid S_0, \ldots, S_n] = M_n$을 만족하는 프로세스를 (랜덤 워크에 대한) **마팅게일(martingale)**이라 부릅니다. $F(S_{n \wedge T_A})$가 마팅게일인 것은 본질적으로 $F$가 $A$에서 조화적인 것과 동치입니다. 마팅게일이 $\mathbb{E}[M_n] = \mathbb{E}[M_0]$을 만족함을 쉽게 확인할 수 있으므로, $S_0 = x$일 때:

$$\sum_{y \in \bar{A}} \mathbb{P}\{S_{n \wedge T_A} = y\} F(y) = \mathbb{E}[M_n] = M_0 = F(x)$$

간단한 논증으로 확률 1로 $T_A < \infty$임을 알 수 있으므로, $n \to \infty$ 극한을 취하면 다음을 얻습니다:

$$(1.11) \quad F(x) = \lim_{n \to \infty} \sum_{y \in \bar{A}} \mathbb{P}\{S_{n \wedge T_A} = y\} F(y) = \sum_{y \in \partial A} \mathbb{P}\{S_{T_A} = y\} F(y)$$

> **♦ 정리: 극한과 합의 교환 조건**
> 유한합이므로 극한과 합의 순서를 교환하는 데 아무런 문제가 없습니다. 만약 $A$가 무한 집합이라면, 극한과 합의 교환을 정당화하기 위해 추가적인 가정이 필요합니다.

**선형대수학적 관점 및 푸아송 커널 (Poisson Kernel):**
$A$가 $N$개의 원소를 갖고 $\partial A$가 $K$개의 원소를 갖는다고 합시다. 디리클레 문제의 해는 $\partial A$ 상의 각 함수($\mathbb{R}^K$의 벡터)에 $A$ 상의 함수($\mathbb{R}^N$의 벡터)를 할당합니다. 따라서 해는 $\mathbb{R}^K$에서 $\mathbb{R}^N$으로 가는 선형 함수(선형 변환)로 간주할 수 있으며, $N \times K$ 행렬로 나타납니다. 해 행렬을 다음과 같이 표현합시다:

$$H_A = [H_A(x, y)]_{x \in A, y \in \partial A}$$

(1.11)을 표현하는 또 다른 방법은 다음과 같습니다:

$$H_A(x, y) = \mathbb{P}\{S_{T_A} = y \mid S_0 = x\}$$

이 행렬을 흔히 **푸아송 커널(Poisson kernel)**이라 부릅니다. 주어진 집합 $A$에 대해, 우리는 푸아송 커널을 이용하여 임의의 경계 함수에 대한 디리클레 문제를 풀 수 있습니다.

> **♦ 정리: 푸아송 커널의 해석학적 vs 확률론적 관점**
> 확률론에 익숙하지 않은 해석학자들은 푸아송 커널을 경계 데이터를 내부의 값으로 변환하는 행렬로만 생각합니다. 반면 확률론자들은 $H_A(x, y)$를 $x$에서 출발한 랜덤 워크가 집합 $A$를 탈출할 때 경계점 $y$에서 탈출할 확률로 해석합니다.

**무한 집합 $A$인 경우 및 유계성(Boundedness) 조건:**
만약 정리 1.5에서 $A$가 무한 집합이 되도록 허용하면 어떻게 될까요? 이 경우 해가 유일하다는 것이 항상 성립하지는 않습니다.
1차원 예시로 $A = \{1, 2, 3, \ldots\}$ 이고 $\partial A = \{0\}$ 인 경우를 고려해 봅시다. 모든 $c \in \mathbb{R}$에 대해 함수 $F(x) = cx$는 원점에서 경계값 0을 가지면서 $A$ 내부에서 조화적입니다.
증명의 어디에서 오차/붕괴가 발생하는 것일까요? 마팅게일 버전을 고려해 봅시다. $F(0) = 0$인 $A$ 상의 조화함수 $F$와 양의 정수 $x$에서 출발하는 단순 랜덤 워크 $S_n$을 생각하면, 동일한 논증으로 $M_n = F(S_{n \wedge T})$가 마팅게일이고 다음이 성립합니다:

$$F(x) = \mathbb{E}[M_n] = \sum_{y=0}^\infty F(y) \, \mathbb{P}\{S_{n \wedge T} = y\}$$

우리는 이전 절에서 확률 1로 $T < \infty$임을 보였습니다. 이는 $\mathbb{P}\{S_{n \wedge T} = 0\} \to 1$, 즉 $\lim_{n \to \infty} \sum_{y > 0} \mathbb{P}\{S_{n \wedge T} = y\} = 0$임을 의미합니다. 그러나 $F$가 **유계(unbounded)**라면, 이로부터 $\lim_{n \to \infty} \sum_{y > 0} F(y) \mathbb{P}\{S_{n \wedge T} = y\} = 0$ 이라고 결론지을 수 없습니다.
그러나 이를 통해 $0$에서의 주어진 경계값을 가지며 $A$에서 조화적인 **유계 함수(bounded function)**는 단 하나뿐임을 알 수 있습니다.

**정리 1.6 (Theorem 1.6).**
$A$가 $\mathbb{Z}^d$의 진부분집합(proper subset)으로서 모든 $x \in \mathbb{Z}^d$에 대해 $\lim_{n \to \infty} \mathbb{P}\{T_A > n \mid S_0 = x\} = 0$이라 하자. $F : \partial A \to \mathbb{R}$이 유계 함수(bounded function)이면, (1.9)를 만족하는 유계인 연장이 유일하게 존재한다. 그 해는 다음과 같이 주어진다:

$$F_0(x) = \mathbb{E}[F(S_{T_A}) \mid S_0 = x] = \sum_{y \in \partial A} \mathbb{P}\{S_{T_A} = y \mid S_0 = x\} \, F(y)$$

---

## §1.3. 열방정식 (Heat equation)

우리는 이제 열 흐름(heat flow)에 대한 수학적 모델을 소개할 것입니다. $A$를 경계 $\partial A$를 갖는 $\mathbb{Z}^d$의 유한 부분집합(finite subset)이라 합시다. 우리는 경계에서의 온도를 항상 0으로 설정하고, 초기 조건으로 $x \in A$에서의 온도를 $p_0(x) = f(x)$로 설정합니다.

각 정수 시간 단위 $n$에서, 시간 $n$에 $x$ 위치에 있는 열은 $2d$개의 가장 가까운 이웃들에게 균등하게 퍼져나갑니다. 만약 그 이웃 중 하나가 경계점(boundary point)이면, 그 지점으로 간 열은 영원히 손실됩니다.

이에 대한 확률론적 관점(probabilistic view)은 $A$ 내부의 온도가 아주 많은 수의 "열 입자(heat particles)"에 의해 제어되는 것으로 생각하는 것입니다. 이 입자들은 $A$를 떠날 때까지 $A$ 상에서 랜덤 워크를 수행하며, $A$를 벗어나는 순간 소멸(killed)합니다. 시간 $n$에서 $x$ 위치의 온도 $p_n(x)$는 $x$에서의 입자 밀도(density)로 주어집니다.

두 해석 모두 온도 $p_n(x)$에 대한 차분 방정식(difference equation)을 제공합니다. $x \in A$에 대해 $x$에서의 온도는 이웃 지점들로부터 들어오는 열의 양으로 주어집니다:

$$p_{n+1}(x) = \frac{1}{2d} \sum_{|y-x|=1} p_n(y)$$

기호 $\partial_n p_n(x) = p_{n+1}(x) - p_n(x)$를 도입하면, 다음과 같이 **열방정식(heat equation)**을 얻게 됩니다:

$$(1.12) \quad \partial_n p_n(x) = L p_n(x), \quad x \in A$$

여기서 $L$은 이전과 마찬가지로 이산 라플라시안(discrete Laplacian)을 나타냅니다. 초기 온도는 다음과 같이 초기 조건으로 주어집니다:

$$(1.13) \quad p_0(x) = f(x), \quad x \in A$$

그리고 경계 조건을 재작성하면 다음과 같습니다:

$$(1.14) \quad p_n(x) = 0, \quad x \in \partial A$$

만약 $x \in A$이고 초기 조건이 $f(x) = 1$ 및 $z \neq x$에서 $f(z) = 0$ 이라면:

$$p_n(y) = \mathbb{P}\{S_{n \wedge T_A} = y \mid S_0 = x\}$$

> **♦ 정리: 열방정식의 결정론적 vs 확률론적 관점**
> 열방정식은 열 흐름에 대한 결정론적(deterministic, 즉 무작위성이 없는) 모델입니다. 확률 없이도 연구될 수 있습니다. 그러나 확률은 개별 무작위 입자들의 이동이라는 관점에서 풍부한 결(richness)을 더해주며, 이 추가적인 관점은 방정식을 이해하는 데 매우 유용합니다.

임의의 초기 조건 $f$가 주어졌을 때, (1.12)–(1.14)를 만족하는 유일한 함수 $p_n$이 존재함을 쉽게 볼 수 있습니다. 실제로 $y \in \partial A$에 대해 모든 $n \ge 0$에서 $p_n(y) = 0$, $x \in A$에 대해 $p_0(x) = f(x)$로 설정하고, $n > 0$에 대해 $x \in A$에서의 $p_n(x)$를 (1.12)에 의해 점화적으로(recursively) 정의하면 됩니다.
이는 (1.12)와 (1.14)를 만족하는 함수들의 집합이 차원 $\#(A)$인 벡터 공간임을 보여줍니다. 실제로 $\{p_n(x) : x \in A\}$는 벡터 $Q^n f$ 입니다.

존재성과 유일성이 확보되면, 남은 문제는 해당 함수를 구하는 것입니다. 유계 집합 $A$에 대해, 이는 선형대수학 문제이며 본질적으로 **행렬 $Q$를 대각화(diagonalizing)하는 문제**가 됩니다.

> **♦ 정리: 대칭행렬의 대각화 정리**
> 선형대수학에서 실수 성분을 갖는 $k \times k$ 대칭행렬 $A$가 주어지면, 우리는 $k$개의 (반드시 다를 필요는 없는) 실수 고윳값(eigenvalues) $\lambda_k \le \lambda_{k-1} \le \cdots \le \lambda_1$ 과, 고유벡터(eigenvectors)이자 서로 직교(orthogonal)하는 $k$개의 벡터 $v_1, \ldots, v_k$ ($A v_j = \lambda_j v_j$)를 찾을 수 있음을 상기합시다. ($A$가 대칭행렬이 아니면 $k$개의 선형독립인 고유벡터를 갖지 못하거나, 일부 고윳값이 실수가 아니거나, 서로 다른 고윳값에 대한 고유벡터들이 직교하지 않을 수 있습니다.)

우리는 $d = 1$인 경우부터 고려할 것입니다. $A = \{1, \ldots, N-1\}$에 대해 함수 $p_n$을 계산해 봅시다. 우리는 다음과 같은 변수분리 형태의 해를 찾는 것으로 시작합니다:

$$(1.15) \quad p_n(x) = \lambda^n \phi(x)$$

만약 $p_n$이 이러한 형태라면:

$$\partial_n p_n(x) = \lambda^{n+1} \phi(x) - \lambda^n \phi(x) = (\lambda - 1) \lambda^n \phi(x)$$

이 깔끔한 형태는 우리가 $Q$의 고윳값과 고유함수(eigenfunctions)를 찾도록 이끕니다. 즉, 다음을 만족하는 $\lambda, \phi$를 구하는 문제입니다:

$$(1.16) \quad Q \phi(x) = \lambda \phi(x), \quad \partial A \text{ 상에서 } \phi \equiv 0$$

> **♦ 정리: 고윳값 및 고유벡터 검색 알고리즘과 삼각함수 아이디어**
> 행렬 $Q$의 고윳값과 고유벡터를 찾는 "알고리즘적" 방법은 먼저 특성 다항식(characteristic polynomial)의 근으로서 고윳값을 구한 다음 각 고윳값에 해당하는 고유벡터를 구하는 것입니다. 때때로 고유벡터에 대해 좋은 추측(guess)을 할 수 있다면 이를 피할 수 있습니다. 우리가 여기서 할 작업이 바로 이것입니다.

사인의 덧셈정리 $\sin((x \pm 1)\theta) = \sin(x\theta)\cos\theta \pm \cos(x\theta)\sin\theta$ 로부터:

$$Q \{ \sin(\theta x) \} = \lambda_\theta \{ \sin(\theta x) \}, \quad \lambda_\theta = \cos\theta$$

여기서 $\{ \sin(\theta x) \}$는 $x \in A$에 대응하는 성분이 $\sin(\theta x)$인 벡터를 나타냅니다.
만약 $\theta_j = \pi j / N$을 선택하면, $\phi_j(x) = \sin(\pi j x / N)$ 은 경계 조건 $\phi_j(0) = \phi_j(N) = 0$을 만족합니다. 이들은 대칭행렬 $Q$에 대해 서로 다른 고윳값을 갖는 고유벡터들이므로 서로 직교하며, 따라서 선형 독립입니다.
따라서 $A$ 상의 모든 함수 $f$는 다음과 같이 유일한 방식으로 표현될 수 있습니다:

$$(1.17) \quad f(x) = \sum_{j=1}^{N-1} c_j \sin\left( \frac{\pi j x}{N} \right)$$

삼각함수로 표현된 이 합을 **유한 푸리에 급수(finite Fourier series)**라 부릅니다.
초기 조건 $f$에 대한 열방정식의 해는 다음과 같습니다:

$$p_n(y) = \sum_{j=1}^{N-1} c_j \left( \cos \frac{j\pi}{N} \right)^n \phi_j(y)$$

고유벡터들의 직교성은 다음을 말해줍니다:

$$\sum_{x=1}^{N-1} \sin\left( \frac{\pi j x}{N} \right) \sin\left( \frac{\pi k x}{N} \right) = 0 \quad (j \neq k)$$

또한 다음이 성립합니다:

$$(1.18) \quad \sum_{x=1}^{N-1} \sin^2\left( \frac{\pi j x}{N} \right) = \frac{N}{2}$$

> **♦ 정리: $N$차 단위근(Roots of Unity)과 제곱합 직교성 증명**
> $N$차 단위근 $\zeta_1, \ldots, \zeta_N$은 $\zeta^N = 1$인 $N$개의 복소수로서 $\zeta_k = \cos(2k\pi/N) + i\sin(2k\pi/N)$으로 주어집니다. 단위근들은 복소평면의 단위원 위에 균등하게 퍼져 있어 $\omega_1 + \dots + \omega_N = 0$ 이며, 이는 $\sum_{j=1}^N \cos(2k\pi/N) = \sum_{j=1}^N \sin(2k\pi/N) = 0$임을 의미합니다. 사인의 배각 공식을 사용하면:
> $$\sum_{j=1}^{N-1} \sin^2\left(\frac{jx\pi}{N}\right) = \frac{1}{2}\sum_{j=0}^{N-1} \left[1 - \cos\left(\frac{2jx\pi}{N}\right)\right] = \frac{N}{2} - \frac{1}{2}\sum_{j=1}^N \cos\left(\frac{2jx\pi}{N}\right)$$
> $x$가 정수이면 마지막 합은 0이 되어 (1.18)을 얻게 됩니다.

특히 초기 조건 $f(x) = 1$, 그리고 $z \neq x$에 대해 $f(z) = 0$인 해를 선택하면 다음을 얻습니다:

$$\mathbb{P}\{S_{n \wedge T_A} = y \mid S_0 = x\} = \frac{2}{N} \sum_{j=1}^{N-1} \phi_j(x) \left( \cos \frac{j\pi}{N} \right)^n \phi_j(y)$$

$n \to \infty$ 일 때 어떤 일이 일어나는지 보는 것은 매우 흥미롭습니다. 큰 $n$에 대해 합은 매우 작아지지만, 고윳값의 절댓값이 최대인 $j = 1$ 및 $j = N - 1$ 항에 의해 지배(dominated)됩니다. 이 두 항은 다음을 제공합니다:

$$\frac{2}{N} \left(\cos \frac{\pi}{N}\right)^n \left[ \sin\left(\frac{\pi x}{N}\right) \sin\left(\frac{\pi y}{N}\right) + (-1)^n \sin\left(\frac{x\pi(N-1)}{N}\right) \sin\left(\frac{y\pi(N-1)}{N}\right) \right]$$

$\sin\left(\frac{x\pi(N-1)}{N}\right) = (-1)^{x+1} \sin\left(\frac{\pi x}{N}\right)$임을 확인할 수 있으므로, $x, y \in \{1, \ldots, N-1\}$에 대해 $n \to \infty$ 일 때:

$$\mathbb{P}\{S_{n \wedge T_A} = y \mid S_0 = x\} \sim \frac{2}{N} \left(\cos \frac{\pi}{N}\right)^n [1 + (-1)^{n+x+y}] \sin\left(\frac{\pi x}{N}\right) \sin\left(\frac{\pi y}{N}\right)$$

큰 $n$에 대해, 워커가 $\{1, \ldots, N-1\}$을 벗어나지 않았다는 조건 하에 워커가 $y$에 위치할 확률은 "패리티(parity)"가 맞다는 가정 하에($n + x + y$가 짝수) 약 $c \sin(\pi y / N)$ 형태가 됩니다. 패리티를 제외하면 극한 분포는 시작점 $x$에 전혀 의존하지 않습니다! 또한 워커는 구간의 "중앙(middle)" 부근의 점들에 존재할 확률이 더 높다는 점에 유의합시다.

위의 예시는 (1.15) 형태의 해를 찾는 기법으로서 **변수분리법(separation of variables)**이라 불리는 기법을 보여줍니다. 비록 고윳값과 고유함수에 대한 명시적 식을 항상 구하는 것이 가능하지는 않더라도, 동일한 아이디어가 모든 $d$에 대해 작동합니다. 유한 집합 $A$에 대해 이는 본질적으로 대각화를 통해 행렬의 거듭제곱을 계산하는 것과 동일합니다. 이를 정리합니다.

**정리 1.7 (Theorem 1.7 - 변수분리법과 열방정식의 해).**
$A$가 $N$개의 원소를 갖는 $\mathbb{Z}^d$의 유한 부분집합이면, (1.16)을 만족하는 실수 고윳값 $\lambda_1, \ldots, \lambda_N$과 $N$개의 선형독립인 고유함수 $\phi_1, \ldots, \phi_N$을 찾을 수 있다. (1.12)–(1.14)의 해는 다음과 같이 주어진다:

$$p_n(x) = \sum_{j=1}^N c_j \lambda_j^n \phi_j(x)$$

여기서 $c_j$는 다음을 만족하도록 선택된다:

$$f(x) = \sum_{j=1}^N c_j \phi_j(x)$$

실제로 고유함수 $\phi_j$는 정규직교(orthonormal)가 되도록 선택할 수 있다:

$$\langle \phi_j, \phi_k \rangle := \sum_{x \in A} \phi_j(x) \phi_k(x) = \delta(k - j)$$

> **♦ 정리: 크로네커 델타(Kronecker Delta) 기호**
> 여기서는 델타 함수 표기법 $\delta(z) = 1 \, (z = 0)$, $\delta(z) = 0 \, (z \neq 0)$을 도입했습니다.

$n \to \infty$ 일 때 $p_n(x) \to 0$ 이므로, 고윳값들의 절댓값은 엄밀히 1보다 작음을 알 수 있습니다. 고윳값들의 크기 순서를 다음과 같이 정할 수 있습니다:

$$1 > \lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_N > -1$$

우리는 $p_n(x, y; A)$를 $x$에서 초기 조건 1이고 나머지에서 0인 열방정식의 해로 작성할 것입니다. 즉:

$$p_n(x, y; A) = \mathbb{P}\{S_n = y, T_A > n \mid S_0 = x\}, \quad x, y \in A$$

$|A| = N$일 때:

$$p_n(x, y; A) = \sum_{j=1}^N c_j(x) \lambda_j^n \phi_j(y)$$

여기서 $c_j(x)$는 $\sum_{j=1}^N c_j(x) \phi_j(y) = \delta(y - x)$를 만족하도록 선택되었습니다. 실제로 이것은 $c_j(x) = \phi_j(x)$임을 말해줍니다. 따라서:

$$p_n(x, y; A) = \sum_{j=1}^N \lambda_j^n \phi_j(x) \phi_j(y)$$

우변의 양이 $x, y$에 대해 대칭(symmetric)임에 유의합시다. $p_n(x, y; A)$의 정의로부터도 이 대칭성이 성립함을 확인할 수 있습니다.

가장 큰 고윳값 $\lambda_1$은 흔히 $\lambda_A$로 표기됩니다. 우리는 다음과 같이 $\lambda_A$의 "변분적(variational)" 정의를 내릴 수 있습니다. 이는 사실 대칭행렬의 최대 고윳값에 관한 정리입니다.

**정리 1.8 (Theorem 1.8 - 대칭행렬 최대 고윳값의 변분 원리).**
$A$가 $\mathbb{Z}^d$의 유한 부분집합이면, $\lambda_A$는 다음과 같이 주어진다:

$$\lambda_A = \sup_f \frac{\langle Q f, f \rangle}{\langle f, f \rangle}$$

여기서 상한(supremum)은 $A$ 상의 모든 영이 아닌 함수 $f$에 대해 취하며, $\langle f, g \rangle = \sum_{x \in A} f(x) g(x)$는 내적이다.

**증명 (Proof).**
$\phi$가 고윳값 $\lambda_1$에 대한 고유벡터이면 $Q\phi = \lambda_1 \phi$ 이고, $f = \phi$로 설정하면 상한이 적어도 $\lambda_1$ 이상임을 보여줍니다.
반대로, 고유함수들로 이루어진 직교기저 $\phi_1, \ldots, \phi_N$이 존재하므로 임의의 $f$를 $f = \sum_{j=1}^N c_j \phi_j$ 로 쓸 수 있습니다. 그러면:

$$\begin{aligned}
\langle Q f, f \rangle &= \left\langle Q \sum_{j=1}^N c_j \phi_j, \sum_{j=1}^N c_j \phi_j \right\rangle \\
&= \left\langle \sum_{j=1}^N c_j Q \phi_j, \sum_{j=1}^N c_j \phi_j \right\rangle \\
&= \sum_{j=1}^N c_j^2 \lambda_j \langle \phi_j, \phi_j \rangle \\
&\le \lambda_1 \sum_{j=1}^N c_j^2 \langle \phi_j, \phi_j \rangle = \lambda_1 \langle f, f \rangle
\end{aligned}$$

위 계산이 고유함수들의 직교성과 $\langle \phi_j, \phi_j \rangle \ge 0$ 사실을 사용했음을 확인하기 바랍니다. $\blacksquare$

이 변분식을 사용하면, $\lambda_1$에 대한 고유함수가 각 $x$에 대해 $\phi_1(x) \ge 0$이 되도록 선택될 수 있음을 알 수 있습니다 (만약 $\phi_1$이 양수값과 음수값을 모두 가진다면 $\langle Q|\phi_1|, |\phi_1|\rangle > \langle Q\phi_1, \phi_1\rangle$이 되기 때문입니다).

$A$에 추가적인 조건을 부여하면 고유함수가 유일해집니다 (즉, $\lambda_2 < \lambda_1$). 우리는 $\mathbb{Z}^d$ 상의 부분집합 $A$ 내의 임의의 두 점이 $A$ 내에 완전히 머무는 이웃 경로로 연결될 때 $A$가 **연결(connected)**되어 있다고 말합니다. 동치로서, $A$가 연결되어 있다는 것은 각 $x, y \in A$에 대해 $p_n(x, y; A) > 0$이 되는 $n$이 존재한다는 것입니다. 이것이 $\lambda_1 > \lambda_2$를 의미함을 보여주는 것은 연습문제로 남깁니다.

최종 정리를 제시하기 전에, 몇 가지 패리티(짝수/홀수) 문제를 다룰 필요가 있습니다.
$x = (x_1, \ldots, x_d) \in \mathbb{Z}^d$ 이면 $\text{par}(x) = (-1)^{x_1 + \cdots + x_d}$ 로 놓습니다. $\text{par}(x) = 1$이면 $x$를 짝수라 부르고, 그렇지 않으면 홀수라 부릅니다.
$n$이 음이 아닌 정수이면:

$$p_n(x, y; A) = 0 \quad \text{if } (-1)^n \text{par}(x + y) = -1$$

만약 $Q\phi = \lambda \phi$ 이면, $Q[\text{par} \, \phi] = -\lambda \, \text{par} \, \phi$ 입니다.

**정리 1.9 (Theorem 1.9).**
$A$가 적어도 2개 이상의 점을 갖는 $\mathbb{Z}^d$의 유한 연결 부분집합이라 하자. 그러면 $\lambda_1 > \lambda_2$, $\lambda_N = -\lambda_1 < \lambda_{N-1}$ 이다. 고유함수 $\phi_1$은 모든 $x \in A$에 대해 $\phi_1(x) > 0$이 되도록 선택할 수 있으며, 다음이 성립한다:

$$\lim_{n \to \infty} \lambda_1^{-n} p_n(x, y; A) = [1 + (-1)^n \text{par}(x + y)] \, \phi_1(x) \phi_1(y)$$

**예시 1.10 (Example 1.10 - $d$차원 직사각형 영역에서의 고윳값과 고유함수).**
고유함수와 고윳값을 정확히 계산할 수 있는 $\mathbb{Z}^d$ 상의 한 집합은 $d$차원 직사각형입니다:

$$A = \{(x_1, \ldots, x_d) \in \mathbb{Z}^d : 1 \le x_j \le N_j - 1\}$$

고유함수들은 $\bar{k} = (k_1, \ldots, k_d) \in A$ 에 의해 색인됩니다:

$$\phi_{\bar{k}}(x_1, \ldots, x_d) = \sin\left( \frac{k_1 \pi x_1}{N_1} \right) \sin\left( \frac{k_2 \pi x_2}{N_2} \right) \cdots \sin\left( \frac{k_d \pi x_d}{N_d} \right)$$

이에 대응하는 고윳값은 다음과 같습니다:

$$\lambda_{\bar{k}} = \frac{1}{d} \left[ \cos\left( \frac{k_1 \pi}{N_1} \right) + \cdots + \cos\left( \frac{k_d \pi}{N_d} \right) \right]$$
