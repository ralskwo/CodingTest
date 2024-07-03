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
