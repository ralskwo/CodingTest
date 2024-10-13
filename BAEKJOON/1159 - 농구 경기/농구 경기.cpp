#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;  // 선수의 수 입력
    vector<string> players(n);  // 선수들의 성을 저장할 벡터
    unordered_map<char, int> first_letter_count;  // 성의 첫 글자를 카운트할 딕셔너리

    // 선수들의 성 입력 및 첫 글자 카운트
    for (int i = 0; i < n; ++i) {
        cin >> players[i];  // 선수의 성 입력
        char first_letter = players[i][0];  // 성의 첫 글자 추출
        first_letter_count[first_letter]++;  // 해당 첫 글자의 출현 횟수 증가
    }

    vector<char> result;  // 5명 이상인 성의 첫 글자를 저장할 벡터

    // 딕셔너리에서 5명 이상인 첫 글자를 추출
    for (auto& entry : first_letter_count) {
        if (entry.second >= 5) {  // 출현 횟수가 5 이상인 경우
            result.push_back(entry.first);  // 첫 글자를 결과에 추가
        }
    }

    if (!result.empty()) {
        sort(result.begin(), result.end());  // 결과를 사전순으로 정렬
        for (char c : result) {
            cout << c;  // 사전순으로 정렬된 첫 글자를 출력
        }
        cout << endl;
    } else {
        cout << "PREDAJA" << endl;  // 조건을 만족하는 첫 글자가 없을 경우
    }

    return 0;
}