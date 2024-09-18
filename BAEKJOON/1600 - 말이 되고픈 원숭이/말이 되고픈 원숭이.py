import sys  # 시스템 모듈 임포트
from collections import deque  # 덱 자료구조 임포트

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

horse_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),  # 말의 이동 방향 정의 (8가지)
               (2, 1), (1, 2), (-1, 2), (-2, 1)]

monkey_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 원숭이의 일반 이동 방향 정의 (4가지)

K = int(input())  # 말처럼 이동할 수 있는 최대 횟수 K 입력
W, H = map(int, input().split())  # 격자판의 가로(W), 세로(H) 크기 입력
grid = [list(map(int, input().split())) for _ in range(H)]  # 격자판 정보 입력

visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]  # 방문 여부를 체크하기 위한 3차원 배열 생성

def bfs():
    queue = deque()  # BFS를 위한 큐 생성
    queue.append((0, 0, 0, 0))  # 시작점 추가 (x좌표, y좌표, 이동 횟수, 말 이동 사용 횟수)
    visited[0][0][0] = True  # 시작점 방문 처리

    while queue:
        x, y, cnt, k = queue.popleft()  # 큐에서 현재 위치와 상태를 꺼냄

        if x == W - 1 and y == H - 1:  # 도착지점에 도달한 경우
            return cnt  # 이동 횟수 반환

        if k < K:  # 말의 이동을 더 사용할 수 있는 경우
            for dx, dy in horse_moves:  # 말의 이동 방향에 대해 반복
                nx, ny = x + dx, y + dy  # 새로운 위치 계산
                nk = k + 1  # 말 이동 횟수 증가
                if 0 <= nx < W and 0 <= ny < H:  # 격자판 범위 내인지 확인
                    if not visited[ny][nx][nk] and grid[ny][nx] == 0:  # 방문하지 않았고 장애물이 없는 경우
                        visited[ny][nx][nk] = True  # 방문 처리
                        queue.append((nx, ny, cnt + 1, nk))  # 큐에 추가

        for dx, dy in monkey_moves:  # 원숭이의 일반 이동 방향에 대해 반복
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            nk = k  # 말 이동 횟수는 그대로
            if 0 <= nx < W and 0 <= ny < H:  # 격자판 범위 내인지 확인
                if not visited[ny][nx][nk] and grid[ny][nx] == 0:  # 방문하지 않았고 장애물이 없는 경우
                    visited[ny][nx][nk] = True  # 방문 처리
                    queue.append((nx, ny, cnt + 1, nk))  # 큐에 추가

    return -1  # 도착지점에 도달할 수 없는 경우 -1 반환

print(bfs())  # 결과 출력