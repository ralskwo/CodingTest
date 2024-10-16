from collections import deque  # BFS 탐색을 위한 deque 모듈을 임포트

def bfs(start, graph, n):  # BFS 탐색을 수행하는 함수 정의
    visited = [False] * (n + 1)  # 방문 여부를 기록할 리스트, n명의 동기들에 대해 False로 초기화
    distance = [-1] * (n + 1)  # 상근이로부터의 거리를 기록할 리스트, -1로 초기화
    queue = deque([start])  # BFS 탐색을 위한 큐, 상근이의 학번인 1을 시작점으로 설정
    
    visited[start] = True  # 상근이의 학번을 방문 처리
    distance[start] = 0  # 상근이의 거리는 0으로 설정
    
    while queue:  # 큐가 빌 때까지 BFS 탐색을 진행
        current = queue.popleft()  # 큐에서 현재 노드를 꺼내옴
        
        for neighbor in graph[current]:  # 현재 노드에 연결된 친구들을 확인
            if not visited[neighbor]:  # 방문하지 않은 친구라면
                visited[neighbor] = True  # 방문 처리
                distance[neighbor] = distance[current] + 1  # 친구의 거리는 현재 노드의 거리 + 1
                queue.append(neighbor)  # 친구를 큐에 추가
    
    invite_count = 0  # 초대할 친구의 수를 세는 변수 초기화
    for i in range(2, n + 1):  # 상근이(1번 학번) 이외의 친구들에 대해
        if 0 < distance[i] <= 2:  # 상근이로부터의 거리가 1 또는 2인 경우
            invite_count += 1  # 초대할 수 있는 친구로 카운트
    
    return invite_count  # 초대할 친구 수 반환

n = int(input())  # 동기들의 수 입력받기
m = int(input())  # 친구 관계의 수 입력받기

graph = [[] for _ in range(n + 1)]  # 각 동기의 친구 관계를 저장할 그래프 생성 (1부터 n까지)

for _ in range(m):  # 주어진 친구 관계 수만큼 반복
    a, b = map(int, input().split())  # 각 친구 관계를 입력받기
    graph[a].append(b)  # a와 b는 친구 관계이므로 a에 b를 추가
    graph[b].append(a)  # b와 a도 친구 관계이므로 b에 a를 추가

result = bfs(1, graph, n)  # 상근이(1번 학번)에서 BFS 탐색 시작
print(result)  # 결혼식에 초대할 친구 수 출력