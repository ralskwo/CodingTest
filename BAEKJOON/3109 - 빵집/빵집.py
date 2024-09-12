import sys
sys.setrecursionlimit(100000)  # 파이썬의 재귀 호출 제한을 늘려줌. 기본 재귀 한도를 100,000으로 설정

R, C = map(int, input().split())  # 격자의 행(R)과 열(C)을 입력받음
grid = [list(input().strip()) for _ in range(R)]  # 각 행을 입력받아 2차원 리스트 형태로 저장

# 이동할 수 있는 방향을 정의 (오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선)
dx = [-1, 0, 1]
dy = [1, 1, 1]

# 방문 여부를 기록할 리스트를 생성 (초기값은 모두 False)
visited = [[False] * C for _ in range(R)]
pipeline_count = 0  # 설치된 파이프라인의 개수를 저장할 변수

# 깊이 우선 탐색(DFS)을 수행하는 함수 정의
def dfs(x, y):
    if y == C - 1:  # 마지막 열에 도착하면 True를 반환 (파이프 설치 성공)
        return True
    
    # 세 방향 (오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선)으로 이동 시도
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]  # 새로운 좌표 계산
        # 새로운 좌표가 유효한 범위 내에 있고, 빈 칸이며, 아직 방문하지 않았다면
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True  # 해당 좌표를 방문 처리
            if dfs(nx, ny):  # 다음 칸으로 재귀적으로 탐색
                return True  # 성공적으로 마지막 열에 도달한 경우 True 반환
    return False  # 모든 방향에서 실패한 경우 False 반환

# 첫 번째 열의 모든 행에서 파이프 설치 시도
for i in range(R):
    if grid[i][0] == '.':  # 첫 번째 열의 빈 칸에서만 파이프 설치를 시도
        if dfs(i, 0):  # 해당 행에서 파이프가 설치 가능하면
            pipeline_count += 1  # 파이프 설치 개수를 증가

print(pipeline_count)  # 설치된 파이프라인의 최대 개수를 출력
