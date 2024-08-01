#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maximalSquare(int n, int m, const vector<string>& matrix_str) {
    if (matrix_str.empty()) {
        return 0;
    }

    vector<vector<int>> dp(n, vector<int>(m, 0));
    int max_side = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (matrix_str[i][j] == '1') {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;  // 첫 행 또는 첫 열인 경우
                } else {
                    // 이전 행, 이전 열, 대각선 값을 참고하여 최소값에 1을 더함
                    dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                }
                // 최대 변의 길이 갱신
                max_side = max(max_side, dp[i][j]);
            }
        }
    }

    // 최대 변의 길이의 제곱이 가장 큰 정사각형의 넓이
    return max_side * max_side;
}

int main() {
    int n, m;
    cin >> n >> m;  // 첫 줄에서 n과 m을 입력 받음
    vector<string> matrix_str(n);
    for (int i = 0; i < n; ++i) {
        cin >> matrix_str[i];  // 다음 n개의 줄에서 문자열 리스트를 입력 받음
    }

    // 함수 호출 및 결과 출력
    cout << maximalSquare(n, m, matrix_str) << endl;

    return 0;
}
