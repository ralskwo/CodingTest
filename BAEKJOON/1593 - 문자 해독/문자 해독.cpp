#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    int g, s_len;
    cin >> g >> s_len; // 단어 W의 길이 g와 문자열 S의 길이 s_len 입력
    string W, S;
    cin >> W >> S; // 단어 W와 문자열 S 입력

    unordered_map<char, int> w_count, window_count;

    // 단어 W의 문자 빈도 계산
    for (char c : W) {
        w_count[c]++;
    }

    // 문자열 S의 첫 g개의 문자 빈도 계산
    for (int i = 0; i < g; i++) {
        window_count[S[i]]++;
    }

    int count = 0; // 조건을 만족하는 경우의 수 저장 변수

    // 첫 번째 윈도우 검사
    if (w_count == window_count) {
        count++;
    }

    // 슬라이딩 윈도우 탐색
    for (int i = g; i < s_len; i++) {
        char start_char = S[i - g]; // 윈도우에서 빠지는 문자
        char end_char = S[i];      // 윈도우에서 추가되는 문자

        window_count[end_char]++;   // 새로 추가된 문자의 빈도 증가
        window_count[start_char]--; // 제외된 문자의 빈도 감소

        if (window_count[start_char] == 0) {
            window_count.erase(start_char); // 빈도가 0이 되면 맵에서 제거
        }

        if (w_count == window_count) {
            count++; // 현재 윈도우가 조건을 만족하면 count 증가
        }
    }

    cout << count << endl; // 조건을 만족하는 부분 문자열 개수 출력
    return 0;
}
