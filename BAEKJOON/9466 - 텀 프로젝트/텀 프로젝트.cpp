#include <iostream>
#include <vector>
#include <stack>
#include <numeric> // accumulate 함수가 포함된 헤더

using namespace std;

int find_teams(int n, vector<int>& choices) {
    vector<int> visited(n + 1, 0);  // 방문 상태를 저장하는 배열 초기화
    vector<int> team(n + 1, 0);  // 팀에 속한 상태를 저장하는 배열 초기화
    int team_count = 0;  // 팀의 개수 초기화

    for (int student = 1; student <= n; ++student) {  // 모든 학생에 대해 탐색 시작
        if (!visited[student]) {  // 해당 학생이 방문되지 않은 경우
            stack<int> stack;  // 스택 초기화
            int current = student;  // 현재 학생을 현재 위치로 설정

            while (!visited[current]) {  // 현재 학생이 방문되지 않은 경우 반복
                visited[current] = student;  // 현재 학생을 방문 상태로 설정
                stack.push(current);  // 현재 학생을 스택에 추가
                current = choices[current];  // 다음 학생으로 이동
            }

            if (visited[current] == student) {  // 싸이클이 형성된 경우
                while (!stack.empty() && stack.top() != current) {  // 스택에서 싸이클의 시작점까지 팝
                    team[stack.top()] = 1;  // 싸이클에 속한 학생을 팀에 속한 것으로 설정
                    stack.pop();
                }
                team[stack.top()] = 1;  // 싸이클의 시작점을 팀에 속한 것으로 설정
                stack.pop();
                team_count += 1;  // 팀의 개수 증가
            }

            while (!stack.empty()) {  // 남아있는 스택 요소 처리
                team[stack.top()] = 0;  // 싸이클에 속하지 않은 학생을 팀에 속하지 않은 것으로 설정
                stack.pop();
            }
        }
    }

    return n - accumulate(team.begin(), team.end(), 0);  // 팀에 속하지 않은 학생의 수 반환
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;  // 테스트 케이스의 수

    vector<int> results;  // 결과를 저장할 벡터 초기화

    while (T--) {
        int n;
        cin >> n;  // 학생의 수
        vector<int> choices(n + 1);

        for (int i = 1; i <= n; ++i) {
            cin >> choices[i];  // 학생들이 선택한 학생 번호
        }

        int result = find_teams(n, choices);  // 팀에 속하지 않은 학생의 수 계산
        results.push_back(result);  // 결과 벡터에 추가
    }

    for (int res : results) {
        cout << res << "\n";  // 각 테스트 케이스의 결과 출력
    }

    return 0;
}
