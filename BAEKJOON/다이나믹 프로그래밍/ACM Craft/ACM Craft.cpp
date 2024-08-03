#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

void acm_craft() {
    int T;
    cin >> T;  // 테스트 케이스의 수

    while (T--) {
        int N, K;
        cin >> N >> K;  // 건물의 수와 규칙의 수

        vector<int> build_times(N + 1);  // 각 건물을 짓는 데 걸리는 시간
        vector<int> indegree(N + 1, 0);  // 각 건물의 진입 차수
        vector<vector<int>> graph(N + 1);  // 그래프 초기화
        vector<int> dp(N + 1, 0);  // 각 건물을 짓는 데 걸리는 최소 시간을 저장할 배열

        // 각 건물의 건설 시간을 설정합니다.
        for (int i = 1; i <= N; ++i) {
            cin >> build_times[i];
        }

        // 그래프를 구성하고 진입 차수를 설정합니다.
        for (int i = 0; i < K; ++i) {
            int X, Y;
            cin >> X >> Y;
            graph[X].push_back(Y);
            indegree[Y]++;
        }

        int target;
        cin >> target;  // 목표 건물

        queue<int> q;

        // 진입 차수가 0인 건물들을 큐에 추가하고, 초기 시간을 설정합니다.
        for (int i = 1; i <= N; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
                dp[i] = build_times[i];
            }
        }

        // 위상 정렬을 수행하면서 각 건물을 짓는 데 걸리는 최소 시간을 계산합니다.
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            for (int neighbor : graph[current]) {
                indegree[neighbor]--;
                dp[neighbor] = max(dp[neighbor], dp[current] + build_times[neighbor]);
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // 목표 건물을 짓는 데 걸리는 최소 시간을 출력합니다.
        cout << dp[target] << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    acm_craft();
    return 0;
}
