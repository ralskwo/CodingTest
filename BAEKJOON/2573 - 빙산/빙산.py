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
