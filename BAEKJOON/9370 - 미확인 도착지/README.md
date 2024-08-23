# 미확인 도착지 문제 풀이 및 설명

https://www.acmicpc.net/problem/9370

## 문제 이해
주어진 문제는 여러 테스트 케이스가 주어지며, 각 테스트 케이스마다 출발점에서 특정 경로를 반드시 지나서 목적지 후보들까지의 최단 경로를 계산하는 것입니다. 여기서 반드시 지나야 하는 특정 경로는 `g`와 `h` 사이의 도로입니다.

## 접근 방식
1. **다익스트라 알고리즘**을 사용하여 출발점(`s`), `g`, `h`로부터 각각 다른 모든 노드까지의 최단 거리를 계산합니다.
2. 목적지 후보가 `s -> g -> h -> 목적지` 경로 또는 `s -> h -> g -> 목적지` 경로를 통해 최단 거리로 도달할 수 있는지 확인합니다.
3. 가능한 목적지 후보들을 오름차순으로 정렬하여 출력합니다.

## 풀이 과정
1. **입력 처리**:
   - 테스트 케이스의 수 `T`를 입력받습니다.
   - 각 테스트 케이스마다 교차로의 수 `n`, 도로의 수 `m`, 목적지 후보의 수 `t`, 출발점 `s`, 반드시 지나야 하는 두 점 `g`와 `h`를 입력받습니다.
   - 그래프 정보를 입력받아 `graph` 리스트에 저장합니다.
   - 목적지 후보들을 `dest_candidates` 리스트에 저장합니다.

2. **다익스트라 알고리즘**:
   - `dijkstra` 함수는 시작점에서 모든 노드까지의 최단 거리를 계산합니다. 이 함수는 우선순위 큐를 사용하여 최단 거리를 효율적으로 계산합니다.
   - 각 테스트 케이스마다 출발점 `s`, `g`, `h`로부터의 최단 거리를 각각 `start_to_all`, `g_to_all`, `h_to_all` 리스트에 저장합니다.

3. **경로 검사**:
   - 각 목적지 후보에 대해 `s -> g -> h -> 목적지` 경로와 `s -> h -> g -> 목적지` 경로의 최단 거리를 계산합니다.
   - 계산된 최단 거리와 실제 최단 거리가 일치하는지 확인하여 일치하는 경우 유효한 목적지 후보로 간주합니다.

4. **결과 출력**:
   - 유효한 목적지 후보들을 오름차순으로 정렬하여 출력합니다.

## 코드
```python
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

```