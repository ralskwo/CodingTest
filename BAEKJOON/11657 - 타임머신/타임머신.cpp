#include <iostream>
#include <vector>
#include <tuple>
#include <limits>

using namespace std;

const long long INF = numeric_limits<long long>::max(); // 무한대를 표현하기 위한 상수

// 벨만-포드 알고리즘 함수
bool bellman_ford(int n, vector<tuple<int, int, int>>& edges, vector<long long>& distance) {
    distance[1] = 0; // 시작 도시의 거리를 0으로 초기화

    // n-1번 반복하여 최단 거리를 계산
    for (int i = 1; i < n; i++) {
        for (auto [u, v, cost] : edges) { // 각 간선을 순회
            if (distance[u] != INF && distance[u] + cost < distance[v]) {
                distance[v] = distance[u] + cost; // 최단 거리 갱신
            }
        }
    }

    // n번째 반복에서 갱신이 발생하면 음수 사이클 존재
    for (auto [u, v, cost] : edges) {
        if (distance[u] != INF && distance[u] + cost < distance[v]) {
            return true; // 음수 사이클 존재
        }
    }

    return false; // 음수 사이클 없음
}

int main() {
    int n, m;
    cin >> n >> m; // 도시 수와 버스 노선 수 입력

    vector<tuple<int, int, int>> edges; // 간선 정보를 저장할 벡터
    vector<long long> distance(n + 1, INF); // 최단 거리 배열을 무한대로 초기화

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c; // 시작 도시, 도착 도시, 비용 입력
        edges.emplace_back(a, b, c); // 간선 추가
    }

    if (bellman_ford(n, edges, distance)) {
        cout << -1 << endl; // 음수 사이클이 존재하면 -1 출력
    } else {
        for (int i = 2; i <= n; i++) {
            if (distance[i] == INF) {
                cout << -1 << endl; // 도달할 수 없는 경우 -1 출력
            } else {
                cout << distance[i] << endl; // 최단 거리 출력
            }
        }
    }

    return 0;
}
