#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

// 전역 변수 선언
int K, N, F;
vector<set<int>> friends; // 각 학생의 친구를 저장하는 인접 리스트
vector<int> selected; // 선택된 학생 목록

// 백트래킹 함수
void backtrack(int start) {
    // 학생을 K명 선택한 경우, 결과 출력
    if (selected.size() == K) {
        sort(selected.begin(), selected.end()); // 학생 번호를 오름차순으로 정렬
        for (int s : selected) {
            cout << s << "\n"; // 한 줄씩 학생 번호 출력
        }
        exit(0); // 프로그램 종료 (가장 먼저 찾은 경우)
    }

    // start부터 N까지 학생을 확인하며 선발
    for (int i = start; i <= N; i++) {
        bool canSelect = true;

        // 현재 학생 i가 이미 선택된 모든 학생과 친구 관계인지 확인
        for (int s : selected) {
            if (friends[i].find(s) == friends[i].end()) {
                canSelect = false;
                break;
            }
        }

        // 선택이 가능한 경우 학생 i를 추가하고 재귀 호출
        if (canSelect) {
            selected.push_back(i);
            backtrack(i + 1);  // 다음 학생을 탐색
            selected.pop_back(); // 탐색이 끝난 후 되돌리기 (백트래킹)
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); // 입출력 속도 향상

    // 입력 처리
    cin >> K >> N >> F;
    friends.resize(N + 1); // 인접 리스트 초기화 (학생 번호 1부터 사용)

    // 친구 관계 입력
    for (int i = 0; i < F; i++) {
        int a, b;
        cin >> a >> b;
        friends[a].insert(b);
        friends[b].insert(a); // 양방향 친구 관계 설정
    }

    // 백트래킹 탐색 시작
    backtrack(1);

    // 조건을 만족하는 조합이 없는 경우
    cout << -1 << "\n";
    return 0;
}
