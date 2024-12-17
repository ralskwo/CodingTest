#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

// BFS 함수: 목표 이모티콘 개수 S를 만드는 최소 시간을 반환
int bfs(int S) {
    // 상태 저장을 위한 큐 (화면 이모티콘 개수, 클립보드 이모티콘 개수, 경과 시간)
    std::queue<std::tuple<int, int, int>> q;
    // 방문 여부 체크 배열
    std::vector<std::vector<bool>> visited(S + 1, std::vector<bool>(S + 1, false));

    // 초기 상태: 화면에 1개, 클립보드 0개, 시간 0초
    q.push({1, 0, 0});
    visited[1][0] = true;

    while (!q.empty()) {
        // 현재 상태를 꺼냄
        int screen, clipboard, time;
        std::tie(screen, clipboard, time) = q.front();
        q.pop();

        // 화면 이모티콘 수가 S에 도달하면 시간 반환
        if (screen == S) {
            return time;
        }

        // 연산 1: 화면 이모티콘을 클립보드에 복사
        if (!visited[screen][screen]) {
            visited[screen][screen] = true;
            q.push({screen, screen, time + 1}); // (현재 화면, 클립보드에 저장된 화면, 시간 + 1)
        }

        // 연산 2: 클립보드 이모티콘을 화면에 붙여넣기
        if (clipboard > 0 && screen + clipboard <= S && !visited[screen + clipboard][clipboard]) {
            visited[screen + clipboard][clipboard] = true;
            q.push({screen + clipboard, clipboard, time + 1}); // 화면에 붙여넣기한 결과 추가
        }

        // 연산 3: 화면 이모티콘 중 하나 삭제
        if (screen > 0 && !visited[screen - 1][clipboard]) {
            visited[screen - 1][clipboard] = true;
            q.push({screen - 1, clipboard, time + 1}); // 화면 이모티콘을 1개 삭제한 상태 추가
        }
    }
    return -1; // 실패하는 경우는 없지만 안전 처리
}

int main() {
    int S;
    cin >> S; // 목표 이모티콘 개수 입력
    cout << bfs(S) << endl; // BFS를 통해 최소 시간 출력
    return 0;
}
