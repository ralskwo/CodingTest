#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 가능한 광고 길이를 찾는 함수
int shortest_ad_length(int L, const string& ad) {
    // KMP 실패 함수 배열 초기화
    vector<int> failure(L, 0);
    int j = 0; // 접두사와 접미사의 일치 길이 추적

    // KMP 실패 함수 계산
    for (int i = 1; i < L; i++) {
        // j가 0보다 크고 현재 문자와 일치하지 않을 경우, 이전 실패 함수 값으로 j 갱신
        while (j > 0 && ad[i] != ad[j]) {
            j = failure[j - 1];
        }
        // 현재 문자가 일치하는 경우, j를 증가시키고 failure 배열에 j 값을 저장
        if (ad[i] == ad[j]) {
            j++;
            failure[i] = j;
        }
    }

    // 반복되는 최소 광고 길이 계산 후 반환
    return L - failure[L - 1];
}

int main() {
    int L; // 광고판의 크기
    string ad; // 현재 광고판에 보이는 문자열

    // 입력 받기
    cin >> L; // 광고판의 크기 입력
    cin >> ad; // 광고판에 보이는 문자열 입력

    // 가능한 가장 짧은 광고 길이 출력
    cout << shortest_ad_length(L, ad) << endl;

    return 0;
}