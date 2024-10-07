#include <iostream>
#include <vector>
using namespace std;

// 0부터 9까지의 숫자가 1부터 n까지 몇 번 등장하는지 세는 함수
vector<int> count_digits(long long n) {
    // n이 0 이하일 경우 모든 숫자 등장 횟수는 0으로 초기화된 리스트 반환
    if (n <= 0) return vector<int>(10, 0);

    // n을 문자열로 변환하여 자리수 확인 (C++에서는 문자열로 변환 후 길이 계산)
    string str_n = to_string(n);
    int length = str_n.length();

    // 0부터 9까지의 각 숫자의 등장 횟수를 저장할 벡터 초기화
    vector<int> counts(10, 0);

    // n의 각 자리수에 대해 등장 빈도를 계산
    for (int i = 0; i < length; i++) {
        // 현재 자리의 숫자를 정수형으로 변환하여 저장
        int curr = str_n[i] - '0';  // char를 int로 변환 (ASCII 값 차이로 계산)
        
        // 현재 자리의 자릿값을 계산 (예: 천의 자리면 1000)
        long long place_value = 1;
        for (int j = 0; j < length - i - 1; j++) place_value *= 10;

        // 현재 자리보다 앞의 모든 완전한 세트에서의 숫자 빈도를 계산
        for (int digit = 0; digit < 10; digit++) {
            counts[digit] += (n / (place_value * 10)) * place_value;
        }

        // 현재 자리의 숫자보다 작은 숫자들의 등장 횟수를 추가
        for (int digit = 0; digit < curr; digit++) {
            counts[digit] += place_value;
        }

        // 현재 자릿수의 숫자가 등장하는 횟수를 더해줌
        counts[curr] += (n % place_value) + 1;

        // 0은 맨 앞자리에 올 수 없으므로, 보정 작업을 수행
        counts[0] -= place_value;
    }

    // 최종적으로 0부터 9까지의 숫자 빈도 벡터 반환
    return counts;
}

int main() {
    // 사용자로부터 숫자 입력 받기
    long long N;
    cin >> N;

    // 0부터 9까지의 숫자 등장 횟수 계산
    vector<int> result = count_digits(N);

    // 결과를 공백으로 구분하여 출력
    for (int i = 0; i < 10; i++) {
        if (i != 0) cout << " ";
        cout << result[i];
    }
    cout << endl;

    return 0;
}
