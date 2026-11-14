# CRR 이항모형에서 블랙-숄즈-머튼(BSM) 모형으로: 핵심 요약

> **핵심 질문:** 권리만 있고 의무는 없는 옵션을 과연 얼마에 사고팔아야 할까?

---

## 1. 복제 포트폴리오와 무차익거래 원칙

옵션 가격은 투자자의 기대나 위험 선호도가 아니라, **주식과 채권(현금 대출)으로 옵션의 만기 보상(pay-off)을 복제하는 비용**으로 결정된다.

### 1) 왜 주식과 채권으로 복제가 가능할까? (직선의 방정식 직관)
1기간 동안 주가가 상승($uS_0$)하거나 하락($dS_0$)하는 두 가지 경우만 존재한다고 하자. 이때 만기 옵션 가치 $(uS_0, C_u)$와 $(dS_0, C_d)$는 평면 위의 **서로 다른 두 점**이다. 두 점을 지나는 직선의 방정식($y = \Delta x + b$)은 유일하게 결정되므로, 옵션의 만기 가치는 주가($x$)에 비례하는 부분과 고정 상수항의 합으로 완벽히 표현된다.

- **기울기(주식 $\Delta$주 보유):** 주가 변화량 대비 옵션 가치 변화량인 민감도($\Delta$)만큼 주식을 보유해 기울기를 맞춘다.
  $$\Delta = \frac{C_u - C_d}{uS_0 - dS_0}$$
- **$y$절편(채권 $B$원 차입/투자):** 주식만 보유했을 때 남거나 모자라는 고정 바닥 금액(베이스라인)은 무위험 채권을 통해 현재가치($B$)로 보정한다.
  $$B = \frac{uC_d - dC_u}{(u - d)(1+r)}$$

### 2) 무차익거래 원칙
만기 시점의 현금흐름이 100% 일치한다면, 현재 시점의 옵션 가격($C_0$) 역시 복제 포트폴리오를 구축하는 데 드는 초기 비용과 같아야 한다. 그렇지 않으면 무위험 차익거래 기회가 발생하기 때문이다.

$$C_0 = \Delta S_0 + B$$

---

## 2. 위험중립확률($p$)과 이항정리를 이용한 일반화

### 1) 기댓값과 할인항의 등장
앞에서 구한 $\Delta$와 $B$를 $C_0 = \Delta S_0 + B$에 대입해 만기 옵션 가치($C_u, C_d$) 기준으로 식을 정리하면, 분자가 **가중평균(기댓값) 꼴**로 묶이고 전체를 무위험 이자율로 **할인**하는 형태가 나타난다.

$$C_0 = \frac{1}{1+r} \left[ p \cdot C_u + (1-p) \cdot C_d \right], \quad \text{단 } p = \frac{(1+r)-d}{u-d}$$

여기서 $p$는 모든 자산의 기대수익률을 무위험 이자율과 같게 만들어 주는 **위험중립확률**($0 \le p \le 1$)이다.

### 2) $n$단계 이항 모형 일반화
1기간 가격식이 확률에 따른 기댓값 꼴이므로, 전체 기간을 $n$단계로 확장하면 독립 시행과 **이항정리**를 적용해 일반화할 수 있다. $n$번 중 상승 횟수를 $j$번($j=0, 1, \dots, n$)이라 할 때 콜옵션 가격은 다음과 같다.

$$C_0 = \frac{1}{(1+r)^n} \sum_{j=0}^{n} \binom{n}{j} p^j (1-p)^{n-j} \max\left(S_0 u^j d^{n-j} - K, \, 0\right)$$

---

## 3. `max` 제거와 복제 구조의 재발견

극한 계산을 방해하는 비선형 $\max$ 기호를 없애기 위해, 옵션이 행사되는 조건($S_0 u^j d^{n-j} \ge K$)을 만족하는 **최소 상승 횟수 $a$**를 도입한다. $j < a$ 구간에서는 어차피 pay-off가 $0$이므로, 시그마 범위를 $j=a$부터 $n$까지로 좁히면 `max` 없이 괄호 안으로 깔끔히 정리할 수 있다.

$$C_0 = \frac{1}{(1+r)^n} \sum_{j=a}^{n} \binom{n}{j} p^j (1-p)^{n-j} \left( S_0 u^j d^{n-j} - K \right)$$

이를 주식 항과 행사가격(현금) 항으로 전개한 뒤, 주식을 기준 자산(Numeraire)으로 삼는 새로운 확률 $p' \equiv p \frac{u}{1+r}$를 정의하고 이항 누적확률 $\Phi(a; n, p) \equiv \sum_{j=a}^n \binom{n}{j} p^j (1-p)^{n-j}$를 쓰면 식이 하나로 묶인다.

