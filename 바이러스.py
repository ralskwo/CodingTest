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
