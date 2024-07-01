# 벽 부수고 이동하기 문제 풀이 과정

## 문제 이해

주어진 문제는 N x M 크기의 미로에서 출발점 (1, 1)에서 도착점 (N, M)까지 이동하는 최단 경로를 찾는 것입니다. 미로는 0과 1로 이루어져 있으며, 1은 이동할 수 없는 벽을, 0은 이동할 수 있는 길을 나타냅니다. 이동은 상하좌우로만 가능합니다. 이동 중 벽을 한 번 부술 수 있습니다.

## 접근 방식

이 문제는 그래프 탐색 문제로, BFS(너비 우선 탐색)를 사용하여 해결할 수 있습니다. BFS는 최단 경로를 찾는 데 효과적입니다. 벽을 부수고 이동할 수 있는 경우를 고려하여 3차원 리스트를 사용하여 방문 여부를 체크합니다.

## 풀이 과정

1. **입력 받기**: N과 M을 입력받고, 미로의 상태를 입력받습니다.
2. **BFS 초기화**: BFS를 위한 큐를 초기화하고, 시작점을 큐에 넣습니다. 또한 방문 여부와 벽을 부쉈는지 여부를 체크하기 위한 3차원 리스트를 초기화합니다.
3. **BFS 수행**: 큐에서 노드를 꺼내 4방향(상, 하, 좌, 우)으로 이동 가능한지 체크합니다. 이동할 수 있는 경우와 벽을 부수고 이동하는 경우를 나누어 처리합니다.
4. **도착점 도달**: 도착점에 도달하면 그때까지의 거리를 반환합니다. 도착점에 도달할 수 없는 경우 -1을 반환합니다.


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