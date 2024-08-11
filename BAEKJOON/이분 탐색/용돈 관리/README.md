# 용돈 관리 문제 풀이 및 설명

https://www.acmicpc.net/problem/6236

## 문제 이해

이 문제는 N일 동안의 일일 지출을 커버할 수 있도록 M번 이하로 인출할 때 필요한 최소 초기 인출 금액 K를 찾는 것입니다. 목표는 첫 번째 인출 금액을 최소화하면서 인출 횟수가 M을 넘지 않도록 하고, 모든 일일 지출을 커버하는 것입니다.

## 입출력 조건

- **입력 조건:**
  - 첫 번째 줄에는 두 개의 정수 N과 M이 주어집니다.
    - \( 1 ≤ N ≤ 100,000 \)
    - \( 1 ≤ M ≤ N \)
  - 다음 N개의 줄에는 매일 사용할 금액이 하나씩 주어집니다.
    - \( 1 ≤ \text{금액} ≤ 10,000 \)

- **출력 조건:**
  - 출력은 한 줄로, 모든 지출을 커버할 수 있는 최소 초기 인출 금액 K를 나타내는 하나의 정수입니다.

## 접근 방식

이 문제는 이분 탐색을 사용하여 K의 최적 값을 찾을 수 있습니다. 이는 다음 단계를 포함합니다:
1. 하한값(`low`)을 일일 지출 중 최대값으로 설정합니다 (K는 최소한 가장 큰 일일 지출을 커버해야 합니다).
2. 상한값(`high`)을 모든 일일 지출의 합으로 설정합니다 (K는 모든 일일 지출을 커버해야 합니다).
3. 이 범위 내에서 이분 탐색을 사용하여 M번 이하의 인출로 모든 지출을 커버할 수 있는 최소 K를 찾습니다.

## 풀이 과정

1. **도우미 함수 정의: `can_withdraw_with_k(k, daily_usage, N, M)`**
   - 인출 횟수를 나타내는 `count`를 1로 초기화합니다.
   - 현재 인출한 금액의 합을 나타내는 `current_sum`을 0으로 초기화합니다.
   - `daily_usage`의 각 일일 지출을 순회하면서:
     - `current_sum + usage`가 `k`를 초과하면, `count`를 증가시키고 `current_sum`을 현재 일일 지출로 재설정합니다.
     - `count`가 `M`을 초과하면, 주어진 `k`가 너무 작음을 나타내는 `False`를 반환합니다.
     - 그렇지 않으면 현재 일일 지출을 `current_sum`에 더합니다.
   - 루프가 완료되고 `count`가 `M`을 초과하지 않으면, 주어진 `k`가 충분함을 나타내는 `True`를 반환합니다.

2. **이분 탐색 함수: `find_minimum_k(N, M, daily_usage)`**
   - `low`를 `daily_usage`의 최대값으로 초기화합니다.
   - `high`를 `daily_usage`의 합으로 초기화합니다.
   - `low`가 `high`보다 작을 동안:
     - `low`와 `high`의 평균값으로 `mid`를 계산합니다.
     - `can_withdraw_with_k(mid, daily_usage, N, M)`을 사용하여 `mid`가 가능한 해인지 확인합니다.
     - 가능하면 `high`를 `mid`로 설정합니다.
     - 불가능하면 `low`를 `mid + 1`로 설정합니다.
   - 최소한의 가능한 `k`인 `low`를 반환합니다.

3. **입력 처리**
   - `sys.stdin.read`를 사용하여 입력값을 읽고 정수 리스트로 나눕니다.
   - 첫 번째와 두 번째 값을 `N`과 `M`으로 설정합니다.
   - 나머지 값을 `daily_usage` 리스트에 저장합니다.

4. **메인 실행**
   - `find_minimum_k`를 `N`, `M`, `daily_usage`로 호출합니다.
   - 모든 지출을 커버할 수 있는 최소 초기 인출 금액 K를 출력합니다.

## 코드 구현

```python
def can_withdraw_with_k(k, daily_usage, N, M):
    count = 1  # 인출 횟수 초기값은 1로 설정
    current_sum = 0  # 현재 인출 금액의 합 초기값은 0으로 설정
    
    for usage in daily_usage:  # 매일 사용할 금액을 순회하며
        if current_sum + usage > k:  # 현재 인출 금액에 오늘 사용할 금액을 더했을 때 k를 초과하면
            count += 1  # 인출 횟수를 증가시킨다
            current_sum = usage  # 현재 인출 금액을 오늘 사용할 금액으로 초기화
            if count > M:  # 인출 횟수가 M을 초과하면
                return False  # False를 반환하여 주어진 k로 인출이 불가능함을 알린다
        else:
            current_sum += usage  # k를 초과하지 않으면 현재 인출 금액에 오늘 사용할 금액을 더한다
            
    return True  # 모든 사용 금액을 k 이내에서 M번 이하로 인출할 수 있으면 True를 반환

def find_minimum_k(N, M, daily_usage):
    low = max(daily_usage)  # 최소 금액 K의 초기값은 매일 사용하는 금액 중 최대값으로 설정
    high = sum(daily_usage)  # 최대 금액 K의 초기값은 모든 날의 사용 금액의 합으로 설정
    
    while low < high:  # 이분 탐색을 통해 적절한 K를 찾는다
        mid = (low + high) // 2  # 중간값을 계산
        if can_withdraw_with_k(mid, daily_usage, N, M):  # 중간값으로 인출이 가능한지 확인
            high = mid  # 가능하면 상한값을 중간값으로 설정
        else:
            low = mid + 1  # 불가능하면 하한값을 중간값+1로 설정
            
    return low  # 최소 금액 K를 반환

# 입력
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])  # 첫 번째 줄의 첫 번째 숫자는 N
M = int(data[1])  # 첫 번째 줄의 두 번째 숫자는 M
daily_usage = list(map(int, data[2:]))  # 나머지 숫자들은 매일 사용할 금액

# 최소 금액 K 계산
minimum_k = find_minimum_k(N, M, daily_usage)

# 출력
print(minimum_k)  # 최소 금액 K를 출력
