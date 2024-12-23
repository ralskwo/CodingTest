#include <iostream>  // 표준 입출력 사용을 위한 헤더
#include <vector>    // 벡터 사용을 위한 헤더
#include <algorithm> // max_element, min_element 사용을 위한 헤더
#include <numeric>   // accumulate 함수 사용을 위한 헤더

using namespace std;

// 블루레이 개수를 계산하는 함수
int countBlurays(const vector<int>& lectures, int size) {
    int count = 1;  // 블루레이 개수 (최소 1개부터 시작)
    int total = 0;  // 현재 블루레이에 담긴 강의 길이 합

    for (int lecture : lectures) {
        // 현재 블루레이에 강의를 추가했을 때 크기를 초과하는 경우
        if (total + lecture > size) {
            count++;  // 새로운 블루레이 필요
            total = lecture;  // 현재 강의를 새로운 블루레이에 담음
        } else {
            total += lecture;  // 초과하지 않으면 현재 블루레이에 계속 추가
        }
    }
    return count;  // 사용된 블루레이 개수 반환
}

// 최소 블루레이 크기를 찾는 이분 탐색 함수
int findMinimumBluraySize(int n, int m, const vector<int>& lectures) {
    int left = *max_element(lectures.begin(), lectures.end());  // 가장 긴 강의 길이 (최소값)
    int right = accumulate(lectures.begin(), lectures.end(), 0);  // 모든 강의 길이의 합 (최대값)
    int answer = right;  // 정답을 저장할 변수, 초기값은 최대값으로 설정

    // 이분 탐색 수행
    while (left <= right) {
        int mid = (left + right) / 2;  // 블루레이 크기의 중간값 설정
        if (countBlurays(lectures, mid) <= m) {
            answer = mid;  // 블루레이 개수가 M개 이하이면 정답 갱신
            right = mid - 1;  // 더 작은 크기를 탐색
        } else {
            left = mid + 1;  // 블루레이 개수가 M개 초과하면 더 큰 크기를 탐색
        }
    }
    return answer;  // 최소 블루레이 크기 반환
}

int main() {
    int n, m;
    cin >> n >> m;  // 강의 개수와 블루레이 개수 입력
    vector<int> lectures(n);
    
    for (int i = 0; i < n; i++) {
        cin >> lectures[i];  // 각 강의 길이 입력
    }

    cout << findMinimumBluraySize(n, m, lectures) << endl;  // 최소 블루레이 크기 출력
    return 0;
}
