# 벽 부수고 이동하기 문제 풀이 과정

https://www.acmicpc.net/problem/2206

## 문제 설명

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단 경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
- 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
- (1, 1)과 (N, M)은 항상 0이라고 가정하자.

### 출력

- 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

### 예제 입력 1
6 4
0100
1110
1000
0000
0111
0000

### 예제 출력 1
15

## 문제 이해

이 문제는 BFS를 사용하여 최단 경로를 찾는 전형적인 문제입니다. 다만, 벽을 한 개까지 부수고 이동할 수 있다는 점이 추가적인 조건입니다.

## 접근 방식

1. **BFS(너비 우선 탐색) 사용**:
   - BFS는 모든 간선의 가중치가 동일할 때 최단 경로를 찾는 데 유용합니다.
   - 큐를 사용하여 현재 위치에서 이동할 수 있는 모든 위치를 탐색합니다.

2. **방문 체크와 거리 리스트 초기화**:
   - 3차원 리스트를 사용하여 벽을 부쉈는지 여부와 함께 방문 여부를 체크합니다.
   - 거리 리스트도 3차원으로 관리하여 각각의 상태에서의 거리를 저장합니다.

3. **벽을 부수는 경우와 부수지 않는 경우 처리**:
   - 이동할 위치가 벽이 아닌 경우와 벽인 경우를 구분하여 처리합니다.
   - 벽인 경우에는 벽을 부쉈는지 여부를 확인하고, 아직 부수지 않았다면 벽을 부수고 이동합니다.

## 코드 설명
```python
from collections import deque

def bfs(maze, n, m):
    # 이동 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화: (x, y, 벽을 부쉈는지 여부)
    queue = deque([(0, 0, 0)])  # 시작점 (0, 0)에서 시작, 벽을 부수지 않은 상태 (0)
    
    # 방문 체크 리스트 초기화
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True  # 시작점 방문 표시
    
    # 거리 리스트 초기화
    distance = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    distance[0][0][0] = 1  # 시작점의 거리
    
    while queue:
        x, y, wall_broken = queue.popleft()  # 현재 위치와 벽을 부쉈는지 여부를 큐에서 꺼냄
        
        # 도착 지점에 도달했을 때
        if x == n - 1 and y == m - 1:
            return distance[x][y][wall_broken]  # 현재까지의 거리 반환
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 다음 위치 계산
            
            if 0 <= nx < n and 0 <= ny < m:  # 미로 범위 내에 있을 때
                if maze[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    # 벽이 아니고, 방문하지 않은 위치일 때
                    visited[nx][ny][wall_broken] = True  # 방문 표시
                    distance[nx][ny][wall_broken] = distance[x][y][wall_broken] + 1  # 거리 업데이트
                    queue.append((nx, ny, wall_broken))  # 큐에 추가
                
                if maze[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    # 벽이지만, 아직 벽을 부수지 않은 경우
                    visited[nx][ny][1] = True  # 방문 표시
                    distance[nx][ny][1] = distance[x][y][wall_broken] + 1  # 거리 업데이트
                    queue.append((nx, ny, 1))  # 큐에 추가 (벽을 부순 상태로)
    
    return -1  # 도착 지점에 도달할 수 없는 경우

# 입력 받기
n, m = map(int, input().split())  # N x M 크기의 미로
maze = [list(map(int, input().strip())) for _ in range(n)]  # 미로의 상태

# 결과 출력
print(bfs(maze, n, m))  # BFS를 수행하여 결과 출력
```