# 떡 먹는 호랑이 문제 풀이 및 설명

<https://www.acmicpc.net/problem/2502>

<https://mayquartet.com/python-백준-2502-떡-먹는-호랑이/>

## 문제 이해

이 문제는 피보나치 수열과 유사한 규칙을 가진 문제입니다. 할머니가 매일 호랑이에게 떡을 주는 규칙은 특정 점화식으로 정의됩니다. 즉, 하루에 주는 떡의 개수는 전날과 그 전날에 준 떡의 개수의 합으로 결정됩니다. 우리는 특정 날짜 `D`에 할머니가 호랑이에게 준 떡의 개수 `K`가 주어졌을 때, 첫째 날과 둘째 날에 각각 몇 개의 떡을 주었는지 `A`와 `B`를 찾아야 합니다.

문제를 해결하기 위해서는 다음을 이해해야 합니다:

- 첫째 날에 주는 떡의 개수를 `A`, 둘째 날에 주는 떡의 개수를 `B`로 정의합니다.
- 점화식 `T[n] = T[n-2] + T[n-1]`를 이용하여 `D`째 날의 떡 개수 `T[D]`를 계산합니다.
- 주어진 조건을 만족하는 `A`와 `B`를 찾는 것이 목표입니다.

## 입출력 조건

- 입력으로는 두 개의 정수 `D`와 `K`가 주어집니다.
  - `D`는 호랑이를 만난 날짜이며, `3 ≤ D ≤ 30`의 범위를 가집니다.
  - `K`는 `D`째 날 호랑이에게 준 떡의 개수이며, `10 ≤ K ≤ 100,000`의 범위를 가집니다.
- 출력으로는 두 줄에 걸쳐 `A`와 `B`를 출력합니다.
  - 첫째 줄에는 첫째 날에 준 떡의 개수 `A`를 출력하고, 둘째 줄에는 둘째 날에 준 떡의 개수 `B`를 출력합니다.
  - `A`와 `B`는 항상 정수이며, `1 ≤ A ≤ B`를 만족합니다.

## 접근 방식

이 문제를 해결하기 위해 다이나믹 프로그래밍과 수학적 분석을 결합해야 합니다. 구체적인 접근 방식은 다음과 같습니다:

1. 점화식 계산:

   - 주어진 문제는 피보나치 수열과 유사한 점화식을 사용합니다. 따라서, 점화식을 이용하여 각 날짜에 해당하는 계수를 계산합니다.
   - 계수란 `T[D] = coeff[D][1] * A + coeff[D][2] * B`에서 `A`와 `B`에 곱해지는 값으로, 이를 반복적으로 계산합니다.

2. 브루트포스 탐색:

   - `A`와 `B`를 구하기 위해 `A`의 가능한 값(1부터 시작)을 대입하여 `K`를 만족하는 `B`를 계산합니다.
   - `B`가 정수이고 `1 ≤ A ≤ B` 조건을 만족하는 경우 답을 찾습니다.

3. 효율성 고려:
   - `A`의 가능한 값은 `K`를 `a_coeff`로 나눈 몫까지만 탐색하면 됩니다. 따라서 계산량을 줄일 수 있습니다.

## 풀이 과정

1. `D`일까지의 계수를 계산합니다:

   - 첫째 날과 둘째 날의 초기 계수는 각각 `[1, 0]`과 `[0, 1]`로 설정합니다.
   - 셋째 날부터는 이전 두 날의 계수를 더하여 각 날의 계수를 계산합니다.

2. `A`와 `B`를 구하기 위한 브루트포스 탐색을 수행합니다:

   - `A`의 가능한 값을 1부터 `K`를 `a_coeff`로 나눈 몫까지만 반복합니다.
   - `K - A * a_coeff`가 `b_coeff`로 나누어떨어질 경우, `B`를 계산합니다.
   - `B`가 정수이고 `1 ≤ A ≤ B` 조건을 만족하면 결과를 반환합니다.

3. 사용자 입력을 받아 계산한 `A`와 `B`를 출력합니다:
   - 입력값을 읽어와 함수로 전달하여 계산 결과를 받습니다.
   - 계산된 `A`와 `B`를 각각 출력합니다.

## 코드 구현

```python
def find_a_and_b(D, K):
    # D일째까지의 계수를 저장할 리스트 초기화
    coeff = [[0, 0] for _ in range(D+1)]

    # 첫째 날 떡 개수는 A, 둘째 날 떡 개수는 B로 표현
    coeff[1] = [1, 0]
    coeff[2] = [0, 1]

    # 셋째 날부터 D일까지의 계수를 계산
    for i in range(3, D+1):
        # i번째 날 A와 B의 계수는 이전 두 날의 계수의 합
        coeff[i][0] = coeff[i-2][0] + coeff[i-1][0]
        coeff[i][1] = coeff[i-2][1] + coeff[i-1][1]

    # D일째 떡 개수 K를 만족하기 위해 필요한 계수
    a_coeff = coeff[D][0]
    b_coeff = coeff[D][1]

    # 가능한 A 값을 1부터 탐색하여 K를 만족하는 A와 B를 찾음
    for A in range(1, K // a_coeff + 1):
        # K에서 A에 대한 값을 뺀 나머지가 B에 의해 나눠떨어지면 유효한 B를 찾음
        if (K - A * a_coeff) % b_coeff == 0:
            B = (K - A * a_coeff) // b_coeff
            return A, B

# 입력값을 읽어와 D와 K에 저장
D, K = map(int, input().split())

# 주어진 D와 K에 대해 A와 B를 계산
A, B = find_a_and_b(D, K)

# 계산된 A와 B를 출력
print(A)
print(B)
```
