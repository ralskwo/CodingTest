#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

pair<int, int> find_closest_to_zero(vector<int>& arr) {
    int n = arr.size(); // 배열의 크기를 변수 n에 저장
    int left = 0; // 시작 포인터를 배열의 첫 번째 요소에 설정
    int right = n - 1; // 끝 포인터를 배열의 마지막 요소에 설정
    int closest_sum = numeric_limits<int>::max(); // 0에 가장 가까운 합을 저장할 변수, 초기값은 무한대
    pair<int, int> answer = {arr[left], arr[right]}; // 가장 가까운 합을 만드는 두 요소의 값을 저장할 변수

    while (left < right) { // 두 포인터가 교차할 때까지 반복
        int current_sum = arr[left] + arr[right]; // 현재 두 포인터가 가리키는 요소의 합을 계산
        if (abs(current_sum) < abs(closest_sum)) { // 현재 합이 0에 더 가까운 경우
            closest_sum = current_sum; // 가장 가까운 합을 업데이트
            answer = {arr[left], arr[right]}; // 두 요소의 값을 업데이트
        }
        
        if (current_sum < 0) { // 현재 합이 0보다 작은 경우
            left++; // 시작 포인터를 오른쪽으로 이동
        } else { // 현재 합이 0보다 크거나 같은 경우
            right--; // 끝 포인터를 왼쪽으로 이동
        }
    }

    return answer; // 0에 가장 가까운 합을 만드는 두 요소의 값을 반환
}

int main() {
    int n; // 총 요소의 개수를 입력 받음
    cin >> n;
    vector<int> arr(n); // 요소들을 저장할 벡터 생성

    for (int i = 0; i < n; ++i) {
        cin >> arr[i]; // 각 요소를 입력 받아 벡터에 저장
    }

    // 0에 가장 가까운 합을 만드는 두 요소를 찾음
    pair<int, int> result = find_closest_to_zero(arr);
    cout << result.first << " " << result.second << endl; // 결과 출력

    return 0;
}
