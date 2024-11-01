#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

int maxSubstringLength(int n, const string& s) {
    int left = 0; // 왼쪽 포인터 초기화
    unordered_map<char, int> charCount; // 각 문자의 개수를 저장할 해시맵 초기화
    int maxLen = 0; // 최대 길이 변수 초기화

    // 오른쪽 포인터를 사용하여 문자열 순회
    for (int right = 0; right < s.size(); ++right) {
        charCount[s[right]]++; // 현재 문자를 해시맵에 추가하고 개수 증가

        // 고유 문자 수가 n을 초과하면 윈도우를 축소
        while (charCount.size() > n) {
            charCount[s[left]]--; // 왼쪽 포인터의 문자 개수 감소
            if (charCount[s[left]] == 0) {
                charCount.erase(s[left]); // 문자 개수가 0이 되면 해시맵에서 삭제
            }
            left++; // 왼쪽 포인터를 오른쪽으로 이동하여 윈도우 축소
        }

        // 최대 길이 갱신
        maxLen = max(maxLen, right - left + 1);
    }

    return maxLen; // 최종 결과 반환
}

int main() {
    int n;
    string s;

    // 입력 처리
    cin >> n >> s;

    // 결과 계산 및 출력
    cout << maxSubstringLength(n, s) << endl;

    return 0;
}