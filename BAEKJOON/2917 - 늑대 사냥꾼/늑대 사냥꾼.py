import sys
import heapq
from collections import deque

# 입력을 더 빠르게 받기 위해 sys.stdin.readline을 사용
input = sys.stdin.readline


def find_positions(forest, N, M):
    # 늑대와 나무의 위치를 찾는 함수
    wolf_position = None
    tree_positions = []
    for i in range(N):
        for j in range(M):
            if forest[i][j] == "V":
                # 늑대의 위치를 저장
                wolf_position = (i, j)
            elif forest[i][j] == "+":
                # 나무의 위치를 리스트에 추가
                tree_positions.append((i, j))
    return wolf_position, tree_positions


def calculate_tree_distances_optimized(forest, N, M, tree_positions):
    # 각 칸에서 가장 가까운 나무까지의 거리를 계산하는 함수
    tree_distances = [[float("inf")] * M for _ in range(N)]
    queue = deque(tree_positions)

    for x, y in tree_positions:
        # 나무가 있는 위치의 거리를 0으로 초기화
        tree_distances[x][y] = 0

    while queue:
        # BFS를 사용하여 각 칸까지의 최소 거리를 계산
        x, y = queue.popleft()
        current_distance = tree_distances[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 상하좌우 네 방향을 확인
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 새로운 위치가 더 가까운 경우 거리를 업데이트하고 큐에 추가
                if tree_distances[nx][ny] > current_distance + 1:
                    tree_distances[nx][ny] = current_distance + 1
                    queue.append((nx, ny))

    return tree_distances


def find_safest_path_optimized(forest, N, M, wolf_position, tree_distances):
    # 가장 안전한 경로를 찾는 함수
    start_x, start_y = wolf_position
    pq = []
    # 우선순위 큐에 시작 위치 추가 (거리의 음수, x좌표, y좌표)
    heapq.heappush(pq, (-tree_distances[start_x][start_y], start_x, start_y))
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True

    while pq:
        # 가장 안전한 경로를 우선적으로 탐색
        min_dist, x, y = heapq.heappop(pq)
        min_dist = -min_dist  # 원래 거리로 변환

        if forest[x][y] == "J":
            # 오두막에 도착하면 최소 안전 거리 반환
            return min_dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 상하좌우 네 방향을 확인
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 새로운 위치가 유효하고 방문하지 않았다면
                visited[nx][ny] = True
                # 현재까지의 최소 거리와 새 위치의 나무까지의 거리 중 작은 값 선택
                new_min_dist = min(min_dist, tree_distances[nx][ny])
                # 우선순위 큐에 새 위치 추가
                heapq.heappush(pq, (-new_min_dist, nx, ny))

    return -1  # 오두막에 도달할 수 없는 경우


def solve():
    # 메인 솔루션 함수
    N, M = map(int, input().split())  # 숲의 크기 입력
    forest = [list(input().strip()) for _ in range(N)]  # 숲의 지도 입력

    # 늑대와 나무의 위치 찾기
    wolf_position, tree_positions = find_positions(forest, N, M)
    # 각 위치에서 나무까지의 거리 계산
    tree_distances = calculate_tree_distances_optimized(forest, N, M, tree_positions)
    # 가장 안전한 경로 찾기
    result = find_safest_path_optimized(forest, N, M, wolf_position, tree_distances)

    print(result)  # 결과 출력


if __name__ == "__main__":
    solve()  # 프로그램 실행
