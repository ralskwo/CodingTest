#include <iostream>
#include <vector>
#include <tuple>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();  // 무한대를 의미하는 상수 정의

// 벨만-포드 알고리즘 함수: 음수 사이클이 존재하면 true, 없으면 false 반환
bool bellmanFord(int n, const vector<tuple<int, int, int>>& edges, int start) {
    vector<int> dist(n + 1, INF);  // 각 지점까지의 최단 거리를 무한대로 초기화
    dist[start] = 0;  // 시작 지점의 거리를 0으로 설정

    for (int i = 0; i < n; i++) {  // 지점의 수만큼 반복
        bool updated = false;  // 이번 반복에서 갱신이 발생했는지 확인
        for (auto [u, v, w] : edges) {  // 모든 간선에 대해 반복
            if (dist[u] != INF && dist[u] + w < dist[v]) {  // u에서 v로의 경로가 최단 경로인지 확인
                dist[v] = dist[u] + w;  // 최단 경로로 갱신
                updated = true;  // 갱신이 발생했음을 표시
                if (i == n - 1) return true;  // n번째 반복에서도 갱신이 있으면 음수 사이클 존재
            }
        }
        if (!updated) break;  // 더 이상 갱신이 없으면 반복 종료
    }
    return false;  // 음수 사이클이 없으면 false 반환
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int TC;
    cin >> TC;  // 테스트 케이스 개수 입력
    while (TC--) {
        int n, m, w;
        cin >> n >> m >> w;  // 지점의 수, 도로의 개수, 웜홀의 개수 입력
        vector<tuple<int, int, int>> edges;  // 간선 정보를 저장할 벡터

        for (int i = 0; i < m; i++) {  // 도로 정보 입력
            int s, e, t;
            cin >> s >> e >> t;
            edges.emplace_back(s, e, t);  // 양방향 도로로 양쪽 추가
            edges.emplace_back(e, s, t);
        }

        for (int i = 0; i < w; i++) {  // 웜홀 정보 입력
            int s, e, t;
            cin >> s >> e >> t;
            edges.emplace_back(s, e, -t);  // 음수 가중치로 단방향 웜홀 추가
        }

        bool hasNegativeCycle = false;
        for (int start = 1; start <= n; start++) {  // 모든 지점을 시작점으로 설정
            if (bellmanFord(n, edges, start)) {  // 음수 사이클이 있는지 확인
                hasNegativeCycle = true;
                break;  // 음수 사이클 발견 시 조기 종료
            }
        }

        cout << (hasNegativeCycle ? "YES" : "NO") << '\n';  // 결과 출력
    }

    return 0;
}