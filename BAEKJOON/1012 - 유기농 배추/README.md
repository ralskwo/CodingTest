# 유기농 배추 문제 풀이 및 설명

<https://www.acmicpc.net/problem/1012>

<https://mayquartet.com/python-백준-1012-유기농-배추/>

## 문제 이해

이 문제는 2차원 평면상에서 배추가 심어진 위치를 그래프로 보고, 연결된 배추의 군집 수를 계산하는 문제입니다. 배추는 상하좌우로만 인접해 있는 경우 연결된 것으로 간주합니다. 연결된 배추 군집 하나당 배추흰지렁이 한 마리가 필요하므로, 배추 군집의 수가 곧 필요한 배추흰지렁이 수를 의미합니다.  
문제를 해결하려면 각 배추밭에서 서로 연결된 배추의 군집을 찾아야 하며, 이를 그래프 탐색 문제로 변환하여 해결할 수 있습니다. 예제 입력과 출력에서 각각의 배추 군집 수를 확인하며, 상하좌우로 연결된 배추를 탐색하는 과정을 정확히 구현하는 것이 중요합니다.

## 입출력 조건

1. **입력**:

   - 첫 줄에는 테스트 케이스의 개수 `T`가 주어집니다.
   - 각 테스트 케이스의 첫 줄에는 배추밭의 가로길이 `M`, 세로길이 `N`, 배추가 심어진 위치의 개수 `K`가 공백으로 구분되어 주어집니다.
   - 다음 `K`개의 줄에는 배추의 위치 `(X, Y)`가 주어집니다. `X`는 배추밭의 가로 좌표, `Y`는 세로 좌표입니다.
   - 두 배추의 위치가 중복되지 않으며, `1 ≤ M, N ≤ 50`, `1 ≤ K ≤ 2500`입니다.

2. **출력**:
   - 각 테스트 케이스에 대해 필요한 배추흰지렁이의 최소 개수를 한 줄에 출력합니다.

## 접근 방식

1. **그래프 모델링**:

   - 배추밭을 2차원 그래프로 생각하며, 배추가 심어진 위치를 노드로 간주합니다.
   - 노드 간의 간선은 상하좌우로 인접한 배추 사이에 존재합니다.

2. **연결 요소 탐색**:

   - 연결 요소의 개수를 세기 위해 깊이 우선 탐색(DFS) 또는 너비 우선 탐색(BFS)을 사용합니다.
   - 배추가 심어진 위치를 방문 처리하여 중복 탐색을 방지합니다.

3. **알고리즘 선택**:

   - DFS와 BFS 중 어떤 것을 사용해도 됩니다. 재귀 호출을 통한 DFS는 구현이 간결하며, 반복문을 사용하는 BFS는 스택 오버플로우 방지에 유리합니다.
   - 방문 여부를 기록하기 위해 `visited` 배열을 사용합니다.

4. **효율성 고려**:
   - 최대 크기가 `50x50`인 배추밭에서 최대 2500개의 배추를 탐색하므로, `O(M * N)` 시간 복잡도로도 충분히 해결할 수 있습니다.
   - 배추 위치가 드문 경우 효율적으로 탐색을 수행하려면, 배추 위치만 기록한 배열을 사용하는 것도 방법입니다.

<https://mayquartet.com/algorithm-알고리즘-dfs-깊이-우선-탐색-알고리즘-이해하기/>

<https://mayquartet.com/algorithm-bfs-너비-우선-탐색-알고리즘/>

## 풀이 과정

1. **초기화**:

   - 각 테스트 케이스마다 `M x N` 크기의 2차원 배열 `field`를 생성하여 배추밭의 상태를 저장합니다.
   - 방문 여부를 기록하기 위해 `visited` 배열을 초기화합니다.

2. **입력 처리**:

   - 배추의 개수 `K`와 각 배추의 위치 `(X, Y)`를 입력받아 `field` 배열에 기록합니다.
   - 배추가 있는 위치를 `1`로 표시하며, 없는 위치는 `0`으로 초기화합니다.

3. **DFS 또는 BFS 수행**:

   - 배추밭을 순회하며 배추가 심어진 위치(`field[y][x] == 1`)이고 아직 방문하지 않은 경우(`visited[y][x] == False`), DFS 또는 BFS를 수행합니다.
   - 탐색 과정에서 연결된 모든 배추를 방문 처리합니다.

4. **군집 개수 계산**:

   - DFS 또는 BFS 호출이 완료되면 하나의 배추 군집 탐색이 완료된 것으로 간주하고, 군집 수(`worm_count`)를 증가시킵니다.
   - 배추밭 전체를 탐색할 때까지 반복합니다.

5. **결과 출력**:
   - 각 테스트 케이스에서 계산한 배추흰지렁이의 수를 리스트에 저장한 뒤, 이를 한 줄씩 출력합니다.

## 코드 구현

```python
from sys import setrecursionlimit
setrecursionlimit(10000)

def dfs(x, y, field, visited, M, N):
    visited[y][x] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and field[ny][nx] == 1:
            dfs(nx, ny, field, visited, M, N)

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    T = int(data[0])
    results = []
    index = 1
    for _ in range(T):
        M, N, K = map(int, data[index].split())
        index += 1
        field = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, data[index].split())
            field[y][x] = 1
            index += 1
        worm_count = 0
        for y in range(N):
            for x in range(M):
                if field[y][x] == 1 and not visited[y][x]:
                    dfs(x, y, field, visited, M, N)
                    worm_count += 1
        results.append(worm_count)
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    solve()

```
