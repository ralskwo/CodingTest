#include <iostream>
#include <vector>
using namespace std;

int movePipe(int N, vector<vector<int>>& house) {
    // DP 테이블 생성: dp[r][c][d]
    // d = 0: 가로, d = 1: 세로, d = 2: 대각선
    vector<vector<vector<int>>> dp(N, vector<vector<int>>(N, vector<int>(3, 0)));
    
    // 초기 상태: (1, 2)에서 가로 방향으로 시작
    dp[0][1][0] = 1;

    // DP 테이블 갱신
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            // 현재 칸이 벽이라면 건너뜀
            if (house[r][c] == 1) continue;

            // 가로 방향에서 이동
            if (c > 0) {
                dp[r][c][0] += dp[r][c - 1][0]; // 가로 -> 가로
                dp[r][c][0] += dp[r][c - 1][2]; // 대각선 -> 가로
            }

            // 세로 방향에서 이동
            if (r > 0) {
                dp[r][c][1] += dp[r - 1][c][1]; // 세로 -> 세로
                dp[r][c][1] += dp[r - 1][c][2]; // 대각선 -> 세로
            }

            // 대각선 방향에서 이동
            if (r > 0 && c > 0 && house[r - 1][c] == 0 && house[r][c - 1] == 0) {
                dp[r][c][2] += dp[r - 1][c - 1][0]; // 가로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][1]; // 세로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][2]; // 대각선 -> 대각선
            }
        }
    }

    // 결과 계산: (N-1, N-1)에서 모든 방향의 경우의 수 합산
    return dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2];
}

int main() {
    int N;
    cin >> N;

    // 집의 상태 입력 받기
    vector<vector<int>> house(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> house[i][j];
        }
    }

    // 결과 출력
    cout << movePipe(N, house) << endl;

    return 0;
}
