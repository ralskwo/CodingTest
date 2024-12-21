#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>  // accumulate 사용
#include <cmath>    // abs 사용

using namespace std;

// 유효한 문제 조합을 세는 함수
int countValidCombinations(int N, int L, int R, int X, vector<int>& A) {
    int count = 0;  // 조건을 만족하는 조합의 개수를 저장하는 변수 초기화

    // 부분 집합을 구하기 위한 비트 마스크 방식 (1부터 2^N - 1까지)
    for (int i = 1; i < (1 << N); i++) {
        vector<int> subset;  // 부분 집합을 저장할 벡터

        // 비트마스크를 사용해 부분 집합 생성
        for (int j = 0; j < N; j++) {
            if (i & (1 << j)) {
                subset.push_back(A[j]);  // j번째 요소를 부분 집합에 추가
            }
        }

        // 부분 집합이 두 개 이상의 문제를 포함해야 함
        if (subset.size() < 2) continue;

        // 부분 집합의 난이도 총합 계산
        int total = accumulate(subset.begin(), subset.end(), 0);

        // 가장 쉬운 문제와 어려운 문제 찾기
        int maxDiff = *max_element(subset.begin(), subset.end()) - 
                      *min_element(subset.begin(), subset.end());

        // 난이도 총합과 난이도 차이 조건 확인
        if (L <= total && total <= R && maxDiff >= X) {
            count++;  // 조건을 만족하면 카운트 증가
        }
    }
    return count;  // 조건을 만족하는 조합의 개수 반환
}

int main() {
    int N, L, R, X;
    cin >> N >> L >> R >> X;  // 문제의 개수, 최소/최대 난이도 합, 최소 난이도 차이 입력

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];  // 각 문제의 난이도 입력
    }

    // 유효한 문제 조합의 개수 계산 및 출력
    cout << countValidCombinations(N, L, R, X, A) << endl;
    return 0;
}
