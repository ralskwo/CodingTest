# 종이의 세로 크기 N과 가로 크기 M을 입력받음
N, M = map(int, input().split())

# 종이에 쓰여 있는 수를 2차원 리스트로 입력받음
paper = [list(map(int, input().split())) for _ in range(N)]

# 테트로미노의 이동 방향을 나타내는 리스트 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 테트로미노를 놓았을 때의 최대 합을 저장할 변수
max_sum = 0

# DFS를 사용하여 가능한 모든 테트로미노 모양을 탐색하는 함수
def dfs(x, y, depth, total):
    global max_sum
    # 깊이가 4가 되면 테트로미노가 완성된 것이므로 최대 합을 갱신
    if depth == 4:
        max_sum = max(max_sum, total)
        return

    # 4방향으로 이동하며 테트로미노의 다음 칸을 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 종이의 경계 안에 있고 아직 방문하지 않은 칸이라면
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 해당 칸을 방문 표시하고 DFS로 재귀 호출
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + paper[nx][ny])
            # 탐색이 끝나면 방문 표시를 해제하여 다음 탐색에 영향을 주지 않도록 함
            visited[nx][ny] = False

# 'ㅗ' 모양 테트로미노를 처리하는 함수
def check_special_shape(x, y):
    global max_sum
    # 'ㅗ' 모양은 각 칸을 중심으로 상하좌우 4방향 중 3방향을 선택하여 모양을 만듦
    for i in range(4):
        total = paper[x][y]
        # 3개의 방향을 선택하여 'ㅗ' 모양을 만듦
        for j in range(3):
            # (i + j) % 4를 통해 순환하며 3방향 선택
            k = (i + j) % 4
            nx = x + directions[k][0]
            ny = y + directions[k][1]
            # 선택한 방향이 종이의 경계를 벗어나면 현재 모양은 무시
            if not (0 <= nx < N and 0 <= ny < M):
                break
            total += paper[nx][ny]
        else:
            # 'ㅗ' 모양이 완성되면 최대 합을 갱신
            max_sum = max(max_sum, total)

# 각 칸을 테트로미노의 시작점으로 설정하여 가능한 모든 테트로미노 모양을 탐색
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        # 현재 칸을 방문 표시하고 DFS를 시작
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        # DFS 탐색이 끝나면 방문 표시를 해제
        visited[i][j] = False
        
        # 'ㅗ' 모양은 DFS로 처리할 수 없으므로 따로 처리
        check_special_shape(i, j)

# 최종적으로 찾은 테트로미노의 최대 합을 출력
print(max_sum)
