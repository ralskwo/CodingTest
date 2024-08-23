import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    # 거리 테이블을 무한대로 초기화
    distances = [INF] * (num_nodes + 1)
    priority_queue = []
    
    # 시작 노드 초기화
    heapq.heappush(priority_queue, (0, start))
    distances[start] = 0
    
    while priority_queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 적 있는 노드라면 무시
        if distances[current_node] < current_distance:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))
    
    return distances

# 테스트 케이스 수 입력
num_test_cases = int(input())
for _ in range(num_test_cases):
    # 교차로(노드) 수, 도로(엣지) 수, 목적지 후보 수 입력
    num_nodes, num_edges, num_dest_candidates = map(int, input().split())
    
    # 시작점, 특정 경로의 시작점(g), 끝점(h) 입력
    start_node, must_pass1, must_pass2 = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(num_nodes + 1)]
    dest_candidates = []

    # 도로 정보 입력
    for _ in range(num_edges):
        node1, node2, weight = map(int, input().split())
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    # 목적지 후보 입력
    for _ in range(num_dest_candidates):
        dest_candidates.append(int(input()))

    # 다익스트라 알고리즘을 통해 시작점, g, h로부터의 최단 거리 계산
    start_to_all = dijkstra(start_node)
    g_to_all = dijkstra(must_pass1)
    h_to_all = dijkstra(must_pass2)

    result = []
    for candidate in dest_candidates:
        # g-h 경로를 거쳐 목적지에 도달하는 두 가지 경우를 체크
        if (start_to_all[must_pass1] + g_to_all[must_pass2] + h_to_all[candidate] == start_to_all[candidate] or
            start_to_all[must_pass2] + h_to_all[must_pass1] + g_to_all[candidate] == start_to_all[candidate]):
            result.append(candidate)

    # 결과를 오름차순으로 정렬 후 출력
    result.sort()
    for r in result:
        print(r, end=' ')
    print()
