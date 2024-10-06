import heapq  # 힙 큐를 사용하기 위해 heapq 모듈을 임포트
import sys    # 표준 입력을 사용하기 위해 sys 모듈을 임포트

input = sys.stdin.read  # 표준 입력을 read() 방식으로 입력 받기
INF = float('inf')      # 무한대를 표현하기 위해 float('inf') 사용

# 입력을 공백을 기준으로 나눠서 리스트로 변환
data = input().split()
index = 0  # 데이터 인덱스를 추적하기 위한 변수

# 첫 번째 줄의 N (분기점의 수)와 M (길의 수)를 정수로 변환하여 저장
N = int(data[index])
M = int(data[index + 1])
index += 2  # 두 값(N, M)을 사용했으므로 인덱스를 2 증가

# 두 번째 줄에 주어진 N개의 정수를 정수 리스트로 변환하여 시야 정보 저장
sight = list(map(int, data[index:index + N]))
index += N  # N개의 시야 정보를 사용했으므로 인덱스를 N만큼 증가

# 각 분기점에 대해 연결된 분기점을 저장할 인접 리스트 생성
graph = [[] for _ in range(N)]

# M개의 간선 정보를 입력 받아 그래프를 구성
for _ in range(M):
    u = int(data[index])      # 시작 분기점 u
    v = int(data[index + 1])  # 도착 분기점 v
    t = int(data[index + 2])  # 두 분기점을 잇는 데 걸리는 시간 t
    index += 3                # 세 값(u, v, t)을 사용했으므로 인덱스를 3 증가

    # 두 분기점 모두 상대 시야에 보이지 않는 경우, 양방향 간선을 그래프에 추가
    if sight[u] == 0 and sight[v] == 0:
        graph[u].append((v, t))
        graph[v].append((u, t))
    # u 분기점이 상대 시야에 보이지 않고 v 분기점이 상대 넥서스인 경우, u에서 v로 가는 간선 추가
    elif sight[u] == 0 and v == N - 1:
        graph[u].append((v, t))
    # v 분기점이 상대 시야에 보이지 않고 u 분기점이 상대 넥서스인 경우, v에서 u로 가는 간선 추가
    elif sight[v] == 0 and u == N - 1:
        graph[v].append((u, t))

# 다익스트라 알고리즘을 통해 최단 경로를 계산하는 함수 정의
def dijkstra(start):
    distances = [INF] * N  # 각 분기점까지의 최단 거리를 무한대로 초기화
    distances[start] = 0   # 시작 분기점의 최단 거리는 0으로 설정
    queue = [(0, start)]   # 시작 분기점을 큐에 추가 (거리, 분기점)

    while queue:
        # 큐에서 최단 거리의 분기점을 꺼내기
        current_distance, current_node = heapq.heappop(queue)

        # 이미 더 짧은 경로가 있는 경우 무시
        if current_distance > distances[current_node]:
            continue

        # 현재 분기점에서 연결된 다른 분기점들을 확인
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # 현재까지 거리 + 이동 거리

            # 새로 계산한 거리가 기존 거리보다 짧은 경우 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # 큐에 새 거리와 분기점 추가

    return distances  # 모든 분기점에 대한 최단 거리를 반환

# 시작 분기점(0)에서 상대 넥서스(N-1)까지의 최단 경로를 계산
result = dijkstra(0)

# 상대 넥서스(N-1)까지의 최단 거리를 출력
# 만약 도달할 수 없으면, -1을 출력
print(result[N-1] if result[N-1] != INF else -1)
