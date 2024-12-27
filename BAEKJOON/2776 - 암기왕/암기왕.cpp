#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);  // 입출력 속도 향상을 위해 iostream의 동기화를 끊음
    cin.tie(0);                   // cin과 cout의 묶음을 풀어 입출력 속도를 높임

    int T;                        // 테스트 케이스 개수
    cin >> T;                     // 테스트 케이스 입력 받음

    while (T--) {                 // T번 반복
        int N, M;                 // 수첩1(N)과 수첩2(M)의 크기
        cin >> N;

        unordered_set<int> notebook1;  // 수첩1을 저장할 해시셋(중복 없이 저장, 빠른 탐색 가능)
        int number;

        // N개의 정수를 수첩1에 저장
        for (int i = 0; i < N; i++) {
            cin >> number;
            notebook1.insert(number);  // 집합에 삽입
        }

        cin >> M;
        vector<int> results;           // 결과를 저장할 벡터

        // 수첩2의 M개의 정수를 확인하고 결과를 저장
        for (int i = 0; i < M; i++) {
            cin >> number;
            if (notebook1.find(number) != notebook1.end()) {
                results.push_back(1);  // 존재하면 1
            } else {
                results.push_back(0);  // 존재하지 않으면 0
            }
        }

        // 결과 출력
        for (int result : results) {
            cout << result << '\n';
        }
    }

    return 0;
}
