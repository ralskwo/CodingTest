from collections import deque

# 방향 벡터를 정의하여 상하좌우 및 대각선 이동을 표현
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


# BFS 함수 정의
def bfs(x, y, grid, visited, h, w):
    # 큐를 생성하고 시작점을 추가
    queue = deque([(x, y)])
    # 시작점을 방문 처리
    visited[x][y] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 좌표를 큐에서 꺼냄
        cx, cy = queue.popleft()
        # 8방향을 탐색
        for dx, dy in directions:
            # 다음 이동 좌표 계산
            nx, ny = cx + dx, cy + dy
            # 다음 좌표가 유효하고 방문하지 않았으며 땅일 경우
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny]
                and grid[nx][ny] == 1
            ):
                # 방문 처리 후 큐에 추가
                visited[nx][ny] = True
                queue.append((nx, ny))


# 섬의 개수를 세는 함수 정의
def count_islands(w, h, grid):
    # 방문 여부를 저장할 2차원 리스트 생성
    visited = [[False] * w for _ in range(h)]
    # 섬의 개수를 저장할 변수 초기화
    count = 0

    # 모든 좌표를 순회
    for i in range(h):
        for j in range(w):
            # 땅이고 방문하지 않았다면 BFS 실행
            if grid[i][j] == 1 and not visited[i][j]:
                # 새로운 섬을 찾았으므로 BFS 호출
                bfs(i, j, grid, visited, h, w)
                # 섬의 개수 증가
                count += 1
    # 최종 섬의 개수 반환
    return count


# 메인 함수 정의
def main():
    while True:
        # 너비와 높이를 입력받음
        w, h = map(int, input().split())
        # 입력이 0 0인 경우 종료
        if w == 0 and h == 0:
            break
        # 지도를 입력받아 2차원 리스트로 저장
        grid = [list(map(int, input().split())) for _ in range(h)]
        # 섬의 개수를 계산
        result = count_islands(w, h, grid)
        # 결과 출력
        print(result)


# 프로그램 시작
if __name__ == "__main__":
    main()