$$C_0 = \underbrace{S_0 \cdot \Phi(a; n, p')}_{\text{변동하는 주식 항 }(\Delta S_0)} - \underbrace{K(1+r)^{-n} \cdot \Phi(a; n, p)}_{\text{고정 행사가격/채권 항 }(-B)}$$

놀랍게도 $n$단계 일반화 공식 역시 최초의 복제 포트폴리오($\Delta S_0 + B$)에서 보았던 **‘변동하는 주식 보유분 - 고정된 행사가격(채권 상환분)’** 구조를 그대로 유지하고 있다.

---

## 4. 이산에서 연속으로: 시간 분할과 스케일링

현실의 주가는 실수($\mathbb{R}^+$) 위에서 움직이고 거래는 끊임없이 일어난다. 따라서 만기 $t$를 $n$개의 미세 구간 $\Delta t = t/n$으로 쪼개고 극한($n \to \infty$)을 취해 연속 모형으로 확장한다.

### 1) 무위험 이자율의 단위 기간 확장
만기 $t$기간의 총 증식인자 $R = e^{rt}$에 대해 단위 기간 증식인자 $\hat{r}$을 $\hat{r} = R^{1/n} = e^{r\frac{t}{n}}$으로 정의하면, $n$번 증식했을 때 정확히 원래의 만기 증식인자 $e^{rt}$로 복원된다. (이산 복리 $\hat{r} = 1 + r\frac{t}{n}$ 역시 $n \to \infty$ 극한에서 $e^{rt}$로 수렴한다.)

### 2) 주가 로그수익률과 단위 평균·단위 분산
만기 주가 $S_t = S_0 u^j d^{n-j}$에 자연로그를 취해 로그수익률을 구하면 다음과 같다.

$$\ln\left(\frac{S_t}{S_0}\right) = j (\ln u - \ln d) + n \ln d$$

이 식에서 확률변수는 상승 횟수 $j \sim \text{Binomial}(n, q)$뿐이므로, 평균과 분산은 오직 $j$에만 걸린다($\mathbb{E}[j]=nq$, $\text{Var}(j)=nq(1-q)$). 이를 $n$으로 묶어내면 한 스텝당 **단위 평균($\hat{\mu}$)**과 **단위 분산($\hat{\sigma}^2$)**을 정의할 수 있다.

$$\mathbb{E}\left[\ln\frac{S_t}{S_0}\right] = n\underbrace{\left[ q\ln u + (1-q)\ln d \right]}_{\text{단위 평균 } \hat{\mu}}, \qquad \text{Var}\left[\ln\frac{S_t}{S_0}\right] = n\underbrace{\left[ q(1-q)(\ln u - \ln d)^2 \right]}_{\text{단위 분산 } \hat{\sigma}^2}$$

### 3) 발산 방지를 위한 $u, d, q$의 스케일링
만약 $\hat{\mu}, \hat{\sigma}^2$가 고정된 상수인 채로 $n \to \infty$로 보내면 총 평균과 총 분산이 무한대로 발산한다. 발산을 막으려면 단위 평균과 단위 분산이 $\Delta t = t/n$ 꼴로 작아져야 하며, 그래야 $n$을 곱했을 때 $n \cdot \frac{t}{n} = t$로 약분되어 유한한 만기 값($\mu t, \sigma^2 t$)으로 수렴한다.

이에 따라 대칭 트리($d = 1/u$) 하에서 총 분산이 $\sigma^2 t$, 총 평균이 $\mu t$와 일치하도록 주가 변동 폭 $u, d$와 실제 상승 확률 $q$를 스케일링한다.

- **총 분산 일치 ($n(\ln u)^2 = \sigma^2 t \implies (\ln u)^2 = \sigma^2 \Delta t$):**
  $$u = e^{\sigma \sqrt{\Delta t}}, \qquad d = e^{-\sigma \sqrt{\Delta t}} = \frac{1}{u}$$
- **총 평균 일치 ($n(2q-1)\ln u = \mu t$):**
  $$q = \frac{1}{2} + \frac{1}{2}\left(\frac{\mu}{\sigma}\right)\sqrt{\Delta t}$$

---

## 5. 연속 수렴과 표준화: $N(d_2)$ 도출

갈톤보드(Galton Board) 원리처럼 독립적인 단위 로그수익률이 무수히 더해지면($n \to \infty$), 중심극한정리에 의해 만기 로그수익률은 정규분포로 수렴하며 평균과 분산으로 **표준화**가 가능해진다.

### 1) $q$에서 $p$로의 전환과 표준화 요소 정리
옵션 평가에는 실제 확률 $q$ 대신 위험중립확률 $p$를 사용하지만, 이항나무의 확률 구조는 변하지 않으므로 이항분포의 평균($np$)과 분산($np(1-p)$), 정규 수렴 성질이 $p$에서도 그대로 성립한다.

행사되지 않을 여확률 $1 - \Phi(a; n, p) = P(j \le a - 1)$을 표준화하기 위해, 필요한 요소들을 $p$ 측정치의 단위 평균 $\hat{\mu}_p = p\ln u + (1-p)\ln d$와 단위 분산 $\hat{\sigma}_p^2 = p(1-p)[\ln(u/d)]^2$을 써서 $\ln(u/d)$ 형태로 표현한다.

- **기댓값:** $np = \dfrac{n\hat{\mu}_p - n\ln d}{\ln(u/d)}$
- **표준편차:** $\sqrt{np(1-p)} = \dfrac{\sqrt{n}\hat{\sigma}_p}{\ln(u/d)}$
- **미행사 경계값:** $a - 1 = \dfrac{\ln(K/S_0) - n\ln d - \epsilon\ln(u/d)}{\ln(u/d)}$ *(단, $0 \le \epsilon < 1$은 정수 보정항)*

이를 표준화 경계식 $\dfrac{(a-1)-np}{\sqrt{np(1-p)}}$에 대입하면 분자의 $n\ln d$와 공통 분모 $\ln(u/d)$가 모두 깔끔하게 약분·소거된다.

$$1 - \Phi(a; n, p) = P\left( Z \le \frac{\ln(K/S_0) - n\hat{\mu}_p - \epsilon\ln(u/d)}{\sqrt{n}\hat{\sigma}_p} \right)$$

### 2) 테일러 전개를 통한 $p$ 근사와 $d_2$ 도출
이제 미소 변수 $x = \sqrt{\Delta t}$($x^2 = \Delta t$)에 대해 $u, d, \hat{r}$을 $x^2$ 항(즉, $n$을 곱했을 때 살아남는 $\Delta t$ 차수)까지 테일러 전개한다.

$$u \approx 1 + \sigma x + \frac{1}{2}\sigma^2 x^2, \qquad d \approx 1 - \sigma x + \frac{1}{2}\sigma^2 x^2, \qquad \hat{r} \approx 1 + r x^2$$

이를 위험중립확률 $p = \frac{\hat{r} - d}{u - d}$에 대입해 정리하면 다음과 같다.

$$p = \frac{1}{2} + \frac{1}{2}\left(\frac{r - \frac{1}{2}\sigma^2}{\sigma}\right)\sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

실제 확률 $q$의 드리프트 $\mu$ 자리가 위험중립 연속 로그 드리프트인 **$r - \frac{1}{2}\sigma^2$**로 바뀐 것이다. 따라서 $n \to \infty$ 극한에서 다음이 성립한다.
- 만기 총 평균: $n\hat{\mu}_p \longrightarrow \left(r - \frac{1}{2}\sigma^2\right)t$
- 만기 총 표준편차: $\sqrt{n}\hat{\sigma}_p \longrightarrow \sigma\sqrt{t}$
- 정수 보정항: $\epsilon\ln(u/d) \longrightarrow 0$

표준화 경계값에 극한을 취하면 BSM 모형의 $-d_2$가 정확히 도출된다.

$$Z_0 = \frac{\ln(K/S_0) - \left(r - \frac{1}{2}\sigma^2\right)t}{\sigma\sqrt{t}} = -\left[\frac{\ln(S_0/K) + \left(r - \frac{1}{2}\sigma^2\right)t}{\sigma\sqrt{t}}\right] = -d_2$$

정규분포의 대칭성($1 - N(-d_2) = N(d_2)$)에 의해 두 번째 항의 이항 행사확률은 **$N(d_2)$**로 수렴한다.

$$\lim_{n \to \infty} \Phi(a; n, p) = N(d_2)$$

---

## 6. 마무리: $p'$을 통한 $N(d_1)$ 도출과 BSM 공식의 완성

첫 번째 항의 확률 $p' = \frac{u}{\hat{r}}p$ 역시 같은 방식으로 테일러 전개($\frac{u}{\hat{r}} \approx 1 + \sigma\sqrt{\Delta t}$)를 적용하면 드리프트의 2차항 부호만 바뀐 형태가 된다.

$$p' = \frac{1}{2} + \frac{1}{2}\left(\frac{r + \frac{1}{2}\sigma^2}{\sigma}\right)\sqrt{\Delta t} + \mathcal{O}(\Delta t)$$

따라서 $p'$ 세계의 총 평균은 $n\hat{\mu}_{p'} \to \left(r + \frac{1}{2}\sigma^2\right)t$로 수렴하고, 동일한 표준화 과정을 거치면 경계값이 $-d_1$으로 도출되어 첫 번째 항의 확률은 **$N(d_1)$**으로 수렴한다(이때 $d_1 = d_2 + \sigma\sqrt{t}$).

결국 $n \to \infty$ 연속 극한을 취하면, 이산 CRR 모형은 블랙-숄즈-머튼(BSM) 연속 모형으로 완벽하게 수렴한다.

$$C_{\text{CRR}} = S_0 \Phi(a; n, p') - K(1+r)^{-n}\Phi(a; n, p) \quad \xrightarrow{n \to \infty} \quad C_{\text{BSM}} = S_0 N(d_1) - K e^{-rt} N(d_2)$$