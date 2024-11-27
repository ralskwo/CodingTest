def can_place(board, x, y, size):
    # 색종이를 놓으려는 위치와 크기를 확인하여, 해당 크기의 색종이를 놓을 수 있는지 검사
    if x + size > 10 or y + size > 10:
        # 색종이가 종이의 범위를 벗어나면 배치할 수 없음
        return False
    for i in range(size):
        for j in range(size):
            if board[x + i][y + j] == 0:
                # 색종이를 놓으려는 영역에 0이 있다면 배치할 수 없음
                return False
    return True


def place_paper(board, x, y, size, value):
    # 색종이를 종이에 놓거나 제거하는 함수
    for i in range(size):
        for j in range(size):
            board[x + i][y + j] = value


def solve(board, papers, count):
    global min_papers
    # 모든 1을 덮었는지 확인
    if all(board[i][j] == 0 for i in range(10) for j in range(10)):
        # 1이 모두 덮였으면 최소 색종이 개수 갱신
        min_papers = min(min_papers, count)
        return

    # 첫 번째 1의 위치를 찾음
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                x, y = i, j
                break
        else:
            continue
        break

    # 색종이 크기별로 배치 시도 (큰 크기부터 순서대로)
    for size in range(5, 0, -1):
        if papers[size] > 0 and can_place(board, x, y, size):
            # 현재 크기의 색종이를 놓음
            place_paper(board, x, y, size, 0)
            papers[size] -= 1

            # 재귀적으로 다음 상태 탐색
            solve(board, papers, count + 1)

            # 탐색이 끝난 뒤 상태를 원래대로 복구
            place_paper(board, x, y, size, 1)
            papers[size] += 1


# 10x10 크기의 종이 상태를 입력으로 받음
board = [list(map(int, input().split())) for _ in range(10)]

# 각 크기의 색종이 개수를 저장 (1x1부터 5x5까지 각 5개씩)
papers = {i: 5 for i in range(1, 6)}

# 최소 색종이 개수를 저장할 변수 (초기값은 무한대로 설정)
min_papers = float("inf")

# 백트래킹 탐색 시작
solve(board, papers, 0)

# 결과 출력 (1을 모두 덮는 것이 불가능한 경우 -1 출력)
print(-1 if min_papers == float("inf") else min_papers)
