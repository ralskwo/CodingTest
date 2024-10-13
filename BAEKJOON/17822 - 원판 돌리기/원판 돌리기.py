from collections import deque

# N: 원판의 수, M: 각 원판에 적힌 숫자의 개수, T: 회전 명령의 개수
N, M, T = map(int, input().split())

# 각 원판의 상태를 입력받아 deque로 저장 (deque는 회전이 용이함)
board = [deque(map(int, input().split())) for _ in range(N)]

# 회전 명령을 (x, d, k) 형태로 입력받아 리스트에 저장
commands = [tuple(map(int, input().split())) for _ in range(T)]

# 인접한 좌표를 탐색할 때 사용할 상하좌우 이동 방향 (dx, dy)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인접한 수를 제거하는 함수
def remove_adjacent():
    # 제거할 좌표들을 저장할 집합 (중복 방지를 위해 set 사용)
    to_remove = set()

    # 모든 원판의 좌표를 순회하며 인접한 같은 수를 찾음
    for i in range(N):
        for j in range(M):
            # 현재 위치의 수가 0이면 (이미 제거된 수) 탐색하지 않음
            if board[i][j] == 0:
                continue
            # 원판 내부에서 좌우로 인접한 수를 검사
            if board[i][j] == board[i][(j + 1) % M]:
                to_remove.add((i, j))  # 현재 위치
                to_remove.add((i, (j + 1) % M))  # 오른쪽 위치
            if board[i][j] == board[i][(j - 1) % M]:
                to_remove.add((i, j))  # 현재 위치
                to_remove.add((i, (j - 1) % M))  # 왼쪽 위치
            # 상하로 인접한 수를 검사 (다른 원판과 연결된 부분)
            if i > 0 and board[i][j] == board[i - 1][j]:
                to_remove.add((i, j))  # 현재 위치
                to_remove.add((i - 1, j))  # 위쪽 원판의 같은 j 위치
            if i < N - 1 and board[i][j] == board[i + 1][j]:
                to_remove.add((i, j))  # 현재 위치
                to_remove.add((i + 1, j))  # 아래쪽 원판의 같은 j 위치

    # 제거할 수가 있다면 그 좌표의 수를 0으로 변경
    if to_remove:
        for i, j in to_remove:
            board[i][j] = 0
        return True  # 인접한 수를 제거한 경우 True 반환
    return False  # 제거할 수가 없는 경우 False 반환

# 원판에 적힌 수들의 평균을 기준으로 값을 조정하는 함수
def adjust_by_average():
    total_sum = 0  # 전체 수의 합
    total_count = 0  # 전체 수의 개수

    # 모든 원판을 순회하며 0이 아닌 수의 합과 개수를 계산
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                total_sum += board[i][j]
                total_count += 1

    # 남아있는 수가 없다면 조정할 필요가 없으므로 함수 종료
    if total_count == 0:
        return
    
    # 평균을 계산
    average = total_sum / total_count

    # 모든 원판을 순회하며 평균보다 크면 1을 빼고, 작으면 1을 더함
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if board[i][j] > average:
                    board[i][j] -= 1
                elif board[i][j] < average:
                    board[i][j] += 1

# 주어진 명령에 따라 원판을 회전시키는 함수
def rotate(x, d, k):
    # x의 배수인 원판을 선택하여 회전
    for i in range(x - 1, N, x):
        if d == 0:  # 시계 방향 회전
            board[i].rotate(k)
        else:  # 반시계 방향 회전
            board[i].rotate(-k)

# T번의 명령을 차례로 수행
for x, d, k in commands:
    rotate(x, d, k)  # 주어진 원판을 회전
    if not remove_adjacent():  # 인접한 수를 제거할 수 없으면
        adjust_by_average()  # 평균을 기준으로 수를 조정

# 최종적으로 원판에 남아있는 수들의 합을 계산
result = sum(sum(row) for row in board)
print(result)  # 결과 출력