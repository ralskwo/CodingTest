#include <iostream>
#include <vector>
using namespace std;

// 에라토스테네스의 체를 사용하여 1000 이하의 소수를 구하는 함수
vector<bool> sieve_of_eratosthenes(int max_num) {
    // max_num + 1 크기의 벡터를 생성하고, 모든 값을 true로 초기화
    vector<bool> sieve(max_num + 1, true);
    sieve[0] = sieve[1] = false; // 0과 1은 소수가 아니므로 false로 설정

    // 2부터 시작하여 max_num의 제곱근까지 반복
    for (int i = 2; i * i <= max_num; i++) {
        if (sieve[i]) { // i가 소수인 경우
            // i의 배수들을 false로 설정 (즉, 소수가 아님)
            for (int j = i * i; j <= max_num; j += i) {
                sieve[j] = false;
            }
        }
    }
    return sieve; // 소수 여부를 나타내는 벡터 반환
}

int main() {
    int N;
    cin >> N; // N개의 수를 입력받음

    vector<int> numbers(N); // N개의 수를 저장할 벡터
    for (int i = 0; i < N; i++) {
        cin >> numbers[i]; // N개의 수를 벡터에 입력받음
    }

    int max_num = 1000; // 문제에서 주어진 수의 최대값 1000
    vector<bool> sieve = sieve_of_eratosthenes(max_num); // 1000 이하의 소수 구하기

    int prime_count = 0; // 소수의 개수를 세기 위한 변수
    for (int i = 0; i < N; i++) {
        if (sieve[numbers[i]]) { // 주어진 수가 소수라면
            prime_count++; // 소수의 개수를 증가시킴
        }
    }

    cout << prime_count << endl; // 소수의 개수를 출력
    return 0;
}
