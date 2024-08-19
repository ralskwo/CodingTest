#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// BFS를 수행하기 위한 방향 벡터 (상, 하, 좌, 우)
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main() {
    int M, N;
    cin >> M >> N;

    vector<vector<int>> farm(N, vector<int>(M));
    queue<pair<int, int>> q;
    int days = 0;

    // 농장의 상태를 입력받고 익은 토마토를 큐에 추가
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> farm[i][j];
            if (farm[i][j] == 1) {
                q.push({i, j});
            }
        }
    }

    // BFS 탐색 시작
    while (!q.empty()) {
        int size = q.size();
        bool changed = false;  // 이번 단계에서 토마토가 익었는지 확인

        for (int i = 0; i < size; i++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            // 네 방향으로 이동
            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                // 유효한 위치인지와 익지 않은 토마토인지 확인
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && farm[nx][ny] == 0) {
                    farm[nx][ny] = 1;  // 토마토를 익게 함
                    q.push({nx, ny});
                    changed = true;
                }
            }
        }

        // 이번 단계에서 토마토가 익었다면 경과 일수를 증가
        if (changed) {
            days++;
        }
    }

    // 모든 토마토가 익었는지 확인
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (farm[i][j] == 0) {  // 익지 않은 토마토가 남아있다면
                cout << -1 << endl;
                return 0;
            }
        }
    }

    // 모든 토마토가 익은 최소 일수를 출력
    cout << days << endl;
    return 0;
}
