from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 임포트

def bfs_tomato_farm(M, N, farm):
    queue = deque()  # BFS를 위한 큐를 생성
    days = 0  # 걸린 일수를 저장할 변수 초기화
    
    # 농장의 모든 위치를 순회하면서 익은 토마토(1)의 위치를 큐에 추가
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                queue.append((i, j, 0))  # (행, 열, 경과일) 형태로 큐에 저장
    
    # BFS에서 사용할 네 방향(상, 하, 좌, 우) 이동을 위한 좌표 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 탐색 시작
    while queue:
        x, y, day = queue.popleft()  # 큐에서 현재 위치와 경과일을 꺼냄
        days = max(days, day)  # 현재까지의 최대 경과일을 갱신
        
        # 네 방향으로 이동하면서 익지 않은 토마토를 익히기
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 다음에 이동할 위치 계산
            
            # 이동한 위치가 농장 내에 있고, 익지 않은 토마토가 있는 경우
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 0:
                farm[nx][ny] = 1  # 해당 위치의 토마토를 익힘
                queue.append((nx, ny, day + 1))  # 큐에 새롭게 익은 토마토의 위치와 경과일을 추가
    
    # BFS가 끝난 후, 농장에 익지 않은 토마토가 남아있는지 확인
    for row in farm:
        if 0 in row:  # 익지 않은 토마토(0)가 존재한다면
            return -1  # 모든 토마토가 익지 않는 경우이므로 -1 반환
    
    return days  # 모든 토마토가 익은 최소 일수를 반환

# 입력값 처리
M, N = map(int, input().split())  # 상자의 가로 크기 M, 세로 크기 N을 입력받음
farm = [list(map(int, input().split())) for _ in range(N)]  # 농장 상태를 2차원 리스트로 입력받음

# BFS를 이용한 최소 일수 계산 및 출력
result = bfs_tomato_farm(M, N, farm)

print(result)  # 결과를 출력