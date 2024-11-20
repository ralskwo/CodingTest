#include <iostream>
#include <vector>
#include <algorithm> // max 함수를 사용하기 위해 포함
using namespace std;

// 스티커 점수의 최대값을 계산하는 함수
vector<int> maxStickerScore(const vector<pair<vector<int>, vector<int>>>& testCases) {
    vector<int> results;

    // 각 테스트 케이스 처리
    for (const auto& stickers : testCases) {
        const vector<int>& row1 = stickers.first;  // 위쪽 행
        const vector<int>& row2 = stickers.second; // 아래쪽 행
        int n = row1.size(); // 열의 개수

        if (n == 1) {
            // 열이 1개인 경우, 두 행의 첫 번째 값 중 최대값을 결과에 추가
            results.push_back(max(row1[0], row2[0]));
            continue;
        }

        // 두 열 전과 한 열 전의 결과를 저장할 변수 초기화
        vector<int> dpPrev(2, 0); // dp[i-2] 초기값
        vector<int> dpCurr = {row1[0], row2[0]}; // dp[i-1] 초기값

        // 두 번째 열부터 마지막 열까지 반복
        for (int i = 1; i < n; i++) {
            vector<int> newDp = {
                max(dpCurr[1], dpPrev[1]) + row1[i], // 위쪽 행의 현재 열
                max(dpCurr[0], dpPrev[0]) + row2[i]  // 아래쪽 행의 현재 열
            };
            dpPrev = dpCurr; // 이전 값을 갱신
            dpCurr = newDp; // 현재 값을 갱신
        }

        // 마지막 열에서의 최대값을 결과에 추가
        results.push_back(max(dpCurr[0], dpCurr[1]));
    }

    return results;
}

int main() {
    int t; // 테스트 케이스 개수
    cin >> t;
    vector<pair<vector<int>, vector<int>>> testCases;

    // 각 테스트 케이스 입력
    for (int i = 0; i < t; i++) {
        int n; // 열의 개수
        cin >> n;
        vector<int> row1(n), row2(n);

        for (int j = 0; j < n; j++) {
            cin >> row1[j]; // 위쪽 행 입력
        }
        for (int j = 0; j < n; j++) {
            cin >> row2[j]; // 아래쪽 행 입력
        }

        testCases.emplace_back(row1, row2); // 각 테스트 케이스를 페어로 저장
    }

    vector<int> results = maxStickerScore(testCases); // 최대 점수 계산

    // 결과 출력
    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}
