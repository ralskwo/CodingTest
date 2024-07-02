# 문제 풀이: 두 경찰차의 최소 이동 거리 계산

https://www.acmicpc.net/problem/2618

## 문제 이해

이 문제는 두 개의 경찰차가 여러 사건을 처리하기 위해 이동해야 하는 최소 거리를 계산하는 문제입니다. 경찰차는 각각 다른 위치에서 시작하여 주어진 순서대로 사건을 처리해야 하며, 각 사건은 도시의 특정 지점에서 발생합니다. 경찰차가 이동하는 총 거리를 최소화하는 것이 목표입니다.

## 입력 형식

1. 첫 번째 줄에는 도시의 크기 \( N \)과 사건의 수 \( W \)가 주어집니다.
2. 다음 \( W \)개의 줄에는 각 사건의 위치가 주어집니다.

## 출력 형식

- 경찰차가 이동해야 하는 최소 거리를 출력합니다.
- 각 사건을 처리하는 경찰차의 순서를 출력합니다.

## 접근 방식

이 문제를 해결하기 위해 동적 계획법(DP)을 사용합니다. 동적 계획법을 사용하면 각 상태에서 최적의 결정을 내릴 수 있으며, 이를 통해 전체 문제를 효율적으로 해결할 수 있습니다. 

DP 배열을 이용하여 두 경찰차의 위치를 상태로 가지는 배열을 정의하고, 각 사건을 처리하면서 최소 거리를 계산합니다.

## 풀이 과정

1. **거리 계산 함수**:
    - 두 지점 사이의 맨해튼 거리를 계산하는 함수를 정의합니다.

2. **DP 배열 초기화**:
    - `dp` 배열을 초기화합니다. `dp[i][j]`는 경찰차 1이 i 번째 사건을 처리하고, 경찰차 2가 j 번째 사건을 처리한 후의 최소 거리를 저장합니다.
    - `trace` 배열을 초기화합니다. `trace[i][j]`는 `dp[i][j]` 값을 갱신할 때의 이전 상태를 저장하여 경로를 추적할 수 있도록 합니다.

3. **반복문을 사용한 동적 계획법**:
    - 각 사건에 대해 두 경찰차의 위치를 갱신하면서 최소 거리를 계산합니다.
    - 경찰차 1과 경찰차 2가 각각 다음 사건을 처리하는 경우를 고려하여 `dp` 배열을 업데이트합니다.

4. **결과 출력 및 경로 추적**:
    - 모든 사건을 처리한 후, `dp` 배열에서 최소 거리를 찾습니다.
    - `trace` 배열을 사용하여 각 사건을 처리한 경찰차의 경로를 추적합니다.
    - 최소 거리와 경로를 출력합니다.

## 코드

```python
def distance(x1, y1, x2, y2):
    # 두 지점 사이의 맨해튼 거리를 계산하는 함수
    return abs(x1 - x2) + abs(y1 - y2)

def solve(n, w, events):
    # DP 테이블 초기화: 경찰차 1과 2가 각각 i, j 번째 사건을 처리한 후의 최소 거리를 저장
    dp = [[float('inf')] * (w + 1) for _ in range(w + 1)]
    dp[0][0] = 0
    # 경로 추적을 위한 테이블 초기화
    trace = [[(-1, -1)] * (w + 1) for _ in range(w + 1)]
    
    # 모든 사건에 대해 반복
    for i in range(w + 1):
        for j in range(w + 1):
            # 다음 처리할 사건 번호
            next_event = max(i, j) + 1
            if next_event > w:
                continue
            
            event_pos = events[next_event]
            # 경찰차 1의 현재 위치
            if i == 0:
                car1_pos = (1, 1)
            else:
                car1_pos = events[i]
            # 경찰차 2의 현재 위치
            if j == 0:
                car2_pos = (n, n)
            else:
                car2_pos = events[j]

            # 경찰차 1이 다음 사건을 처리하는 경우의 거리 계산
            new_dist_car1 = dp[i][j] + distance(car1_pos[0], car1_pos[1], event_pos[0], event_pos[1])
            # 경찰차 2가 다음 사건을 처리하는 경우의 거리 계산
            new_dist_car2 = dp[i][j] + distance(car2_pos[0], car2_pos[1], event_pos[0], event_pos[1])
            
            # dp 배열 업데이트 및 경로 추적
            if new_dist_car1 < dp[next_event][j]:
                dp[next_event][j] = new_dist_car1
                trace[next_event][j] = (i, j)
            if new_dist_car2 < dp[i][next_event]:
                dp[i][next_event] = new_dist_car2
                trace[i][next_event] = (i, j)
    
    # 최소 거리를 찾고, 마지막 사건을 처리한 후의 위치 추적
    result = float('inf')
    last_i, last_j = -1, -1
    for i in range(w + 1):
        if dp[w][i] < result:
            result = dp[w][i]
            last_i, last_j = w, i
        if dp[i][w] < result:
            result = dp[i][w]
            last_i, last_j = i, w
    
    # 경로 추적: 어떤 경찰차가 사건을 처리했는지 기록
    path = []
    x, y = last_i, last_j
    while trace[x][y] != (-1, -1):
        px, py = trace[x][y]
        if px == x:
            path.append(2)
        else:
            path.append(1)
        x, y = px, py
    
    path.reverse()
    return result, path

# 입력 처리
import sys
input = sys.stdin.read
data = input().strip().split()
index = 0

# 도시의 크기
n = int(data[index])
index += 1
# 사건의 수
w = int(data[index])
index += 1

# 사건의 위치
events = [(0, 0)] * (w + 1)
for i in range(1, w + 1):
    x = int(data[index])
    index += 1
    y = int(data[index])
    index += 1
    events[i] = (x, y)

# 문제 해결 및 결과 출력
result, path = solve(n, w, events)
print(result)
for p in path:
    print(p)
```