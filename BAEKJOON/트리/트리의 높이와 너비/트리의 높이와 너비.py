import sys

input = sys.stdin.readline

# 중위 순회 (In-Order Traversal)로 노드의 번호를 매긴다.
def in_order(v):
    global order

    if v:
        in_order(tree[v][0])  # 왼쪽 자식 방문
        tree[v][4] = order  # 현재 노드의 번호를 저장
        order += 1  # 다음 번호 증가
        in_order(tree[v][1])  # 오른쪽 자식 방문

# 깊이 우선 탐색 (DFS)로 트리의 깊이를 계산한다.
def dfs(cur, depth):
    global max_depth
    visited[cur] = True  # 현재 노드를 방문 처리
    tree[cur][3] = depth  # 현재 노드의 깊이를 저장
    if max_depth < depth:
        max_depth = depth  # 최대 깊이 갱신

    for i in range(2):  # 왼쪽, 오른쪽 자식 순회
        if not visited[tree[cur][i]]:
            dfs(tree[cur][i], depth + 1)  # 자식을 방문하며 깊이를 1 증가

N = int(input())  # 노드의 개수를 입력받음

tree = [[0, 0, 0, 0, 0] for i in range(N + 1)]  # 트리 초기화: 왼쪽 자식, 오른쪽 자식, 부모, 깊이, 너비
for _ in range(N):
    node, left, right = map(int, input().split())

    if left == -1: left = 0  # 자식이 없으면 0으로 설정
    if right == -1: right = 0

    tree[node][0] = left  # 왼쪽 자식 설정
    tree[node][1] = right  # 오른쪽 자식 설정

    tree[left][2] = node  # 왼쪽 자식의 부모 설정
    tree[right][2] = node  # 오른쪽 자식의 부모 설정

visited = [False] * (N + 1)  # 방문 배열 초기화
visited[0] = True  # 0번 노드는 사용하지 않음

# 루트 노드 찾기
root = 0
for i in range(1, N + 1):
    if tree[i][2] == 0:
        root = i

# 트리의 최대 깊이 찾기
max_depth = 0
dfs(root, 1)  # 루트 노드부터 깊이 우선 탐색 시작
order = 1  # 중위 순회에서 사용할 번호 초기화
in_order(root)  # 루트 노드부터 중위 순회 시작

# 각 깊이별로 너비를 계산하기 위해 리스트 초기화
depth_list = [[] for _ in range(max_depth + 1)]
for j in range(1, N + 1):
    depth_list[tree[j][3]].append(tree[j][4])  # 각 깊이별로 너비 저장

result = []
# 깊이별 너비 계산
for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:  # 해당 깊이에 노드가 하나만 있으면 너비는 1
        result.append(1)
    else:  # 노드가 여러 개 있으면
        result.append(max(depth_list[i]) - min(depth_list[i]) + 1)  # 가장 큰 너비 - 가장 작은 너비 + 1

# 최대 너비를 가지는 깊이를 찾음
print(result.index(max(result), 1), max(result))
