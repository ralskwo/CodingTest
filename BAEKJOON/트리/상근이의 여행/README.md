# 문제 이해, 접근 방식 및 풀이 과정

https://www.acmicpc.net/problem/9372

## 문제 이해

상근이는 겨울방학 동안 자가용 비행기를 타고 여러 나라를 여행하려고 합니다. 각 나라를 여행하기 위해 최소한의 비행기 종류를 이용하고자 합니다. 각 테스트 케이스마다 주어진 비행기 경로를 통해 모든 나라를 방문할 수 있도록 최소한의 비행기 종류의 개수를 구하는 문제입니다.

## 접근 방식

1. **그래프 모델링**: 각 나라는 그래프의 정점(Vertex)으로, 비행기 경로는 간선(Edge)으로 모델링합니다. 간선의 가중치는 모두 동일하게 1로 설정합니다.
2. **최소 스패닝 트리(MST)**: 그래프의 모든 정점을 연결하면서, 간선의 가중치 합이 최소가 되는 트리를 구성합니다. MST를 구성하기 위해 크루스칼(Kruskal) 알고리즘을 사용합니다.
3. **Union-Find 자료구조**: 크루스칼 알고리즘에서 간선의 추가 시 사이클을 방지하기 위해 Union-Find 자료구조를 사용합니다.

## 풀이 과정

1. **Union-Find 자료구조 정의**:
    - `find` 함수: 특정 정점의 루트 부모를 찾습니다.
    - `union` 함수: 두 집합을 병합합니다.
2. **크루스칼 알고리즘 구현**:
    - 간선을 가중치 기준으로 정렬합니다.
    - 정렬된 간선을 하나씩 선택하여 MST를 구성합니다. 이때 사이클이 생기지 않도록 Union-Find 자료구조를 사용합니다.
3. **입력 데이터 처리 및 결과 출력**:
    - 입력 데이터를 파싱하여 각 테스트 케이스의 나라 수(N)와 비행기 경로 수(M)를 가져옵니다.
    - 각 테스트 케이스마다 최소 스패닝 트리를 구성하여 최소 비행기 종류의 개수를 구합니다.
    - 결과를 출력합니다.

## 코드
```python
import sys
input = sys.stdin.read

# Union-Find 자료구조에서 부모를 찾는 함수
def find(parent, x):
    if parent[x] != x:  # 부모가 자기 자신이 아니면, 재귀적으로 부모를 찾아감
        parent[x] = find(parent, parent[x])
    return parent[x]

# Union-Find 자료구조에서 두 집합을 합치는 함수
def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:  # 두 집합이 다른 경우에만 합침
        if rank[rootX] > rank[rootY]:  # rank를 기준으로 더 높은 쪽에 합침
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# 최소 스패닝 트리를 구성하여 최소 비행기 종류 개수를 구하는 함수
def minimum_flights(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    edges.sort()  # 간선을 가중치 기준으로 정렬
    
    mst_weight = 0
    mst_edges = 0
    
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):  # 사이클이 생기지 않도록 간선을 추가
            union(parent, rank, u, v)
            mst_weight += weight
            mst_edges += 1
            if mst_edges == n - 1:  # MST가 완성되면 종료
                break
                
    return mst_edges

def main():
    data = input().strip().split()
    index = 0
    
    T = int(data[index])  # 테스트 케이스 수
    index += 1
    
    results = []
    
    for _ in range(T):
        n = int(data[index])  # 나라의 수
        m = int(data[index + 1])  # 비행기 종류의 수
        index += 2
        
        edges = []
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            edges.append((1, u, v))  # 모든 가중치를 1로 설정 (문제 조건)
            
        result = minimum_flights(n, edges)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

```