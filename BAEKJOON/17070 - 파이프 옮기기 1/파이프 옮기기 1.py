def move_pipe(N, house):
    # DP 테이블 초기화: 각 칸마다 3개의 방향(가로, 세로, 대각선)에 대한 경우를 저장
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

    # 초기 상태 설정: 파이프는 (1, 2)에서 가로 방향으로 시작 (인덱스는 0부터 시작)
    dp[0][1][0] = 1

    # 격자판의 모든 칸을 순회하며 DP 테이블 갱신
    for r in range(N):
        for c in range(N):
            # 현재 칸이 벽인 경우 이동 불가하므로 건너뜀
            if house[r][c] == 1:
                continue

            # 가로 방향에서 이동 가능한 경우
            if c > 0:  # 왼쪽 칸이 존재해야 함
                dp[r][c][0] += dp[r][c - 1][0]  # 가로 -> 가로
                dp[r][c][0] += dp[r][c - 1][2]  # 대각선 -> 가로

            # 세로 방향에서 이동 가능한 경우
            if r > 0:  # 위쪽 칸이 존재해야 함
                dp[r][c][1] += dp[r - 1][c][1]  # 세로 -> 세로
                dp[r][c][1] += dp[r - 1][c][2]  # 대각선 -> 세로

            # 대각선 방향에서 이동 가능한 경우
            if r > 0 and c > 0 and house[r - 1][c] == 0 and house[r][c - 1] == 0:
                # 대각선 이동은 현재 칸 외에도 상, 좌 칸이 모두 빈 칸이어야 함
                dp[r][c][2] += dp[r - 1][c - 1][0]  # 가로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][1]  # 세로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][2]  # 대각선 -> 대각선

    # 파이프의 끝이 (N, N)에 도달하는 모든 방향의 방법 수를 합산하여 반환
    return dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]


# 입력값으로 격자판의 크기 N과 집의 상태를 받음
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 계산된 결과를 출력
print(move_pipe(N, house))
