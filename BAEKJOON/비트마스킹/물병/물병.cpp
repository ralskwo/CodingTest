#include <iostream>
using namespace std;

// 이진수로 변환된 숫자에서 1의 개수를 세는 함수
int count_set_bits(int x) {
    int count = 0;
    while (x > 0) {
        if (x % 2 == 1)
            count++;
        x /= 2;
    }
    return count;
}

// 최소 추가 물병의 수를 계산하는 함수
int min_bottle_purchase(int N, int K) {
    // 추가로 구매할 물병의 수 초기화
    int purchase_count = 0;

    // N의 물병 개수에서 1의 개수가 K 이하가 될 때까지 반복
    while (count_set_bits(N) > K) {
        // 물병을 하나 추가 구매하여 N을 1 증가
        N += 1;
        // 구매한 물병의 수를 증가
        purchase_count += 1;
    }

    // 필요한 최소 추가 물병의 수를 반환
    return purchase_count;
}

int main() {
    int N, K;
    
    // 입력 값을 받아 N과 K로 분리
    cin >> N >> K;

    // 결과를 계산하여 출력
    int result = min_bottle_purchase(N, K);
    cout << result << endl;

    return 0;
}
