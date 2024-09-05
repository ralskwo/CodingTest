#include <iostream>
#include <deque>
#include <cstdio>  // scanf, printf 사용을 위한 헤더
using namespace std;

int main() {
    int N, L;

    // N: 수열의 길이, L: 슬라이딩 윈도우의 크기 입력
    scanf("%d %d", &N, &L);

    int A[N];

    // 수열 A 입력
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    // 슬라이딩 윈도우의 최솟값을 찾기 위한 덱
    deque<int> dq;

    // 결과값을 저장하는 처리
    for (int i = 0; i < N; i++) {
        // 덱의 첫 번째 요소가 현재 윈도우 범위를 벗어나면 제거
        if (!dq.empty() && dq.front() < i - L + 1) {
            dq.pop_front();
        }

        // 새로운 값이 들어올 때, 덱의 마지막 값이 현재 값보다 크면 제거
        while (!dq.empty() && A[dq.back()] > A[i]) {
            dq.pop_back();
        }

        // 현재 인덱스를 덱에 추가
        dq.push_back(i);

        // 현재 윈도우에서의 최솟값 출력
        printf("%d ", A[dq.front()]);
    }

    return 0;
}
