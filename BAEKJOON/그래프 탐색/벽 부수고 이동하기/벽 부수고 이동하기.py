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
