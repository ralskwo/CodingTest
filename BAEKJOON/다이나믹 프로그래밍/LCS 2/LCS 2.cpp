#include <iostream>
#include <vector>
#include <string>

using namespace std;

// LCS 함수 정의
pair<int, string> lcs(const string& X, const string& Y) {
    int m = X.length();  // 첫 번째 문자열의 길이
    int n = Y.length();  // 두 번째 문자열의 길이

    // DP 테이블 생성 (0으로 초기화된 (m+1)x(n+1) 배열)
    vector<vector<int>> L(m + 1, vector<int>(n + 1, 0));

    // DP 테이블 채우기
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (X[i - 1] == Y[j - 1]) {
                L[i][j] = L[i - 1][j - 1] + 1;  // 문자가 같으면 대각선 위 + 1
            } else {
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);  // 문자가 다르면 위 또는 왼쪽 값 중 큰 값
            }
        }
    }

    // LCS의 길이
    int length_of_lcs = L[m][n];

    // LCS 문자열 구성 (역추적)
    int index = L[m][n];
    string lcs(index, ' ');  // LCS 문자열을 저장할 리스트
    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs[index - 1] = X[i - 1];  // 공통 문자를 LCS 리스트에 저장
            --i;
            --j;
            --index;
        } else if (L[i - 1][j] > L[i][j - 1]) {
            --i;  // 위쪽 값이 더 크면 위로 이동
        } else {
            --j;  // 왼쪽 값이 더 크면 왼쪽으로 이동
        }
    }

    return {length_of_lcs, lcs};  // LCS의 길이와 LCS 문자열을 반환
}

int main() {
    // 입력 받기
    string X, Y;
    getline(cin, X);
    getline(cin, Y);

    // 함수 호출 및 결과 출력
    auto result = lcs(X, Y);
    int length_of_lcs = result.first;
    string lcs_str = result.second;

    cout << length_of_lcs << endl;  // LCS의 길이 출력
    if (length_of_lcs > 0) {
        cout << lcs_str << endl;  // LCS 문자열 출력
    }

    return 0;
}
