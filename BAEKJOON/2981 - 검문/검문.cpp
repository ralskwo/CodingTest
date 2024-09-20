#include <iostream>  // 입출력 처리를 위한 헤더
#include <vector>    // 벡터를 사용하기 위한 헤더
#include <algorithm> // 정렬, 최대공약수, 약수 계산을 위한 헤더
#include <cmath>     // 수학 계산을 위한 헤더

using namespace std;

// 최대 공약수를 구하는 함수
int gcd(int a, int b) {
    while (b) {  // b가 0이 될 때까지 반복
        int temp = a % b;  // a를 b로 나눈 나머지를 구함
        a = b;  // a에 b 값을 대입
        b = temp;  // b에 나머지를 대입
    }
    return a;  // 최대 공약수를 반환
}

// 주어진 수의 약수를 구하는 함수
vector<int> find_divisors(int num) {
    vector<int> divisors;  // 약수를 저장할 벡터
    for (int i = 2; i <= sqrt(num); i++) {  // 2부터 num의 제곱근까지 반복
        if (num % i == 0) {  // i가 num의 약수인지 확인
            divisors.push_back(i);  // i를 약수로 추가
            if (i != num / i) {  // i와 num / i가 다르면 num / i도 약수
                divisors.push_back(num / i);  // num / i를 약수로 추가
            }
        }
    }
    divisors.push_back(num);  // num 자신을 약수로 추가
    sort(divisors.begin(), divisors.end());  // 약수를 오름차순으로 정렬
    return divisors;  // 약수 리스트를 반환
}

int main() {
    int n;  // 입력받을 수의 개수
    cin >> n;  // 첫 번째 줄에서 수의 개수를 입력받음
    
    vector<int> numbers(n);  // 입력받은 수를 저장할 벡터
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];  // 각각의 수를 입력받음
    }

    sort(numbers.begin(), numbers.end());  // 숫자들을 오름차순으로 정렬

    int g = numbers[1] - numbers[0];  // 첫 번째와 두 번째 수의 차이로 g를 초기화
    for (int i = 2; i < n; i++) {
        g = gcd(g, numbers[i] - numbers[i - 1]);  // 차이들의 최대 공약수를 구함
    }

    vector<int> result = find_divisors(g);  // g의 약수를 구함

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";  // 약수들을 공백으로 구분하여 출력
    }
    
    return 0;  // 프로그램 종료
}
