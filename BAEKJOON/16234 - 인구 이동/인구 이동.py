from collections import deque  # deque를 사용하기 위해 collections 모듈에서 가져옴

N, L, R = map(int, input().split())  # N: 땅의 크기, L: 인구 차이 하한선, R: 인구 차이 상한선
population = [list(map(int, input().split())) for _ in range(N)]  # 각 나라의 인구수를 2차원 리스트로 입력 받음
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향을 나타내는 벡터

def bfs(start_row, start_col, visited):  # BFS를 통해 연합을 찾고, 인구 이동을 수행하는 함수
    queue = deque()  # BFS를 위한 큐 생성
    queue.append((start_row, start_col))  # 시작점을 큐에 추가
    visited[start_row][start_col] = True  # 시작점 방문 처리
    union = [(start_row, start_col)]  # 연합에 포함된 나라를 저장할 리스트

    total_population = population[start_row][start_col]  # 연합의 총 인구수를 현재 나라의 인구수로 초기화
    country_count = 1  # 연합에 속한 나라의 개수를 1로 초기화

    while queue:  # 큐가 빌 때까지 반복
        row, col = queue.popleft()  # 큐에서 하나의 나라를 꺼냄

        for dr, dc in directions:  # 상, 하, 좌, 우 네 방향에 대해 반복
            new_row, new_col = row + dr, col + dc  # 새로운 나라의 좌표 계산

            # 새로운 좌표가 배열의 범위를 벗어나지 않고, 아직 방문하지 않은 경우
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
                # 두 나라의 인구 차이가 L 이상 R 이하인 경우
                if L <= abs(population[row][col] - population[new_row][new_col]) <= R:
                    visited[new_row][new_col] = True  # 새로운 나라를 방문 처리
                    queue.append((new_row, new_col))  # 새로운 나라를 큐에 추가
                    union.append((new_row, new_col))  # 새로운 나라를 연합에 추가
                    total_population += population[new_row][new_col]  # 연합의 총 인구수에 새로운 나라의 인구수 추가
                    country_count += 1  # 연합의 나라 수 1 증가

    new_population = total_population // country_count  # 연합에 속한 나라들의 새로운 인구수 계산 (소수점 버림)
    for row, col in union:  # 연합에 속한 모든 나라에 대해
        population[row][col] = new_population  # 연합의 모든 나라의 인구수를 새로운 인구수로 갱신

    return len(union) > 1  # 연합의 크기가 1보다 크면 인구 이동이 발생한 것으로 간주

days = 0  # 인구 이동이 발생한 일수를 0으로 초기화

while True:  # 무한 반복
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 나타내는 2차원 리스트 초기화
    movement_occurred = False  # 인구 이동이 발생했는지 여부를 나타내는 변수 초기화

    for r in range(N):  # 모든 나라에 대해 행을 기준으로 반복
        for c in range(N):  # 모든 나라에 대해 열을 기준으로 반복
            if not visited[r][c]:  # 방문하지 않은 나라에 대해
                if bfs(r, c, visited):  # 해당 나라를 시작으로 BFS를 수행
                    movement_occurred = True  # 인구 이동이 발생했음을 표시

    if not movement_occurred:  # 인구 이동이 발생하지 않았으면
        break  # 반복 종료

    days += 1  # 인구 이동이 발생한 날 수 1 증가

print(days)  # 최종적으로 인구 이동이 발생한 일수를 출력
