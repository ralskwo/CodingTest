# 빙산 문제 풀이 및 설명

https://www.acmicpc.net/problem/2573

https://mayquartet.com/python-%ed%8c%8c%ec%9d%b4%ec%8d%ac-%eb%b0%b1%ec%a4%80-2573-%eb%b9%99%ec%82%b0-%eb%ac%b8%ec%a0%9c-%ed%92%80%ec%9d%b4-%eb%b0%8f-%ec%84%a4%eb%aa%85/

## 문제 이해

이 문제는 빙산이 시간이 지남에 따라 어떻게 분리되는지를 시뮬레이션하는 문제입니다. 빙산의 각 부분은 동서남북 방향으로 바닷물에 인접해 있을수록 더 빨리 녹습니다. 따라서 매년 빙산의 높이를 감소시키며, 빙산이 여러 덩어리로 분리되는 최초의 시점을 찾아야 합니다. 주어진 빙산이 모두 녹을 때까지 분리되지 않는다면 0을 출력합니다. 이 문제를 해결하기 위해서는 빙산이 녹는 과정을 반복적으로 시뮬레이션하고, 빙산이 언제 분리되는지 확인해야 합니다.

## 입출력 조건

- **입력:**
  - 첫 줄에 2차원 배열의 행(`N`)과 열(`M`)의 개수가 주어집니다. (`3 ≤ N, M ≤ 300`)
  - 다음 `N`개의 줄에 빙산의 높이 정보가 주어집니다. 각 칸에는 `0` 이상 `10` 이하의 정수가 주어지며, `0`은 바다를, 1 이상의 값은 빙산의 높이를 나타냅니다.
  - 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 `0`이 주어집니다.
- **출력:**
  - 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 출력합니다.
  - 만약 빙산이 전부 녹을 때까지 분리되지 않으면 `0`을 출력합니다.

## 접근 방식

이 문제는 시뮬레이션과 그래프 탐색을 사용하여 해결할 수 있습니다. 빙산의 녹는 과정과 분리 여부를 확인하기 위해 매년 반복적인 연산이 필요합니다. 이를 위해 다음 알고리즘 및 방식을 사용합니다:

1. **빙산 높이 감소 시뮬레이션:** 매년 빙산의 높이를 감소시킵니다. 빙산의 각 칸은 동서남북 방향으로 인접한 바다(0) 칸의 수만큼 높이가 감소합니다.
2. **빙산 덩어리 확인:** 매년 빙산이 여러 덩어리로 분리되었는지 확인합니다. 분리 여부를 확인하기 위해 BFS 또는 DFS와 같은 그래프 탐색 알고리즘을 사용합니다. 이 탐색을 통해 빙산의 덩어리 수를 계산합니다.
3. **조기 종료 조건:** 빙산이 분리되면 해당 연도를 반환하고 시뮬레이션을 종료합니다. 만약 빙산이 모두 녹아 0이 되면, 분리된 적이 없으므로 0을 출력합니다.
4. **효율적인 탐색:** 빙산이 있는 위치만을 저장하고 관리하여 불필요한 연산을 줄여야 합니다. 이를 통해 시간 초과를 방지합니다.

## 풀이 과정

1. **빙산 위치 저장:** 주어진 빙산 배열에서 빙산이 있는 칸의 위치를 저장합니다. 이를 통해 매년 빙산이 녹는 과정을 효율적으로 처리할 수 있습니다.
2. **빙산 녹이기:** 매년마다 빙산의 모든 칸에 대해 인접한 바다 칸의 수를 계산하여 빙산의 높이를 감소시킵니다. 이때 동시에 모든 빙산의 높이를 감소시켜야 하므로, 먼저 녹을 양을 계산한 뒤 실제로 높이를 줄입니다.
3. **빙산 덩어리 수 확인:** 빙산이 녹은 후, BFS를 사용하여 현재 빙산이 몇 개의 덩어리로 분리되어 있는지 확인합니다. BFS는 연결 요소를 찾는 데 효과적인 방법이며, 현재 위치에서 시작하여 연결된 모든 빙산을 탐색하여 방문합니다.
4. **분리 여부 확인:** 만약 빙산이 두 덩어리 이상으로 분리되었다면 현재 경과한 시간을 반환합니다.
5. **반복:** 분리되지 않았다면 다시 빙산을 녹이고, 이 과정을 반복합니다. 만약 모든 빙산이 녹아 0이 되면, 0을 출력하고 종료합니다.
6. **종료:** 위 과정을 통해 빙산이 분리되는 시점 또는 녹아 없어지는 시점을 찾을 수 있습니다. 이때까지 분리되지 않으면 0을 출력하며, 분리되었다면 그 시점을 출력합니다.

