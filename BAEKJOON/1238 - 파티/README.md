# 파티 문제 풀이 및 설명

https://www.acmicpc.net/problem/1238

## 문제 이해
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있습니다. 이 학생들은 파티에 참석하기 위해 모여야 하며, 파티가 끝난 후 다시 각자의 마을로 돌아가야 합니다. 학생들이 파티에 참석하고 돌아가는 시간은 다 다를 수 있으며, 우리는 가장 오래 걸리는 학생의 소요 시간을 구해야 합니다.

## 접근 방식
1. **그래프 모델링**: 각 마을을 노드로, 도로를 엣지로 하는 그래프를 모델링합니다. 각 엣지는 단방향이고, 특정 소요 시간이 있습니다.
2. **다익스트라 알고리즘**: 시작점 `X`로부터 모든 마을로 가는 최단 거리를 계산합니다. 이를 위해 다익스트라 알고리즘을 사용합니다.
3. **소요 시간 계산**: 각 학생이 `X`로 가는 시간과 다시 돌아오는 시간을 계산합니다.
4. **최대 소요 시간**: 모든 학생들 중 가장 오래 걸리는 학생의 소요 시간을 출력합니다.

## 풀이 과정
1. **입력 처리**:
   - 첫 번째 줄에서 N, M, X를 입력받습니다.
   - 두 번째 줄부터 M개의 도로 정보를 입력받습니다.
2. **다익스트라 알고리즘**:
   - `X`에서 각 마을까지 가는 최단 거리를 계산합니다.
   - 각 마을에서 `X`로 돌아오는 최단 거리를 계산합니다.
3. **최대 소요 시간 계산**:
   - 각 학생의 왕복 시간을 계산하여 가장 큰 값을 찾습니다.

## 코드
```python
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
```