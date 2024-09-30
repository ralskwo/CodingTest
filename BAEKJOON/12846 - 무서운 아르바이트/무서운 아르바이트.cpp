#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

// 최대 이익을 계산하는 함수
long long maxProfit(int n, vector<int>& wages) {
    vector<int> left(n);  // 각 날에 대해 왼쪽으로 확장 가능한 최대 범위를 저장할 배열
    vector<int> right(n); // 각 날에 대해 오른쪽으로 확장 가능한 최대 범위를 저장할 배열
    stack<int> s;         // 스택을 이용하여 확장 가능한 범위를 계산하기 위한 스택

    // 왼쪽으로 확장 가능한 최대 범위를 계산
    for (int i = 0; i < n; i++) {
        while (!s.empty() && wages[s.top()] >= wages[i]) { // 현재 일급이 스택의 마지막 일급보다 작거나 같으면
            s.pop(); // 스택에서 제거하여 왼쪽 확장 불가능한 범위로 설정
        }
        left[i] = s.empty() ? 0 : s.top() + 1; // 왼쪽 확장 가능한 최대 범위 설정
        s.push(i); // 현재 위치를 스택에 추가
    }

    // 스택을 비워 오른쪽 범위 계산에 사용
    while (!s.empty()) s.pop();

    // 오른쪽으로 확장 가능한 최대 범위를 계산
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && wages[s.top()] >= wages[i]) { // 현재 일급이 스택의 마지막 일급보다 작거나 같으면
            s.pop(); // 스택에서 제거하여 오른쪽 확장 불가능한 범위로 설정
        }
        right[i] = s.empty() ? n - 1 : s.top() - 1; // 오른쪽 확장 가능한 최대 범위 설정
        s.push(i); // 현재 위치를 스택에 추가
    }

    long long max_profit = 0; // 최대 이익을 저장할 변수 초기화

    // 각 날에 대해 최대 이익을 계산
    for (int i = 0; i < n; i++) {
        long long current_profit = (long long)wages[i] * (right[i] - left[i] + 1); // 현재 날의 일급과 최대 일수로 이익 계산
        max_profit = max(max_profit, current_profit); // 최대 이익을 갱신
    }

    return max_profit; // 최종 최대 이익 반환
}

int main() {
    int n; // 일을 할 수 있는 날의 수
    cin >> n;

    vector<int> wages(n); // 각 날의 일급을 저장할 배열
    for (int i = 0; i < n; i++) {
        cin >> wages[i]; // 각 날의 일급 입력
    }

    cout << maxProfit(n, wages) << endl; // 최대 이익 계산 및 출력

    return 0;
}
