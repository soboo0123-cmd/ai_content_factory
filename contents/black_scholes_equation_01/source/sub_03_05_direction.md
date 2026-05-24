# 3.5 최소 상승 횟수(a) 판별을 통한 내가격(ITM) 조건 정의 - 집필 방향 및 수식 가이드

## 1. 핵심 개념 및 원본 데이터
- **실습 목표**: 옵션 공식 내의 $\max(S_T - K, 0)$ 연산자에서 가치가 $0$이 되는 무의미한 외가격(OTM) 구간을 털어내고, 실제 수익이 발생하는 최소 주가 상승 횟수 $a$의 수학적 하한을 도출합니다.
- **수식 유도**:
  - 만기 주가가 행사가격을 초과할 조건: $u^j d^{n-j} S \ge K$
  - 양변에 자연로그를 취해 $j$에 대해 정리:
    $$j \ln u + (n-j) \ln d \ge \ln(K/S)$$
    $$j(\ln u - \ln d) \ge \ln(K/S) - n \ln d$$
    $$j \ge \frac{\ln\left(\frac{K}{S \cdot d^n}\right)}{\ln\left(\frac{u}{d}\right)}$$
  - 만족하는 최소 정수 $a$ 정의:
    $$a = \left\lceil \frac{\ln\left(\frac{K}{S \cdot d^n}\right)}{\ln\left(\frac{u}{d}\right)} \right\rceil$$

## 2. 독자 대상 가이드 및 집필 지침
- 올림 기호(Ceiling, $\lceil \cdot \rceil$)의 수학적 정의와 금융공학적 의미를 독자 수준에 맞춰 친절히 풀어쓰세요.