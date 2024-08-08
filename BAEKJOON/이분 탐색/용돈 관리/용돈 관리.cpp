#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// 도우미 함수: 주어진 금액 k로 M번 이하로 인출이 가능한지 확인
bool can_withdraw_with_k(int k, const vector<int>& daily_usage, int N, int M) {
    int count = 1;  // 인출 횟수
    int current_sum = 0;  // 현재 인출한 금액의 합

    for (int usage : daily_usage) {
        if (current_sum + usage > k) {  // 현재 인출 금액에 오늘 사용할 금액을 더했을 때 k를 초과하면
            count++;  // 인출 횟수를 증가시킨다
            current_sum = usage;  // 현재 인출 금액을 오늘 사용할 금액으로 초기화
            if (count > M) {  // 인출 횟수가 M을 초과하면
                return false;  // false를 반환하여 주어진 k로 인출이 불가능함을 알린다
            }
        } else {
            current_sum += usage;  // k를 초과하지 않으면 현재 인출 금액에 오늘 사용할 금액을 더한다
        }
    }

    return true;  // 모든 사용 금액을 k 이내에서 M번 이하로 인출할 수 있으면 true를 반환
}

// 이분 탐색 함수: 최소 금액 K를 찾음
int find_minimum_k(int N, int M, const vector<int>& daily_usage) {
    int low = *max_element(daily_usage.begin(), daily_usage.end());  // 최소 금액 K의 초기값은 매일 사용하는 금액 중 최대값으로 설정
    int high = accumulate(daily_usage.begin(), daily_usage.end(), 0);  // 최대 금액 K의 초기값은 모든 날의 사용 금액의 합으로 설정

    while (low < high) {  // 이분 탐색을 통해 적절한 K를 찾는다
        int mid = (low + high) / 2;  // 중간값을 계산
        if (can_withdraw_with_k(mid, daily_usage, N, M)) {  // 중간값으로 인출이 가능한지 확인
            high = mid;  // 가능하면 상한값을 중간값으로 설정
        } else {
            low = mid + 1;  // 불가능하면 하한값을 중간값+1로 설정
        }
    }

    return low;  // 최소 금액 K를 반환
}

int main() {
    int N, M;
    cin >> N >> M;  // 첫 번째 줄의 첫 번째 숫자는 N, 두 번째 숫자는 M
    vector<int> daily_usage(N);

    for (int i = 0; i < N; ++i) {
        cin >> daily_usage[i];  // 나머지 숫자들은 매일 사용할 금액
    }

    // 최소 금액 K 계산
    int minimum_k = find_minimum_k(N, M, daily_usage);

    // 출력
    cout << minimum_k << endl;  // 최소 금액 K를 출력

    return 0;
}
