from collections import deque  # BFS 탐색을 위해 deque를 가져옴

def move(x, y, dx, dy):  # 주어진 방향으로 구슬을 이동시키는 함수
    count = 0  # 이동한 칸 수를 저장할 변수
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':  # 벽이나 구멍에 도달할 때까지 반복
        x += dx  # 구슬을 x 방향으로 이동
        y += dy  # 구슬을 y 방향으로 이동
        count += 1  # 이동 횟수 증가
    return x, y, count  # 최종 위치와 이동 횟수를 반환

def bfs():  # BFS 탐색을 통해 최단 경로를 찾는 함수
    queue = deque([(rx, ry, bx, by, 1)])  # 빨간 구슬, 파란 구슬의 초기 위치와 깊이(1)를 큐에 추가
    visited = set([(rx, ry, bx, by)])  # 방문한 위치를 기록하여 중복 탐색을 방지

    while queue:  # 큐가 빌 때까지 반복
        crx, cry, cbx, cby, depth = queue.popleft()  # 현재 상태(구슬 위치와 깊이)를 큐에서 꺼냄

        if depth > 10:  # 이동 횟수가 10을 넘으면 더 이상 탐색하지 않음
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:  # 네 방향(상하좌우)으로 기울이기 시도
            nrx, nry, r_count = move(crx, cry, dx, dy)  # 빨간 구슬을 해당 방향으로 이동
            nbx, nby, b_count = move(cbx, cby, dx, dy)  # 파란 구슬을 해당 방향으로 이동

            if board[nbx][nby] != 'O':  # 파란 구슬이 구멍에 빠지지 않은 경우에만 진행
                if board[nrx][nry] == 'O':  # 빨간 구슬이 구멍에 빠진 경우
                    return depth  # 성공한 횟수를 반환하고 종료

                if nrx == nbx and nry == nby:  # 빨간 구슬과 파란 구슬이 같은 위치에 도달한 경우
                    if r_count > b_count:  # 더 많이 이동한 구슬을 한 칸 뒤로 조정
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                if (nrx, nry, nbx, nby) not in visited:  # 아직 방문하지 않은 위치일 경우
                    visited.add((nrx, nry, nbx, nby))  # 방문 위치로 등록
                    queue.append((nrx, nry, nbx, nby, depth+1))  # 큐에 새로운 상태를 추가하여 탐색

    return -1  # 10번 이하의 이동으로 빨간 구슬을 구멍에 넣을 수 없는 경우 -1 반환

N, M = map(int, input().split())  # 보드의 크기를 입력 받음
board = [list(input().strip()) for _ in range(N)]  # 보드의 상태를 2차원 리스트로 입력 받음

rx, ry, bx, by = 0, 0, 0, 0  # 빨간 구슬과 파란 구슬의 위치를 저장할 변수 초기화
for i in range(N):  # 보드의 모든 위치를 순회하면서
    for j in range(M):
        if board[i][j] == 'R':  # 빨간 구슬 위치를 찾으면
            rx, ry = i, j  # 빨간 구슬의 위치를 저장
        elif board[i][j] == 'B':  # 파란 구슬 위치를 찾으면
            bx, by = i, j  # 파란 구슬의 위치를 저장

print(bfs())  # BFS 함수를 호출하여 결과를 출력