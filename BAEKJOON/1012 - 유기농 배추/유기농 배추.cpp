#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 상하좌우 이동을 위한 방향 벡터
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

// BFS를 사용하여 연결된 배추를 탐색
void bfs(int x, int y, vector<vector<int>>& field, vector<vector<bool>>& visited, int M, int N) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[y][x] = true; // 현재 위치를 방문 처리

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        // 상하좌우로 이동하며 연결된 배추 탐색
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            // 범위 내에 있고, 방문하지 않았으며, 배추가 있는 경우
            if (nx >= 0 && nx < M && ny >= 0 && ny < N && !visited[ny][nx] && field[ny][nx] == 1) {
                visited[ny][nx] = true; // 방문 처리
                q.push({nx, ny}); // 다음 탐색 위치 추가
            }
        }
    }
}

int main() {
    int T; // 테스트 케이스 수
    cin >> T;

    while (T--) {
        int M, N, K; // 가로 길이, 세로 길이, 배추의 개수
        cin >> M >> N >> K;

        vector<vector<int>> field(N, vector<int>(M, 0)); // 배추밭 정보
        vector<vector<bool>> visited(N, vector<bool>(M, false)); // 방문 여부

        // 배추의 위치 입력
        for (int i = 0; i < K; i++) {
            int x, y;
            cin >> x >> y;
            field[y][x] = 1; // 배추가 있는 곳을 1로 표시
        }

        int worm_count = 0; // 필요한 지렁이 수
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                // 배추가 있고 방문하지 않은 경우
                if (field[y][x] == 1 && !visited[y][x]) {
                    bfs(x, y, field, visited, M, N); // BFS를 통해 연결된 배추 탐색
                    worm_count++; // 새로운 군집 발견
                }
            }
        }

        cout << worm_count << endl; // 결과 출력
    }

    return 0;
}