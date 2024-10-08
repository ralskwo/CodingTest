# 거의 최단 경로 문제 풀이 및 설명

https://www.acmicpc.net/problem/5719

## **문제 이해**
이 문제는 GPS 네비게이션 시스템이 사용자의 출발지와 도착지 사이의 최단 경로를 계산하는 상황을 다룹니다. 그러나 이 네비게이션 시스템은 항상 최단 경로만 찾지 않고 거의 최단 경로도 찾습니다. '거의 최단 경로'란 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 경로를 의미합니다. 예를 들어, 도로 네트워크에서 최단 경로가 여러 개일 수 있지만, 그 중에서 최단 경로에 포함되지 않은 경로를 찾아야 합니다. 이 문제는 최단 경로를 찾는 것뿐만 아니라, 최단 경로를 제거한 후 거의 최단 경로를 찾는 두 단계의 작업을 요구합니다.

## **입출력 조건**
### 입력
- 입력은 여러 개의 테스트 케이스로 이루어져 있습니다.
- 각 테스트 케이스의 첫 번째 줄에는 장소의 수 \(N\) (2 ≤ \(N\) ≤ 500)과 도로의 수 \(M\) (1 ≤ \(M\) ≤ 10,000)이 주어집니다.
- 두 번째 줄에는 시작점 \(S\)와 도착점 \(D\)가 주어집니다. (\(S ≤ D\), \(0 ≤ S, D < N\))
- 다음 \(M\)개의 줄에는 도로의 정보 \(U, V, P\)가 주어집니다. (\(U ≤ V\), \(0 ≤ U, V < N\), \(1 ≤ P ≤ 10^3\))
- \(U\)에서 \(V\)로 가는 도로는 최대 한 개이며, \(U\)에서 \(V\)로 가는 도로와 \(V\)에서 \(U\)로 가는 도로는 다른 도로입니다.
- 입력의 마지막 줄에는 "0 0"이 주어집니다.

### 출력
- 각 테스트 케이스에 대해, 거의 최단 경로의 길이를 출력합니다.
- 만약, 거의 최단 경로가 없는 경우에는 -1을 출력합니다.

## **접근 방식**
이 문제는 그래프 이론에서 최단 경로를 찾는 알고리즘을 이해하고 응용해야 합니다. 기본적으로 다익스트라 알고리즘을 사용하여 최단 경로를 찾은 후, 최단 경로에 포함된 간선을 제거하고 다시 다익스트라 알고리즘을 사용하여 거의 최단 경로를 찾는 방식으로 접근할 수 있습니다. 
1. 다익스트라 알고리즘을 사용하여 시작점에서 도착점까지의 최단 경로를 찾습니다.
2. 최단 경로에 포함된 간선을 제거합니다.
3. 간선이 제거된 그래프에서 다시 다익스트라 알고리즘을 사용하여 거의 최단 경로를 찾습니다.

## **풀이 과정**
1. **그래프 초기화 및 입력 처리**:
    - 입력 데이터를 읽어와 그래프와 역 그래프를 초기화합니다. 역 그래프는 간선을 반대로 저장하여 최단 경로 추적에 사용됩니다.
    
2. **최단 경로 찾기**:
    - 다익스트라 알고리즘을 사용하여 시작점에서 모든 노드까지의 최단 거리를 계산합니다.
    - 이때, 도착점까지의 최단 거리도 저장합니다.

3. **최단 경로 간선 제거**:
    - 역 그래프를 사용하여 도착점에서 시작점으로 역추적하며 최단 경로에 포함된 간선을 찾습니다.
    - 찾은 간선을 원래 그래프에서 제거합니다.
    
4. **거의 최단 경로 찾기**:
    - 간선이 제거된 그래프에서 다시 다익스트라 알고리즘을 사용하여 시작점에서 모든 노드까지의 최단 거리를 계산합니다.
    - 이때, 도착점까지의 새로운 최단 거리를 저장합니다.
    - 새로운 최단 거리가 무한대이면, 거의 최단 경로가 없는 것이므로 -1을 출력합니다.

5. **결과 출력**:
    - 각 테스트 케이스의 결과를 출력합니다.

