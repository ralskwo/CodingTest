def n_queen(N):
    # 퀸을 배치하는 함수. 현재 row 행에 퀸을 놓을 수 있는 위치를 탐색한다.
    # cols: 현재까지 퀸이 놓인 열 정보 (비트마스크로 관리)
    # diag1: 좌하향 대각선 정보 (비트마스크로 관리)
    # diag2: 우하향 대각선 정보 (비트마스크로 관리)
    def solve(row, cols, diag1, diag2):
        # 모든 행에 퀸을 놓았을 경우 (즉, row == N이면 N개의 퀸을 모두 놓은 것임)
        if row == N:
            return 1  # 유효한 배치 하나를 찾았으므로 1을 반환

        count = 0  # 가능한 배치의 수를 세기 위한 변수

        # 가능한 퀸의 위치를 비트마스크로 계산
        # (~(cols | diag1 | diag2))는 퀸을 놓을 수 없는 자리(열, 대각선)를 제외한 자리
        # ((1 << N) - 1)은 N개의 열을 표현하는 비트마스크 (모든 열이 1인 상태)
        available_positions = (~(cols | diag1 | diag2)) & ((1 << N) - 1)

        # available_positions에 퀸을 놓을 수 있는 자리가 있을 때까지 반복
        while available_positions:
            # 가능한 위치 중 가장 오른쪽의 비트(퀸을 놓을 자리)를 구함
            pos = available_positions & -available_positions

            # 해당 비트를 지워서 퀸을 그 위치에 놓음
            available_positions -= pos

            # 다음 행으로 넘어가면서 퀸을 놓고, 열과 대각선 정보를 갱신
            # cols | pos: 현재 열에 퀸을 놓았음을 기록
            # (diag1 | pos) << 1: 좌하향 대각선에 대한 정보 업데이트 (한 칸씩 왼쪽으로 밀림)
            # (diag2 | pos) >> 1: 우하향 대각선에 대한 정보 업데이트 (한 칸씩 오른쪽으로 밀림)
            count += solve(row + 1, cols | pos, (diag1 | pos) << 1, (diag2 | pos) >> 1)

        # row 행에서 가능한 모든 경우를 다 확인한 후 가능한 배치 수를 반환
        return count

    # solve 함수를 호출하여 0번째 행부터 시작하고, 초기 상태에서는 퀸이 놓이지 않았으므로 모두 0으로 초기화
    return solve(0, 0, 0, 0)

# 사용자로부터 N을 입력받음
N = int(input())

# N-Queen 문제의 해결 방법 수를 출력
print(n_queen(N))
