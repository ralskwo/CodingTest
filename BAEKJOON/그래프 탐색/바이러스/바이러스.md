## 바이러스 문제 풀이 과정

### 문제 이해

주어진 문제는 네트워크 상에서 1번 컴퓨터가 바이러스에 감염되었을 때, 바이러스가 퍼질 수 있는 모든 컴퓨터의 수를 찾는 것입니다. 컴퓨터들은 네트워크로 연결되어 있으며, 연결된 컴퓨터는 상호 간에 바이러스가 전파될 수 있습니다. 

### 접근 방식

이 문제는 그래프 탐색 문제로, DFS(깊이 우선 탐색) 또는 BFS(너비 우선 탐색)를 사용하여 해결할 수 있습니다. 감염된 컴퓨터를 시작점으로 하여 연결된 모든 컴퓨터를 탐색하여 감염된 컴퓨터의 수를 세면 됩니다.

### 풀이 과정

1. **입력 받기**: 컴퓨터의 수와 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수를 입력받습니다.
2. **그래프 초기화**: 각 컴퓨터를 정점으로 하는 그래프를 초기화하고, 연결 정보를 입력받아 그래프를 구성합니다.
3. **BFS 또는 DFS 수행**: 1번 컴퓨터를 시작점으로 BFS 또는 DFS를 수행하여 감염될 수 있는 모든 컴퓨터를 탐색합니다.
4. **결과 출력**: 1번 컴퓨터를 제외한 나머지 감염된 컴퓨터의 수를 출력합니다.

### 상세 풀이

1. **입력 데이터 처리**:
    - 첫 줄에 컴퓨터의 수 \( N \)과 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 \( M \)을 입력받습니다.
    - \( M \)개의 줄에 걸쳐 네트워크 연결 정보를 입력받아 그래프를 구성합니다.

2. **BFS 또는 DFS 구현**:
    - BFS를 사용하여 1번 컴퓨터와 연결된 모든 컴퓨터를 탐색합니다.
    - 방문한 컴퓨터를 체크하여 중복 탐색을 방지합니다.

3. **탐색 과정**:
    - 큐에서 현재 컴퓨터를 꺼내 연결된 컴퓨터를 탐색하고, 방문하지 않은 컴퓨터를 큐에 추가합니다.
    - 감염된 컴퓨터의 수를 카운트합니다.

4. **결과 출력**:
    - 1번 컴퓨터를 제외한 나머지 감염된 컴퓨터의 수를 출력합니다.

### 코드 설명

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# 입력 받기
n = int(input().strip())  # 컴퓨터의 수
m = int(input().strip())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# 그래프 초기화
graph = {i: [] for i in range(1, n + 1)}

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS를 통해 1번 컴퓨터와 연결된 모든 컴퓨터를 찾기
infected_computers = bfs(graph, 1)

# 1번 컴퓨터 제외
infected_computers.remove(1)

# 결과 출력
print(len(infected_computers))
