#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int floyd_warshall_min_cycle(int V, const vector<vector<int>>& edges) {
    // 거리 행렬 초기화
    vector<vector<int>> dist(V, vector<int>(V, INF));

    // 주어진 간선 정보로 거리 행렬 초기화
    for (const auto& edge : edges) {
        int a = edge[0] - 1, b = edge[1] - 1, c = edge[2];
        dist[a][b] = min(dist[a][b], c);
    }

    // Floyd-Warshall 알고리즘 실행
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                // 오버플로우 방지
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // 최소 사이클 찾기
    int min_cycle = INF;
    for (int i = 0; i < V; i++) {
        min_cycle = min(min_cycle, dist[i][i]);
    }

    // 결과 반환 (사이클이 없으면 -1 반환)
    return min_cycle == INF ? -1 : min_cycle;
}

int main() {
    int V, E;
    cin >> V >> E;  // 마을 수와 도로 수 입력

    vector<vector<int>> edges(E, vector<int>(3));
    for (int i = 0; i < E; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];  // 도로 정보 입력
    }

    int result = floyd_warshall_min_cycle(V, edges);  // 최소 사이클 계산
    cout << result << endl;  // 결과 출력

    return 0;
}