import sys
sys.setrecursionlimit(10000)  # 파이썬의 기본 재귀 깊이 제한을 늘려서 깊은 재귀 호출이 가능하게 설정

def dfs(x, y):
    if x == N - 1 and y == M - 1:  # 목적지에 도달했을 때, 경로를 찾았으므로 1 반환
        return 1

    if dp[y][x] != -1:  # 이미 계산된 경로 수가 있으면 해당 값을 반환하여 중복 계산 방지
        return dp[y][x]

    dp[y][x] = 0  # 현재 위치에서 가능한 경로 수를 0으로 초기화

    for dx, dy in directions:  # 상하좌우 네 방향에 대해 이동 가능성 확인
        nx, ny = x + dx, y + dy  # 이동할 새로운 위치 좌표
        if 0 <= nx < N and 0 <= ny < M and heights[ny][nx] < heights[y][x]:  # 지도 범위 내에 있고 현재 위치보다 높이가 낮은 경우
            dp[y][x] += dfs(nx, ny)  # 다음 지점으로 이동하여 경로의 수를 누적하여 더함

    return dp[y][x]  # 계산된 현재 위치의 경로 수를 반환

M, N = map(int, input().split())  # 지도 세로 크기 M과 가로 크기 N 입력받기
heights = [list(map(int, input().split())) for _ in range(M)]  # M줄에 걸쳐 각 지점의 높이를 입력받아 heights 리스트에 저장
dp = [[-1] * N for _ in range(M)]  # dp 테이블을 -1로 초기화하여 방문하지 않은 지점을 표시
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우 이동을 위한 방향 벡터 설정

result = dfs(0, 0)  # 시작 지점 (0, 0)에서 dfs 호출하여 목적지까지의 경로의 수 계산
print(result)  # 계산된 경로의 수 출력