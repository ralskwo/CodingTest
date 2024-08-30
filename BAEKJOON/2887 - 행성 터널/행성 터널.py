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
