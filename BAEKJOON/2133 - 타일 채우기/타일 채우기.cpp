#include <iostream>
#include <vector>

using namespace std;

int count_tiling_ways(int N) {
    // N이 1 이하일 경우 채울 수 있는 경우의 수는 0
    if (N <= 0) {
        return 0;
    }
    
    // N이 1인 경우 채울 수 있는 경우의 수는 0
    if (N == 1) {
        return 0;
    }
    
    // N이 2인 경우 채울 수 있는 경우의 수는 3 (기본 케이스)
    if (N == 2) {
        return 3;
    }
    
    // DP 배열 초기화
    vector<int> dp(N + 1, 0);
    
    // 기본 케이스 설정
    dp[0] = 1;  // 3x0 벽은 아무것도 채우지 않은 경우 1가지
    dp[2] = 3;  // 3x2 벽을 채우는 경우의 수
    
    // DP 점화식을 이용하여 경우의 수 계산
    for (int i = 4; i <= N; i += 2) {
        dp[i] = 4 * dp[i - 2] - dp[i - 4];
    }
    
    return dp[N];
}

int main() {
    int N;
    cin >> N;
    
    cout << count_tiling_ways(N) << endl;
    
    return 0;
}
