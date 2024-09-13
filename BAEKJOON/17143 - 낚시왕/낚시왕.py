from collections import defaultdict

# 격자의 크기와 상어의 수를 입력받는다.
R, C, M = map(int, input().split())

# 상어 정보를 저장할 딕셔너리. 키는 (r, c) 좌표, 값은 [속도 s, 방향 d, 크기 z].
sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = [s, d, z]  # 입력 좌표는 1부터 시작하므로 0-based 좌표로 변경하여 저장

# 상하좌우 이동을 위한 방향 배열 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
dr = [-1, 1, 0, 0]  # 행 이동 (위로 -1, 아래로 +1)
dc = [0, 0, 1, -1]  # 열 이동 (오른쪽 +1, 왼쪽 -1)

# 상어가 이동하는 함수
def move_sharks():
    # 새로 이동된 상어의 정보를 저장할 딕셔너리
    new_sharks = defaultdict(list)

    # 모든 상어에 대해 이동을 처리
    for (r, c), (s, d, z) in sharks.items():
        nr, nc, nd = r, c, d  # 현재 상어의 좌표와 방향을 가져옴

        # 상하 이동(1: 위, 2: 아래)일 때
        if d == 1 or d == 2:
            s %= (R - 1) * 2  # 상하 이동은 (R-1) * 2 주기를 가짐 (리밋 없이 계속 이동할 수 없도록 주기 처리)
            for _ in range(s):
                if nr == 0 and d == 1:  # 맨 위쪽에 도달하고 위로 이동할 경우, 아래로 방향 전환
                    d = 2
                elif nr == R-1 and d == 2:  # 맨 아래쪽에 도달하고 아래로 이동할 경우, 위로 방향 전환
                    d = 1
                nr += dr[d-1]  # 새 좌표로 이동

        # 좌우 이동(3: 오른쪽, 4: 왼쪽)일 때
        else:
            s %= (C - 1) * 2  # 좌우 이동은 (C-1) * 2 주기를 가짐
            for _ in range(s):
                if nc == 0 and d == 4:  # 맨 왼쪽에 도달하고 왼쪽으로 이동할 경우, 오른쪽으로 방향 전환
                    d = 3
                elif nc == C-1 and d == 3:  # 맨 오른쪽에 도달하고 오른쪽으로 이동할 경우, 왼쪽으로 방향 전환
                    d = 4
                nc += dc[d-1]  # 새 좌표로 이동

        # 상어가 이동한 후, 같은 위치에 상어가 있을 경우 크기가 큰 상어만 남도록 처리
        if (nr, nc) in new_sharks:
            if new_sharks[(nr, nc)][2] < z:  # 크기가 더 큰 상어가 있으면 기존 상어를 덮어씀
                new_sharks[(nr, nc)] = [s, d, z]
        else:
            new_sharks[(nr, nc)] = [s, d, z]  # 빈 칸이면 새로운 상어 정보를 저장

    return new_sharks  # 이동이 완료된 상어들의 새로운 상태 반환

# 낚시왕이 잡은 상어의 크기를 저장할 변수
total_size = 0

# 낚시왕이 1번 열부터 마지막 열까지 이동하며 상어를 잡는 과정
for king_pos in range(C):
    # 1번 열부터 차례대로 가장 가까운 상어를 잡는 과정
    for row in range(R):
        if (row, king_pos) in sharks:  # 현재 낚시왕이 있는 열에서 가장 가까운 상어를 찾음
            total_size += sharks[(row, king_pos)][2]  # 상어 크기를 합산
            del sharks[(row, king_pos)]  # 상어를 잡았으므로 해당 상어는 삭제
            break  # 한 마리만 잡을 수 있으므로 루프 종료

    # 상어들이 이동하는 과정
    sharks = move_sharks()

# 낚시왕이 잡은 상어 크기의 총합을 출력
print(total_size)
