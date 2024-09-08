from collections import deque

# R: 호수의 행 개수, C: 호수의 열 개수 입력 받음
R, C = map(int, input().split())

# 호수의 상태를 저장하는 2차원 리스트. 입력에서 각 줄을 받아 리스트로 변환
lake = [list(input().strip()) for _ in range(R)]

# 방향벡터. 상, 하, 좌, 우로 이동하기 위한 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백조의 위치를 저장할 리스트
swans = []

# 물이 있는 위치를 저장할 큐 (BFS 탐색을 위한 큐)
water_queue = deque()

# 호수 상태를 순회하며 백조의 위치와 물의 위치를 저장
for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':  # 백조의 위치일 경우
            swans.append((i, j))  # 백조 위치 저장
            lake[i][j] = '.'  # 백조가 있는 곳을 물로 변경
        if lake[i][j] == '.':  # 물 공간일 경우
            water_queue.append((i, j))  # 물의 위치를 큐에 저장

# 첫 번째 백조의 위치를 BFS 시작점으로 큐에 저장
swan_queue = deque([swans[0]])

# 백조가 이동한 위치를 기록하기 위한 방문 배열
visited_swan = [[False] * C for _ in range(R)]
visited_swan[swans[0][0]][swans[0][1]] = True  # 첫 번째 백조의 위치를 방문 처리

# 다음 날 백조가 이동할 수 있는 얼음의 위치를 저장하는 큐
next_swan_queue = deque()

# 물과 얼음을 녹이는 BFS 함수
def melt_ice():
    next_water_queue = deque()  # 다음 날에 물이 될 얼음의 위치를 저장하는 큐
    while water_queue:  # 물의 위치를 하나씩 처리
        x, y = water_queue.popleft()  # 현재 물의 위치를 꺼냄
        for i in range(4):  # 상, 하, 좌, 우로 인접한 위치를 확인
            nx, ny = x + dx[i], y + dy[i]  # 새로운 좌표 계산
            if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == 'X':  # 인접한 칸이 얼음일 경우
                lake[nx][ny] = '.'  # 얼음을 물로 변환
                next_water_queue.append((nx, ny))  # 녹은 물의 위치를 큐에 저장
    return next_water_queue  # 다음 날에 녹을 물의 위치를 반환

# 백조가 이동할 수 있는지 확인하는 BFS 함수
def move_swan():
    global next_swan_queue  # 전역 변수 사용
    while swan_queue:  # 백조의 이동을 처리하는 큐
        x, y = swan_queue.popleft()  # 현재 백조의 위치를 꺼냄
        if (x, y) == swans[1]:  # 두 번째 백조의 위치에 도착하면
            return True  # 백조들이 만났음을 나타내는 True 반환
        for i in range(4):  # 상, 하, 좌, 우로 인접한 위치를 확인
            nx, ny = x + dx[i], y + dy[i]  # 새로운 좌표 계산
            if 0 <= nx < R and 0 <= ny < C and not visited_swan[nx][ny]:  # 유효한 좌표이고 아직 방문하지 않은 경우
                visited_swan[nx][ny] = True  # 방문 처리
                if lake[nx][ny] == '.':  # 인접한 칸이 물일 경우
                    swan_queue.append((nx, ny))  # 물이므로 백조가 이동할 수 있음
                elif lake[nx][ny] == 'X':  # 인접한 칸이 얼음일 경우
                    next_swan_queue.append((nx, ny))  # 얼음이므로 다음 날에 이동할 수 있음
    return False  # 백조들이 아직 만나지 못했음을 나타내는 False 반환

# 전체 과정을 해결하는 함수
def solve():
    global water_queue, swan_queue, next_swan_queue  # 전역 변수 사용
    days = 0  # 날짜를 세기 위한 변수
    while True:  # 매일 반복
        if move_swan():  # 백조들이 만날 수 있으면
            return days  # 걸린 날짜를 반환하고 종료
        water_queue = melt_ice()  # 물을 확장하여 얼음을 녹임
        swan_queue, next_swan_queue = next_swan_queue, deque()  # 백조의 이동 경로를 다음 날로 갱신
        days += 1  # 하루가 지나면 날짜 증가

# 결과 출력
print(solve())
