#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// 모든 가능한 수식을 생성하는 재귀 함수
void generateExpressions(int n, string currentExpr, vector<string> &results, int currentNum) {
    // 수식이 완성된 경우
    if (currentNum > n) {
        string evalExpr = currentExpr;
        evalExpr.erase(remove(evalExpr.begin(), evalExpr.end(), ' '), evalExpr.end());
        // 공백 제거 후 수식을 계산
        int result = 0, term = 0, sign = 1;
        for (char c : evalExpr) {
            if (isdigit(c)) {
                term = term * 10 + (c - '0');
            } else {
                result += sign * term;
                term = 0;
                sign = (c == '+' ? 1 : -1);
            }
        }
        result += sign * term;
        // 결과가 0이면 결과 리스트에 추가
        if (result == 0) results.push_back(currentExpr);
        return;
    }

    // 다음 숫자를 생성하며 '+' 연산 추가
    generateExpressions(n, currentExpr + "+" + to_string(currentNum), results, currentNum + 1);
    // 다음 숫자를 생성하며 '-' 연산 추가
    generateExpressions(n, currentExpr + "-" + to_string(currentNum), results, currentNum + 1);
    // 다음 숫자를 생성하며 공백 추가
    generateExpressions(n, currentExpr + " " + to_string(currentNum), results, currentNum + 1);
}

// 메인 함수
int main() {
    int t;
    cin >> t; // 테스트 케이스의 개수를 입력받음
    while (t--) {
        int n;
        cin >> n; // 테스트 케이스의 N을 입력받음
        vector<string> results;
        generateExpressions(n, "1", results, 2); // 숫자 1로 시작하는 수식 생성
        sort(results.begin(), results.end()); // 결과를 ASCII 순서로 정렬
        for (const string &expr : results) {
            cout << expr << endl; // 각 수식을 출력
        }
        if (t > 0) cout << endl; // 테스트 케이스 사이에 빈 줄 추가
    }
    return 0;
}