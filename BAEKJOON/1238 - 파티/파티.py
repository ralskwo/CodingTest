import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 임포트
import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 사용

def dijkstra(start, n, graph):
    # 시작점에서 모든 노드까지의 최단 거리를 계산하는 함수
    distances = [INF] * (n + 1)  # 모든 거리 값을 무한으로 초기화
    distances[start] = 0  # 시작점의 거리는 0으로 설정
    priority_queue = [(0, start)]  # 우선순위 큐에 시작점을 삽입

    while priority_queue:
        # 우선순위 큐에서 가장 짧은 거리를 가진 노드 꺼내기
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue  # 이미 처리된 적 있는 노드라면 무시
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight  # 현재 노드를 거쳐서 인접 노드로 가는 거리 계산
            
            if distance < distances[adjacent]:  # 더 짧은 경로가 발견되면
                distances[adjacent] = distance  # 최단 거리 갱신
                heapq.heappush(priority_queue, (distance, adjacent))  # 우선순위 큐에 삽입
    
    return distances  # 시작점에서 각 노드까지의 최단 거리를 반환

# 입력 처리
N, M, X = map(int, input().split())  # N: 노드의 수, M: 간선의 수, X: 파티 장소

graph = [[] for _ in range(N + 1)]  # 일반 그래프 초기화
reverse_graph = [[] for _ in range(N + 1)]  # 역 그래프 초기화

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))  # 일반 그래프에 간선 정보 추가
    reverse_graph[end].append((start, time))  # 역 그래프에 간선 정보 추가

# X에서 각 마을로 가는 최단 거리
to_party = dijkstra(X, N, graph)

# 각 마을에서 X로 돌아오는 최단 거리
from_party = dijkstra(X, N, reverse_graph)

# 왕복 시간 계산 및 최대 값 찾기
max_time = 0
for i in range(1, N + 1):
    total_time = to_party[i] + from_party[i]
    if total_time > max_time:
        max_time = total_time

print(max_time)
