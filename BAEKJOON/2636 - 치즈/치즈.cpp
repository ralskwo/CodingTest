#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// 상하좌우 방향을 나타내는 벡터
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// BFS로 외부 공기와 치즈 접촉을 찾는 함수
void bfs(vector<vector<int>>& cheese, vector<vector<bool>>& visited, int n, int m) {
    queue<pair<int, int>> q; // BFS를 위한 큐
    q.push({0, 0}); // 외부 공기를 (0, 0)에서 시작
    visited[0][0] = true; // (0, 0) 방문 처리

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // 상하좌우 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 내에 있고, 아직 방문하지 않은 위치라면
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                // 공기라면
                if (cheese[nx][ny] == 0) {
                    visited[nx][ny] = true;
                    q.push({nx, ny}); // 큐에 추가하여 계속 탐색
                }
                // 치즈라면
                else if (cheese[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    cheese[nx][ny] = 2; // 다음에 녹일 치즈로 표시
                }
            }
        }
    }
}

// 공기와 접촉한 치즈를 녹이는 함수
int melt_cheese(vector<vector<int>>& cheese, int n, int m) {
    int melted = 0; // 녹은 치즈 개수를 카운트
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (cheese[i][j] == 2) { // 녹을 치즈는 2로 표시됨
                cheese[i][j] = 0; // 치즈를 녹임
                melted++;
            }
        }
    }
    return melted; // 녹은 치즈 개수를 반환
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> cheese(n, vector<int>(m)); // 치즈 상태 저장
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> cheese[i][j]; // 입력으로 치즈 상태 받음
        }
    }

    int time = 0; // 치즈가 녹는 데 걸린 시간
    int last_cheese = 0; // 마지막 남은 치즈 개수

    while (true) {
        vector<vector<bool>> visited(n, vector<bool>(m, false)); // 방문 여부 초기화
        bfs(cheese, visited, n, m); // BFS로 외부 공기와 접촉한 치즈 탐색

        int melted = melt_cheese(cheese, n, m); // 치즈를 녹임
        if (melted == 0) break; // 더 이상 녹을 치즈가 없으면 종료

        last_cheese = melted; // 마지막으로 남은 치즈 개수 기록
        time++; // 시간이 1시간 증가
    }

    cout << time << endl; // 치즈가 모두 녹는 데 걸린 시간 출력
    cout << last_cheese << endl; // 마지막으로 남은 치즈 개수 출력

    return 0;
}