import heapq  # 힙큐 모듈을 불러옴 (다익스트라 알고리즘에서 우선순위 큐로 사용할 것)

def shortest_path(N, D, shortcuts):
    dist = [float('inf')] * (D + 1)  # 고속도로의 길이 D까지의 거리를 저장하는 리스트, 처음에는 무한대로 설정
    dist[0] = 0  # 시작 위치(0)까지의 거리는 0으로 설정

    pq = []  # 우선순위 큐를 저장할 리스트
    heapq.heappush(pq, (0, 0))  # 시작점 (거리 0, 위치 0)을 우선순위 큐에 삽입

    while pq:  # 큐가 빌 때까지 반복
        current_dist, current_pos = heapq.heappop(pq)  # 큐에서 가장 짧은 거리를 가진 위치를 꺼냄

        if current_dist > dist[current_pos]:  # 만약 현재 거리가 이미 처리된 거리보다 크면 무시
            continue

        if current_pos + 1 <= D and dist[current_pos + 1] > current_dist + 1:
            dist[current_pos + 1] = current_dist + 1  # 직선으로 다음 위치까지 이동하는 경우
            heapq.heappush(pq, (dist[current_pos + 1], current_pos + 1))  # 갱신된 거리를 큐에 삽입

        for start, end, length in shortcuts:  # 지름길을 탐색
            if current_pos == start and end <= D and dist[end] > current_dist + length:
                dist[end] = current_dist + length  # 지름길을 통해 도착하는 경우 더 짧다면 갱신
                heapq.heappush(pq, (dist[end], end))  # 갱신된 거리를 큐에 삽입

    return dist[D]  # D 위치까지의 최소 거리를 반환

N, D = map(int, input().split())  # 지름길의 개수 N과 고속도로의 길이 D 입력
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]  # N개의 지름길 정보를 입력받아 리스트로 저장

print(shortest_path(N, D, shortcuts))  # 최단 경로를 계산한 후 출력