# 섬의 개수 문제 풀이 및 설명

<https://www.acmicpc.net/problem/4963>

<https://mayquartet.com/python-백준-4963-섬의-개수/>

## 문제 이해

이 문제는 2차원 배열로 표현된 지도를 탐색하여 "섬"의 개수를 세는 것입니다. 지도에서 `1`은 땅을, `0`은 바다를 의미합니다. 섬은 땅(`1`)들이 가로, 세로, 대각선으로 연결되어 있는 그룹을 말합니다.

예를 들어, `1`이 가로, 세로 또는 대각선으로 연결되어 있다면 이는 하나의 섬으로 간주됩니다. 입력으로는 여러 개의 테스트 케이스가 주어지며, 각 테스트 케이스는 너비 `w`와 높이 `h`를 포함합니다.

지도 밖으로 나갈 수 없으며, 지도 내에서만 탐색을 진행해야 합니다. 각각의 테스트 케이스에 대해 발견된 섬의 개수를 출력하는 프로그램을 작성해야 합니다.

## 입출력 조건

### 입력 조건

1. 각 테스트 케이스의 첫 번째 줄에는 정수 `w`와 `h`가 주어집니다. 여기서 `w`는 지도의 너비, `h`는 지도의 높이를 나타냅니다.
2. `w`와 `h`는 모두 `0`보다 크고 `50` 이하인 양의 정수입니다.
3. 그 다음 `h`줄에 걸쳐 `w`개의 정수(`0` 또는 `1`)로 이루어진 지도가 주어집니다.
4. 입력의 마지막 줄에는 `0 0`이 주어지며, 이는 더 이상 테스트 케이스가 없음을 의미합니다.

### 출력 조건

1. 각 테스트 케이스에 대해 하나의 줄에 섬의 개수를 출력합니다.
2. 테스트 케이스별로 섬의 개수를 구하고 순서대로 출력합니다.

## 접근 방식

1. 이 문제는 그래프 탐색 문제로 볼 수 있습니다. 지도는 2차원 배열로 표현되며, 각 칸을 노드로 간주합니다.
2. 노드 간의 연결은 가로, 세로, 대각선의 인접성을 기준으로 정의됩니다. 즉, 한 노드에서 이동할 수 있는 방향은 총 8방향입니다.
3. 연결된 노드들을 하나의 그룹(즉, 섬)으로 탐색하기 위해 **BFS**(너비 우선 탐색) 또는 **DFS**(깊이 우선 탐색)를 사용할 수 있습니다.
4. 지도를 순회하면서 아직 방문하지 않은 땅(`1`)을 발견할 때마다 탐색을 시작합니다. 탐색이 끝나면 섬의 개수를 증가시킵니다.
5. 탐색 중에는 방문한 노드를 기록하여 중복 탐색을 방지해야 합니다. 이를 위해 `visited`라는 2차원 배열을 사용합니다.
6. 모든 칸을 탐색한 후 섬의 개수를 반환합니다.

<https://mayquartet.com/algorithm-bfs-너비-우선-탐색-알고리즘/>

<https://mayquartet.com/algorithm-알고리즘-dfs-깊이-우선-탐색-알고리즘-이해하기/>

## 풀이 과정

1. `directions` 배열을 사용해 8방향 이동을 정의합니다. 이는 상하좌우 및 대각선 이동을 가능하게 합니다.
2. 입력값을 처리합니다. 테스트 케이스는 여러 개로 이루어져 있으며, 마지막 줄 `0 0`이 나올 때까지 반복적으로 입력을 받습니다.
3. 각 테스트 케이스에서 다음 단계를 수행합니다.
   - 너비 `w`와 높이 `h`를 읽어옵니다.
   - 지도 정보를 2차원 배열 `grid`로 저장합니다.
   - 방문 여부를 기록하기 위한 2차원 배열 `visited`를 생성하고 초기화합니다.
4. 지도를 순회하며 아직 방문하지 않은 땅(`1`)을 발견하면 BFS 또는 DFS를 호출합니다. 탐색의 시작점으로부터 연결된 모든 땅을 방문 처리합니다.
5. BFS 또는 DFS 호출이 끝날 때마다 섬의 개수를 하나 증가시킵니다.
6. 모든 칸에 대해 탐색을 완료한 후 섬의 개수를 결과로 저장합니다.
7. 각 테스트 케이스에 대해 결과를 출력합니다.

이 과정에서 BFS는 다음과 같은 방식으로 작동합니다.

- 큐를 사용하여 현재 탐색 중인 노드를 관리합니다.
- 시작점 노드를 큐에 넣고 방문 처리합니다.
- 큐에서 노드를 하나 꺼내고, `directions`를 활용해 8방향을 탐색합니다.
- 조건에 맞는 노드(지도 범위 내, 미방문, 땅인 경우)만 큐에 추가합니다.
- 큐가 빌 때까지 위 과정을 반복합니다.

DFS를 사용할 경우, 재귀 호출로 연결된 노드를 탐색합니다. 로직은 BFS와 유사하지만, 큐 대신 재귀 스택을 사용하여 깊이 우선으로 탐색이 이루어집니다.

## 코드 구현

```python
from collections import deque

# 방향 벡터를 정의하여 상하좌우 및 대각선 이동을 표현
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# BFS 함수 정의
def bfs(x, y, grid, visited, h, w):
    # 큐를 생성하고 시작점을 추가
    queue = deque([(x, y)])
    # 시작점을 방문 처리
    visited[x][y] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 좌표를 큐에서 꺼냄
        cx, cy = queue.popleft()
        # 8방향을 탐색
        for dx, dy in directions:
            # 다음 이동 좌표 계산
            nx, ny = cx + dx, cy + dy
            # 다음 좌표가 유효하고 방문하지 않았으며 땅일 경우
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
                # 방문 처리 후 큐에 추가
                visited[nx][ny] = True
                queue.append((nx, ny))

# 섬의 개수를 세는 함수 정의
def count_islands(w, h, grid):
    # 방문 여부를 저장할 2차원 리스트 생성
    visited = [[False] * w for _ in range(h)]
    # 섬의 개수를 저장할 변수 초기화
    count = 0

    # 모든 좌표를 순회
    for i in range(h):
        for j in range(w):
            # 땅이고 방문하지 않았다면 BFS 실행
            if grid[i][j] == 1 and not visited[i][j]:
                # 새로운 섬을 찾았으므로 BFS 호출
                bfs(i, j, grid, visited, h, w)
                # 섬의 개수 증가
                count += 1
    # 최종 섬의 개수 반환
    return count

# 메인 함수 정의
def main():
    while True:
        # 너비와 높이를 입력받음
        w, h = map(int, input().split())
        # 입력이 0 0인 경우 종료
        if w == 0 and h == 0:
            break
        # 지도를 입력받아 2차원 리스트로 저장
        grid = [list(map(int, input().split())) for _ in range(h)]
        # 섬의 개수를 계산
        result = count_islands(w, h, grid)
        # 결과 출력
        print(result)

# 프로그램 시작
if __name__ == "__main__":
    main()
```
