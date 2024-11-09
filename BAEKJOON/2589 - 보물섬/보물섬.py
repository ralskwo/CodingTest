from collections import deque  # BFS 구현을 위해 deque를 사용하기 위해 임포트

n, m = map(int, input().split())  # 지도 크기인 세로(n)와 가로(m)를 입력받음
treasure_map = [input().strip() for _ in range(n)]  # 보물 지도를 입력받아 리스트로 저장

# 상하좌우 이동을 위한 방향 벡터 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색을 수행하는 함수 정의
def bfs(x, y):
    # BFS를 위한 큐를 생성하고 시작 위치 (x, y)와 거리(0)를 큐에 추가
    queue = deque([(x, y, 0)])
    
    # 방문 여부를 확인하기 위한 2차원 배열 생성
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True  # 시작 위치를 방문으로 표시
    
    max_distance = 0  # 현재 BFS 탐색에서의 최대 거리를 저장하는 변수
    
    # 큐가 빌 때까지 반복하여 BFS 수행
    while queue:
        cx, cy, dist = queue.popleft()  # 큐에서 현재 위치와 거리를 가져옴
        max_distance = max(max_distance, dist)  # 최장 거리 갱신
        
        # 네 방향으로 이동하며 인접한 육지를 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy  # 새로운 위치 계산
            
            # 이동한 위치가 지도 범위 내에 있고, 방문하지 않았으며, 육지인 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and treasure_map[nx][ny] == 'L':
                visited[nx][ny] = True  # 새로운 위치를 방문으로 표시
                queue.append((nx, ny, dist + 1))  # 거리 1 증가하여 큐에 추가
                
    return max_distance  # BFS 탐색에서 발견한 최장 거리를 반환

# 전체 탐색에서의 최장 최단 거리를 저장할 변수
max_treasure_distance = 0

# 모든 육지 위치에서 BFS 탐색을 수행하여 최장 거리를 갱신
for i in range(n):
    for j in range(m):
        if treasure_map[i][j] == 'L':  # 현재 위치가 육지인 경우에만 탐색
            max_treasure_distance = max(max_treasure_distance, bfs(i, j))  # 최장 거리 갱신

# 보물이 묻힌 두 위치 간의 최장 최단 거리를 출력
print(max_treasure_distance)