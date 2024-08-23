# 특공대 문제 풀이 및 설명

https://www.acmicpc.net/problem/4008

## 문제 이해

이 문제는 군인들의 전투력을 최적의 방식으로 구간으로 나누어, 각 구간의 조정된 전투력의 합을 최대화하는 것을 목표로 합니다. 군인들은 연속된 구간으로 나누어지며, 각 구간의 전투력 합에 대해 주어진 계수 `a`, `b`, `c`를 사용하여 조정된 전투력이 계산됩니다. 문제를 해결하기 위해서는 이러한 조정된 전투력의 합을 최대화할 수 있는 최적의 구간 나누기 방법을 찾아야 합니다.

문제를 해결하기 위해서는 군인들의 전투력을 합산하는 방법과, 그 합에 대해 최적의 조정 전투력을 계산하는 방법을 고려해야 합니다. 문제의 핵심은 각 구간을 어떻게 나누느냐에 따라 전체 전투력의 합이 달라지며, 이로 인해 최적의 조정 전투력을 계산하는 알고리즘이 필요하다는 것입니다.

## 입출력 조건

**입력 조건**:

- 첫 번째 줄에 군인의 수 `n`이 주어집니다. (1 ≤ n ≤ 1,000,000)
- 두 번째 줄에 계수 `a`, `b`, `c`가 주어집니다. (`a < 0`, `-10^7 ≤ b ≤ 10^7`, `-30,000,000 ≤ c ≤ 30,000,000`)
- 세 번째 줄에 각 군인의 전투력 `x1, x2, ..., xn`이 공백으로 구분되어 주어집니다. (1 ≤ xi ≤ 100)

**출력 조건**:

- 가능한 최대 조정 전투력의 합을 한 줄에 출력합니다.

## 접근 방법

이 문제를 해결하기 위해 Convex Hull Trick 알고리즘을 사용합니다. Convex Hull Trick은 주어진 선형 함수들의 최적화 문제를 해결하는 데 유용한 알고리즘입니다. 이 문제에서는 각 구간의 전투력 합에 대해 최적의 조정 전투력을 계산하기 위해 Convex Hull Trick을 활용할 수 있습니다.

구체적으로, 문제를 `dp`(동적 프로그래밍)로 접근하되, 각 `dp[i]`를 계산할 때 Convex Hull Trick을 사용하여 이전 단계에서 최적의 값을 효율적으로 계산합니다. 이를 통해 시간 복잡도를 `O(n)` 또는 `O(n log n)`으로 줄일 수 있습니다.

## 풀이 과정

1. **문제 분석 및 설계**:

   - 문제의 핵심은 주어진 군인들의 전투력을 연속된 구간으로 나누고, 각 구간의 조정된 전투력을 계산하여 그 합을 최대화하는 것입니다.
   - 조정된 전투력은 `a*S^2 + b*S + c`로 주어지며, 여기서 `S`는 특정 구간의 전투력 합입니다.
   - 각 구간의 전투력을 합산하고, 이를 통해 얻어진 조정된 전투력을 최대화할 수 있는 최적의 구간 나누기 방법을 찾아야 합니다.

2. **Convex Hull Trick 적용**:

   - Convex Hull Trick은 선형 함수의 집합에서 주어진 x 값에 대해 최대 또는 최소 값을 효율적으로 찾는 알고리즘입니다. 이 문제에서는 각 구간의 전투력 합에 대해 최대 조정 전투력을 찾는 데 사용됩니다.
   - 새로운 직선을 추가할 때, 기존의 직선 중 더 이상 최적의 값을 제공하지 않는 직선을 제거하여 `deque`에 최적의 직선만 유지합니다.
   - `deque`에 저장된 직선들 중 최적의 직선을 선택하여 주어진 `x` 값에서 최대 값을 계산합니다.

3. **동적 프로그래밍과 Convex Hull Trick 통합**:

   - 동적 프로그래밍을 사용하여 `dp[j]`를 계산합니다. `dp[j]`는 `1`번부터 `j`번까지의 군인을 구간으로 나누었을 때 가능한 최대 조정 전투력의 합을 의미합니다.
   - 각 위치 `j`에서 이전 위치 `i`에서 최적의 구간을 찾아 `dp[j]`를 계산하는데, 이 과정에서 Convex Hull Trick을 사용하여 효율적으로 최적의 값을 찾습니다.
   - 이를 통해 `O(n)` 또는 `O(n log n)`의 시간 복잡도로 문제를 해결할 수 있습니다.

