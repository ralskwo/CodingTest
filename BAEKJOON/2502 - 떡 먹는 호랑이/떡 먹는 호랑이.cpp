#include <iostream>
#include <vector>
using namespace std;

// A와 B를 계산하는 함수
pair<int, int> findAandB(int D, int K) {
    // 계수 배열 초기화
    vector<pair<int, int>> coeff(D + 1);
    coeff[1] = {1, 0}; // 첫째 날: A의 계수만 1
    coeff[2] = {0, 1}; // 둘째 날: B의 계수만 1

    // 점화식을 기반으로 D일까지의 계수를 계산
    for (int i = 3; i <= D; ++i) {
        coeff[i].first = coeff[i - 2].first + coeff[i - 1].first; // A의 계수
        coeff[i].second = coeff[i - 2].second + coeff[i - 1].second; // B의 계수
    }

    // A와 B를 찾기 위해 가능한 A를 1부터 탐색
    for (int A = 1; A <= K / coeff[D].first; ++A) {
        // 남은 값이 B 계수로 나누어떨어지는지 확인
        if ((K - A * coeff[D].first) % coeff[D].second == 0) {
            int B = (K - A * coeff[D].first) / coeff[D].second; // B 계산
            return {A, B}; // A와 B 반환
        }
    }

    return {-1, -1}; // 이 경우는 문제에서 주어지지 않음
}

int main() {
    int D, K;
    cin >> D >> K; // 입력값 받기

    pair<int, int> result = findAandB(D, K); // 계산된 A와 B 받기

    cout << result.first << endl; // 첫째 날 떡 개수 출력
    cout << result.second << endl; // 둘째 날 떡 개수 출력

    return 0;
}
