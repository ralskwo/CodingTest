from sys import (
    setrecursionlimit,
)  # 재귀 함수 호출 한도를 설정하기 위해 필요한 모듈 임포트

setrecursionlimit(
    10000
)  # 재귀 호출 한도를 10000으로 설정하여 깊은 탐색이 가능하도록 설정


# 깊이 우선 탐색(DFS)을 수행하는 함수
def dfs(x, y, field, visited, M, N):
    visited[y][x] = True  # 현재 위치를 방문 처리
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향 정의
    for dx, dy in directions:  # 각 방향에 대해 탐색 수행
        nx, ny = x + dx, y + dy  # 다음 탐색 위치 계산
        # 이동 가능한 범위 내에서 아직 방문하지 않았고 배추가 심어진 경우
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and field[ny][nx] == 1:
            dfs(nx, ny, field, visited, M, N)  # 다음 위치에 대해 재귀적으로 DFS 호출


# 입력을 처리하고 문제를 해결하는 함수
def solve():
    import sys  # 표준 입력과 출력을 처리하기 위한 모듈 임포트

    input = sys.stdin.read  # 표준 입력으로부터 데이터를 읽어오는 함수 지정
    data = input().strip().split("\n")  # 입력 데이터를 줄 단위로 분리
    T = int(data[0])  # 테스트 케이스의 개수를 첫 번째 줄에서 읽음
    results = []  # 각 테스트 케이스 결과를 저장할 리스트 초기화
    index = 1  # 현재 데이터를 읽을 인덱스 초기화
    for _ in range(T):  # 각 테스트 케이스에 대해 반복
        M, N, K = map(
            int, data[index].split()
        )  # 배추밭의 가로길이, 세로길이, 배추 개수 입력
        index += 1  # 다음 데이터로 인덱스 이동
        field = [[0] * M for _ in range(N)]  # 배추밭을 나타내는 2차원 리스트 초기화
        visited = [
            [False] * M for _ in range(N)
        ]  # 방문 여부를 기록할 2차원 리스트 초기화
        for _ in range(K):  # 배추의 위치를 입력받아 배추밭에 표시
            x, y = map(int, data[index].split())  # 배추의 x, y 좌표 읽기
            field[y][x] = 1  # 배추가 있는 위치를 1로 표시
            index += 1  # 다음 데이터로 인덱스 이동
        worm_count = 0  # 필요한 지렁이 수를 초기화
        for y in range(N):  # 배추밭의 모든 칸을 탐색
            for x in range(M):
                # 배추가 있고 아직 방문하지 않은 경우
                if field[y][x] == 1 and not visited[y][x]:
                    dfs(x, y, field, visited, M, N)  # 연결된 모든 배추를 방문 처리
                    worm_count += 1  # 새로운 지렁이 하나 추가
        results.append(worm_count)  # 현재 테스트 케이스 결과를 저장
    sys.stdout.write("\n".join(map(str, results)) + "\n")  # 모든 결과를 출력


# 프로그램의 실행 시작점
if __name__ == "__main__":
    solve()  # 문제 해결 함수 호출
