## 7. 블랙-숄즈-머튼(BSM) 연속모형과의 1:1 비교

이 공식, 어디서 많이 본 형태 아닌가요? 
맞습니다! 바로 금융공학의 정점이라 불리는 **블랙-숄즈-머튼(BSM) 연속 옵션 가격 결정 공식**과 완벽히 1:1로 대응됩니다.

### BSM 연속 모형 공식
$$C = S_0 \cdot N(d_1) - K \cdot e^{-rt} \cdot N(d_2)$$

이산모형(CRR)과 연속모형(BSM)의 각 구성 요소를 일대일로 비교해보면 다음과 같이 놀라울 정도로 완벽하게 짝을 이룹니다.

| 구성 요소 | CRR 이산 이항 모형 | BSM 연속 모형 ($n \to \infty$) | 핵심 의미 및 물리적 해석 |
| :--- | :--- | :--- | :--- |
| **기초자산 가치** | $S_0$ | $S_0$ | 현재 주식의 시장 가치 |
| **주가측도 행사확률** | $\Phi(a; n, p')$ | $N(d_1)$ | 주식을 기준(Numeraire)으로 할 때 만기에 옵션이 행사될 가중 확률 |
| **행사가격 현재가치** | $K (1+r)^{-n}$ | $K e^{-rt}$ | 행사가격 $K$를 현재 시점 가치로 할인한 금액 |
| **위험중립 행사확률** | $\Phi(a; n, p)$ | $N(d_2)$ | 현금을 기준(Numeraire)으로 할 때 만기에 옵션이 행사될 확률(ITM 확률) |

---

### 각 항의 구조적 직관 한눈에 보기

1. **첫 번째 항 ($S_0 \Phi(a; n, p') \longleftrightarrow S_0 N(d_1)$)**
   - 옵션이 만기에 행사되었을 때 손에 쥐게 되는 **'주식의 현재 가치'**입니다. 
   - 현재 주가 $S_0$에 주가 가중 행사확률 $\Phi(a; n, p')$ (연속에서는 $N(d_1)$)을 곱하여 산출합니다.

2. **두 번째 항 ($K (1+r)^{-n} \Phi(a; n, p) \longleftrightarrow K e^{-rt} N(d_2)$)**
   - 옵션이 만기에 행사되었을 때 지불해야 하는 **'행사가격 지불액의 현재 할인 가치'**입니다. 
   - 행사가격의 현재가치 $K(1+r)^{-n}$ (연속에서는 $K e^{-rt}$)에 위험중립 행사확률 $\Phi(a; n, p)$ (연속에서는 $N(d_2)$)를 곱하여 차감합니다.

---

### 결론: 이산에서 연속으로의 완벽한 수렴

기간 $n$을 무한히 쪼개는 연속 극한($n \to \infty$)을 취하면:
- 이산 이항 누적확률 $\Phi(a; n, p')$는 연속 표준정규누적분포 **$N(d_1)$**으로 수렴하고,
- 이산 이항 누적확률 $\Phi(a; n, p)$는 연속 표준정규누적분포 **$N(d_2)$**로 수렴합니다.

결국 **CRR 이항 모형**과 **BSM 연속 모형**은 별개의 공식이 아니라, **동일한 무차익 복제 원리와 위험중립 평가 원리가 이산(Discrete)과 연속(Continuous)이라는 형식의 차이로 표현된 하나의 동일한 법칙**이었음을 알 수 있습니다!

---

## 8. 이산 모형에서 연속 모형으로의 확장 메커니즘

### 8.1 연속 모형 확장의 필요성
- **주가의 연속성**: 현실의 주가는 이산적인 몇 개의 값만 갖는 것이 아니라 실수 범위($\mathbb{R}^+$) 내의 연속적인 값을 가집니다.
- **거래의 빈도성**: 현실의 거래는 특정 이산 시점에만 일어나는 것이 아니라 지속적이고 매우 빈번하게 일어납니다.

---

### 8.2 CRR의 핵심 접근법: 단위 기간 분할과 스케일링
- 전체 $t$기간을 $n$개의 미세한 단위 기간 $\Delta t = t/n$으로 쪼갭니다.
- 만기 시점($t$)의 이자율 증식 및 주가 변동을 **'단위 시점에서의 값'**으로 상정하고, 이를 $n$번 곱하거나 더하여 다시 만기 종착지의 값으로 복원합니다.

---

### 8.3 무위험 이자율의 단위 기간 확장

우선 이자율부터 단위 기간 이자율 $\hat{r}$을 구해보겠습니다.

만기 $t$기간 동안의 전체 무위험 증식인자를 $R$이라 할 때, $n$번 쪼갠 단위 기간 증식인자 $\hat{r}$을 $R^{1/n}$으로 정의하면, 이 단위 기간 증식인자를 $n$번 곱했을 때 완벽히 만기 총 증식인자 $R$로 복원됩니다.

$$(\hat{r})^n = \left(R^{1/n}\right)^n = R$$

이를 금융공학적 수식 표기로 나타내면 다음과 같습니다.

1. **연속 복리 기준**: $t$기간 전체 증식이 $e^{rt}$일 때, 단위 기간 증식인자를 $\hat{r} = e^{r t/n}$으로 정의하면 이를 $n$번 곱해 정확히 $e^{rt}$가 됩니다.
   $$\left(e^{r \frac{t}{n}}\right)^n = e^{rt}$$

2. **이산 복리 기준**: 단위 이자율을 $\hat{r} = 1 + r \frac{t}{n}$으로 정의해도, $n \to \infty$ 극한을 취하면 자연상수 $e$의 정의에 의해 연속 증식률로 수렴합니다.
   $$\lim_{n \to \infty} \left(1 + \frac{rt}{n}\right)^n = e^{rt}$$

---

### 8.4 주가 로그수익률의 평균과 '단위 평균'의 도출

#### 1) 왜 평균과 분산이 필요한가?
이산 이항 나무에서는 마디(node)마다 주가 경로를 하나하나 셀 수 있었지만, 연속 모형에서는 $n \to \infty$로 가기 때문에 주가의 개별 경로를 일일이 계산하는 것이 불가능해집니다. 
따라서 연속 모형에서는 **수익률의 평균(기댓값)과 분산**을 이용한 확률분포(정규분포/로그정규분포)를 구축하여 확률과 옵션 가치를 계산해야 합니다.

#### 2) 주가 변동의 로그수익률 표현
예를 들어 총 5번의 스텝 중 주가가 $u, d, u, u, d$ (상승 3번, 하강 2번)로 움직였다면 만기 주가는 다음과 같습니다.
$$S_t = u^3 d^2 S_0$$

양변을 $S_0$로 나누고 자연로그를 취하면 주가의 로그수익률이 도출됩니다.
$$\ln\left(\frac{S_t}{S_0}\right) = 3 \ln u + 2 \ln d$$

이를 일반화하여 총 $n$번의 스텝 중 상승 횟수를 확률변수 $j$, 1회 상승 확률을 $q$라 하면 하강 횟수는 $(n-j)$가 됩니다. 식을 전개하여 $j$로 묶어 정리하면 다음과 같습니다.
$$\ln\left(\frac{S_t}{S_0}\right) = j \ln u + (n-j) \ln d = j (\ln u - \ln d) + n \ln d$$

#### 3) 기댓값(평균)과 이항분포의 기댓값 $nq$
이제 이 로그수익률에 기댓값(평균) $\mathbb{E}[\cdot]$를 취해봅시다. 수식에서 확률적인 변수는 오직 상승 횟수 $j$뿐이므로, 평균 기호는 $j$에만 걸리게 됩니다.
$$\mathbb{E}\left[\ln\left(\frac{S_t}{S_0}\right)\right] = \mathbb{E}[j] (\ln u - \ln d) + n \ln d$$

이때 상승 횟수 $j$는 시행 횟수 $n$, 성공 확률 $q$인 **이항분포 $\text{Binomial}(n, q)$**를 따르므로, 이항분포의 평균 공식에 의해 $\mathbb{E}[j] = nq$가 됩니다.
> **💡 $nq$의 직관적 의미**: 동전을 100번 던질 때 앞면이 나올 확률이 0.5라면, 평균적인 앞면 출현 횟수는 $100 \times 0.5 = 50$회가 됩니다. 마찬가지로 $n$번 중 평균 상승 횟수는 $nq$회입니다.

#### 4) $n$으로 묶어내기: '주가 수익률의 단위 평균' 상정
$\mathbb{E}[j] = nq$를 대입하여 정리하면 다음과 같습니다.
$$\mathbb{E}\left[\ln\left(\frac{S_t}{S_0}\right)\right] = nq (\ln u - \ln d) + n \ln d = n \left[ q \ln u + (1-q) \ln d \right]$$

여기서 전체 시행 횟수 $n$으로 묶어낸 괄호 안의 값 $\hat{\mu}$를 **'주가 수익률의 단위 평균(Per-step Mean Log-return)'**으로 정의합니다.
$$\hat{\mu} = q \ln u + (1-q) \ln d$$

결국 전체 $t$기간 동안의 총 평균 로그수익률은 **단위 평균 $\hat{\mu}$를 $n$번 더한(곱한) 것**이 됩니다.
$$\mathbb{E}\left[\ln\left(\frac{S_t}{S_0}\right)\right] = n \cdot \hat{\mu}$$

---

### 8.5 주가 로그수익률의 분산과 '단위 분산'의 도출

#### 1) 로그수익률 식에 분산 $\text{Var}(\cdot)$ 적용하기
동일하게 로그수익률 식 $\ln\left(\frac{S_t}{S_0}\right) = j (\ln u - \ln d) + n \ln d$에 분산 기호 $\text{Var}(\cdot)$를 취해봅시다.

분산의 성질에 의해:
1. 더해진 상수항 $n \ln d$는 변동하지 않는 확정된 값이므로 분산 계산 시 **0으로 사라집니다** ($\text{Var}(X + C) = \text{Var}(X)$).
2. 확률변수 $j$ 앞에 곱해진 상수 $(\ln u - \ln d)$는 **제곱이 되어 밖으로 나옵니다** ($\text{Var}(a X) = a^2 \text{Var}(X)$).

따라서 로그수익률의 분산식은 오직 상승 횟수 $j$의 분산에 의해 결정됩니다.
$$\text{Var}\left(\ln\left(\frac{S_t}{S_0}\right)\right) = (\ln u - \ln d)^2 \cdot \text{Var}(j)$$

#### 2) 이항분포의 분산 $nq(1-q)$와 50:50의 의미
상승 횟수 $j$는 이항분포 $\text{Binomial}(n, q)$를 따르므로, 이항분포의 분산 공식에 의해 $\text{Var}(j) = nq(1-q)$가 됩니다.

> **💡 $nq(1-q)$의 직관적 의미**: 
> 시행 횟수 $n$이 일정할 때 $q(1-q)$ 값은 상승과 하강 확률의 편중이 없는 **50 대 50 ($q = 0.5$)일 때 최댓값(0.25)**을 갖습니다. 즉, 어느 한쪽으로 쏠리지 않고 방향성의 불확실성이 가장 클 때 주가 수익률의 분산(위험)도 가장 극대화됩니다.

#### 3) $n$으로 묶어내기: '주가 수익률의 단위 분산' 상정
$\text{Var}(j) = nq(1-q)$를 대입하여 정리하면 총 분산식은 다음과 같습니다.
$$\text{Var}\left(\ln\left(\frac{S_t}{S_0}\right)\right) = (\ln u - \ln d)^2 \cdot nq(1-q) = n \left[ q(1-q)(\ln u - \ln d)^2 \right]$$

여기서 전체 시행 횟수 $n$으로 묶어낸 괄호 안의 값 $\hat{\sigma}^2$를 **'주가 수익률의 단위 분산(Per-step Variance of Log-return)'**으로 정의합니다.
$$\hat{\sigma}^2 = q(1-q)(\ln u - \ln d)^2$$

결국 전체 $t$기간 동안의 총 로그수익률의 분산은 **단위 분산 $\hat{\sigma}^2$를 $n$번 더한(곱한) 것**이 됩니다.
$$\text{Var}\left(\ln\left(\frac{S_t}{S_0}\right)\right) = n \cdot \hat{\sigma}^2$$

---

### 8.6 주가 변동 폭($u, d$)의 스케일링 도출

#### 1) 변동 폭 고정 시 발생하는 발산 역설
만약 $n \to \infty$로 시간 간격($\Delta t = t/n$)을 무한히 쪼개면서 1회 상승/하강 폭 $u, d$를 고정된 값으로 둔다면, 총 분산 $n \cdot \hat{\sigma}^2$이 **무한대($\infty$)로 발산**해버리는 현실과 떨어진 결론이 나옵니다.
시간 간격 $\Delta t$는 0에 가깝게 좁아지는데 $u, d$ 폭이 그대로라면, 미세한 찰나마다 커다란 변동이 일어나는 셈이기 때문입니다.

따라서 시행 횟수 $n$이 늘어남에 따라 $u$와 $d$ 역시 1에 가깝게 미세하게 스케일링되어야 합니다.

#### 2) $n$단계 합산 분산과 연속시간 참 분산의 일치

**[1단계] 1단계 로그수익률의 2차 모멘트**
대칭 트리 $d = 1/u$를 상정하면, 1단계($\Delta t$) 로그수익률 $Y_i$는 확률 $q$로 $+\ln u$, 확률 $1-q$로 $-\ln u$를 갖는 이산 확률변수입니다.
이때 1단계 로그수익률의 2차 모멘트는 다음과 같습니다.
$$\mathbb{E}[Y_i^2] = q(\ln u)^2 + (1-q)(-\ln u)^2 = (\ln u)^2$$

**[2단계] $n$단계 합산 분산과 연속시간 분산 $\sigma^2 t$의 일치 조건**
만기까지 총 $n$번의 독립적인 주가 이동이 있으므로, 만기 총 분산은 1단계 분산의 $n$배가 됩니다.
$$\text{Var}\left[\ln \frac{S_t}{S_0}\right] \approx n \cdot \mathbb{E}[Y_i^2] = n(\ln u)^2$$

이 이산 합산 분산이 연속시간에서의 참된 현실 분산인 **$\sigma^2 t$**와 완벽히 일치해야 합니다.
$$n(\ln u)^2 = \sigma^2 t \implies (\ln u)^2 = \sigma^2 \frac{t}{n} = \sigma^2 \Delta t$$

#### 3) CRR 스케일링 공식의 완성
양변에 제곱근을 취하면 $u$와 $d$의 스케일링 공식이 탄생합니다.
$$\ln u = \sigma \sqrt{\Delta t} = \sigma \sqrt{\frac{t}{n}}$$

$$\implies u = e^{\sigma \sqrt{\Delta t}} = e^{\sigma \sqrt{t/n}}, \quad d = e^{-\sigma \sqrt{\Delta t}} = e^{-\sigma \sqrt{t/n}} = \frac{1}{u}$$

---

### 8.7 주가 상승 확률($q$)의 도출

#### 1) 1단계 평균식과 참 평균 $\mu t$의 일치
앞서 도출한 대칭 트리 조건($d = 1/u \implies \ln d = -\ln u$)을 1단계 로그수익률 평균식에 대입하면 다음과 같습니다.
$$\mathbb{E}[Y_i] = q \ln u + (1-q) \ln d = q \ln u + (1-q)(-\ln u) = (2q - 1) \ln u$$

만기 $t$까지 총 $n$번 이동했을 때의 총 평균 로그수익률은 1단계 평균의 $n$배가 됩니다.
$$\mathbb{E}\left[\ln \frac{S_t}{S_0}\right] = n \cdot \mathbb{E}[Y_i] = n (2q - 1) \ln u$$

이 이산 합산 평균이 연속시간 모형의 참된 평균 로그수익률 **$\mu t$**와 일치해야 합니다.
$$n (2q - 1) \ln u = \mu t$$

#### 2) 스케일링 공식 $\ln u = \sigma \sqrt{\Delta t}$ 대입 및 $q$ 구하기
앞서 구한 스케일링 공식 $\ln u = \sigma \sqrt{\Delta t} = \sigma \sqrt{\frac{t}{n}}$을 대입합니다.
$$n (2q - 1) \cdot \sigma \sqrt{\frac{t}{n}} = \mu t$$

양변을 정리하여 $q$에 대해 방정식으로 풀면 다음과 같습니다.
$$\sqrt{n} (2q - 1) \sigma = \mu \sqrt{t} \implies (2q - 1) \sigma = \mu \sqrt{\frac{t}{n}} = \mu \sqrt{\Delta t}$$

$$2q - 1 = \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$$

$$\therefore q = \frac{1}{2} + \frac{1}{2} \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$$

#### 3) 주가 상승 확률($q$)이 갖는 직관적 의미
- **기본 확률 $\frac{1}{2}$ (50%)**: 주가 상승과 하강의 기본 확률은 대칭적인 $50\%$($1/2$)에서 출발합니다.
- **미세 조정 항 $\frac{1}{2}\left(\frac{\mu}{\sigma}\right)\sqrt{\Delta t}$**: 주가가 위로 올라가려는 추세(드리프트 $\mu$)가 변동성($\sigma$) 대비 얼마나 강한가($\frac{\mu}{\sigma}$)에 따라, 상승 확률이 $50\%$에서 아주 살짝 **위쪽으로 편향(drifted)**됩니다.
- $\Delta t \to 0$ ($n \to \infty$)이 되면 $q \to \frac{1}{2}$로 수렴하지만, 이 미세한 $\sqrt{\Delta t}$ 수준의 상승 우위가 $n$번 누적되어 최종 만기 시점의 참 평균 $\mu t$를 형성합니다.

---

### 8.8 검증: 스케일링 변수 대입을 통한 발산 역설의 완벽한 해결

앞서 도출한 스케일링된 변수 $u, d, q$를 다시 원래의 단위 평균 및 총 평균 식에 대입하여 $n \to \infty$에서 발산 문제가 실제로 어떻게 해결되는지 검증해 봅시다.

#### 1) 도출된 스케일링 변수 복습
- $\ln u = \sigma \sqrt{\Delta t} = \sigma \sqrt{\frac{t}{n}}$
- $\ln d = -\sigma \sqrt{\Delta t} = -\sigma \sqrt{\frac{t}{n}}$
- $q = \frac{1}{2} + \frac{1}{2} \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$

#### 2) 단위 평균 $\hat{\mu}$에 대입하기
이항 모형에서 1단계 단위 평균 로그수익률 수식에 대칭 조건($\ln d = -\ln u$)을 전개하면 다음과 같습니다.
$$\hat{\mu} = \mathbb{E}[Y_i] = q \ln u + (1-q) \ln d = q \ln u + (1-q)(-\ln u) = (2q - 1) \ln u$$

여기서 $(2q - 1)$ 부분에 $q = \frac{1}{2} + \frac{1}{2} \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$를 대입하여 정리해 봅시다.
$$2q - 1 = 2 \left( \frac{1}{2} + \frac{1}{2} \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t} \right) - 1 = 1 + \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t} - 1 = \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$$

이제 $(2q - 1) = \left(\frac{\mu}{\sigma}\right) \sqrt{\Delta t}$와 $\ln u = \sigma \sqrt{\Delta t}$를 단위 평균 식 $\hat{\mu} = (2q - 1) \ln u$에 대입합니다.
$$\hat{\mu} = \left( \frac{\mu}{\sigma} \sqrt{\Delta t} \right) \cdot \left( \sigma \sqrt{\Delta t} \right) = \mu \cdot (\sqrt{\Delta t})^2 = \mu \Delta t = \mu \frac{t}{n}$$

> **✨ 깨달음의 순간**: 한 스텝 당 평균 로그수익률 $\hat{\mu}$는 고정된 상수가 아니라, 시행 횟수 $n$이 늘어남에 따라 무한히 작아지는 **$\mu \frac{t}{n}$**로 완벽하게 스케일링됩니다.

#### 3) 만기 총 평균 로그수익률의 계산 (발산 해결)
이제 만기 시점까지 $n$번 이동했을 때의 총 평균 로그수익률을 구하기 위해 단위 평균을 $n$번 곱해봅시다.
$$\mathbb{E}\left[\ln \frac{S_t}{S_0}\right] = n \cdot \hat{\mu} = n \cdot \left( \mu \frac{t}{n} \right)$$

시행 횟수 $n$과 분모의 $n$이 **완벽하게 약분**됩니다!
$$\mathbb{E}\left[\ln \frac{S_t}{S_0}\right] = \mu t$$

#### 4) 분산 역시 동일하게 수렴 ($\sigma^2 t$)
마찬가지로 단위 분산 $\hat{\sigma}^2 = q(1-q)(\ln u - \ln d)^2$에 대입하면:
- $\ln u - \ln d = 2 \sigma \sqrt{\Delta t} \implies (\ln u - \ln d)^2 = 4 \sigma^2 \Delta t$
- $q(1-q) = \left(\frac{1}{2} + \dots\right)\left(\frac{1}{2} - \dots\right) \approx \frac{1}{4}$ ($\Delta t \to 0$ 시)

$$\hat{\sigma}^2 \approx \frac{1}{4} \cdot 4 \sigma^2 \Delta t = \sigma^2 \Delta t = \sigma^2 \frac{t}{n}$$

총 분산 역시 $n$을 곱하면 분모 $n$이 약분되어 정확히 **$\sigma^2 t$**로 안착됩니다.
$$\text{Var}\left[\ln \frac{S_t}{S_0}\right] = n \cdot \hat{\sigma}^2 = n \cdot \left( \sigma^2 \frac{t}{n} \right) = \sigma^2 t$$

#### 5) 결론: 무한대($n$)와 무한소($1/n$)의 완벽한 상쇄
$n \to \infty$로 쪼갤 때 $u, d, q$를 적절히 스케일링하지 않으면 시행 횟수 $n$ 때문에 무한대로 발산하지만, CRR의 스케일링 공식을 적용하면 1단계 평균과 분산이 정확히 $1/n$의 비율로 작아져($\mu \frac{t}{n}, \sigma^2 \frac{t}{n}$), **$n \times \frac{1}{n} = 1$로 상쇄되며 폭발하던 값이 우리가 원하던 현실의 만기 평균 $\mu t$와 분산 $\sigma^2 t$로 완벽하게 수렴**하게 됩니다.

---

## 9. 주가 로그수익률의 정규분포 수렴과 옵션 행사확률 $N(d_2)$ 도출

### 9.1 갈톤보드(Galton Board)로 이해하는 로그수익률의 정규분포 수렴

앞서 주가의 **로그수익률**이 단위 로그수익률들의 **'합'**으로 표현됨을 보았습니다. 
그렇다면 왜 단위 수익률들을 무수히 많이 더하면($n \to \infty$) 주가 로그수익률은 정규분포(종 모양)로 수렴하게 될까요? 

이를 가장 직관적으로 이해할 수 있는 물리 장치가 바로 **갈톤보드(Galton Board)**입니다.

```
       ●  (구슬 투입: S_0)
      / \
     ●   ●  (1단계 좌/우 튕김)
    / \ / \
   ●   ●   ●  (2단계)
  / \ / \ / \
 ●   ●   ●   ● (n단계...)
=================
  | |█|██|█| |  (바닥: 정규분포 종 모양 완성!)
```

#### 1) 갈톤보드의 원리
삼각형 형태로 핀이 촘촘히 박힌 판 위에 구슬을 떨어뜨리면, 구슬은 핀에 부딪힐 때마다 50%의 확률로 **오른쪽(상승)** 또는 **왼쪽(하강)**으로 튕겨 내려갑니다.

- **극단적인 경우의 희소성**: 구슬이 핀을 만날 때마다 매번 오른쪽으로만 튕기거나($u^n$), 매번 왼쪽으로만 튕길($d^n$) 확률은 극히 드뭅니다. (동전을 100번 던져 100번 모두 앞면이 나올 확률과 같습니다.)
- **중앙 쏠림 현상**: 대부분의 구슬은 오른쪽과 왼쪽으로 번갈아 튕기며 내려오기 때문에, 바닥에 도달했을 때는 **가운데(평균 부근)에 가장 많은 구슬이 쌓이게 됩니다.**

학교 한 학급에서 키가 아주 작거나 아주 큰 학생은 극히 드물고 대부분 평균 키 근처에 모여 있는 것처럼, 구슬이 쌓인 바닥의 모양은 완벽한 **대칭형 종 모양(Bell Curve), 즉 정규분포**를 형성합니다.

#### 2) 주가 로그수익률과의 연결
주가의 로그수익률 역시 갈톤보드의 구슬과 똑같이 움직입니다.
$$\ln\left(\frac{S_t}{S_0}\right) = \sum_{i=1}^{n} Y_i$$

기간을 무한히 쪼갤수록($n \to \infty$, 핀의 층수가 무한히 많아질수록) 미세한 단위 로그수익률들($+\ln u$ 또는 $-\ln u$)이 수없이 누적되면서, 만기 로그수익률의 확률분포는 **완벽한 정규분포 $\mathcal{N}(\mu t, \sigma^2 t)$**로 자연스럽게 수렴하게 됩니다.

---

### 9.2 이산 행사확률 $\Phi(a; n, p)$의 연속 수렴 유도

이제 주가 로그수익률이 정규분포로 수렴한다는 사실을 바탕으로, 이산 모형의 옵션 행사확률 $\Phi(a; n, p)$를 연속 모형으로 변환해 봅시다.

#### 1) 이산 모형의 여확률(미행사 확률) 정의
- 옵션이 행사될 이항 누적확률: $\Phi(a; n, p) = P(j \ge a)$
- 옵션이 행사되지 않을 여확률: $1 - \Phi(a; n, p) = P(j < a) = P(j \le a - 1)$

#### 2) 측도 전환: 왜 $q$에서 $p$로 전환되며, 왜 동일한 통계 성질이 성립하는가?

**① 무차익 복제 포트폴리오와 위험중립 확률 $p$의 선택**
- 앞서 살펴보았듯 옵션 가격은 주가의 실제 상승 확률 $q$나 투자자의 위험 선호도에 의해 결정되는 것이 아닙니다. 
- 주식과 무위험 자산을 조합해 옵션과 동일한 현금흐름을 만드는 **무차익 복제 포트폴리오(Replication Portfolio)** 원리에 따라, 옵션 평가 공식에는 실제 확률 $q$ 대신 **위험중립 확률 $p$**가 사용됩니다.

**② 왜 $q$에서 성립한 이항분포 성질이 $p$에서도 그대로 성립하는가?**
- 주가의 이항나무 구조(시행 횟수 $n$, 상승 폭 $u$, 하강 폭 $d$)와 확률변수인 상승 횟수 $j$의 결합 구조는 전혀 변하지 않습니다.
- 이항분포 $\text{Binomial}(n, \cdot)$의 핵심 성질인 **[평균 $= n \times \text{성공확률}$]**, **[분산 $= n \times \text{성공확률} \times (1-\text{성공확률})$]**, 그리고 **[중심극한정리에 의한 정규분포 수렴]**은 파라미터가 $q$이든 $p$이든 이항분포라는 확률 구조 자체에서 오는 고유한 통계적 성질입니다.
- 따라서 파라미터를 실제 확률 $q$에서 위험중립 확률 $p$로 바꾼다 해도, 이항분포의 모든 수학적 구조와 성질은 $p$에서도 **100% 동일하게 성립**하게 됩니다.

**③ $q$에서 $p$로의 자연스러운 측도 전환과 4가지 핵심 요소**
이에 따라 옵션 가치 평가를 위한 표준화 작업 시, 확률 측도를 실제 세상($q$)에서 위험중립 세상($p$)으로 전환하여 다음 4가지 핵심 요소를 사용합니다.
1. **확률변수**: $j$ (상승 횟수)
2. **위험중립 평균**: $\mathbb{E}[j] = np$  *(실제 평균 $nq$의 위험중립 대응)*
3. **위험중립 표준편차**: $\sqrt{\text{Var}(j)} = \sqrt{np(1-p)}$  *(실제 표준편차 $\sqrt{nq(1-q)}$의 위험중립 대응)*
4. **미행사 경계값**: $a - 1$

또한, 위험중립 세상에서의 1단계 평균 로그수익률임을 명시하기 위해 **위험중립 단위 평균 $\hat{\mu}_p$**를 다음과 같이 정의합니다.
$$\hat{\mu}_p = p \ln u + (1-p) \ln d = (2p - 1) \ln u$$

#### 3) 여확률 $P(j \le a-1)$의 표준화 수식 전개
위의 4가지 요소를 이용해 미행사 확률 $P(j \le a - 1)$의 양변을 [변수 - 평균] / [표준편차]로 표준화하면 다음과 같이 변형됩니다.

$$1 - \Phi(a; n, p) = P(j \le a - 1) = P\left( \frac{j - np}{\sqrt{np(1-p)}} \le \frac{(a - 1) - np}{\sqrt{np(1-p)}} \right)$$

$$= P\left( Z \le \frac{(a - 1) - np}{\sqrt{np(1-p)}} \right)$$

#### 4) [예고편] 연속 극한($n \to \infty$)에서 BSM의 $N(d_2)$로의 마법 같은 수렴!
스텝 수 $n \to \infty$로 취하는 연속 극한에서는, 우변 경계값이 놀랍게도 BSM 연속 모형의 핵심 변수인 **$-d_2$**로 정확히 수렴하게 됩니다.
$$1 - \Phi(a; n, p) \longrightarrow N(-d_2)$$

여기에 정규분포의 좌우 대칭 성질($1 - N(-x) = N(x)$)을 적용하면:
$$\Phi(a; n, p) \longrightarrow N(d_2)$$

즉, 이산 모형의 이항 행사확률 $\Phi(a; n, p)$가 연속 모형의 위험중립 행사확률 **$N(d_2)$**로 완벽하게 수렴하는 마법이 일어납니다! 
*(다음 파트에서 이 경계값 $\frac{(a - 1) - np}{\sqrt{np(1-p)}}$가 어떻게 정확히 $-d_2$로 유도되는지 그 세부 수식을 본격적으로 파헤쳐 보겠습니다!)*

---

### 9.3 이산 표준화 인자들의 단계별 도출 및 순수 이산 표준화식 대입

테일러 전개나 연속 극한을 취하기에 앞서, 먼저 순수한 이산(Discrete) 상태에서 표준화에 필요한 4가지 인자($j$, $np$, $\sqrt{np(1-p)}$, $a-1$)를 $\ln(u/d)$를 포함한 이산 변수 그대로 도출하고, 이를 원래의 이항 표준화식에 대입해 보겠습니다.

---

#### 1단계: 확률변수 $j$ (상승 횟수와 로그수익률의 관계)

만기 주가 $S_n = S_0 u^j d^{n-j}$의 양변을 $S_0$로 나누고 자연로그를 취하면 다음과 같습니다.
$$\ln\left(\frac{S_n}{S_0}\right) = j \ln u + (n-j) \ln d = j (\ln u - \ln d) + n \ln d$$

분모 표현을 위해 $\ln(u/d) = \ln u - \ln d$로 나타내면:
$$\ln\left(\frac{S_n}{S_0}\right) = j \ln(u/d) + n \ln d$$

이 식으로부터 상승 횟수 $j$를 로그수익률 표현으로 직접 추출할 수 있습니다.
$$j = \frac{\ln(S_n/S_0) - n \ln d}{\ln(u/d)}$$

---

#### 2단계: 위험중립 단위 평균 $\hat{\mu}_p$와 위험중립 기댓값 $np$

8.4절에서 구했던 1단계 단위 평균 로그수익률 공식에서 확률 $q$를 위험중립 확률 $p$로 전환하여 **위험중립 단위 평균 $\hat{\mu}_p$**를 정의합니다.
$$\hat{\mu}_p = p \ln u + (1-p) \ln d = p (\ln u - \ln d) + \ln d = p \ln(u/d) + \ln d$$

위 식을 $p$에 대해 정리하면 다음과 같습니다.
$$\hat{\mu}_p - \ln d = p \ln(u/d) \implies p = \frac{\hat{\mu}_p - \ln d}{\ln(u/d)}$$

양변에 시행 횟수 $n$을 곱하면 위험중립 기댓값 $np$가 도출됩니다.
$$np = \frac{n \hat{\mu}_p - n \ln d}{\ln(u/d)}$$

---

#### 3단계: 위험중립 단위 분산 $\hat{\sigma}_p^2$와 위험중립 표준편차 $\sqrt{np(1-p)}$

8.5절의 단위 분산 공식에서 확률 $q$를 위험중립 확률 $p$로 전환하여 **위험중립 단위 분산 $\hat{\sigma}_p^2$**를 정의합니다.
$$\hat{\sigma}_p^2 = p(1-p)(\ln u - \ln d)^2 = p(1-p) [\ln(u/d)]^2$$

양변을 $[\ln(u/d)]^2$로 나누어 $p(1-p)$만 남기면:
$$p(1-p) = \frac{\hat{\sigma}_p^2}{[\ln(u/d)]^2}$$

양변에 제곱근을 취하고 $\sqrt{n}$을 곱하면 위험중립 표준편차 $\sqrt{np(1-p)}$가 구성됩니다.
$$\sqrt{p(1-p)} = \frac{\hat{\sigma}_p}{\ln(u/d)} \implies \sqrt{np(1-p)} = \frac{\sqrt{n} \hat{\sigma}_p}{\ln(u/d)}$$

---

#### 4단계: 미행사 경계값 $a-1$

옵션이 만기에 행사되기(In-the-Money) 위한 조건은 $u^a d^{n-a} S_0 - K \ge 0$ (즉, $S_n \ge K$)을 만족하는 최소 상승 횟수 $a$를 찾는 것입니다.
$$a \ln u + (n-a) \ln d \ge \ln(K/S_0) \implies a \ln(u/d) + n \ln d \ge \ln(K/S_0)$$

$$a \ge \frac{\ln(K/S_0) - n \ln d}{\ln(u/d)}$$

이를 만족하는 최소 정수가 $a$이므로, **행사되지 않을 최고 상승 횟수 $a-1$**은 경계값 식에 등호를 붙이고 정수화 보정항 $\epsilon$ ($0 \le \epsilon < 1$)을 뺀 형태가 됩니다.
$$a - 1 = \frac{\ln(K/S_0) - n \ln d}{\ln(u/d)} - \epsilon$$

여기서 $\epsilon$항을 분모 $\ln(u/d)$와 통분하여 분자로 올려 묶어주면 다음과 같습니다.
$$a - 1 = \frac{\ln(K/S_0) - n \ln d - \epsilon \ln(u/d)}{\ln(u/d)}$$

---

#### 5단계: 원래의 이항 표준화식 $\frac{(a-1) - np}{\sqrt{np(1-p)}}$에 구한 값 대입 및 치환

이제 2단계, 3단계, 4단계에서 구한 표현식을 원래의 여확률 표준화식 $\frac{(a-1) - np}{\sqrt{np(1-p)}}$에 직접 대입하여 치환해 봅시다.

**1) 분자 $(a-1) - np$에 4단계와 2단계의 식 대입**
$$(a-1) - np = \frac{\ln(K/S_0) - n \ln d - \epsilon \ln(u/d)}{\ln(u/d)} - \frac{n \hat{\mu}_p - n \ln d}{\ln(u/d)}$$

$$= \frac{\ln(K/S_0) - n \ln d - \epsilon \ln(u/d) - n \hat{\mu}_p + n \ln d}{\ln(u/d)}$$

분자의 $-n \ln d$와 $+n \ln d$가 서로 소거(상쇄)되므로 분자는 다음과 같이 간결하게 정리됩니다.
$$(a-1) - np = \frac{\ln(K/S_0) - n \hat{\mu}_p - \epsilon \ln(u/d)}{\ln(u/d)}$$

**2) 전체 표준화식에 3단계 분모식 대입 및 분모 $\ln(u/d)$ 약분**
$$\frac{(a-1) - np}{\sqrt{np(1-p)}} = \frac{\frac{\ln(K/S_0) - n \hat{\mu}_p - \epsilon \ln(u/d)}{\ln(u/d)}}{\frac{\sqrt{n} \hat{\sigma}_p}{\ln(u/d)}}$$

분자와 분모의 공통 분모인 $\ln(u/d)$가 약분되어 소거됩니다!
$$\frac{(a-1) - np}{\sqrt{np(1-p)}} = \frac{\ln(K/S_0) - n \hat{\mu}_p - \epsilon \ln(u/d)}{\sqrt{n} \hat{\sigma}_p}$$

---

## 9.4 테일러 전개를 이용한 핵심 인자들의 근사치 도출

### 1. 테일러 전개의 목적 및 2차항까지 전개하는 이유
- **테일러 전개의 목적**: 지수함수($e^{\text{값}}$) 형태로 표현된 주가 변동 폭($u, d$)과 이자율 증식인자($\hat{r}$)를 복잡한 지수 연산 대신 **다항식(더하기/빼기) 형태**로 변환하여, $n \to \infty$ 극한에서 식을 쉽게 소거하고 정리하기 위함입니다.
- **2차항까지 전개하는 이유**: 미소변수 $x = \sqrt{t/n}$에 대해 $x^2 = t/n = \Delta t$ 입니다. 시행 횟수 $n = t/x^2$ 이므로, **$x$의 2차항($x^2 = \Delta t$)까지 전개해야 $n$을 곱했을 때 유한한 값($O(1)$, 예: $rt, \sigma^2 t$)으로 살아남습니다.** ($x^3$ 이상의 고차항은 $n$과 곱해져도 $x \to 0$에 의해 모두 0으로 사라집니다.)

### 2. 기본 도구 제시
> **💡 지수함수 테일러 전개 기본 공식**
> $$e^y = 1 + y + \frac{1}{2}y^2 + \mathcal{O}(y^3)$$

### 3. $x = \sqrt{t/n}$ 치환 및 3가지 핵심 인자 테일러 전개
- **치환 변수 설정**: $x = \sqrt{\frac{t}{n}}$ (따라서 $x^2 = \frac{t}{n} = \Delta t$)

1. **상승 폭 ($u$) 의 2차항 전개** ($y = \sigma x$ 대입)
   $$u = e^{\sigma \sqrt{t/n}} = e^{\sigma x} = 1 + \sigma x + \frac{1}{2}\sigma^2 x^2 + \mathcal{O}(x^3)$$

2. **하강 폭 ($d$) 의 2차항 전개** ($y = -\sigma x$ 대입)
   $$d = e^{-\sigma \sqrt{t/n}} = e^{-\sigma x} = 1 - \sigma x + \frac{1}{2}\sigma^2 x^2 + \mathcal{O}(x^3)$$

3. **단위 기간 무위험 증식인자 ($\hat{r}$) 의 2차항 전개** ($y = r x^2$ 대입)
   $$\hat{r} = e^{r \frac{t}{n}} = e^{r x^2} = 1 + r x^2 + \mathcal{O}(x^4)$$

---

## 9.5 테일러 전개를 통한 위험중립 확률 $p$의 근사치 도출 및 실제 확률 $q$와의 비교

### 1. 위험중립 확률 $p$의 이산 무차익 공식 상기
이항 모형에서 무차익 복제 원리에 의해 도출된 위험중립 상승 확률 $p$의 정의는 다음과 같습니다.
$$p = \frac{\hat{r} - d}{u - d}$$

---

### 2. $u, d, \hat{r}$의 테일러 2차 근사식 대입 및 분모·분자 계산

9.4절에서 도출한 $x = \sqrt{t/n} = \sqrt{\Delta t}$ 치환 및 2차항 테일러 전개식을 대입합니다.

#### 1) 분모 ($u - d$) 계산
$$u - d = \left(1 + \sigma x + \frac{1}{2}\sigma^2 x^2 + \mathcal{O}(x^3)\right) - \left(1 - \sigma x + \frac{1}{2}\sigma^2 x^2 + \mathcal{O}(x^3)\right)$$

상수항 $1$과 2차항 $\frac{1}{2}\sigma^2 x^2$이 소거되므로 분모는 다음과 같이 간결해집니다.
$$u - d = 2\sigma x + \mathcal{O}(x^3)$$

#### 2) 분자 ($\hat{r} - d$) 계산
$$\hat{r} - d = \left(1 + r x^2 + \mathcal{O}(x^4)\right) - \left(1 - \sigma x + \frac{1}{2}\sigma^2 x^2 + \mathcal{O}(x^3)\right)$$

상수항 $1$이 소거되고, $x$의 차수별로 묶어 정리하면 다음과 같습니다.
$$\hat{r} - d = \sigma x + \left(r - \frac{1}{2}\sigma^2\right) x^2 + \mathcal{O}(x^3)$$

---

### 3. 위험중립 확률 $p$의 최종 테일러 근사식 도출

구한 분모와 분자를 $p = \frac{\hat{r} - d}{u - d}$ 식에 대입합니다.

$$p = \frac{\sigma x + \left(r - \frac{1}{2}\sigma^2\right) x^2 + \mathcal{O}(x^3)}{2\sigma x + \mathcal{O}(x^3)}$$

분자, 분모를 $2\sigma x$로 나누어 정리하면:

$$p = \frac{1}{2} + \frac{r - \frac{1}{2}\sigma^2}{2\sigma} x + \mathcal{O}(x^2)$$

여기서 치환 변수 $x = \sqrt{\frac{t}{n}} = \sqrt{\Delta t}$를 다시 복원하면, 테일러 전개를 이용한 **위험중립 확률 $p$의 핵심 근사식**이 완성됩니다!

$$\therefore p = \frac{1}{2} + \frac{1}{2} \left( \frac{r - \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

---

### 4. 실제 확률 $q$와 위험중립 확률 $p$의 아름다운 구조적 대칭성

앞서 8.7절에서 구한 실제 세계에서의 주가 상승 확률 $q$와 방금 구한 위험중립 세계에서의 상승 확률 $p$를 비교해봅시다.

| 구분 | 확률 공식 표현 | 핵심 편향 인자 (Drift) |
| :--- | :--- | :--- |
| **실제 세상 확률 ($q$)** | $q = \frac{1}{2} + \frac{1}{2} \left( \frac{\mu}{\sigma} \right) \sqrt{\Delta t}$ | **$\mu$** (주가의 실제 기댓값 수익률) |
| **위험중립 세상 확률 ($p$)** | $p = \frac{1}{2} + \frac{1}{2} \left( \frac{r - \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t}$ | **$r - \frac{1}{2}\sigma^2$** (위험중립 연속 로그 드리프트) |

> **💡 금융공학적 통찰 및 직관**
> 1. **기본 출발점 50%**: 실제 세상이나 위험중립 세상 모두 주가의 기본 움직임은 대칭적인 **50%($1/2$)**에서 출발합니다.
> 2. **드리프트 치환 ($\mu \longrightarrow r - \frac{1}{2}\sigma^2$)**: 
>    - 실제 세상에서는 투자자의 위험 선호도가 반영된 주가 상승률 **$\mu$**가 확률을 위쪽으로 편향시킵니다.
>    - 반면 위험중립 세상에서는 위험 프리미엄이 제거되어 기댓값 수익률이 무위험 이자율 $r$로 치환되는데, 연속시간 로그수익률 관점에서는 변동성에 의한 젠센의 부등식(Jensen's Inequality) 차감항인 **$-\frac{1}{2}\sigma^2$**가 자연스럽게 결합하여 **$r - \frac{1}{2}\sigma^2$**가 편향을 결정합니다.
> 3. **샤프 비율 형태의 스케일링**: 두 확률 모두 드리프트를 변동성 $\sigma$로 나눈 값($\frac{\text{Drift}}{\sigma}$)에 비례하여 미세하게 편향되며, 이 미세한 편향이 $n \to \infty$ 극한에서 누적되어 연속시간 BSM 모형의 분포를 완벽하게 형성하게 됩니다.

---

## 9.6 테일러 전개와 위험중립 확률 $p$를 이용한 최종 표준화 및 $N(d_2)$ 도출

### 1. 9.3절 이산 표준화식 상기

9.3절 5단계에서 우리는 미행사 여확률 $1 - \Phi(a; n, p)$의 이항 표준화식을 다음과 같이 공통 분모 $\ln(u/d)$를 약분하여 정리했습니다.

$$1 - \Phi(a; n, p) = P\left( Z \le \frac{(a-1) - np}{\sqrt{np(1-p)}} \right) = P\left( Z \le \frac{\ln(K/S_0) - n \hat{\mu}_p - \epsilon \ln(u/d)}{\sqrt{n} \hat{\sigma}_p} \right)$$

---

### 2. 테일러 근사치 대입 및 연속 극한($n \to \infty$) 적용

이제 9.4절과 9.5절에서 도출한 테일러 근사치 및 연속 극한 결과를 위 표준화식의 우변 경계값에 대입해 봅시다.

1. **위험중립 총 평균 $n \hat{\mu}_p$ 의 수렴**:
   9.5절에서 구한 $p = \frac{1}{2} + \frac{1}{2} \left( \frac{r - \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t}$ 와 테일러 전개식을 1단계 위험중립 평균 $\hat{\mu}_p = (2p-1)\ln u$ 에 대입하면, $n$을 곱한 만기 총 평균은 다음과 같이 수렴합니다.
   $$n \hat{\mu}_p \longrightarrow \left( r - \frac{1}{2}\sigma^2 \right) t$$
   *(실제 확률 $q$ 식의 $\mu t$ 자리에 위험중립 연속 로그 드리프트인 $(r - \frac{1}{2}\sigma^2)t$ 가 정확히 대응됩니다.)*

2. **위험중립 총 표준편차 $\sqrt{n} \hat{\sigma}_p$ 의 수렴**:
   1단계 위험중립 분산 근사치 $\hat{\sigma}_p^2 \approx \sigma^2 \Delta t = \sigma^2 \frac{t}{n}$ 에 $n$을 곱하고 제곱근을 취하면 만기 총 표준편차로 수렴합니다.
   $$\sqrt{n} \hat{\sigma}_p \longrightarrow \sigma \sqrt{t}$$

3. **잔여 정수화 보정항 $\epsilon \ln(u/d)$ 의 소멸**:
   $n \to \infty$ 극한에서 단위 시간 간격 $\Delta t \to 0$이 되므로, $\ln(u/d) \approx 2\sigma \sqrt{\Delta t} \to 0$입니다. 
   따라서 정수 보정항 $\epsilon \ln(u/d)$는 0으로 완전히 소거됩니다.

---

### 3. 미행사 경계값 $Z_0$의 도출 및 $-d_2$와의 일치

위 수렴 결과들을 표준화 경계값 식에 대입하면 다음과 같습니다.

$$Z_0 = \lim_{n \to \infty} \frac{\ln(K/S_0) - n \hat{\mu}_p - \epsilon \ln(u/d)}{\sqrt{n} \hat{\sigma}_p} = \frac{\ln(K/S_0) - \left( r - \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}}$$

여기서 자연로그의 성질 $\ln(K/S_0) = -\ln(S_0/K)$를 이용하여 마이너스 기호를 밖으로 묶어내면:

$$Z_0 = \frac{-\ln(S_0/K) - \left( r - \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}} = -\left[ \frac{\ln(S_0/K) + \left( r - \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}} \right]$$

대괄호 안의 식은 바로 BSM 연속 모형의 핵심 변수인 **$d_2$**의 정의입니다!
$$d_2 = \frac{\ln(S_0/K) + \left( r - \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}}$$

따라서 미행사 여확률의 표준화 경계값 $Z_0$는 정확히 **$-d_2$**로 도출됩니다.

$$Z_0 = -d_2$$

---

### 4. 정규분포의 대칭성을 통한 행사확률 $N(d_2)$의 최종 도출

미행사 여확률의 연속 극한이 $N(-d_2)$이므로, 옵션이 행사될 이항 누적확률 $\Phi(a; n, p)$의 연속 극한은 다음과 같이 유도됩니다.

$$1 - \Phi(a; n, p) \longrightarrow N(-d_2)$$

$$\implies \Phi(a; n, p) \longrightarrow 1 - N(-d_2)$$

이때 표준정규분포 $N(x)$의 좌우 대칭성 성질인 **$1 - N(-x) = N(x)$**를 적용하면:

$$\therefore \lim_{n \to \infty} \Phi(a; n, p) = N(d_2)$$

이산 이항 모형(CRR)의 위험중립 행사확률 $\Phi(a; n, p)$가 연속 극한에서 블랙-숄즈-머튼(BSM) 모형의 **$N(d_2)$**로 완벽히 수렴함을 증명했습니다!

---

> **💡 [독자 참고] Cox-Ross-Rubinstein(1979) 원 논문 표기법과의 일치성 확인**
> 
> Cox, Ross, Rubinstein의 1979년 원 논문(Option Pricing: A Simplified Approach)을 참고하는 독자라면, 원 논문의 이산 경계값이 본 원고의 표현과 살짝 다르게 보여 혼란스러울 수 있습니다.
> 
> - **CRR(1979) 원 논문의 표기**: 단위 기간 무위험 증식인자를 이산 이자율 $r$ (본 원고의 $\hat{r}$)로 나타내어, 행사 경계값 식을 $\ln\left(\frac{K r^{-n}}{S_0}\right)$ 형태로 기술했습니다.
> - **본 원고와의 일치성**: $\ln\left(\frac{K r^{-n}}{S_0}\right) = \ln(K/S_0) - n \ln r$ 로 분리할 수 있습니다. 연속시간 극한($n \to \infty$)에서는 단위 증식인자의 $n$승이 만기 연속 할인인자 $e^{rt}$로 수렴하므로 ($r^n \to e^{rt}$ 또는 $n \ln r \to rt$),
>   $$\lim_{n \to \infty} \ln\left(\frac{K r^{-n}}{S_0}\right) = \ln\left(\frac{K}{S_0}\right) - rt = \ln\left(\frac{K e^{-rt}}{S_0}\right)$$
> 
> 즉, 원 논문의 이산 표기 $r^{-n}$은 연속시간에서 **현금의 만기 현재가치 할인인자 $e^{-rt}$**로 완벽하게 변환되므로, 본 원고에서 전개한 BSM 수렴식과 정확히 동일한 결과입니다.

---

## 9.7 첫 번째 항의 비밀: 확률 $p'$과 $N(d_1)$의 도출 및 $d_1 = d_2 + \sigma\sqrt{t}$ 유도

### 1. 첫 번째 항의 확률 $p'$의 정의 (CRR 1979 원 논문 방식)

BSM 옵션 가격 공식의 첫 번째 항인 주식 가치 항 $S_0 N(d_1)$에 대응하는 이산 이항 모형의 표현식은 $S_0 \Phi(a; n, p')$ 입니다.
Cox, Ross, Rubinstein(1979) 원 논문에서는 이 첫 번째 항을 묶어내는 과정에서 **새로운 확률 $p'$**을 다음과 같이 정의합니다.

$$p' \equiv \frac{u}{\hat{r}} p$$

---

### 2. 테일러 전개를 통한 $p'$의 근사식 및 드리프트 변화

9.4절에서 구한 $u = e^{\sigma \sqrt{\Delta t}}$와 $\hat{r} = e^{r \Delta t}$의 비(ratio)를 테일러 전개해 봅시다.

$$\frac{u}{\hat{r}} = \frac{e^{\sigma \sqrt{\Delta t}}}{e^{r \Delta t}} = e^{\sigma \sqrt{\Delta t} - r \Delta t} \approx 1 + \sigma \sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

이제 9.5절에서 구한 위험중립 확률 $p = \frac{1}{2} + \frac{1}{2}\left(\frac{r - \frac{1}{2}\sigma^2}{\sigma}\right)\sqrt{\Delta t}$ 식에 위 테일러 근사치를 곱합니다.

$$p' = \left( 1 + \sigma \sqrt{\Delta t} \right) \cdot \left[ \frac{1}{2} + \frac{1}{2}\left(\frac{r - \frac{1}{2}\sigma^2}{\sigma}\right)\sqrt{\Delta t} \right] + \mathcal{O}(\Delta t)$$

$$= \frac{1}{2} + \frac{1}{2} \sigma \sqrt{\Delta t} + \frac{1}{2}\left(\frac{r - \frac{1}{2}\sigma^2}{\sigma}\right)\sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

분자 항을 $\frac{1}{2\sigma}\sqrt{\Delta t}$ 로 공통으로 묶어주면:

$$p' = \frac{1}{2} + \frac{1}{2\sigma} \left[ \sigma^2 + r - \frac{1}{2}\sigma^2 \right] \sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

$$\therefore p' = \frac{1}{2} + \frac{1}{2} \left( \frac{r + \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

> **💡 $p$와 $p'$의 명쾌한 드리프트 비교**
> - **위험중립 확률 $p$ (현금 기준)**: $p = \frac{1}{2} + \frac{1}{2} \left( \frac{r - \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t} \implies \text{로그 드리프트: } r - \frac{1}{2}\sigma^2$
> - **주가측도 확률 $p'$ (주식 기준)**: $p' = \frac{1}{2} + \frac{1}{2} \left( \frac{r + \frac{1}{2}\sigma^2}{\sigma} \right) \sqrt{\Delta t} \implies \text{로그 드리프트: } r + \frac{1}{2}\sigma^2$
>
> 오직 2차 모멘트 항의 부호만 **마이너스($-\frac{1}{2}\sigma^2$)에서 플러스($+\frac{1}{2}\sigma^2$)**로 바뀐 것을 볼 수 있습니다!

---

### 3. $d_1$의 도출 및 연속 수렴 $N(d_1)$

이제 $p'$의 위험중립 단위 평균 $\hat{\mu}_{p'} = (2p'-1)\ln u$에 $n$을 곱한 만기 총 평균을 구하면 다음과 같습니다.

$$n \hat{\mu}_{p'} \longrightarrow \left( r + \frac{1}{2}\sigma^2 \right) t$$

이 총 평균을 9.6절과 동일한 이항 표준화식에 대입하면 $p'$ 세계에서의 표준화 경계값 $Z_0'$이 도출됩니다.

$$Z_0' = \lim_{n \to \infty} \frac{\ln(K/S_0) - n \hat{\mu}_{p'}}{\sqrt{n} \hat{\sigma}_{p'}} = \frac{\ln(K/S_0) - \left( r + \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}}$$

$$\implies Z_0' = -\left[ \frac{\ln(S_0/K) + \left( r + \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}} \right] = -d_1$$

여기서 대괄호 안의 값이 바로 BSM 모형의 **$d_1$**입니다!

$$d_1 = \frac{\ln(S_0/K) + \left( r + \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}}$$

따라서 미행사 여확률 $1 - \Phi(a; n, p') \to N(-d_1)$이 되며, 대칭성($1 - N(-d_1) = N(d_1)$)에 의해 첫 번째 항의 확률 역시 완벽히 수렴합니다.

$$\therefore \lim_{n \to \infty} \Phi(a; n, p') = N(d_1)$$

---

### 4. $d_1$과 $d_2$의 대수적 관계 증명 ($d_1 = d_2 + \sigma \sqrt{t}$)

마지막으로 BSM 모형의 두 핵심 변수 $d_1$과 $d_2$ 사이의 유명한 관계식을 증명해 봅시다. $d_1$의 분자에 있는 드리프트 항 $r + \frac{1}{2}\sigma^2$를 $(r - \frac{1}{2}\sigma^2) + \sigma^2$로 분해합니다.

$$d_1 = \frac{\ln(S_0/K) + \left( r - \frac{1}{2}\sigma^2 + \sigma^2 \right) t}{\sigma \sqrt{t}}$$

$$= \frac{\ln(S_0/K) + \left( r - \frac{1}{2}\sigma^2 \right) t}{\sigma \sqrt{t}} + \frac{\sigma^2 t}{\sigma \sqrt{t}}$$

앞의 분수는 정확히 $d_2$이고, 뒤의 분수는 약분되어 $\sigma \sqrt{t}$가 됩니다!

$$\therefore d_1 = d_2 + \sigma \sqrt{t}$$

---

### 5. 최종 결론: CRR 이항 모형에서 BSM 연속 모형으로의 완벽한 완성

이로써 이산 CRR 모형의 콜옵션 가격식:

$$C_{\text{CRR}} = S_0 \Phi(a; n, p') - K (1+r)^{-n} \Phi(a; n, p)$$

에 $n \to \infty$ 극한을 취하면 각 구성 요소가:
- $S_0 \longrightarrow S_0$
- $\Phi(a; n, p') \longrightarrow N(d_1)$
- $K(1+r)^{-n} \longrightarrow K e^{-rt}$
- $\Phi(a; n, p) \longrightarrow N(d_2)$

로 각각 수렴하여, 최종적으로 블랙-숄즈-머튼(BSM) 연속 옵션 가격 결정 공식을 완벽하게 완성하게 됩니다!

$$C_{\text{BSM}} = S_0 N(d_1) - K e^{-rt} N(d_2)$$






