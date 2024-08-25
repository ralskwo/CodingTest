from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 import

def bfs(start, prison_map, h, w):
    # 거리를 저장할 2차원 리스트를 초기화. 초기값은 무한대(float('inf'))
    dist = [[float('inf')] * (w + 2) for _ in range(h + 2)]
    
    # 시작 위치를 deque에 추가하고, 시작 위치의 거리를 0으로 설정
    queue = deque([start])
    dist[start[0]][start[1]] = 0

    # BFS를 수행하여 모든 경로를 탐색
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄

        # 네 방향(상, 하, 좌, 우)으로 이동할 수 있는 경우를 검사
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy  # 다음 이동할 위치 계산
            # 다음 위치가 감옥 평면도 내에 있는지 확인
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                # 다음 위치가 벽이 아니고 아직 방문하지 않은 경우
                if prison_map[nx][ny] != '*' and dist[nx][ny] == float('inf'):
                    # 다음 위치가 문인 경우
                    if prison_map[nx][ny] == '#':
                        dist[nx][ny] = dist[x][y] + 1  # 문의 개수를 증가시키며 이동
                        queue.append((nx, ny))  # 다음 위치를 큐에 추가
                    else:
                        dist[nx][ny] = dist[x][y]  # 문이 아니면 동일한 거리로 이동
                        queue.appendleft((nx, ny))  # 큐의 앞에 추가해 우선적으로 처리

    return dist  # 시작점으로부터 각 위치까지의 최소 거리를 반환

def solve(prison_map, h, w):
    prisoners = []  # 죄수들의 위치를 저장할 리스트
    # 감옥 평면도 전체를 탐색하며 죄수들의 위치를 찾음
    for i in range(h + 2):
        for j in range(w + 2):
            if prison_map[i][j] == '$':
                prisoners.append((i, j))  # 죄수의 위치를 리스트에 추가
    
    # 감옥 밖에서 시작하는 BFS를 수행하여 거리 계산
    dist1 = bfs((0, 0), prison_map, h, w)
    # 첫 번째 죄수 위치에서 시작하는 BFS를 수행하여 거리 계산
    dist2 = bfs(prisoners[0], prison_map, h, w)
    # 두 번째 죄수 위치에서 시작하는 BFS를 수행하여 거리 계산
    dist3 = bfs(prisoners[1], prison_map, h, w)

    result = float('inf')  # 최솟값을 저장하기 위해 초기값을 무한대로 설정

    # 감옥 전체를 탐색하면서 모든 위치에서의 문의 개수를 계산
    for i in range(h + 2):
        for j in range(w + 2):
            if prison_map[i][j] != '*':
                total_cost = dist1[i][j] + dist2[i][j] + dist3[i][j]  # 세 경로의 합산 값을 계산
                if prison_map[i][j] == '#':
                    total_cost -= 2  # 문이 겹치는 경우 중복 비용 제거
                result = min(result, total_cost)  # 최소값을 업데이트

    return result  # 최종적으로 계산된 최소 문의 개수를 반환

def main():
    T = int(input())  # 테스트 케이스의 개수를 입력받음
    results = []  # 결과를 저장할 리스트
    for _ in range(T):
        h, w = map(int, input().split())  # 감옥의 높이와 너비를 입력받음
        prison_map = ['.' * (w + 2)]  # 맵의 테두리를 .으로 초기화하여 외부를 표시
        for _ in range(h):
            prison_map.append('.' + input() + '.')  # 맵의 각 줄을 입력받아 양 옆에 .을 추가
        prison_map.append('.' * (w + 2))  # 맵의 테두리를 .으로 초기화하여 외부를 표시

        result = solve(prison_map, h, w)  # 주어진 맵에 대해 최소 문의 개수를 계산
        results.append(result)  # 결과를 리스트에 추가
    
    for result in results:
        print(result)  # 각 테스트 케이스의 결과를 출력

if __name__ == "__main__":
    main()  # 프로그램의 진입점