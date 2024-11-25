#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 8방향 이동을 나타내는 방향 벡터
int directions[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };

// BFS를 수행하는 함수
void bfs(int x, int y, vector<vector<int>>& grid, vector<vector<bool>>& visited, int h, int w) {
    queue<pair<int, int>> q; // BFS를 위한 큐 선언
    q.push({x, y}); // 시작점을 큐에 추가
    visited[x][y] = true; // 방문 처리

    while (!q.empty()) { // 큐가 빌 때까지 반복
        auto [cx, cy] = q.front(); // 현재 위치를 가져옴
        q.pop(); // 큐에서 제거

        for (int i = 0; i < 8; i++) { // 8방향을 확인
            int nx = cx + directions[i][0];
            int ny = cy + directions[i][1];

            // 유효한 좌표인지 확인
            if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
                // 땅이고 방문하지 않았다면
                if (grid[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true; // 방문 처리
                    q.push({nx, ny}); // 큐에 추가
                }
            }
        }
    }
}

// 섬의 개수를 세는 함수
int countIslands(int w, int h, vector<vector<int>>& grid) {
    vector<vector<bool>> visited(h, vector<bool>(w, false)); // 방문 여부를 저장할 배열
    int count = 0; // 섬의 개수 초기화

    for (int i = 0; i < h; i++) { // 모든 칸을 순회
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == 1 && !visited[i][j]) { // 땅이고 방문하지 않았다면
                bfs(i, j, grid, visited, h, w); // BFS 호출
                count++; // 섬의 개수 증가
            }
        }
    }
    return count; // 최종 섬의 개수 반환
}

int main() {
    while (true) {
        int w, h;
        cin >> w >> h; // 너비와 높이 입력
        if (w == 0 && h == 0) break; // 종료 조건

        vector<vector<int>> grid(h, vector<int>(w)); // 지도 데이터
        for (int i = 0; i < h; i++) { // 지도 입력
            for (int j = 0; j < w; j++) {
                cin >> grid[i][j];
            }
        }

        cout << countIslands(w, h, grid) << endl; // 결과 출력
    }
    return 0;
}
