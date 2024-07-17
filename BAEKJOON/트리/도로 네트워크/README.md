# 도로 네트워크 문제 풀이 및 설명 

https://www.acmicpc.net/problem/3176

## 문제 이해

주어진 문제는 여러 도시와 그 도시를 연결하는 도로 네트워크에서 두 도시를 연결하는 경로 중 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 찾는 것입니다. 입력으로는 도시와 도로 정보가 주어지며, 우리는 특정 두 도시를 연결하는 경로의 도로 길이를 계산해야 합니다.

### 입력 형식

1. 첫 번째 줄에 도시의 수 \(N\)과 경로의 수 \(M\)이 주어집니다. (2 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000)
2. 다음 \(M\)개의 줄에는 각 도로를 나타내는 세 개의 정수 \(A\), \(B\), \(C\)가 주어집니다. \(A\)와 \(B\)는 도시를 나타내고 \(C\)는 그 도로의 길이를 나타냅니다.
3. 그 다음 줄에는 경로의 수 \(K\)가 주어집니다. (1 ≤ K ≤ 100,000)
4. 다음 \(K\)개의 줄에는 두 도시 \(D\)와 \(E\)가 주어집니다. 우리는 이 두 도시를 연결하는 경로에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 구해야 합니다.

### 출력 형식

각 경로에 대해 \(D\)와 \(E\)를 연결하는 경로에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 출력합니다.

## 접근 방식

이 문제는 트리 구조를 활용하기 때문에, 트리에서 두 노드 사이의 경로를 찾고 그 경로에서의 최소 및 최대 간선 길이를 찾는 것이 핵심입니다. 이를 위해서 다음과 같은 접근 방식을 사용할 수 있습니다:

1. **깊이 우선 탐색(DFS)**: 트리를 탐색하여 각 노드의 깊이와 부모 노드를 기록합니다. 또한 각 노드로부터 부모 노드까지의 최소 및 최대 간선 길이를 기록합니다.
2. **Binary Lifting**: 트리의 두 노드 사이의 최소 공통 조상(LCA)를 효율적으로 찾기 위해 2의 제곱 형태로 부모 노드를 저장합니다. 이를 통해 LCA를 O(log N) 시간에 찾을 수 있습니다.
3. **LCA를 이용한 경로 탐색**: 두 노드의 LCA를 찾은 후, LCA에서 두 노드까지의 경로를 탐색하며 최소 및 최대 간선 길이를 계산합니다.

이 접근 방식을 사용하면, 각 쿼리에 대해 효율적으로 답을 구할 수 있습니다.

## 풀이 과정

1. **그래프 입력 및 초기화**:
   - 입력된 도시와 도로 정보를 읽어 그래프를 인접 리스트 형태로 저장합니다.
   - DFS를 사용하여 각 노드의 깊이와 부모 노드를 기록하고, 각 노드에서 부모 노드까지의 최소 및 최대 간선 길이를 초기화합니다.

2. **DFS 탐색을 통한 초기화**:
   - `dfs` 함수를 사용하여 각 노드를 탐색하며 깊이, 부모, 최소 및 최대 간선 길이를 설정합니다.
   - 초기화된 깊이와 부모 정보를 바탕으로 Binary Lifting을 수행하여 2의 제곱 형태로 부모 노드를 설정합니다.

3. **Binary Lifting**:
   - 각 노드의 2^i번째 부모와 그 부모로 가는 최소 및 최대 간선 길이를 설정합니다.
   - 이를 통해 두 노드 사이의 최소 공통 조상을 효율적으로 찾을 수 있도록 준비합니다.

4. **LCA 및 경로 탐색**:
   - 주어진 두 노드의 깊이를 맞추기 위해 더 깊은 노드를 위로 이동시킵니다.
   - 두 노드의 깊이가 같아지면, 두 노드를 동시에 위로 이동시키며 최소 공통 조상을 찾습니다.
   - 이 과정에서 경로상의 최소 및 최대 간선 길이를 갱신합니다.

5. **쿼리 처리 및 결과 출력**:
   - 각 쿼리에 대해 두 노드의 LCA를 찾고, 그 경로에서의 최소 및 최대 간선 길이를 계산합니다.
   - 각 쿼리에 대한 결과를 출력합니다.

