#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Union-Find 자료구조에서 부모를 찾는 함수
int find(vector<int>& parent, int x) {
    if (parent[x] != x) {  // 부모가 자기 자신이 아니면, 재귀적으로 부모를 찾아감
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

// Union-Find 자료구조에서 두 집합을 합치는 함수
void union_sets(vector<int>& parent, vector<int>& rank, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    
    if (rootX != rootY) {  // 두 집합이 다른 경우에만 합침
        if (rank[rootX] > rank[rootY]) {  // rank를 기준으로 더 높은 쪽에 합침
            parent[rootY] = rootX;
        } else if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else {
            parent[rootY] = rootX;
            rank[rootX] += 1;
        }
    }
}

// 최소 스패닝 트리를 구성하여 최소 비행기 종류 개수를 구하는 함수
int minimum_flights(int n, vector<pair<int, pair<int, int>>>& edges) {
    vector<int> parent(n + 1);
    vector<int> rank(n + 1, 0);
    
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
    }
    
    sort(edges.begin(), edges.end());  // 간선을 가중치 기준으로 정렬
    
    int mst_weight = 0;
    int mst_edges = 0;
    
    for (const auto& edge : edges) {
        int weight = edge.first;
        int u = edge.second.first;
        int v = edge.second.second;
        
        if (find(parent, u) != find(parent, v)) {  // 사이클이 생기지 않도록 간선을 추가
            union_sets(parent, rank, u, v);
            mst_weight += weight;
            mst_edges += 1;
            if (mst_edges == n - 1) {  // MST가 완성되면 종료
                break;
            }
        }
    }
    
    return mst_edges;
}

int main() {
    int T;
    cin >> T;  // 테스트 케이스 수
    
    vector<int> results;
    
    for (int t = 0; t < T; ++t) {
        int n, m;
        cin >> n >> m;  // 나라의 수와 비행기 종류의 수
        
        vector<pair<int, pair<int, int>>> edges;
        
        for (int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            edges.push_back({1, {u, v}});  // 모든 가중치를 1로 설정 (문제 조건)
        }
        
        int result = minimum_flights(n, edges);
        results.push_back(result);
    }
    
    for (const auto& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
