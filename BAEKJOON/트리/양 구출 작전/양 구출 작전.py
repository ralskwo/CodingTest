import sys
sys.setrecursionlimit(10**6)  # 재귀 한도를 늘림
input = sys.stdin.read

def dfs(node):
    total_sheep = 0  # 현재 노드에서 시작해 구출한 양의 수

    # 현재 노드에서의 양과 늑대 수를 누적
    if animals[node][0] == 'S':
        total_sheep += animals[node][1]  # 현재 노드에 양이 있으면 양의 수 누적
    elif animals[node][0] == 'W':
        total_sheep -= animals[node][1]  # 현재 노드에 늑대가 있으면 늑대 수를 양의 수에서 뺌

    # 자식 노드 방문
    for next_node in graph[node]:
        total_sheep += dfs(next_node)  # 자식 노드의 반환 값을 현재 노드에 누적

    # 양이 음수가 되지 않도록 조정
    return max(total_sheep, 0)

# 입력 처리
data = input().strip().split()
n = int(data[0])

# 각 섬의 동물 정보와 그래프 초기화
animals = [None] * (n + 1)
graph = [[] for _ in range(n + 1)]

index = 1
for i in range(2, n + 1):
    a = data[index]
    p = int(data[index + 1])
    parent = int(data[index + 2])
    animals[i] = (a, p)
    graph[parent].append(i)
    index += 3

# 초기 상태 설정 (1번 섬에는 동물 없음)
animals[1] = ('S', 0)

# DFS를 통해 구출한 양의 수 계산 및 결과 출력
total_sheep = dfs(1)
print(total_sheep)
