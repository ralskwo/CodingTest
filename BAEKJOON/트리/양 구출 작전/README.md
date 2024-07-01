# 문제 풀이 과정

## 문제 이해 및 접근 방법

### 문제 이해
1. 여러 섬이 연결된 나라가 있습니다. 1번 섬부터 N번 섬까지 있으며, 1번 섬에는 아무런 동물도 없습니다.
2. 각 섬에는 양(S) 또는 늑대(W)가 있습니다.
3. 늑대는 양을 잡아먹기 때문에, 양을 안전하게 1번 섬으로 이동시키려면 양이 늑대보다 많아야 합니다.
4. 각 섬은 다른 섬과 다리로 연결되어 있으며, 이 다리를 통해서만 다른 섬으로 이동할 수 있습니다.
5. 1번 섬에서 출발하여 최대한 많은 양을 구출하는 것이 목표입니다.

### 접근 방법
1. **그래프 구성**:
   - 각 섬을 노드로, 다리를 간선으로 하는 그래프를 구성합니다.
   - 각 노드에는 양이나 늑대의 수가 저장됩니다.

2. **DFS(깊이 우선 탐색) 이용**:
   - DFS를 통해 리프 노드부터 시작하여 양과 늑대의 수를 누적 계산합니다.
   - 현재 노드에서 자식 노드로 내려가면서 양과 늑대의 수를 합산합니다.
   - 누적된 양의 수에서 늑대의 수를 뺀 값을 부모 노드로 반환합니다.
   - 루트 노드에서 최종적으로 구출된 양의 총합을 계산합니다.

## 코드 구현

```python
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
```