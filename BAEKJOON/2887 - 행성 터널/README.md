# 행성 터널 문제 풀이 및 설명

https://www.acmicpc.net/problem/2887

https://mayquartet.com/python-%ed%8c%8c%ec%9d%b4%ec%8d%ac-%eb%b0%b1%ec%a4%80-2887-%ed%96%89%ec%84%b1-%ed%84%b0%eb%84%90-%eb%ac%b8%ec%a0%9c-%ed%92%80%ec%9d%b4-%eb%b0%8f-%ec%84%a4%eb%aa%85/

## 문제 이해

이 문제는 행성들이 3차원 공간에서 위치하고 있을 때, 이들을 터널로 연결하여 하나의 네트워크로 만드는 데 필요한 최소 비용을 계산하는 문제입니다. 각 행성은 3차원 좌표계 상에서 하나의 점으로 나타낼 수 있으며, 두 행성을 연결하는 터널의 비용은 세 좌표 축(x, y, z)에서의 차이 중 가장 작은 값으로 정의됩니다. 주어진 모든 행성을 연결하기 위해서는 최소 스패닝 트리(Minimum Spanning Tree, MST)를 만들어야 하며, 이때 필요한 최소 비용을 구하는 것이 문제의 핵심입니다.

## 입출력 조건

- **입력 조건**:
  - 첫 번째 줄에 행성의 개수 `N`이 주어집니다. (`1 ≤ N ≤ 100,000`)
  - 그 다음 `N`개의 줄에 각 행성의 x, y, z 좌표가 정수로 주어집니다. 좌표 값은 `-10^9` 이상 `10^9` 이하의 범위를 가집니다.
- **출력 조건**:
  - 모든 행성을 터널로 연결하는 데 필요한 최소 비용을 출력합니다.

## 접근 방식

이 문제는 그래프 이론에서 최소 스패닝 트리를 구하는 문제로, Kruskal 알고리즘을 사용해 해결할 수 있습니다. Kruskal 알고리즘은 간선을 비용 오름차순으로 정렬한 후, 사이클을 생성하지 않는 간선들을 선택해 나가는 방식으로 최소 스패닝 트리를 구성합니다.

하지만 이 문제에서는 모든 가능한 간선(두 행성 간의 거리)을 고려하면, 시간 복잡도가 매우 커지기 때문에 최적화가 필요합니다. 이를 해결하기 위해:

1. 각 좌표 축(x, y, z)별로 행성들을 정렬한 후, 인접한 행성들 간의 간선만을 고려합니다.
2. 이러한 방식으로 얻어진 간선들로 Kruskal 알고리즘을 적용하여 최소 스패닝 트리를 구성합니다.

## 풀이 과정

1. **Disjoint Set(Union-Find) 자료구조 초기화**:
   - 사이클을 판별하기 위해 Disjoint Set(서로소 집합) 자료구조를 사용합니다. 이 구조는 각 행성이 속한 집합을 관리하며, 두 행성이 동일한 집합에 속해 있는지를 효율적으로 확인할 수 있게 해줍니다.
2. **행성 좌표 정렬 및 간선 생성**:

   - 각 행성의 x, y, z 좌표에 대해 별도로 정렬을 수행합니다.
   - 정렬된 좌표들을 기준으로 인접한 행성 간의 간선을 생성하며, 이 간선의 비용은 두 행성 간의 좌표 차이 중 가장 작은 값으로 계산합니다.
   - 이 방식으로 생성된 간선들만을 대상으로 Kruskal 알고리즘을 적용하여 최소 스패닝 트리를 구성합니다.

3. **Kruskal 알고리즘 적용**:

   - 앞서 생성된 간선들을 비용에 따라 오름차순으로 정렬합니다.
   - 정렬된 간선을 하나씩 선택하여, 해당 간선이 두 행성을 연결할 때 사이클이 생기지 않는다면 그 간선을 최소 스패닝 트리에 포함시킵니다.
   - 이 과정에서 Disjoint Set 자료구조를 사용해 사이클 발생 여부를 확인하고, 사이클이 발생하지 않는 경우 두 집합을 합칩니다.

4. **최종 비용 계산 및 출력**:
   - Kruskal 알고리즘을 통해 선택된 간선들의 비용을 모두 합산하여 최소 비용을 계산합니다.
   - 계산된 최소 비용을 출력합니다.

## 코드 구현

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # 각 원소의 부모를 저장하는 리스트, 초기에는 자기 자신이 부모
        self.rank = [1] * n           # 각 원소의 트리 깊이를 저장하는 리스트, 초기 깊이는 1

    def find(self, u):
        if self.parent[u] != u:       # 현재 원소가 자신의 부모가 아니라면
            self.parent[u] = self.find(self.parent[u])  # 부모를 재귀적으로 찾고, 경로 압축을 수행
        return self.parent[u]          # 부모를 반환

    def union(self, u, v):
        root_u = self.find(u)          # u의 루트를 찾음
        root_v = self.find(v)          # v의 루트를 찾음

        if root_u != root_v:           # 루트가 다르다면, 즉 두 집합이 다르다면
            if self.rank[root_u] > self.rank[root_v]:  # u의 트리 깊이가 더 크다면
                self.parent[root_v] = root_u           # v의 루트를 u의 루트로 설정
            elif self.rank[root_u] < self.rank[root_v]: # v의 트리 깊이가 더 크다면
                self.parent[root_u] = root_v           # u의 루트를 v의 루트로 설정
            else:                                      # 트리 깊이가 같다면
                self.parent[root_v] = root_u           # v의 루트를 u의 루트로 설정하고
                self.rank[root_u] += 1                 # u의 트리 깊이를 증가시킴
            return True                                # 두 집합이 합쳐졌으므로 True 반환
        return False                                   # 이미 같은 집합이라면 False 반환

def min_spanning_tree_cost(n, planets):
    edges = []  # 간선 목록을 저장할 리스트

    for dim in range(3):  # x, y, z 축에 대해 반복
        planets.sort(key=lambda x: x[dim])  # 각 축에 대해 행성들을 정렬

        for i in range(1, n):  # 정렬된 행성들 간의 인접한 간선을 계산
            cost = abs(planets[i][dim] - planets[i - 1][dim])  # 인접 행성 간의 좌표 차이 중 최소값을 비용으로 설정
            edges.append((cost, planets[i][3], planets[i - 1][3]))  # 간선을 추가 (비용, 행성1, 행성2)

    edges.sort()  # 간선들을 비용 순으로 정렬
    dsu = DisjointSet(n)  # Disjoint Set 자료구조 초기화
    total_cost = 0  # 총 비용 초기화

    for cost, u, v in edges:  # 모든 간선을 순회
        if dsu.union(u, v):   # 사이클이 발생하지 않는다면 두 집합을 병합
            total_cost += cost  # 간선의 비용을 총 비용에 추가

    return total_cost  # 모든 행성을 연결하는 데 필요한 최소 비용 반환

# 입력 처리
n = int(input())  # 행성의 수 입력 받기
planets = []  # 행성 좌표와 인덱스를 저장할 리스트

for i in range(n):  # n개의 행성 좌표를 입력 받음
    x, y, z = map(int, input().split())  # 각 행성의 x, y, z 좌표 입력 받기
    planets.append((x, y, z, i))  # 행성의 좌표와 인덱스를 튜플로 저장

# 결과 출력
print(min_spanning_tree_cost(n, planets))  # 최소 스패닝 트리 비용을 계산하여 출력
```
