from collections import deque

# 상하좌우 방향을 나타내는 벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS(너비 우선 탐색)를 통해 외부 공기와 접촉하는 치즈를 탐색하는 함수
def bfs(cheese, visited, n, m):
    queue = deque()  # BFS에 사용할 큐 생성
    queue.append((0, 0))  # 외부 공기는 (0, 0)에서 시작
    visited[0][0] = True  # (0, 0) 위치는 방문한 것으로 표시

    # 큐가 빌 때까지 BFS 실행
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        # 상하좌우 네 방향에 대해 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 다음 좌표 설정
            # 범위 내에 있고 아직 방문하지 않은 위치라면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 해당 위치가 공기라면
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = True  # 방문한 것으로 표시
                    queue.append((nx, ny))  # 큐에 해당 위치 추가
                # 해당 위치가 치즈라면
                elif cheese[nx][ny] == 1:
                    visited[nx][ny] = True  # 방문한 것으로 표시
                    cheese[nx][ny] = 2  # 공기와 접촉한 치즈로 표시 (다음에 녹음)

# 공기와 접촉한 치즈를 녹이는 함수
def melt_cheese(cheese, n, m):
    melted = 0  # 녹은 치즈의 개수를 저장할 변수
    # 모든 좌표를 순회하며 녹일 치즈를 확인
    for i in range(n):
        for j in range(m):
            # 치즈가 공기와 접촉해서 녹는 상태라면
            if cheese[i][j] == 2:
                cheese[i][j] = 0  # 치즈를 녹임
                melted += 1  # 녹은 치즈 개수 증가
    return melted  # 녹은 치즈의 개수를 반환

# 문제를 해결하는 메인 함수
def solve():
    # 입력을 받아서 판의 크기(n, m)와 치즈 상태를 저장
    n, m = map(int, input().split())  # 세로(n)와 가로(m)의 크기 입력
    cheese = [list(map(int, input().split())) for _ in range(n)]  # 치즈의 상태 입력 (2차원 리스트)

    time = 0  # 치즈가 녹는 데 걸리는 시간을 저장할 변수
    last_cheese = 0  # 마지막에 남은 치즈의 개수를 저장할 변수

    # 치즈가 모두 녹을 때까지 반복
    while True:
        visited = [[False] * m for _ in range(n)]  # 방문 여부를 체크하는 배열 초기화
        bfs(cheese, visited, n, m)  # BFS로 외부 공기와 접촉한 치즈 찾기

        melted = melt_cheese(cheese, n, m)  # 녹은 치즈의 개수를 계산
        if melted == 0:  # 더 이상 녹을 치즈가 없다면
            break  # 반복을 종료

        last_cheese = melted  # 마지막으로 녹은 치즈의 개수를 저장
        time += 1  # 시간을 1시간 증가

    print(time)  # 치즈가 모두 녹는 데 걸린 시간 출력
    print(last_cheese)  # 모두 녹기 직전 남아 있던 치즈의 개수 출력

# 프로그램의 시작점
if __name__ == "__main__":
    solve()  # 메인 함수 호출