## 코드 구현
```python
import sys
import collections

# 표준 입력을 더 효율적으로 처리하기 위해 sys 모듈을 사용합니다.
input = sys.stdin.read
# 재귀 깊이 제한을 설정하여 트리 깊이가 깊은 경우에도 재귀가 문제없이 동작하도록 합니다.
sys.setrecursionlimit(100000)

def dfs(node, parent, depth, graph, depths, parents, min_edge, max_edge):
    # 현재 노드의 깊이를 기록합니다.
    depths[node] = depth
    # 현재 노드의 부모를 기록합니다.
    parents[node][0] = parent
    # 인접 노드를 탐색합니다.
    for neighbor, weight in graph[node]:
        if neighbor != parent:  # 부모 노드는 다시 방문하지 않습니다.
            min_edge[neighbor][0] = weight  # 인접 노드로 가는 도로의 길이를 최소 간선으로 기록합니다.
            max_edge[neighbor][0] = weight  # 인접 노드로 가는 도로의 길이를 최대 간선으로 기록합니다.
            dfs(neighbor, node, depth + 1, graph, depths, parents, min_edge, max_edge)  # 재귀적으로 탐색합니다.

def preprocess(N, graph):
    LOG = 17  # 노드의 최대 개수에 대한 로그 값으로, 2^17 > 100000이므로 17로 설정합니다.
    depths = [-1] * (N + 1)  # 각 노드의 깊이를 저장할 리스트입니다.
    parents = [[-1] * LOG for _ in range(N + 1)]  # 각 노드의 2^i번째 부모를 저장할 리스트입니다.
    min_edge = [[float('inf')] * LOG for _ in range(N + 1)]  # 각 노드의 2^i번째 부모로 가는 최소 도로 길이입니다.
    max_edge = [[-float('inf')] * LOG for _ in range(N + 1)]  # 각 노드의 2^i번째 부모로 가는 최대 도로 길이입니다.

    # 깊이 우선 탐색을 통해 깊이, 부모, 최소 및 최대 간선 길이를 초기화합니다.
    dfs(1, -1, 0, graph, depths, parents, min_edge, max_edge)

    # Binary lifting을 통해 각 노드의 2^i번째 부모를 계산합니다.
    for j in range(1, LOG):
        for i in range(1, N + 1):
            if parents[i][j-1] != -1:
                parents[i][j] = parents[parents[i][j-1]][j-1]
                min_edge[i][j] = min(min_edge[i][j-1], min_edge[parents[i][j-1]][j-1])
                max_edge[i][j] = max(max_edge[i][j-1], max_edge[parents[i][j-1]][j-1])

    return depths, parents, min_edge, max_edge

def lca(u, v, depths, parents, min_edge, max_edge):
    if depths[u] < depths[v]:
        u, v = v, u  # u가 더 깊도록 설정합니다.

    LOG = 17
    min_res = float('inf')
    max_res = -float('inf')

    # u와 v의 깊이를 동일하게 맞춥니다.
    for i in range(LOG-1, -1, -1):
        if depths[u] - (1 << i) >= depths[v]:
            min_res = min(min_res, min_edge[u][i])
            max_res = max(max_res, max_edge[u][i])
            u = parents[u][i]

    if u == v:
        return min_res, max_res

    # u와 v가 공통 조상이 될 때까지 부모를 따라 올라갑니다.
    for i in range(LOG-1, -1, -1):
        if parents[u][i] != -1 and parents[u][i] != parents[v][i]:
            min_res = min(min_res, min_edge[u][i], min_edge[v][i])
            max_res = max(max_res, max_edge[u][i], max_edge[v][i])
            u = parents[u][i]
            v = parents[v][i]

    min_res = min(min_res, min_edge[u][0], min_edge[v][0])
    max_res = max(max_res, max_edge[u][0], max_edge[v][0])

    return min_res, max_res

def main():
    input_data = input().split()  # 표준 입력을 한 번에 읽고 공백으로 분리합니다.
    index = 0

    N = int(input_data[index])
    index += 1

    graph = collections.defaultdict(list)  # 그래프를 인접 리스트로 표현합니다.
    for _ in range(N - 1):
        A = int(input_data[index])
        index += 1
        B = int(input_data[index])
        index += 1
        C = int(input_data[index])
        index += 1
        graph[A].append((B, C))  # 양방향 그래프이므로 양쪽에 간선을 추가합니다.
        graph[B].append((A, C))

    # 전처리 과정을 통해 깊이, 부모, 최소 및 최대 간선 길이를 계산합니다.
    depths, parents, min_edge, max_edge = preprocess(N, graph)

    Q = int(input_data[index])
    index += 1

    results = []
    for _ in range(Q):
        D = int(input_data[index])
        index += 1
        E = int(input_data[index])
        index += 1
        min_res, max_res = lca(D, E, depths, parents, min_edge, max_edge)  # 각 쿼리에 대해 LCA를 구하고 최소 및 최대 도로 길이를 찾습니다.
        results.append((min_res, max_res))

    for result in results:
        print(result[0], result[1])  # 결과를 출력합니다.

if __name__ == "__main__":
    main()  # 메인 함수를 호출하여 프로그램을 실행합니다.
