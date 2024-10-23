#include <iostream>
#include <string>
#include <deque>
using namespace std;

string makeLargestNumber(int N, int K, const string& number) {
    // 결과를 저장할 deque를 초기화합니다.
    deque<char> dq;
    
    // 입력된 숫자의 각 자릿수를 순서대로 처리합니다.
    for (char num : number) {
        // deque가 비어있지 않고, 아직 제거할 수 있는 수가 남아 있으며,
        // deque의 마지막 수가 현재 수보다 작을 때 제거합니다.
        while (!dq.empty() && K > 0 && dq.back() < num) {
            dq.pop_back(); // 더 큰 수를 만들기 위해 작은 수를 제거합니다.
            K--; // 제거한 수의 개수를 1 줄입니다.
        }
        // 현재 수를 deque에 추가합니다.
        dq.push_back(num);
    }
    
    // 만약 K가 남아있다면, 뒤에서부터 K개의 숫자를 제거합니다.
    while (K > 0) {
        dq.pop_back();
        K--;
    }
    
    // deque에 있는 숫자들을 문자열로 합쳐서 반환합니다.
    string result(dq.begin(), dq.end());
    return result;
}

int main() {
    int N, K;
    string number;

    // 첫째 줄에서 N과 K를 입력받습니다.
    cin >> N >> K;
    // 둘째 줄에서 N자리 숫자를 입력받습니다.
    cin >> number;

    // K개의 수를 제거했을 때 얻을 수 있는 가장 큰 수를 출력합니다.
    cout << makeLargestNumber(N, K, number) << endl;

    return 0;
}