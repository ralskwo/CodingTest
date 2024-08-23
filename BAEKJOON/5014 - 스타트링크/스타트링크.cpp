#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

string elevator(int F, int S, int G, int U, int D) {
    vector<int> visited(F + 1, -1);  // 방문 여부와 버튼 누름 횟수를 저장할 벡터를 초기화합니다. 초기값은 -1로 설정하여 방문하지 않음을 표시합니다.
    queue<pair<int, int>> q;  // 현재 층과 버튼 누름 횟수를 저장하는 큐를 초기화합니다.
    q.push(make_pair(S, 0));  // 시작 층 S와 누름 횟수 0을 추가합니다.
    visited[S] = 0;  // 시작 층은 방문했으므로 0으로 설정합니다.
    
    while (!q.empty()) {  // 큐가 빌 때까지 반복합니다.
        int current_floor, presses;
        tie(current_floor, presses) = q.front();  // 큐에서 현재 층과 버튼 누름 횟수를 가져옵니다.
        q.pop();
        
        if (current_floor == G) {  // 현재 층이 목표 층과 같으면
            return to_string(presses);  // 버튼 누름 횟수를 반환합니다.
        }
        
        // 위로 이동
        if (current_floor + U <= F && visited[current_floor + U] == -1) {  // 위로 이동한 층이 총 층 수를 넘지 않고 아직 방문하지 않았다면
            visited[current_floor + U] = presses + 1;  // 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
            q.push(make_pair(current_floor + U, presses + 1));  // 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
        }
        
        // 아래로 이동
        if (current_floor - D > 0 && visited[current_floor - D] == -1) {  // 아래로 이동한 층이 1층 이상이고 아직 방문하지 않았다면
            visited[current_floor - D] = presses + 1;  // 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
            q.push(make_pair(current_floor - D, presses + 1));  // 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
        }
    }
    
    return "use the stairs";  // 큐가 비고도 목표 층에 도달하지 못하면 "use the stairs"를 반환합니다.
}

int main() {
    int F, S, G, U, D;
    cin >> F >> S >> G >> U >> D;  // 입력된 값을 정수로 변환하여 F, S, G, U, D에 각각 저장합니다.

    // 함수 호출 및 결과 출력
    string result = elevator(F, S, G, U, D);  // elevator 함수를 호출하고 결과를 result에 저장합니다.
    cout << result << endl;  // 결과를 출력합니다.

    return 0;
}
