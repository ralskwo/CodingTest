#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int T; // 테스트 케이스의 수
    cin >> T;
    
    while (T--) {
        int N, M, K; // 집의 개수, 연속된 집의 개수, 방범장치 조건
        cin >> N >> M >> K;
        
        vector<int> money(N); // 각 집의 돈 정보를 저장할 벡터
        for (int i = 0; i < N; i++) {
            cin >> money[i]; // 각 집의 돈 정보 입력
        }

        // 특수 케이스 처리: M == N인 경우
        if (M == N) {
            int totalSum = 0; // 모든 집의 돈 합을 계산
            for (int i = 0; i < N; i++) {
                totalSum += money[i];
            }
            cout << (totalSum < K ? 1 : 0) << endl; // 조건에 따라 출력
            continue;
        }

        // 슬라이딩 윈도우 초기화
        int currentSum = 0;
        for (int i = 0; i < M; i++) {
            currentSum += money[i]; // 처음 M개의 합을 계산
        }

        int count = 0; // 조건을 만족하는 경우의 수

        // 슬라이딩 윈도우 실행
        for (int i = 0; i < N; i++) {
            if (currentSum < K) {
                count++; // 조건을 만족하면 카운트 증가
            }
            
            // 윈도우 이동: 첫 번째 값 제거, 새로운 값 추가
            currentSum -= money[i];
            currentSum += money[(i + M) % N]; // 원형 배열 처리
        }

        cout << count << endl; // 결과 출력
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); // 입출력 최적화
    solve(); // 문제 해결 함수 호출
    return 0;
}
