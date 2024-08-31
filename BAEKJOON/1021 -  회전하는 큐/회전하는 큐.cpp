#include <iostream>   // 표준 입출력 사용
#include <deque>      // deque 자료구조 사용
#include <algorithm>  // min 함수 사용

using namespace std;

int min_operations(int n, int m, deque<int>& positions) {
    deque<int> dq;  // 큐를 초기화할 deque 선언
    for (int i = 1; i <= n; i++) {
        dq.push_back(i);  // 1부터 n까지의 숫자를 큐에 추가
    }

    int operations = 0;  // 연산 횟수를 저장할 변수

    for (int i = 0; i < m; i++) {
        int position = positions[i];  // 뽑아낼 목표 위치
        int idx = find(dq.begin(), dq.end(), position) - dq.begin();  // 목표 위치의 인덱스를 찾음

        if (idx < dq.size() - idx) {  // 왼쪽으로 회전하는 것이 빠른 경우
            operations += idx;  // 왼쪽으로 회전한 횟수를 누적
            while (idx--) {
                dq.push_back(dq.front());  // 큐의 맨 앞 원소를 맨 뒤로 이동
                dq.pop_front();  // 맨 앞 원소 제거
            }
        } else {  // 오른쪽으로 회전하는 것이 빠른 경우
            operations += dq.size() - idx;  // 오른쪽으로 회전한 횟수를 누적
            int rotations = dq.size() - idx;
            while (rotations--) {
                dq.push_front(dq.back());  // 큐의 맨 뒤 원소를 맨 앞으로 이동
                dq.pop_back();  // 맨 뒤 원소 제거
            }
        }

        dq.pop_front();  // 목표 위치의 원소를 큐에서 제거
    }

    return operations;  // 총 연산 횟수를 반환
}

int main() {
    int n, m;  // 큐의 크기 n과 뽑아낼 위치의 수 m
    cin >> n >> m;

    deque<int> positions(m);  // 뽑아낼 위치를 저장할 deque
    for (int i = 0; i < m; i++) {
        cin >> positions[i];  // 뽑아낼 위치 입력
    }

    cout << min_operations(n, m, positions) << endl;  // 최소 연산 횟수를 계산하고 출력
    return 0;
}
