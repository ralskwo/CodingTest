#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // N: 수열의 길이, S: 목표 부분합
    int N, S;
    cin >> N >> S;

    // 수열을 저장할 벡터
    vector<int> numbers(N);
    for (int i = 0; i < N; i++) {
        cin >> numbers[i];  // 수열의 각 원소 입력
    }

    // 슬라이딩 윈도우의 두 포인터와 부분합
    int start = 0, end = 0, current_sum = 0;
    int min_length = N + 1;  // 최소 길이 초기화, N보다 큰 값으로 설정

    // 슬라이딩 윈도우 탐색 시작
    while (true) {
        if (current_sum >= S) {
            // 현재 부분합이 S 이상일 때, 최소 길이 갱신
            min_length = min(min_length, end - start);
            current_sum -= numbers[start];  // 시작 지점의 값을 부분합에서 제외
            start++;  // 시작 포인터 오른쪽으로 이동
        } else if (end == N) {
            // 끝 포인터가 수열 끝에 도달하면 종료
            break;
        } else {
            // 부분합이 S보다 작으면 끝 포인터 확장
            current_sum += numbers[end];
            end++;
        }
    }

    // 부분합을 만족하는 최소 길이를 출력, 없으면 0 출력
    if (min_length == N + 1) {
        cout << 0 << endl;  // 불가능한 경우
    } else {
        cout << min_length << endl;  // 가능한 경우
    }

    return 0;
}
