from collections import deque

def find_largest_block_group(N, grid):
    # 블록 그룹을 찾기 위한 방문 체크 배열 생성
    visited = [[False] * N for _ in range(N)]
    # 상하좌우 탐색을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 가장 큰 블록 그룹을 저장할 변수
    largest_group = []
    # 가장 큰 블록 그룹 내 무지개 블록 수를 저장할 변수
    max_rainbow_count = -1
    # 블록 그룹의 기준 블록 위치를 저장할 변수
    standard_block = (-1, -1)

    # BFS를 이용하여 블록 그룹을 찾는 함수
    def bfs(r, c, color):
        # BFS 탐색을 위한 큐 초기화
        queue = deque([(r, c)])
        # 현재 그룹에 속한 블록의 위치 리스트
        group = [(r, c)]
        # 무지개 블록의 위치 리스트
        rainbow_blocks = []
        # 방문 표시
        visited[r][c] = True
        # 무지개 블록 수 카운트
        rainbow_count = 0
        # BFS 탐색 시작
        while queue:
            x, y = queue.popleft()
            # 상하좌우 인접한 블록 탐색
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                # 격자 범위 내에 있고 방문하지 않은 블록만 탐색
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    # 같은 색상의 블록이나 무지개 블록이면 그룹에 추가
                    if grid[nx][ny] == color or grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        group.append((nx, ny))
                        # 무지개 블록인 경우 카운트 및 리스트에 추가
                        if grid[nx][ny] == 0:
                            rainbow_count += 1
                            rainbow_blocks.append((nx, ny))

        # 무지개 블록은 다른 그룹에서 다시 사용될 수 있으므로 방문 표시 초기화
        for x, y in rainbow_blocks:
            visited[x][y] = False

        # 그룹과 무지개 블록 수 반환
        return group, rainbow_count

    # 격자 전체를 탐색하여 블록 그룹 찾기
    for i in range(N):
        for j in range(N):
            # 일반 블록이고 방문하지 않은 경우에만 그룹 탐색 시작
            if grid[i][j] > 0 and not visited[i][j]:
                group, rainbow_count = bfs(i, j, grid[i][j])
                # 그룹 크기가 2 이상이어야 유효한 그룹
                if len(group) >= 2:
                    # 기준 블록은 일반 블록 중 가장 위쪽, 왼쪽에 있는 블록 선택
                    standard_block_candidate = min((x, y) for x, y in group if grid[x][y] > 0)
                    # 가장 큰 그룹을 찾기 위한 조건 비교
                    if (len(group), rainbow_count, standard_block_candidate) > (
                        len(largest_group), max_rainbow_count, standard_block):
                        # 새로운 가장 큰 그룹 갱신
                        largest_group = group
                        max_rainbow_count = rainbow_count
                        standard_block = standard_block_candidate

    # 가장 큰 그룹 반환
    return largest_group

def apply_gravity(N, grid):
    # 중력 작용: 각 열에 대해 아래로 블록을 내림
    for col in range(N):
        # 블록이 내려올 빈 공간의 행 인덱스
        empty_row = N - 1
        # 아래쪽에서 위쪽으로 탐색
        for row in range(N - 1, -1, -1):
            # 검은색 블록을 만난 경우 그 위로는 중력이 작용하지 않음
            if grid[row][col] == -1:
                empty_row = row - 1
            # 일반 블록이나 무지개 블록을 만나면 아래로 이동
            elif grid[row][col] >= 0:
                # 빈 공간이 있으면 블록을 내림
                if empty_row != row:
                    grid[empty_row][col] = grid[row][col]
                    grid[row][col] = -2  # 빈 공간을 표시하기 위해 -2 사용
                # 빈 공간 인덱스를 위로 한 칸 이동
                empty_row -= 1

def rotate_counter_clockwise(N, grid):
    # 격자를 90도 반시계 방향으로 회전하는 함수
    new_grid = [[-2] * N for _ in range(N)]  # 새로운 격자 생성
    for i in range(N):
        for j in range(N):
            # 회전한 위치에 값 할당
            new_grid[N - j - 1][i] = grid[i][j]
    return new_grid

def play_game(N, grid):
    # 게임 진행 및 점수 계산
    total_score = 0
    while True:
        # 1. 가장 큰 블록 그룹 찾기
        largest_group = find_largest_block_group(N, grid)
        # 더 이상 블록 그룹이 없으면 게임 종료
        if not largest_group:
            break

        # 2. 블록 그룹 제거 및 점수 계산
        for r, c in largest_group:
            grid[r][c] = -2  # 블록 제거를 위해 빈 공간으로 표시
        total_score += len(largest_group) ** 2  # 점수 = 블록 수의 제곱

        # 3. 중력 작용
        apply_gravity(N, grid)

        # 4. 격자를 90도 반시계 방향으로 회전
        grid = rotate_counter_clockwise(N, grid)

        # 5. 중력 재적용
        apply_gravity(N, grid)

    # 총 점수 반환
    return total_score

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 입력 파싱
    N, M = int(data[0]), int(data[1])
    grid = []
    index = 2
    for _ in range(N):
        row = list(map(int, data[index:index + N]))
        grid.append(row)
        index += N

    # 게임 진행 및 결과 출력
    result = play_game(N, grid)
    print(result)

if __name__ == "__main__":
    main()
