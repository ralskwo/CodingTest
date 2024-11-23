#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

void solve() {
    int n; // 추의 개수
    cin >> n;

    vector<int> weights(n); // 추의 무게 리스트
    for (int i = 0; i < n; ++i) {
        cin >> weights[i];
    }

    int m; // 구슬의 개수
    cin >> m;

    vector<int> marbles(m); // 구슬의 무게 리스트
    for (int i = 0; i < m; ++i) {
        cin >> marbles[i];
    }

    int max_weight = 40000; // 구슬의 최대 무게
    bool dp[40001]; // DP 테이블, dp[x]는 무게 x를 만들 수 있는지 여부
    memset(dp, false, sizeof(dp)); // DP 테이블을 모두 false로 초기화
    dp[0] = true; // 무게 0은 항상 만들 수 있음

    // 추를 이용해 가능한 무게를 DP 테이블에 기록
    for (int weight : weights) {
        bool current[40001]; // 현재 추를 추가했을 때의 상태를 저장할 배열
        memcpy(current, dp, sizeof(dp)); // 기존 DP 테이블 복사

        for (int w = 0; w <= max_weight; ++w) {
            if (dp[w]) { // 현재 무게 w가 가능한 경우
                if (w + weight <= max_weight) {
                    current[w + weight] = true; // 추를 왼쪽에 놓는 경우
                }
                if (abs(w - weight) <= max_weight) {
                    current[abs(w - weight)] = true; // 추를 오른쪽에 놓는 경우
                }
            }
        }
        memcpy(dp, current, sizeof(dp)); // 갱신된 테이블을 DP 테이블로 복사
    }

    // 결과를 저장할 벡터
    vector<char> result;

    // 각 구슬의 무게가 DP 테이블에 있는지 확인
    for (int marble : marbles) {
        if (marble <= max_weight && dp[marble]) {
            result.push_back('Y'); // 가능하면 Y
        } else {
            result.push_back('N'); // 불가능하면 N
        }
    }

    // 결과 출력
    for (int i = 0; i < result.size(); ++i) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}
