#include <iostream>
#include <vector>
#include <algorithm> // max 함수를 사용하기 위해 포함
using namespace std;

int main() {
    // N: 전체 날짜의 수, K: 연속된 날짜의 수
    int N, K;
    cin >> N >> K;

    // 온도를 저장할 벡터
    vector<int> temperatures(N);

    // 온도 입력
    for (int i = 0; i < N; i++) {
        cin >> temperatures[i];
    }

    // 초기 K일의 합을 계산
    int current_sum = 0;
    for (int i = 0; i < K; i++) {
        current_sum += temperatures[i];
    }

    // 최대값을 현재 합으로 초기화
    int max_sum = current_sum;

    // 슬라이딩 윈도우를 사용하여 최대값 계산
    for (int i = K; i < N; i++) {
        // 현재 합에서 맨 앞 값을 빼고 새 값을 더함
        current_sum = current_sum - temperatures[i - K] + temperatures[i];
        // 최대값 갱신
        max_sum = max(max_sum, current_sum);
    }

    // 최대값 출력
    cout << max_sum << endl;

    return 0;
}