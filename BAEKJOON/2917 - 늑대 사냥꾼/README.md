# 늑대 사냥꾼 문제 풀이 및 설명

<https://www.acmicpc.net/problem/2917>

<https://mayquartet.com/python-백준-2917-늑대-사냥꾼/>

# 문제 이해

이 문제는 늑대(현우)가 사냥꾼들을 피해 안전하게 오두막으로 대피하는 상황을 시뮬레이션합니다. 숲은 2차원 그리드로 표현되며, 늑대는 나무와의 거리를 최대화하면서 이동해야 합니다. 이는 그래프 탐색 문제의 변형으로, 최단 경로를 찾는 것이 아니라 '가장 안전한' 경로를 찾아야 한다는 점에서 독특합니다. '안전'의 정의가 경로 상의 모든 지점에서 가장 가까운 나무까지의 거리의 최솟값을 최대화하는 것이라는 점을 이해하는 것이 중요합니다. 이는 일반적인 최단 경로 알고리즘을 변형하여 접근해야 함을 시사합니다.

## 입출력 조건

### 입력 조건

- 숲의 크기를 나타내는 두 정수 **N**과 **M**이 주어집니다 (1 ≤ N, M ≤ 500).
- 이어서 **N**개의 줄에 걸쳐 숲의 상태를 나타내는 문자열이 주어집니다.
- 각 문자열은 **M**개의 문자로 구성되며:
  - `.`은 빈 공간
  - `+`는 나무
  - `V`는 늑대의 위치
  - `J`는 오두막의 위치를 나타냅니다.
- 늑대(`V`)와 오두막(`J`)은 각각 하나씩만 존재하며, 최소한 하나의 나무(`+`)가 있음이 보장됩니다.

### 출력 조건

- 출력은 단일 정수로, 가장 안전한 경로에서 나무와 늑대 사이의 최소 거리를 나타냅니다.
- 만약 오두막에 도달할 수 없는 경우, 이는 별도로 처리되어야 합니다.

---

## 접근 방식

이 문제를 해결하기 위해서는 그래프 탐색 알고리즘을 변형하여 사용해야 합니다. 구체적으로, 다익스트라 알고리즘의 변형된 버전을 사용할 수 있습니다. 일반적인 다익스트라 알고리즘이 시작점에서 각 노드까지의 최단 거리를 찾는 데 반해, 이 문제에서는 '안전 거리'를 최대화해야 합니다. 접근 방식은 다음과 같습니다:

1. **각 위치에서 가장 가까운 나무까지의 거리 계산**

   - 다중 소스 BFS(너비 우선 탐색)를 사용하여 효율적으로 수행할 수 있습니다.

2. **변형된 다익스트라 알고리즘 사용**

   - 늑대의 시작 위치에서 오두막까지의 '가장 안전한' 경로를 찾습니다.
   - 우선순위 큐를 사용하여 항상 현재까지 가장 안전한 경로를 먼저 탐색합니다.

3. **경로 상의 '안전 거리' 정의**
   - 각 위치에서의 '안전 거리'를 해당 위치까지의 경로 상에서 나무와의 최소 거리로 정의합니다.

이 접근 방식은 그리디한 방법으로 최적의 해를 찾을 수 있으며, 우선순위 큐를 사용함으로써 효율적인 탐색이 가능합니다.

<https://mayquartet.com/algorithm-dijkstra-다익스트라-알고리즘-이해하기/>

<https://mayquartet.com/algorithm-bfs-너비-우선-탐색-알고리즘/>

---

## 풀이 과정

### 1. 입력 처리

- 숲의 크기와 상태를 입력받아 2차원 리스트로 저장합니다.
- 이 과정에서 늑대의 위치와 모든 나무의 위치를 찾아 별도로 저장합니다.

### 2. 나무까지의 거리 계산

- 다중 소스 BFS를 사용하여 각 위치에서 가장 가까운 나무까지의 거리를 계산합니다.
- 모든 나무의 위치를 시작점으로 하여 BFS를 수행하며, 각 위치까지의 최소 거리를 기록합니다.
- 이 과정의 시간 복잡도는 **O(NM)**입니다.

### 3. 안전한 경로 찾기

