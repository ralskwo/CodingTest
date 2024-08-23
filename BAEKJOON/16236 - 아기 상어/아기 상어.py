from collections import deque

def bfs(start_x, start_y, size, grid):
    N = len(grid)
    # 네 방향(상, 하, 좌, 우)을 나타내는 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    # BFS를 위한 큐 초기화, 초기 위치와 거리를 큐에 추가
    queue = deque([(start_x, start_y, 0)])  
    # 방문한 위치를 저장하기 위한 집합
    visited = set()
    visited.add((start_x, start_y))
    # 먹을 수 있는 물고기 리스트 초기화
    fish = []

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                # 상어가 지나갈 수 있거나 먹을 수 있는 경우
                if grid[nx][ny] <= size:  
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
                    # 상어가 먹을 수 있는 물고기
                    if 0 < grid[nx][ny] < size:  
                        fish.append((dist + 1, nx, ny))
    
    # 먹을 수 있는 물고기가 없으면 None 반환
    if not fish:
        return None
    # 거리, 행, 열 순으로 정렬하여 가장 가까운 물고기 반환
    fish.sort()
    return fish[0]  # (거리, x, y)

def baby_shark(grid):
    N = len(grid)
    # 상어의 초기 위치를 찾고 grid에서 제거
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                shark_x, shark_y = i, j
                grid[i][j] = 0

    size = 2
    eaten = 0
    time = 0

    while True:
        # BFS를 사용하여 먹을 수 있는 물고기를 찾음
        result = bfs(shark_x, shark_y, size, grid)
        if not result:
            break
        dist, shark_x, shark_y = result
        time += dist
        grid[shark_x][shark_y] = 0
        eaten += 1
        # 상어가 현재 크기만큼 물고기를 먹으면 크기 증가
        if eaten == size:
            size += 1
            eaten = 0

    return time

# 입력 받기
N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(baby_shark(grid))
