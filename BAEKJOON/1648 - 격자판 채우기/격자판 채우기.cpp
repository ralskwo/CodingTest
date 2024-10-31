#include <iostream>
#include <vector>
using namespace std;

const int MOD = 9901; // 나머지 값 설정

// 가능한 다음 상태를 생성하는 함수
void generateNextStates(int pos, int N, int current_state, int next_state, vector<int>& nextStates) {
    // 현재 위치가 N에 도달했으면 현재 next_state를 nextStates에 추가하고 종료
    if (pos == N) {
        nextStates.push_back(next_state);
        return;
    }
    
    // 현재 위치에 도미노가 놓여있는 경우, 다음 위치로 이동
    if (current_state & (1 << pos)) {
        generateNextStates(pos + 1, N, current_state, next_state, nextStates);
    } else {
        // 세로로 도미노 배치 가능
        generateNextStates(pos + 1, N, current_state, next_state | (1 << pos), nextStates);
        
        // 가로로 도미노 배치 가능 여부 확인
        if (pos + 1 < N && !(current_state & (1 << (pos + 1)))) {
            generateNextStates(pos + 2, N, current_state, next_state, nextStates);
        }
    }
}

// 주어진 격자판을 채우는 방법의 수를 계산하는 함수
int countWaysToFill(int N, int M) {
    // 격자판의 칸 수가 홀수일 경우 도미노로 완전히 채울 수 없으므로 0 반환
    if ((N * M) % 2 != 0) return 0;

    // DP 테이블 초기화: dp[열][상태 비트마스크] 형태
    vector<vector<int>> dp(M + 1, vector<int>(1 << N, 0));
    dp[0][0] = 1; // 초기 상태 설정

    // 각 열을 순차적으로 탐색하여 상태 전이
    for (int col = 0; col < M; ++col) {
        for (int state = 0; state < (1 << N); ++state) {
            // 현재 상태가 불가능한 경우 스킵
            if (dp[col][state] == 0) continue;

            // 다음 상태 생성
            vector<int> nextStates;
            generateNextStates(0, N, state, 0, nextStates);
            for (int nextState : nextStates) {
                dp[col + 1][nextState] = (dp[col + 1][nextState] + dp[col][state]) % MOD;
            }
        }
    }

    // 마지막 열이 완전히 채워진 상태에서의 가능한 배치 수 반환
    return dp[M][0];
}

int main() {
    int N, M;
    cin >> N >> M; // 입력 값: 격자판의 세로 크기 N과 가로 크기 M
    cout << countWaysToFill(N, M) << endl; // 가능한 배치 수 출력
    return 0;
}