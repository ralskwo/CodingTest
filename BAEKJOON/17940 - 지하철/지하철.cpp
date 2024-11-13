#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <limits>

using namespace std;
const int INF = numeric_limits<int>::max();  // 무한대를 나타내기 위한 상수

void solve() {
    int N, M;
    cin >> N >> M;  // 지하철역 수와 도착지 역 번호 입력
    
    vector<int> companies(N);  // 각 역의 소속 회사 정보
    for (int i = 0; i < N; ++i) {
        cin >> companies[i];  // 각 역의 회사 정보를 입력받음
    }

    vector<vector<int>> adj_matrix(N, vector<int>(N));  // 역 간 연결 상태와 시간을 저장하는 인접 행렬
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> adj_matrix[i][j];  // 각 역 간의 연결 상태와 시간을 입력받음
        }
    }

    vector<vector<pair<int, int>>> dist(N, vector<pair<int, int>>(2, {INF, INF}));  // 최소 환승 횟수와 시간을 저장할 배열
    dist[0][companies[0]] = {0, 0};  // 출발지의 회사로 시작하여 환승 횟수와 시간을 0으로 설정

    priority_queue<tuple<int, int, int, int>, vector<tuple<int, int, int, int>>, greater<>> pq;
    pq.emplace(0, 0, 0, companies[0]);  // 우선순위 큐에 (환승 횟수, 시간, 현재 위치, 회사) 형태로 추가

    while (!pq.empty()) {
        auto [transfers, time, node, curr_company] = pq.top();
        pq.pop();

        if (make_pair(transfers, time) > dist[node][curr_company]) {
            continue;  // 이미 더 좋은 경로로 방문된 경우 스킵
        }

        for (int next_node = 0; next_node < N; ++next_node) {
            int travel_time = adj_matrix[node][next_node];  // 현재 역에서 다음 역까지의 이동 시간
            if (travel_time == 0) {
                continue;  // 연결되지 않은 경우 스킵
            }

            int next_company = companies[next_node];  // 다음 역의 소속 회사
            int new_transfers = transfers + (curr_company != next_company ? 1 : 0);  // 회사가 다르면 환승 횟수 증가
            int new_time = time + travel_time;  // 이동 시간 추가

            if (make_pair(new_transfers, new_time) < dist[next_node][next_company]) {
                dist[next_node][next_company] = {new_transfers, new_time};  // 최소 환승 및 시간으로 업데이트
                pq.emplace(new_transfers, new_time, next_node, next_company);  // 업데이트된 경로를 큐에 추가
            }
        }
    }

    auto result = min(dist[M][0], dist[M][1]);  // 도착지에서 최소 환승과 최소 시간을 찾음
    cout << result.first << " " << result.second << endl;  // 환승 횟수와 총 소요 시간을 출력
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();  // 메인 함수에서 문제를 해결하는 함수를 호출
    return 0;
}