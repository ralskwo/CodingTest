import sys

input = sys.stdin.read
from itertools import combinations

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 꽃이 차지하는 5개의 칸에 대한 비용을 계산하는 함수
def calculate_cost(board, x, y, N):
    cost = board[x][y]  # 꽃의 중심 부분 비용
    # 상하좌우의 꽃잎 위치에 대한 비용을 계산
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        cost += board[nx][ny]
    return cost  # 총 비용 반환


# 꽃이 화단을 벗어나는지 여부를 확인하는 함수
def is_valid(x, y, N):
    # 중심 좌표가 1부터 N-2까지만 가능, 이를 벗어나면 False 반환
    if x <= 0 or x >= N - 1 or y <= 0 or y >= N - 1:
        return False
    return True


# 꽃이 다른 꽃과 겹치는지 확인하는 함수
def check_overlap(visited, x, y):
    # 중심 부분이 이미 방문된 경우 겹침
    if visited[x][y]:
        return False
    # 상하좌우 꽃잎이 방문되었는지 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny]:
            return False
    return True  # 겹치지 않으면 True 반환


# 꽃을 심고 방문 처리를 수행하는 함수
def place_flower(visited, x, y, place):
    visited[x][y] = place  # 중심 부분 방문 처리
    # 상하좌우 꽃잎 부분도 방문 처리
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        visited[nx][ny] = place


# 문제 해결 함수
def solve(N, board):
    # 가능한 꽃의 중심 좌표 후보 생성 (1, 1)부터 (N-2, N-2)까지
    candidates = [(x, y) for x in range(1, N - 1) for y in range(1, N - 1)]
    min_cost = float("inf")  # 최소 비용을 무한대로 초기화

    # 3개의 꽃을 심을 수 있는 모든 조합 생성
    for comb in combinations(candidates, 3):
        visited = [[False] * N for _ in range(N)]  # 방문 여부 초기화
        total_cost = 0  # 현재 조합에 대한 총 비용
        valid = True  # 현재 조합이 유효한지 여부 확인

        # 조합에 있는 각 꽃의 위치에 대해 반복
        for x, y in comb:
            # 화단 범위를 벗어나거나, 꽃이 겹치는 경우 유효하지 않음
            if not is_valid(x, y, N) or not check_overlap(visited, x, y):
                valid = False
                break  # 더 이상 탐색할 필요 없으므로 중단
            # 꽃을 심을 수 있는 경우 비용을 계산하고 방문 처리
            total_cost += calculate_cost(board, x, y, N)
            place_flower(visited, x, y, True)

        # 유효한 조합에 대해 최소 비용을 갱신
        if valid:
            min_cost = min(min_cost, total_cost)

    return min_cost  # 최소 비용 반환


# 입력을 처리하는 메인 함수
def main():
    data = input().splitlines()  # 표준 입력을 한 줄씩 읽음
    N = int(data[0])  # 첫 번째 줄에서 화단의 크기 N을 읽음
    # 나머지 줄에서 화단의 각 지점별 비용을 2차원 리스트로 변환
    board = [list(map(int, line.split())) for line in data[1:]]

    # 최소 비용을 계산하고 출력
    print(solve(N, board))


main()  # 프로그램 실행