- 변형된 다익스트라 알고리즘을 사용하여 가장 안전한 경로를 찾습니다.
- 우선순위 큐를 사용하여 현재까지의 최소 안전 거리가 가장 큰 경로를 우선적으로 탐색합니다.
- 각 위치를 방문할 때마다, 해당 위치까지의 경로에서의 최소 안전 거리(즉, 나무와의 최소 거리)를 계산하고 이를 우선순위 큐에 저장합니다.
- 오두막에 도달하면 그때의 안전 거리를 반환합니다.

### 4. 결과 출력

- 찾은 가장 안전한 경로의 최소 안전 거리를 출력합니다.
- 만약 오두막에 도달할 수 없는 경우, 적절한 값(예: `-1`)을 출력합니다.

---

## 시간 복잡도

- 그래프의 모든 위치를 최대 한 번씩만 방문하므로, 전체 시간 복잡도는 **O(NM log(NM))**입니다.
  - 여기서 `log(NM)` 항은 우선순위 큐 연산에서 발생합니다.
- 이 방법은 주어진 문제의 제약 조건(1 ≤ N, M ≤ 500) 내에서 효율적으로 동작할 수 있습니다.

## 코드 구현

```python
import sys
import heapq
from collections import deque

# 입력을 더 빠르게 받기 위해 sys.stdin.readline을 사용
input = sys.stdin.readline

def find_positions(forest, N, M):
    # 늑대와 나무의 위치를 찾는 함수
    wolf_position = None
    tree_positions = []
    for i in range(N):
        for j in range(M):
            if forest[i][j] == 'V':
                # 늑대의 위치를 저장
                wolf_position = (i, j)
            elif forest[i][j] == '+':
                # 나무의 위치를 리스트에 추가
                tree_positions.append((i, j))
    return wolf_position, tree_positions

def calculate_tree_distances_optimized(forest, N, M, tree_positions):
    # 각 칸에서 가장 가까운 나무까지의 거리를 계산하는 함수
    tree_distances = [[float('inf')] * M for _ in range(N)]
    queue = deque(tree_positions)

    for x, y in tree_positions:
        # 나무가 있는 위치의 거리를 0으로 초기화
        tree_distances[x][y] = 0

    while queue:
        # BFS를 사용하여 각 칸까지의 최소 거리를 계산
        x, y = queue.popleft()
        current_distance = tree_distances[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 상하좌우 네 방향을 확인
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 새로운 위치가 더 가까운 경우 거리를 업데이트하고 큐에 추가
                if tree_distances[nx][ny] > current_distance + 1:
                    tree_distances[nx][ny] = current_distance + 1
                    queue.append((nx, ny))

    return tree_distances

def find_safest_path_optimized(forest, N, M, wolf_position, tree_distances):
    # 가장 안전한 경로를 찾는 함수
    start_x, start_y = wolf_position
    pq = []
    # 우선순위 큐에 시작 위치 추가 (거리의 음수, x좌표, y좌표)
    heapq.heappush(pq, (-tree_distances[start_x][start_y], start_x, start_y))
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True

    while pq:
        # 가장 안전한 경로를 우선적으로 탐색
        min_dist, x, y = heapq.heappop(pq)
        min_dist = -min_dist  # 원래 거리로 변환

        if forest[x][y] == 'J':
            # 오두막에 도착하면 최소 안전 거리 반환
            return min_dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 상하좌우 네 방향을 확인
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 새로운 위치가 유효하고 방문하지 않았다면
                visited[nx][ny] = True
                # 현재까지의 최소 거리와 새 위치의 나무까지의 거리 중 작은 값 선택
                new_min_dist = min(min_dist, tree_distances[nx][ny])
                # 우선순위 큐에 새 위치 추가
                heapq.heappush(pq, (-new_min_dist, nx, ny))

    return -1  # 오두막에 도달할 수 없는 경우

def solve():
    # 메인 솔루션 함수
    N, M = map(int, input().split())  # 숲의 크기 입력
    forest = [list(input().strip()) for _ in range(N)]  # 숲의 지도 입력

    # 늑대와 나무의 위치 찾기
    wolf_position, tree_positions = find_positions(forest, N, M)
    # 각 위치에서 나무까지의 거리 계산
    tree_distances = calculate_tree_distances_optimized(forest, N, M, tree_positions)
    # 가장 안전한 경로 찾기
    result = find_safest_path_optimized(forest, N, M, wolf_position, tree_distances)

    print(result)  # 결과 출력

if __name__ == "__main__":
    solve()  # 프로그램 실행
```
