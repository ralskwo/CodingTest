from collections import deque  # deque를 사용하여 뱀의 몸을 관리

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위쪽 방향 벡터

def turn(direction, c):  # 방향 전환 함수
    if c == 'L':  # 왼쪽으로 90도 회전할 때
        return (direction - 1) % 4  # 현재 방향에서 왼쪽으로 90도 회전한 새로운 방향 계산
    else:  # 'D' 즉, 오른쪽으로 90도 회전할 때
        return (direction + 1) % 4  # 현재 방향에서 오른쪽으로 90도 회전한 새로운 방향 계산

def simulate():  # 뱀 게임 시뮬레이션 함수
    n = int(input())  # 보드의 크기 입력
    k = int(input())  # 사과의 개수 입력
    board = [[0] * n for _ in range(n)]  # NxN 크기의 보드를 0으로 초기화

    for _ in range(k):  # 사과의 위치 설정
        x, y = map(int, input().split())  # 각 사과의 위치 입력
        board[x-1][y-1] = 1  # 해당 위치에 사과 표시 (1로 설정)

    l = int(input())  # 방향 전환 횟수 입력
    changes = {}  # 방향 전환 정보를 저장할 딕셔너리
    for _ in range(l):  # 각 방향 전환 정보를 입력받음
        x, c = input().split()  # 시간과 방향 정보 입력
        changes[int(x)] = c  # 시간을 키로, 방향을 값으로 딕셔너리에 저장

    snake = deque([(0, 0)])  # 뱀의 초기 위치 (0, 0)을 덱에 저장
    direction = 0  # 뱀의 초기 방향 (오른쪽)
    time = 0  # 게임이 진행된 시간 초기화

    while True:  # 게임이 종료될 때까지 반복
        time += 1  # 1초 경과
        head_x, head_y = snake[-1]  # 뱀의 현재 머리 위치
        new_head_x = head_x + directions[direction][0]  # 새로운 머리 위치 x 좌표
        new_head_y = head_y + directions[direction][1]  # 새로운 머리 위치 y 좌표

        if not (0 <= new_head_x < n and 0 <= new_head_y < n):  # 벽에 부딪혔는지 확인
            break  # 벽에 부딪혔으면 게임 종료
        if (new_head_x, new_head_y) in snake:  # 자기 몸에 부딪혔는지 확인
            break  # 자기 몸에 부딪혔으면 게임 종료

        snake.append((new_head_x, new_head_y))  # 뱀의 새로운 머리 위치 추가

        if board[new_head_x][new_head_y] == 1:  # 사과가 있는 경우
            board[new_head_x][new_head_y] = 0  # 사과를 먹었으므로 보드에서 사과 제거
        else:
            snake.popleft()  # 사과가 없으면 꼬리를 줄여서 뱀의 길이 유지

        if time in changes:  # 현재 시간이 방향 전환 정보에 있는지 확인
            direction = turn(direction, changes[time])  # 방향 전환 실행

    return time  # 게임이 종료된 시간을 반환

print(simulate())  # 시뮬레이션 실행 후 결과 출력