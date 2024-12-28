#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 최대 합을 구하는 함수
int max_sequence_sum(vector<int>& nums) {
    vector<int> positive;  // 양수를 저장하는 리스트
    vector<int> negative;  // 음수와 0을 저장하는 리스트
    int result = 0;  // 최종 결과값을 저장하는 변수

    // 주어진 수열을 순회하며 분류
    for (int num : nums) {
        if (num > 1) {  
            positive.push_back(num);  // 1보다 큰 양수는 positive 리스트에 저장
        } else if (num == 1) {
            result += 1;  // 1은 바로 더하는 것이 유리
        } else {
            negative.push_back(num);  // 음수와 0은 negative 리스트에 저장
        }
    }

    // 양수는 내림차순으로 정렬 (큰 것부터 묶기 위해)
    sort(positive.begin(), positive.end(), greater<int>());
    // 음수는 오름차순으로 정렬 (작은 것부터 묶기 위해)
    sort(negative.begin(), negative.end());

    // 양수 묶기
    int i = 0;
    while (i + 1 < positive.size()) {  // 인덱스 초과 방지
        result += positive[i] * positive[i + 1];  // 두 개씩 묶어 곱한 결과를 더함
        i += 2;  // 두 개씩 묶었으므로 인덱스를 2 증가
    }
    // 묶지 못하고 남은 양수 처리
    if (i < positive.size()) {
        result += positive[i];  // 남은 양수는 그대로 더함
    }

    // 음수 묶기
    i = 0;
    while (i + 1 < negative.size()) {  // 인덱스 초과 방지
        result += negative[i] * negative[i + 1];  // 두 개씩 묶어 곱한 결과를 더함
        i += 2;  // 두 개씩 묶었으므로 인덱스를 2 증가
    }
    // 묶지 못하고 남은 음수 처리
    if (i < negative.size()) {
        if (find(nums.begin(), nums.end(), 0) != nums.end()) {
            result += 0;  // 0이 있는 경우 음수와 묶어 상쇄
        } else {
            result += negative[i];  // 0이 없으면 음수를 그대로 더함
        }
    }

    return result;  // 최종 결과 반환
}

int main() {
    int n;
    cin >> n;  // 수열의 크기 입력
    vector<int> nums(n);  // 수열을 저장할 벡터
    for (int i = 0; i < n; i++) {
        cin >> nums[i];  // 수열의 각 수 입력
    }
    cout << max_sequence_sum(nums) << endl;  // 결과 출력
    return 0;
}
