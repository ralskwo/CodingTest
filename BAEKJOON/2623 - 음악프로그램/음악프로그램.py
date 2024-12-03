from collections import deque  # deque를 사용하기 위해 collections 모듈을 불러옴

# 가수의 수 N과 보조 PD의 수 M 입력
n, m = map(int, input().split())

# 그래프와 진입 차수를 초기화
graph = {
    i: [] for i in range(1, n + 1)
}  # 각 가수를 키로, 빈 리스트를 값으로 가지는 그래프 생성
indegree = {i: 0 for i in range(1, n + 1)}  # 각 가수의 진입 차수를 0으로 초기화

# 보조 PD가 정한 가수의 순서를 입력받아 그래프와 진입 차수를 설정
for _ in range(m):
    data = list(map(int, input().split()))  # 보조 PD가 입력한 순서를 리스트로 변환
    for i in range(2, len(data)):  # 각 순서의 가수를 그래프에 간선으로 추가
        graph[data[i - 1]].append(data[i])  # 이전 가수에서 현재 가수로 향하는 간선 추가
        indegree[data[i]] += 1  # 현재 가수의 진입 차수를 1 증가


# 위상 정렬 알고리즘 정의
def topological_sort():
    queue = deque()  # 진입 차수가 0인 노드를 처리하기 위한 큐 생성
    result = []  # 최종 결과를 저장할 리스트

    # 모든 노드 중 진입 차수가 0인 노드를 큐에 추가
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐를 이용하여 위상 정렬 수행
    while queue:
        current = queue.popleft()  # 큐에서 하나의 노드를 꺼냄
        result.append(current)  # 꺼낸 노드를 결과 리스트에 추가

        # 현재 노드와 연결된 모든 노드에 대해 진입 차수를 감소
        for neighbor in graph[current]:
            indegree[neighbor] -= 1  # 진입 차수 감소
            if indegree[neighbor] == 0:  # 진입 차수가 0이 된 노드를 큐에 추가
                queue.append(neighbor)

    # 정렬된 노드 개수가 전체 노드 수와 다르면 사이클이 존재하므로 불가능
    if len(result) != n:
        return [0]  # 순서가 불가능하므로 0을 반환
    return result  # 정렬된 결과를 반환


# 위상 정렬 결과를 실행하고 출력
result = topological_sort()
for r in result:
    print(r)  # 결과를 한 줄씩 출력
