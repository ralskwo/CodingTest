#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// 함수 정의 및 행 상태를 세는 함수
int maxOnRows(int N, int M, vector<string>& lampStates, int K) {
    unordered_map<string, int> rowCount;  // 각 행 상태의 출현 횟수를 저장하는 해시맵
    int maxOn = 0;  // 최대 켜진 행의 수를 저장할 변수

    // 각 행의 상태를 카운팅
    for (const auto& row : lampStates) {
        rowCount[row]++;
    }

    // 각 행 상태에 대해 반복
    for (const auto& [row, count] : rowCount) {
        int zeroCount = count_if(row.begin(), row.end(), [](char c) { return c == '0'; });  // 행에서 0의 개수를 셈

        // 조건 확인: zeroCount가 K보다 작거나 같고, (K - zeroCount)가 짝수여야 함
        if (zeroCount <= K && (K - zeroCount) % 2 == 0) {
            maxOn = max(maxOn, count);  // 조건을 만족하면 maxOn을 갱신
        }
    }

    return maxOn;  // 최대 켜진 행의 수 반환
}

int main() {
    int N, M, K;
    cin >> N >> M;  // N과 M 입력받기
    vector<string> lampStates(N);

    // 램프 상태 입력받기
    for (int i = 0; i < N; i++) {
        cin >> lampStates[i];
    }

    cin >> K;  // K 입력받기

    // 결과 계산 및 출력
    cout << maxOnRows(N, M, lampStates, K) << endl;

    return 0;
}
