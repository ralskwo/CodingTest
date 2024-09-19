def robot_cleaner():
    # 방의 크기 N과 M을 입력받음
    N, M = map(int, input().split())
    # 로봇 청소기의 시작 위치 (r, c)와 바라보는 방향 d를 입력받음
    r, c, d = map(int, input().split())
    # 방의 상태를 2차원 리스트로 입력받음
    room = [list(map(int, input().split())) for _ in range(N)]

    # 로봇이 이동할 때 사용할 방향 벡터 정의: 북, 동, 남, 서
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 청소한 칸의 수를 저장할 변수 초기화
    cleaned_count = 0

    # 로봇 청소기의 동작을 무한 루프를 통해 시뮬레이션
    while True:
        # 현재 칸이 청소되지 않은 경우, 청소함
        if room[r][c] == 0:
            room[r][c] = 2  # 청소한 칸은 2로 표시
            cleaned_count += 1  # 청소한 칸의 수를 증가시킴

        # 주변 4칸 중 청소할 수 있는 칸이 있는지 확인하기 위한 플래그
        has_cleanable_adjacent = False
        # 4방향을 모두 확인
        for i in range(4):
            # 현재 방향에서 반시계 방향으로 90도 회전
            d = (d + 3) % 4
            # 회전 후 이동할 위치 계산
            nr, nc = r + directions[d][0], c + directions[d][1]

            # 이동할 위치가 청소되지 않은 빈 칸인 경우
            if room[nr][nc] == 0:
                # 그 방향으로 한 칸 전진
                r, c = nr, nc
                # 청소할 수 있는 칸이 있음을 표시
                has_cleanable_adjacent = True
                # 한 칸 전진했으므로 다음 동작을 위해 반복문 종료
                break

        # 4방향 모두 확인했는데 청소할 수 있는 인접 칸이 없는 경우
        if not has_cleanable_adjacent:
            # 바라보는 방향을 유지한 채로 후진할 위치 계산
            back_d = (d + 2) % 4
            back_r, back_c = r + directions[back_d][0], c + directions[back_d][1]

            # 후진할 위치가 벽이 아닌 경우
            if room[back_r][back_c] != 1:
                # 후진함
                r, c = back_r, back_c
            else:
                # 후진할 수 없는 경우 작동 멈춤
                break

    # 로봇 청소기가 청소한 칸의 수를 출력
    print(cleaned_count)

# 로봇 청소기 시뮬레이션 함수 실행
robot_cleaner()
