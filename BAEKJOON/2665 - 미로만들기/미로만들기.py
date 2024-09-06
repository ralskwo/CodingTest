from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 임포트

# 4방향(상, 하, 좌, 우)으로 이동할 때의 x축, y축 변화를 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_min_change(n, grid):  # BFS 알고리즘을 이용하여 최소 검은 방 변경 수를 계산하는 함수
    # 각 방까지 도달할 때 최소로 검은 방을 흰 방으로 바꾼 횟수를 저장하는 배열을 생성, 처음에는 무한대 값으로 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 출발점인 (0,0)은 흰 방이므로 변경할 필요가 없으므로 0으로 설정
    dist[0][0] = 0
    
    # 시작점 (0, 0)을 deque에 추가, BFS 시작
    dq = deque([(0, 0)])
    
    # deque가 빌 때까지 반복, BFS 탐색 진행
    while dq:
        # deque에서 현재 좌표를 꺼냄
        x, y = dq.popleft()
        
        # 4방향으로 이동 시도
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 이동하려는 좌표가 유효한 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 이동하려는 방이 흰 방이고, 이전보다 적은 비용으로 도달할 수 있으면
                if grid[nx][ny] == '1' and dist[nx][ny] > dist[x][y]:
                    # 그 방까지의 최소 비용을 업데이트
                    dist[nx][ny] = dist[x][y]
                    # 흰 방은 비용이 추가되지 않으므로 deque의 앞에 추가
                    dq.appendleft((nx, ny))
                # 이동하려는 방이 검은 방이고, 이전보다 적은 비용으로 도달할 수 있으면
                elif grid[nx][ny] == '0' and dist[nx][ny] > dist[x][y] + 1:
                    # 검은 방을 흰 방으로 바꾸는 비용(1)을 추가하여 최소 비용을 업데이트
                    dist[nx][ny] = dist[x][y] + 1
                    # 검은 방은 비용이 추가되므로 deque의 뒤에 추가
                    dq.append((nx, ny))
    
    # 도착점 (n-1, n-1)에 도달할 때 최소로 검은 방을 흰 방으로 바꾼 횟수를 반환
    return dist[n-1][n-1]

# 첫 번째 줄에서 n을 입력받음
n = int(input())

# n개의 줄에서 각 줄마다 방의 상태를 입력받아 리스트로 저장
grid = [input().strip() for _ in range(n)]

# BFS 탐색 결과를 출력
print(bfs_min_change(n, grid))
