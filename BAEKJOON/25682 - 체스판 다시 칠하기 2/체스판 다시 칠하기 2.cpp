#include <iostream>                     // 입출력을 위해 iostream 헤더를 포함합니다
#include <vector>                       // 동적 배열(vector) 사용을 위해 vector 헤더를 포함합니다
#include <string>                       // 문자열(string) 사용을 위해 string 헤더를 포함합니다
#include <algorithm>                    // min 함수를 사용하기 위해 algorithm 헤더를 포함합니다
using namespace std;                    // std 네임스페이스를 사용합니다

int main() {
    ios::sync_with_stdio(false);        // C++ 표준 입출력과 C 표준 입출력의 동기화를 해제하여 속도를 향상시킵니다
    cin.tie(nullptr);                   // cin과 cout의 묶음을 해제하여 입출력 속도를 높입니다

    int N, M, K;                        // 보드의 행(N), 열(M), 체스판의 크기(K)를 저장할 변수를 선언합니다
    cin >> N >> M >> K;                 // N, M, K 값을 입력받습니다

    vector<string> board(N);            // 보드의 상태를 저장할 문자열 벡터를 크기 N으로 선언합니다
    for (int i = 0; i < N; i++) {         // 보드의 각 행을 입력받기 위한 반복문입니다
        cin >> board[i];                // 각 행의 문자열을 입력받아 board 벡터에 저장합니다
    }

    // 패턴1과 패턴2에 대해 각각의 불일치 여부를 누적합으로 계산할 2차원 배열을 (N+1) x (M+1) 크기로 0으로 초기화합니다
    vector<vector<int>> p1(N + 1, vector<int>(M + 1, 0));
    vector<vector<int>> p2(N + 1, vector<int>(M + 1, 0));

    for (int i = 0; i < N; i++) {         // 각 행을 순회합니다
        for (int j = 0; j < M; j++) {     // 각 열을 순회합니다
            char expected1, expected2;    // 두 가지 체스판 패턴에 대해 예상되는 색을 저장할 변수를 선언합니다
            if ((i + j) % 2 == 0) {       // (행 인덱스 + 열 인덱스)가 짝수이면
                expected1 = 'W';        // 패턴1은 흰색('W')이어야 합니다
                expected2 = 'B';        // 패턴2는 검은색('B')이어야 합니다
            } else {                      // (행 인덱스 + 열 인덱스)가 홀수이면
                expected1 = 'B';        // 패턴1은 검은색('B')이어야 합니다
                expected2 = 'W';        // 패턴2는 흰색('W')이어야 합니다
            }
            // 현재 칸의 색과 예상되는 색을 비교하여 불일치하면 1, 일치하면 0을 저장합니다
            int v1 = (board[i][j] != expected1) ? 1 : 0;
            int v2 = (board[i][j] != expected2) ? 1 : 0;

            // 2차원 누적합 공식: 현재 칸의 누적합 = 현재 칸 값 + 위쪽 누적합 + 왼쪽 누적합 - 대각선 위 왼쪽 누적합
            p1[i + 1][j + 1] = v1 + p1[i][j + 1] + p1[i + 1][j] - p1[i][j];
            p2[i + 1][j + 1] = v2 + p2[i][j + 1] + p2[i + 1][j] - p2[i][j];
        }
    }

    int ans = 1e9;                      // 최소 재칠 횟수를 저장할 변수 ans를 매우 큰 값으로 초기화합니다

    for (int i = 0; i <= N - K; i++) {    // 가능한 모든 K×K 영역의 시작 행 인덱스를 순회합니다
        for (int j = 0; j <= M - K; j++) {  // 가능한 모든 K×K 영역의 시작 열 인덱스를 순회합니다
            // 누적합을 활용하여 (i, j)에서 시작하는 K×K 영역의 불일치 개수를 계산합니다
            int mismatches1 = p1[i + K][j + K] - p1[i][j + K] - p1[i + K][j] + p1[i][j];
            int mismatches2 = p2[i + K][j + K] - p2[i][j + K] - p2[i + K][j] + p2[i][j];
            // 두 패턴 중 더 적은 재칠 횟수를 현재 ans와 비교하여 갱신합니다
            ans = min(ans, min(mismatches1, mismatches2));
        }
    }

    cout << ans << "\n";               // 계산된 최소 재칠 횟수를 출력합니다
    return 0;                          // 프로그램을 종료합니다
}