4. **구현 및 최적화**:
   - 전체적인 구현은 Convex Hull Trick 클래스를 정의하고, 이를 사용하여 각 단계에서 최대 조정 전투력을 계산하는 방식으로 이루어집니다.
   - 메모리 사용을 최소화하기 위해 `dp` 배열을 사용하지 않고, 현재 단계에서 필요한 값만 저장하여 계산합니다.
   - `prefix_sum`을 사용하여 각 구간의 전투력 합을 계산하며, 이를 바탕으로 조정된 전투력을 계산합니다.
   - 최종적으로 계산된 최대 조정 전투력을 출력합니다.

## 구현 코드

```python
from collections import deque

class ConvexHullTrick:
    def __init__(self):  # 클래스 초기화
        self.hull = deque()  # 최적의 직선을 저장하기 위한 deque 초기화

    def add_line(self, m, c):  # 새로운 직선을 추가하는 함수
        while len(self.hull) >= 2:  # 현재 deque에 두 개 이상의 직선이 있을 때
            if self.is_redundant(m, c):  # 새로운 직선이 기존 직선을 대체할 수 있는지 확인
                self.hull.pop()  # 기존 직선 제거
            else:
                break  # 대체할 수 없으면 루프 종료
        self.hull.append((m, c))  # 새로운 직선을 deque에 추가

    def is_redundant(self, m, c):  # 새로운 직선이 불필요한지 확인하는 함수
        last1 = self.hull[-1]  # 마지막 직선
        last2 = self.hull[-2]  # 마지막에서 두 번째 직선
        # 직선 교차점 비교를 통해 새로운 직선이 최적의 영역에 있는지 확인
        return (c - last1[1]) * (last2[0] - last1[0]) <= (last1[1] - last2[1]) * (last1[0] - m)

    def get_max(self, x):  # 주어진 x 값에서 최적의 직선 값을 계산하는 함수
        while len(self.hull) >= 2 and self.evaluate(self.hull[0], x) <= self.evaluate(self.hull[1], x):  # deque의 첫 두 직선 중 더 나은 것을 찾음
            self.hull.popleft()  # 최적이 아닌 첫 번째 직선을 제거
        return self.evaluate(self.hull[0], x)  # 최적의 직선 값을 반환

    def evaluate(self, line, x):  # 직선의 y 값을 계산하는 함수
        return line[0] * x + line[1]

def max_adjusted_combat_power(n, a, b, c, x):  # 최대 조정 전투력을 계산하는 함수
    dp_prev = 0  # 이전 dp 값을 저장할 변수 초기화
    prefix_sum = 0  # 누적 합을 저장할 변수 초기화

    cht = ConvexHullTrick()  # Convex Hull Trick 객체 생성
    cht.add_line(0, 0)  # 첫 번째 직선 추가 (m=0, c=0)

    for j in range(1, n + 1):  # 1번 군인부터 n번 군인까지 반복
        prefix_sum += x[j - 1]  # 현재 군인의 전투력을 누적 합에 더함
        S = prefix_sum  # 현재 구간의 합 S
        dp_curr = a * S * S + b * S + c + cht.get_max(S)  # 현재 구간에서의 최대 조정 전투력 계산
        cht.add_line(-2 * a * S, dp_curr + a * S * S - b * S)  # 새로운 직선을 Convex Hull Trick에 추가
        dp_prev = dp_curr  # 현재 dp 값을 이전 dp 값으로 업데이트

    return dp_prev  # 마지막 dp 값을 반환 (최대 조정 전투력)

import sys
input = sys.stdin.read  # 입력을 받기 위한 함수
data = input().split()  # 입력 데이터를 공백 기준으로 분리

n = int(data[0])  # 군인의 수 n
a = int(data[1])  # 계수 a
b = int(data[2])  # 계수 b
c = int(data[3])  # 계수 c
x = list(map(int, data[4:]))  # 각 군인의 전투력을 리스트로 변환

print(max_adjusted_combat_power(n, a, b, c, x))  # 최대 조정 전투력을 계산하고 출력
```
