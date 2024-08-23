import sys
# 재귀 호출의 최대 깊이를 설정합니다. 트리의 최대 크기가 크기 때문에 재귀 호출의 깊이를 넉넉히 설정합니다.
sys.setrecursionlimit(200000)

# 표준 입력을 읽어옵니다.
input = sys.stdin.read
# 입력 데이터를 공백을 기준으로 분리하여 리스트로 만듭니다.
data = input().split()

# 첫 번째 입력: 트리의 정점의 수 N, 루트의 번호 R, 쿼리의 수 Q
N = int(data[0])
R = int(data[1])
Q = int(data[2])

from collections import defaultdict, deque

# 트리를 표현할 그래프를 만듭니다. defaultdict(list)를 사용하여 기본값을 빈 리스트로 설정합니다.
graph = defaultdict(list)

# 입력 데이터의 인덱스를 설정합니다. (현재 3번째 데이터부터 읽기 시작)
index = 3
# N-1개의 간선 정보를 읽어들입니다.
for _ in range(N - 1):
    U = int(data[index])
    V = int(data[index + 1])
    # U와 V 사이에 간선을 추가합니다.
    graph[U].append(V)
    graph[V].append(U)
    # 인덱스를 2 증가시켜 다음 간선 정보를 읽어들일 준비를 합니다.
    index += 2

# 각 노드의 서브트리 크기를 저장할 배열을 만듭니다. 초기값은 모두 0입니다.
subtree_size = [0] * (N + 1)

# DFS(깊이 우선 탐색)를 정의합니다.
def dfs(node, parent):
    # 현재 노드의 서브트리 크기를 1로 시작합니다. (자기 자신)
    size = 1
    # 현재 노드의 모든 인접 노드를 확인합니다.
    for neighbor in graph[node]:
        # 인접 노드가 부모 노드가 아니면 탐색을 계속합니다.
        if neighbor != parent:
            # 자식 노드의 서브트리 크기를 더합니다.
            size += dfs(neighbor, node)
    # 서브트리 크기를 저장합니다.
    subtree_size[node] = size
    return size

# 루트 노드 R에서 DFS를 시작합니다. 부모 노드는 -1로 설정합니다.
dfs(R, -1)

# 쿼리를 처리합니다.
results = []
for _ in range(Q):
    U = int(data[index])
    # 쿼리 노드 U의 서브트리 크기를 결과에 추가합니다.
    results.append(str(subtree_size[U]))
    index += 1

# 결과를 출력합니다. 각 결과를 줄바꿈으로 구분합니다.
print("\n".join(results))
