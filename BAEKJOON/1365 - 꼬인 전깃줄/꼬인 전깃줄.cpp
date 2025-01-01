#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 가장 긴 증가하는 부분 수열(LIS)을 구하는 함수
int minimum_cut_wires(int N, vector<int>& poles) {
    vector<int> lis;  // LIS를 저장하는 벡터

    for (int i = 0; i < N; i++) {
        // 이분 탐색으로 poles[i]가 들어갈 위치를 찾음
        auto pos = lower_bound(lis.begin(), lis.end(), poles[i]);

        if (pos == lis.end()) {
            // LIS의 끝에 위치하면 새로운 요소 추가
            lis.push_back(poles[i]);
        } else {
            // 이미 LIS에 포함된 경우 해당 위치 값을 갱신
            *pos = poles[i];
        }
    }

    // 전체 전봇대에서 LIS 길이를 뺀 값이 잘라야 할 전선 개수
    return N - lis.size();
}

int main() {
    int N;  // 전봇대의 개수
    cin >> N;

    vector<int> poles(N);  // 전봇대 연결 상태 저장
    for (int i = 0; i < N; i++) {
        cin >> poles[i];  // 전봇대 연결 상태 입력
    }

    cout << minimum_cut_wires(N, poles) << endl;  // 결과 출력
    return 0;
}
