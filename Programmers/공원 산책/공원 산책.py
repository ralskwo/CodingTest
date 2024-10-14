def solution(park, routes):
    H = len(park)  # 공원의 세로 길이를 변수 H에 저장
    W = len(park[0])  # 공원의 가로 길이를 변수 W에 저장

    for i in range(H):  # 공원의 모든 행을 순차적으로 탐색
        for j in range(W):  # 각 행의 모든 열을 순차적으로 탐색
            if park[i][j] == 'S':  # 시작 지점을 찾으면
                x, y = i, j  # 시작 지점의 좌표를 x, y로 설정

    direction = {  # 각 방향에 따른 좌표 변화를 정의
        'N': (-1, 0),  # 북쪽으로 이동: x축 -1, y축 변화 없음
        'S': (1, 0),   # 남쪽으로 이동: x축 +1, y축 변화 없음
        'W': (0, -1),  # 서쪽으로 이동: y축 -1, x축 변화 없음
        'E': (0, 1)    # 동쪽으로 이동: y축 +1, x축 변화 없음
    }

    for route in routes:  # 각 명령어를 순차적으로 처리
        dir, n = route.split()  # 명령어에서 방향과 이동 칸 수를 분리
        n = int(n)  # 이동할 거리를 정수형으로 변환

        dx, dy = direction[dir]  # 이동할 방향에 따른 좌표 변화량을 설정
        nx, ny = x, y  # 현재 좌표를 임시로 nx, ny에 저장
        valid_move = True  # 이동 가능 여부를 체크하는 플래그 변수

        for _ in range(n):  # 이동할 거리만큼 반복
            nx += dx  # x 좌표를 이동
            ny += dy  # y 좌표를 이동

            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':  # 공원을 벗어나거나 장애물을 만나면
                valid_move = False  # 해당 이동은 불가능하므로 플래그를 False로 설정
                break  # 이동을 중단하고 명령을 무시

        if valid_move:  # 만약 유효한 이동이라면
            x, y = nx, ny  # 최종 좌표를 갱신

    return [x, y]  # 로봇 강아지의 최종 위치를 반환