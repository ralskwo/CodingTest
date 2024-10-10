from collections import deque  # deque 라이브러리 임포트

def tomato_ripening(M, N, H, box):  # 토마토가 익는 최소 일수를 구하는 함수 정의
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]  # 위, 아래, 앞, 뒤, 왼쪽, 오른쪽 6방향을 나타내는 리스트
    queue = deque()  # BFS를 위한 큐 정의
    total_tomatoes = 0  # 전체 토마토의 개수를 저장할 변수 초기화
    ripe_tomatoes = 0  # 익은 토마토의 개수를 저장할 변수 초기화
    
    # 상자의 각 층, 행, 열을 순회하면서 익은 토마토 위치를 큐에 추가하고 전체 토마토와 익은 토마토 개수를 센다
    for h in range(H):  # 층을 순회
        for n in range(N):  # 행을 순회
            for m in range(M):  # 열을 순회
                if box[h][n][m] == 1:  # 현재 위치의 토마토가 익은 상태라면
                    queue.append((h, n, m, 0))  # (층, 행, 열, 현재까지의 일수)를 큐에 추가
                    ripe_tomatoes += 1  # 익은 토마토 개수 증가
                if box[h][n][m] != -1:  # 토마토가 있는 칸이라면 (빈 칸이 아닌 경우)
                    total_tomatoes += 1  # 전체 토마토 개수 증가

    # 처음부터 모든 토마토가 익어있는 상태인 경우
    if ripe_tomatoes == total_tomatoes:  # 익은 토마토 개수와 전체 토마토 개수가 동일하면
        return 0  # 0일이 걸리므로 0 반환
    
    days = 0  # 최소 일수를 저장할 변수 초기화
    while queue:  # 큐가 빌 때까지 반복
        z, x, y, days = queue.popleft()  # 큐에서 현재 위치와 경과된 일수를 꺼낸다
        
        # 6방향으로 인접한 위치를 탐색
        for dz, dx, dy in directions:  # 각 방향에 대해 반복
            nz, nx, ny = z + dz, x + dx, y + dy  # 새로운 위치 계산
            # 새로운 위치가 상자 범위 내에 있고, 익지 않은 토마토(0)가 있다면
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = 1  # 익은 토마토로 상태 변경
                queue.append((nz, nx, ny, days + 1))  # 큐에 (새로운 위치, 경과된 일수 + 1)을 추가

    # 모든 토마토가 익었는지 확인
    for h in range(H):  # 층을 순회
        for n in range(N):  # 행을 순회
            for m in range(M):  # 열을 순회
                if box[h][n][m] == 0:  # 익지 않은 토마토가 있다면
                    return -1  # 모든 토마토를 익게 만들 수 없으므로 -1 반환

    return days  # 최소 일수 반환

# 입력 처리
M, N, H = map(int, input().split())  # 첫 줄에서 가로 크기, 세로 크기, 높이 입력 받기
box = []  # 토마토 상태를 저장할 3차원 리스트 초기화
for _ in range(H):  # 층의 수만큼 반복
    box.append([list(map(int, input().split())) for _ in range(N)])  # 각 층의 토마토 상태를 입력 받아 추가

# 결과 출력
print(tomato_ripening(M, N, H, box))  # 함수 호출 후 최소 일수를 출력