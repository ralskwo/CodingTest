import sys

sys.setrecursionlimit(
    100000
)  # 재귀 깊이 제한을 100,000으로 설정 (DFS 사용 시 스택 제한을 피하기 위해)


def dfs(x, y):  # (x, y) 지점에서 시작하는 DFS 함수 정의
    if (
        dp[x][y] != -1
    ):  # 이미 계산된 dp 값이 있는 경우, 해당 값을 반환하여 중복 계산 방지
        return dp[x][y]
    dp[x][y] = 1  # 초기값 설정: 현재 위치는 최소 1칸 이동 가능
    for dx, dy in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]:  # 네 방향(상, 하, 좌, 우)으로 탐색
        nx, ny = x + dx, y + dy  # 다음 탐색 위치 계산
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            # 다음 위치가 범위 내에 있고, 대나무 양이 현재 위치보다 많은 경우
            dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))
            # 이동 후의 최대 칸 수를 계산하여 dp 값 갱신
    return dp[x][y]  # 현재 위치에서 가능한 최대 칸 수 반환


n = int(input())  # 대나무 숲의 크기 n 입력 받음
forest = [list(map(int, input().split())) for _ in range(n)]
# 대나무 숲의 정보를 n x n 크기의 2차원 리스트로 입력 받음
dp = [[-1] * n for _ in range(n)]
# dp 배열을 -1로 초기화하여 아직 탐색되지 않은 상태를 표시
result = 0  # 결과값을 저장할 변수 초기화
for i in range(n):  # 대나무 숲의 모든 지점을 순회하며 시작 지점으로 설정
    for j in range(n):
        result = max(result, dfs(i, j))
        # 각 지점에서 시작한 dfs 결과 중 최댓값으로 갱신
print(result)  # 최종 결과 출력
