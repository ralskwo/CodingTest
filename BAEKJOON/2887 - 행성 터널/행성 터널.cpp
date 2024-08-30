#include <iostream>                // 표준 입력 및 출력을 위한 헤더 파일
#include <vector>                  // 벡터 사용을 위한 헤더 파일
#include <algorithm>               // 정렬 함수 등을 사용하기 위한 헤더 파일
#include <tuple>                   // 튜플 사용을 위한 헤더 파일

using namespace std;               // std 네임스페이스를 전역으로 사용

// Disjoint Set 자료구조 정의 (Union-Find)
class DisjointSet {
public:
    vector<int> parent, rank;      // 각 원소의 부모와 트리의 깊이를 저장할 벡터

    DisjointSet(int n) {           // 생성자: n개의 원소에 대해 초기화
        parent.resize(n);          // parent 벡터 크기 조정
        rank.resize(n, 1);         // rank 벡터를 1로 초기화
        for (int i = 0; i < n; ++i) {
            parent[i] = i;         // 초기에는 각 원소가 자신의 부모가 됨
        }
    }

    // 부모 찾기 (경로 압축)
    int find(int u) {
        if (u != parent[u]) {      // 현재 원소가 자신의 부모가 아니라면
            parent[u] = find(parent[u]); // 재귀적으로 부모를 찾아서 부모 갱신 (경로 압축)
        }
        return parent[u];          // 부모를 반환
    }

    // 두 집합 합치기 (Union by rank)
    bool unionSets(int u, int v) {
        int root_u = find(u);      // u의 루트를 찾음
        int root_v = find(v);      // v의 루트를 찾음

        if (root_u != root_v) {    // 루트가 다르다면, 즉 두 집합이 다르다면
            if (rank[root_u] > rank[root_v]) { // u의 트리 깊이가 더 크다면
                parent[root_v] = root_u;       // v의 루트를 u의 루트로 설정
            } else if (rank[root_u] < rank[root_v]) { // v의 트리 깊이가 더 크다면
                parent[root_u] = root_v;       // u의 루트를 v의 루트로 설정
            } else {                           // 트리 깊이가 같다면
                parent[root_v] = root_u;       // v의 루트를 u의 루트로 설정하고
                rank[root_u]++;                // u의 트리 깊이를 증가시킴
            }
            return true;                       // 두 집합이 합쳐졌으므로 true 반환
        }
        return false;                          // 이미 같은 집합이라면 false 반환
    }
};

// 특정 차원의 좌표 값을 반환하는 함수
int getDim(const tuple<int, int, int, int>& t, int dim) {
    if (dim == 0) return get<0>(t);  // dim이 0이면 x 좌표 반환
    if (dim == 1) return get<1>(t);  // dim이 1이면 y 좌표 반환
    return get<2>(t);                // 그 외에는 z 좌표 반환
}

int main() {
    int n;                            // 행성의 수
    cin >> n;                         // 행성의 수 입력 받기

    vector<tuple<int, int, int, int>> planets(n); // 행성의 좌표와 인덱스를 저장할 벡터

    for (int i = 0; i < n; ++i) {     // 각 행성의 좌표와 인덱스를 입력 받음
        int x, y, z;
        cin >> x >> y >> z;           // 행성의 x, y, z 좌표 입력 받기
        planets[i] = {x, y, z, i};    // 행성의 좌표와 인덱스를 튜플로 저장
    }

    vector<tuple<int, int, int>> edges; // 간선 목록 (비용, 행성1, 행성2)

    // x, y, z 좌표별로 정렬 후 인접 행성 간의 간선 추가
    for (int dim = 0; dim < 3; ++dim) { 
        sort(planets.begin(), planets.end(), [dim](auto &a, auto &b) {
            return getDim(a, dim) < getDim(b, dim); // 각 좌표 축(dim) 별로 행성들을 정렬
        });

        for (int i = 1; i < n; ++i) {  // 인접한 행성 간의 간선을 생성
            int cost = abs(getDim(planets[i], dim) - getDim(planets[i - 1], dim)); // 비용 계산
            int u = get<3>(planets[i]);     // 첫 번째 행성의 인덱스
            int v = get<3>(planets[i - 1]); // 두 번째 행성의 인덱스
            edges.emplace_back(cost, u, v); // 간선 목록에 추가
        }
    }

    sort(edges.begin(), edges.end()); // 간선들을 비용 순으로 정렬

    DisjointSet dsu(n);               // Disjoint Set 초기화
    int total_cost = 0;               // 총 비용 초기화

    // Kruskal 알고리즘으로 최소 스패닝 트리 생성
    for (auto &[cost, u, v] : edges) {  // 각 간선을 순회하며
        if (dsu.unionSets(u, v)) {      // 두 집합이 합쳐지면 (사이클이 아니면)
            total_cost += cost;         // 그 간선의 비용을 총 비용에 더함
        }
    }

    cout << total_cost << endl;        // 최종 최소 비용 출력

    return 0;
}
