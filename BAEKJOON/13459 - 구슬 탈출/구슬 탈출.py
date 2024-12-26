from collections import deque  # BFS를 위한 deque 라이브러리 임포트

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 이동 방향 벡터 (x축)
dy = [0, 0, -1, 1]  # 상, 하, 좌, 우 이동 방향 벡터 (y축)


# 구슬을 기울여서 이동시키는 함수
def move(x, y, dx, dy, board):
    count = 0  # 이동 거리(구슬이 몇 칸 이동했는지)
    # 구슬이 벽(#)을 만나거나 구멍(O)에 빠질 때까지 이동
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx  # x 방향으로 이동
        y += dy  # y 방향으로 이동
        count += 1  # 이동 횟수 증가
    return x, y, count  # 이동한 위치와 이동 거리 반환


# BFS(너비 우선 탐색)로 구슬 탈출 시뮬레이션을 수행하는 함수
def bfs(board, rx, ry, bx, by):
    queue = deque()  # BFS를 위한 큐 초기화
    queue.append(
        (rx, ry, bx, by, 0)
    )  # 초기 상태(빨간 구슬, 파란 구슬 위치, 횟수)를 큐에 추가
    visited = set()  # 방문 상태를 저장하는 집합
    visited.add((rx, ry, bx, by))  # 초기 상태를 방문 상태에 추가

    while queue:
        rx, ry, bx, by, depth = queue.popleft()  # 큐에서 상태를 하나 꺼냄

        if depth >= 10:  # 10번 이상 기울이면 실패로 간주
            return 0

        for i in range(4):  # 네 방향(상, 하, 좌, 우)으로 기울이기
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i], board)  # 빨간 구슬 이동
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i], board)  # 파란 구슬 이동

            if board[nbx][nby] == "O":  # 파란 구슬이 구멍에 빠지면 실패 (계속 진행)
                continue
            if board[nrx][nry] == "O":  # 빨간 구슬이 구멍에 빠지면 성공
                return 1

            # 두 구슬이 같은 위치에 있을 경우
            if nrx == nbx and nry == nby:
                # 더 많이 이동한 구슬을 한 칸 뒤로 이동
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 현재 상태가 방문하지 않은 상태라면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))  # 방문 상태 기록
                queue.append((nrx, nry, nbx, nby, depth + 1))  # 다음 상태를 큐에 추가

    return 0  # 10번 이내에 성공하지 못한 경우 실패


# 문제를 해결하는 함수 (입력 데이터를 기반으로 보드 상태 초기화 및 BFS 호출)
def solve(board):
    N = len(board)  # 보드의 세로 크기
    M = len(board[0])  # 보드의 가로 크기
    rx = ry = bx = by = 0  # 빨간 구슬, 파란 구슬 위치 초기화

    for i in range(N):  # 보드의 각 행을 순회
        for j in range(M):  # 보드의 각 열을 순회
            if board[i][j] == "R":  # 빨간 구슬 위치 찾기
                rx, ry = i, j
            if board[i][j] == "B":  # 파란 구슬 위치 찾기
                bx, by = i, j

    return bfs(board, rx, ry, bx, by)  # 초기 구슬 위치를 바탕으로 BFS 수행 및 결과 반환


# 프로그램의 진입점
if __name__ == "__main__":
    N, M = map(int, input().split())  # 보드의 세로(N), 가로(M) 크기 입력
    board = [list(input().strip()) for _ in range(N)]  # N줄에 걸쳐 보드 상태 입력
    print(solve(board))  # 구슬 탈출 가능 여부 출력
