from collections import deque

def bfs_maze(maze, n, m):
    # 이동 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 도착 지점에 도달했을 때
        if x == n - 1 and y == m - 1:
            return dist
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    # 도착 지점에 도달할 수 없는 경우
    return -1

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 결과 출력
print(bfs_maze(maze, n, m))
