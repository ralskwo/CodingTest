# 백도어 문제 풀이 및 설명

<https://www.acmicpc.net/problem/17396>

<https://mayquartet.com/python-파이썬-백준-17396-백도어/>

## 문제 이해

이 문제는 그래프 이론과 최단 경로 탐색 문제입니다. 주어진 문제에서 유섭이는 특정 지점(상대의 넥서스)까지 가능한 최단 경로를 찾아야 합니다. 그러나 모든 경로를 탐색할 수는 없습니다. 유섭이는 적의 시야에 보이는 분기점을 지나갈 수 없으므로, 적의 시야에 걸리지 않는 경로를 찾아야 합니다. 이 문제의 핵심은 유효한 경로(적의 시야에 걸리지 않는 경로)만을 통해 상대 넥서스까지 갈 수 있는 최소 시간을 구하는 것입니다. 만약 상대 넥서스까지 도달할 수 없는 경우도 있으므로, 그 경우에는 -1을 출력해야 합니다.

이 문제를 해결하기 위해서는 그래프의 각 정점과 간선을 적절히 관리해야 하며, 시야에 대한 조건을 적용하여 유효한 경로만을 탐색하는 알고리즘을 구현해야 합니다.

## 입출력 조건

### 입력 조건

1. 첫 번째 줄에는 두 개의 정수 `N`과 `M`이 공백으로 구분되어 주어집니다. 여기서 `N`은 분기점의 수를, `M`은 분기점들 사이를 잇는 길의 수를 의미합니다. (`1 ≤ N ≤ 100,000`, `1 ≤ M ≤ 300,000`)
2. 두 번째 줄에는 `N`개의 정수 `a0, a1, ..., aN-1`가 공백으로 구분되어 주어집니다. 각 정수 `ai`는 해당 분기점이 상대 시야에 보이는지 여부를 나타냅니다.
   - `ai`가 `0`이면 해당 분기점이 상대의 시야에 보이지 않음을 의미합니다.
   - `ai`가 `1`이면 해당 분기점이 상대의 시야에 보임을 의미합니다.
   - 추가로, `a0 = 0`이며 `aN-1 = 1`입니다. 즉, 유섭이가 현재 위치한 `0`번 분기점은 시야에 걸리지 않으며, 상대 넥서스인 `N-1`번 분기점은 시야에 보이지만 예외적으로 갈 수 있습니다.
3. 이후 `M`개의 줄에는 세 개의 정수 `a, b, t`가 공백으로 구분되어 주어집니다. 이는 `a`번 분기점과 `b`번 분기점을 잇는 데 `t`만큼의 시간이 걸린다는 것을 의미합니다. `a`와 `b`는 서로 다른 분기점을 나타내며, 두 분기점을 잇는 길은 양방향입니다. (`0 ≤ a, b < N`, `a ≠ b`, `1 ≤ t ≤ 100,000`)

### 출력 조건

- 첫 번째 줄에 유섭이가 현재 위치(`0`번 분기점)에서 상대 넥서스(`N-1`번 분기점)까지 안 들키고 갈 수 있는 최소 시간을 출력합니다.
- 만약 상대 넥서스까지 도달할 수 없는 경우, `-1`을 출력합니다.

## 접근 방식

이 문제는 그래프 이론과 최단 경로 탐색을 이용하여 해결할 수 있습니다. 적의 시야에 걸리는 분기점들은 방문할 수 없기 때문에, 이러한 제약 조건을 고려하여 최단 경로를 찾아야 합니다. 문제 해결을 위한 접근 방식은 다음과 같습니다:

1. **그래프 초기화 및 입력 데이터 처리**:

   - 그래프의 각 분기점들을 노드로, 분기점 사이의 길을 간선으로 표현할 수 있습니다.
   - 모든 분기점과 간선 정보를 인접 리스트를 사용하여 그래프로 구성합니다.
   - 적의 시야에 보이는 분기점들(시야 정보가 `1`인 분기점)은 방문할 수 없으므로 해당 분기점으로 가는 길은 무시합니다. 단, 상대 넥서스(`N-1`번 분기점)는 예외적으로 방문이 가능합니다.

2. **최단 경로 탐색 알고리즘 선택**:

   - 이 문제는 가중치가 있는 그래프에서의 최단 경로를 구하는 문제이므로, `다익스트라 알고리즘`을 사용합니다.
   - 다익스트라 알고리즘은 시작점에서부터 각 노드(분기점)까지의 최단 거리를 우선순위 큐를 사용하여 효율적으로 탐색할 수 있습니다.
   - 다익스트라 알고리즘을 이용하여 `0`번 분기점에서 `N-1`번 분기점까지의 최단 경로를 구합니다.

3. **유효한 경로 판단**:

   - 다익스트라 알고리즘을 수행할 때, 적의 시야에 보이는 분기점은 방문하지 않도록 조건을 설정합니다.
   - `graph` 리스트에 간선 정보를 추가할 때, 적의 시야에 보이지 않는 분기점들만을 연결합니다.
   - 상대 넥서스(`N-1`번 분기점)는 시야에 보이지만 예외적으로 이동이 가능하므로 이 점을 고려하여 경로를 설정합니다.

4. **결과 출력**:
   - 다익스트라 알고리즘을 통해 구한 최단 거리 중 상대 넥서스(`N-1`번 분기점)까지의 최단 거리를 출력합니다.
   - 만약 `N-1`번 분기점까지의 최단 거리가 초기값(무한대)로 남아 있다면, 이는 도달할 수 없는 경우이므로 `-1`을 출력합니다.

<https://mayquartet.com/algorithm-dijkstra-다익스트라-알고리즘-이해하기/>

## 풀이 과정

1. **그래프와 입력 데이터 초기화**:

   - `graph` 리스트를 이용하여 인접 리스트 형태로 그래프를 초기화합니다.
   - `sight` 리스트를 사용하여 각 분기점의 시야 여부를 저장합니다.
   - `M`개의 간선 정보를 입력 받아 `graph` 리스트에 연결된 분기점 정보를 추가합니다.
   - 이때, 두 분기점 모두 시야에 걸리지 않거나, 한 분기점이 `N-1`번 분기점(상대 넥서스)인 경우에만 간선을 추가합니다.

2. **다익스트라 알고리즘을 통한 최단 경로 탐색**:

   - `distances` 리스트를 사용하여 시작점에서 각 분기점까지의 최단 거리를 저장합니다. 초기에는 모든 값을 `INF`로 설정하고, 시작점의 거리는 `0`으로 설정합니다.
   - 우선순위 큐를 사용하여 시작점에서부터 각 분기점을 탐색합니다. 이때 큐에는 `(거리, 분기점)` 형태로 저장하여, 현재 탐색 중인 분기점의 최단 거리를 기준으로 다음 분기점을 선택합니다.
   - 현재 분기점에서 인접한 다른 분기점들로 이동할 때, 새로 계산된 거리가 더 짧다면 `distances`를 갱신하고 큐에 추가합니다.

3. **상대 넥서스까지의 최단 거리 출력**:
   - 다익스트라 알고리즘을 수행한 후, 상대 넥서스(`N-1`번 분기점)까지의 최단 거리를 `distances[N-1]`에서 확인합니다.
   - 만약 `distances[N-1]`의 값이 `INF`라면, 이는 상대 넥서스까지 도달할 수 없는 경우이므로 `-1`을 출력합니다.
   - 그렇지 않다면 상대 넥서스까지의 최단 거리를 출력하여 문제의 답을 도출합니다.

## 코드 구현

```python
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
```