## 코드 구현

```python
from collections import deque

# 동서남북 방향을 나타내는 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 사용하여 빙산의 한 덩어리를 탐색하는 함수
def bfs(x, y, visited, iceberg):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True  # 현재 위치를 방문 처리

    while queue:
        x, y = queue.popleft()  # 큐에서 하나의 좌표를 꺼냄

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 동서남북 방향으로 인접한 칸을 탐색

            # 배열 범위 내에 있고, 아직 방문하지 않은 빙산 칸인 경우
            if 0 <= nx < len(iceberg) and 0 <= ny < len(iceberg[0]):
                if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny))  # 인접한 칸을 큐에 추가

# 빙산을 녹이는 함수
def melt_iceberg(iceberg, iceberg_positions):
    melt = [[0] * len(iceberg[0]) for _ in range(len(iceberg))]  # 각 칸의 녹을 양을 저장할 배열
    new_iceberg_positions = []  # 녹은 후에도 남아 있는 빙산의 위치를 저장할 리스트

    for x, y in iceberg_positions:
        if iceberg[x][y] > 0:
            sea_count = 0  # 주변의 바다 칸의 개수를 카운트
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if iceberg[nx][ny] == 0:  # 바다(0)인 경우
                    sea_count += 1
            melt[x][y] = sea_count  # 현재 빙산 칸에 대해 녹을 양을 저장

    for x, y in iceberg_positions:
        if iceberg[x][y] > 0:
            iceberg[x][y] = max(0, iceberg[x][y] - melt[x][y])  # 빙산의 높이를 줄임
            if iceberg[x][y] > 0:  # 녹은 후에도 남아 있는 경우
                new_iceberg_positions.append((x, y))  # 새로운 빙산 위치를 리스트에 추가

    return new_iceberg_positions  # 업데이트된 빙산 위치 반환

# 현재 빙산이 몇 개의 덩어리로 분리되어 있는지 계산하는 함수
def count_iceberg_parts(iceberg, iceberg_positions):
    visited = [[False] * len(iceberg[0]) for _ in range(len(iceberg))]
    count = 0  # 빙산 덩어리의 개수를 저장할 변수

    for x, y in iceberg_positions:
        if iceberg[x][y] > 0 and not visited[x][y]:  # 빙산이고 아직 방문하지 않은 경우
            bfs(x, y, visited, iceberg)  # BFS를 사용하여 하나의 덩어리를 탐색
            count += 1  # 덩어리의 개수 증가

    return count  # 빙산의 총 덩어리 개수 반환

# 시뮬레이션을 진행하여 빙산이 분리되는 시점을 찾는 함수
def simulate(iceberg):
    year = 0  # 경과한 시간을 나타내는 변수
    iceberg_positions = [(x, y) for x in range(1, len(iceberg) - 1)
                         for y in range(1, len(iceberg[0]) - 1) if iceberg[x][y] > 0]

    while iceberg_positions:
        parts = count_iceberg_parts(iceberg, iceberg_positions)  # 빙산의 덩어리 개수를 확인

        if parts >= 2:  # 빙산이 두 덩어리 이상으로 분리되었을 때
            return year  # 경과한 시간을 반환

        iceberg_positions = melt_iceberg(iceberg, iceberg_positions)  # 빙산을 녹임
        year += 1  # 시간이 1년 경과

    return 0  # 모두 녹을 때까지 분리되지 않으면 0 반환

# 입력 받기
n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

# 시뮬레이션 시작
result = simulate(iceberg)
print(result)
```