## 코드 구현
```python
import heapq
import sys

input = sys.stdin.read  # 표준 입력을 한 번에 읽어오는 input 함수를 정의합니다.

def dijkstra(graph, start, n):
    distances = [float('inf')] * n  # 모든 노드에 대한 거리 값을 무한대로 초기화합니다.
    distances[start] = 0  # 시작점의 거리는 0으로 설정합니다.
    priority_queue = [(0, start)]  # 우선순위 큐에 시작점을 추가합니다.
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # 우선순위 큐에서 가장 작은 값을 가진 노드를 꺼냅니다.
        
        if current_distance > distances[current_node]:  # 현재 노드의 거리가 기록된 거리보다 크면 건너뜁니다.
            continue
        
        for adjacent, weight in graph[current_node]:  # 현재 노드에 인접한 모든 노드를 확인합니다.
            distance = current_distance + weight  # 현재 노드를 거쳐서 가는 거리를 계산합니다.
            
            if distance < distances[adjacent]:  # 새로운 거리가 기존 거리보다 작으면 업데이트합니다.
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))  # 우선순위 큐에 새로운 거리를 추가합니다.
                
    return distances  # 모든 노드에 대한 최단 거리를 반환합니다.

def remove_shortest_paths(graph, reverse_graph, shortest_distances, D):
    queue = [D]  # 도착점에서 시작하는 큐를 초기화합니다.
    removed_edges = set()  # 제거된 간선을 추적하기 위한 집합을 초기화합니다.
    
    while queue:
        node = queue.pop()  # 큐에서 노드를 꺼냅니다.
        for prev, weight in reverse_graph[node]:  # 현재 노드로 들어오는 모든 간선을 확인합니다.
            if shortest_distances[prev] + weight == shortest_distances[node]:  # 최단 경로에 포함되는 간선인지 확인합니다.
                if (prev, node) not in removed_edges:  # 이미 제거된 간선이 아니면 제거합니다.
                    graph[prev].remove((node, weight))  # 그래프에서 간선을 제거합니다.
                    removed_edges.add((prev, node))  # 제거된 간선을 집합에 추가합니다.
                    queue.append(prev)  # 이전 노드를 큐에 추가하여 계속 탐색합니다.
                    
def almost_shortest_path():
    input_data = input()  # 입력 데이터를 한 번에 읽어옵니다.
    results = []  # 결과를 저장할 리스트를 초기화합니다.
    data = input_data.split()  # 입력 데이터를 공백 기준으로 나눕니다.
    index = 0  # 데이터 인덱스를 초기화합니다.
    
    while True:
        N = int(data[index])  # 장소의 수를 읽어옵니다.
        M = int(data[index+1])  # 도로의 수를 읽어옵니다.
        
        if N == 0 and M == 0:  # 입력의 끝을 확인합니다.
            break
        
        index += 2
        S = int(data[index])  # 시작점을 읽어옵니다.
        D = int(data[index+1])  # 도착점을 읽어옵니다.
        index += 2
        
        graph = [[] for _ in range(N)]  # 그래프를 초기화합니다.
        reverse_graph = [[] for _ in range(N)]  # 역 그래프를 초기화합니다.
        
        for _ in range(M):
            U = int(data[index])  # 도로의 시작점을 읽어옵니다.
            V = int(data[index+1])  # 도로의 끝점을 읽어옵니다.
            P = int(data[index+2])  # 도로의 가중치를 읽어옵니다.
            index += 3
            
            graph[U].append((V, P))  # 그래프에 간선을 추가합니다.
            reverse_graph[V].append((U, P))  # 역 그래프에 간선을 추가합니다.
        
        shortest_distances = dijkstra(graph, S, N)  # 다익스트라 알고리즘으로 최단 거리를 계산합니다.
        shortest_distance = shortest_distances[D]  # 도착점까지의 최단 거리를 저장합니다.
        
        if shortest_distance == float('inf'):  # 최단 거리가 무한대이면 도달할 수 없는 경우입니다.
            results.append(-1)  # -1을 결과에 추가합니다.
            continue
        
        remove_shortest_paths(graph, reverse_graph, shortest_distances, D)  # 최단 경로에 포함된 간선을 제거합니다.
        
        new_distances = dijkstra(graph, S, N)  # 다시 다익스트라 알고리즘을 사용하여 새로운 최단 거리를 계산합니다.
        new_distance = new_distances[D]  # 새로운 도착점까지의 거리를 저장합니다.
        
        if new_distance == float('inf'):  # 새로운 최단 거리가 무한대이면 거의 최단 경로가 없는 경우입니다.
            results.append(-1)  # -1을 결과에 추가합니다.
        else:
            results.append(new_distance)  # 거의 최단 경로의 거리를 결과에 추가합니다.
    
    for result in results:  # 모든 결과를 출력합니다.
        print(result)

almost_shortest_path()  # 거의 최단 경로를 찾는 함수를 호출합니다.
