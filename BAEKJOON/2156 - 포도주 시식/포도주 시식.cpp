#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxWineAmount(int n, vector<int>& wines) {
    // 만약 포도주 잔이 하나만 있다면, 그 잔의 포도주 양을 반환
    if (n == 1) {
        return wines[0];
    }
    
    // 만약 포도주 잔이 두 개만 있다면, 두 잔의 포도주 양을 더한 값을 반환
    if (n == 2) {
        return wines[0] + wines[1];
    }
    
    // dp 배열을 초기화합니다. dp[i]는 i번째 잔까지 최대로 마실 수 있는 포도주 양을 저장합니다.
    vector<int> dp(n, 0);
    
    // 기본 값 설정
    dp[0] = wines[0];  // 첫 번째 잔을 고려할 때의 최댓값
    dp[1] = wines[0] + wines[1];  // 첫 번째와 두 번째 잔을 고려할 때의 최댓값
    
    // 첫 번째, 두 번째, 세 번째 잔을 고려할 때의 최댓값
    dp[2] = max({wines[0] + wines[1],  // 경우 1: 첫 번째와 두 번째 잔을 마신다.
                 wines[0] + wines[2],  // 경우 2: 첫 번째와 세 번째 잔을 마신다.
                 wines[1] + wines[2]});  // 경우 3: 두 번째와 세 번째 잔을 마신다.
    
    // 네 번째 잔부터 n번째 잔까지 dp 배열을 채웁니다.
    for (int i = 3; i < n; ++i) {
        // i번째 잔에 대한 최댓값은 세 가지 경우 중 최대값입니다:
        dp[i] = max({dp[i-1],  // 경우 1: i번째 잔을 건너뛰는 경우
                     dp[i-2] + wines[i],  // 경우 2: i번째 잔을 마시고 (i-1)번째 잔을 건너뛰는 경우
                     dp[i-3] + wines[i-1] + wines[i]});  // 경우 3: i번째 잔과 (i-1)번째 잔을 마시고 (i-2)번째 잔을 건너뛰는 경우
    }
    
    // 결과는 n개의 잔을 고려한 최댓값입니다.
    return dp[n-1];
}

int main() {
    int n;
    cin >> n;  // 포도주 잔의 개수를 입력 받습니다.
    
    vector<int> wines(n);
    for (int i = 0; i < n; ++i) {
        cin >> wines[i];  // 각 포도주 잔에 들어 있는 포도주 양을 입력 받습니다.
    }
    
    // 최대로 마실 수 있는 포도주의 양을 출력합니다.
    cout << maxWineAmount(n, wines) << endl;
    
    return 0;
}
