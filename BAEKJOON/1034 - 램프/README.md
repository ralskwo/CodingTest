# 램프 문제 풀이 및 설명

https://www.acmicpc.net/problem/1034

## 문제 이해

이 문제에서는 각 1x1 램프가 있는 직사각형 테이블에서 모든 램프를 켜거나 끄는 방법을 찾는 것입니다. 각 행에는 스위치가 있으며, 이 스위치를 누를 때마다 해당 행의 모든 램프의 상태가 반전됩니다. 문제의 목표는 스위치를 \( K \)번 눌러 최대한 많은 행이 완전히 켜지도록 하는 것입니다. 각 행은 켜진 상태('1')와 꺼진 상태('0')로 이루어져 있으며, 행이 전부 '1'로 이루어져 있으면 "켜진 행"으로 간주됩니다.

이 문제는 주어진 스위치 누름 횟수 \( K \) 내에서 최대한 많은 행을 켜기 위해 최적의 스위치 조합을 찾는 문제입니다. 따라서 각 행의 상태와 \( K \)의 관계를 잘 분석하고 최적의 전략을 찾아야 합니다.

## 입출력 조건

### 입력 조건:

- 첫 번째 줄에는 \( N \)과 \( M \)이 주어집니다. 여기서 \( N \)은 행의 수, \( M \)은 열의 수를 의미합니다.
- 그 다음 \( N \)개의 줄에는 각 행의 램프 상태가 '0'과 '1'로 이루어진 문자열로 주어집니다.
- 마지막 줄에는 스위치 누름 횟수 \( K \)가 주어집니다.

### 출력 조건:

- 스위치를 \( K \)번 눌러서 켤 수 있는 최대한 많은 "켜진 행"의 수를 출력합니다.

## 접근 방법

이 문제를 해결하기 위해서는 다음과 같은 전략을 사용할 수 있습니다:

1. **행 상태 분석**: 모든 행의 상태를 분석하고, 동일한 상태를 가진 행들이 몇 번 등장하는지 확인합니다. 이를 통해 동일한 행 상태가 반복되는 패턴을 찾습니다.
2. **스위치 누름 횟수 \( K \)와 행 상태의 관계 분석**: 각 행의 상태에서 '0'의 개수를 세고, 해당 행을 모두 '1'로 바꾸기 위해 몇 번의 스위치 누름이 필요한지 계산합니다. \( K \)와 0의 개수의 관계를 통해 해당 행을 모두 켜는 것이 가능한지 판단합니다.
3. **최대 켜진 행의 수 계산**: 조건에 맞게 모든 램프를 켤 수 있는 행의 수를 최대화하는 방법을 찾습니다.

## 풀이 과정

1. **행 상태 카운팅**:
   - 입력받은 각 행의 상태를 문자열로 처리하고, 이 상태가 얼마나 자주 등장하는지를 세기 위해 Python의 `Counter` 클래스를 사용합니다. 이를 통해 동일한 상태를 가진 행의 개수를 파악할 수 있습니다.
2. **0의 개수 계산 및 조건 확인**:

   - 각 행에서 '0'의 개수를 세어 해당 행을 모두 '1'로 바꾸는 것이 가능한지 확인합니다.
   - 이때 조건은 두 가지입니다:
     1. 행의 0의 개수가 \( K \)보다 작거나 같아야 합니다. \( K \)번의 스위치 누름으로 모든 '0'을 '1'로 바꿀 수 있어야 하기 때문입니다.
     2. \( K \)에서 0의 개수를 뺀 값이 짝수여야 합니다. 스위치를 한 번 누를 때마다 행 전체가 반전되기 때문에, 최종 상태에서 모든 램프가 켜지려면 짝수 번의 반전이 필요합니다.

3. **최대 켜진 행의 수 계산**:

   - 조건을 만족하는 경우, 해당 행 상태가 몇 번 등장했는지 확인하고, 이를 통해 현재까지의 최대 켜진 행의 수를 갱신합니다.
   - 반복문을 통해 모든 행 상태를 검토하여 최종적으로 최대 켜진 행의 수를 계산합니다.

4. **결과 출력**:
   - 계산된 최대 켜진 행의 수를 출력합니다. 이 값이 주어진 조건에서 최적의 답이 됩니다.

## 코드 구현

```python
def max_on_rows(N, M, lamp_states, K):  # N, M, 램프 상태와 K를 입력으로 받는 함수 정의
    from collections import Counter  # collections 모듈에서 Counter 클래스를 가져옴

    row_count = Counter(lamp_states)  # 각 행의 상태가 몇 번 나타나는지 세어서 row_count에 저장
    max_on = 0  # 최대 켜진 행의 수를 저장할 변수 초기화

    for row, count in row_count.items():  # 각 행과 그 행의 개수에 대해 반복
        zero_count = row.count('0')  # 해당 행에서 0의 개수를 셈
        if zero_count <= K and (K - zero_count) % 2 == 0:  # 조건을 만족하는지 확인
            max_on = max(max_on, count)  # 조건을 만족하면 max_on을 갱신

    return max_on  # 최대 켜진 행의 수 반환

N, M = map(int, input().split())  # 첫 줄에서 N(행의 수)과 M(열의 수)을 입력받음
lamp_states = [input().strip() for _ in range(N)]  # 다음 N줄에서 램프 상태를 입력받아 리스트로 저장
K = int(input().strip())  # 마지막 줄에서 K를 입력받음

result = max_on_rows(N, M, lamp_states, K)  # 함수 호출하여 결과 계산
print(result)  # 결과 출력
```
