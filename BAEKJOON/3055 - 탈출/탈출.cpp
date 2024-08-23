#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

int R, C;
vector<string> forest;
vector<vector<int>> water_time;
vector<vector<int>> hedgehog_time;
queue<pair<int, int>> water_queue;
queue<pair<int, int>> hedgehog_queue;

int bfs_escape() {
    while (!water_queue.empty()) {
        int x = water_queue.front().first;
        int y = water_queue.front().second;
        water_queue.pop();

        // 상하좌우 이동
        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < R && ny >= 0 && ny < C && forest[nx][ny] == '.' && water_time[nx][ny] == -1) {
                water_time[nx][ny] = water_time[x][y] + 1;
                water_queue.push({nx, ny});
            }
        }
    }

    while (!hedgehog_queue.empty()) {
        int x = hedgehog_queue.front().first;
        int y = hedgehog_queue.front().second;
        hedgehog_queue.pop();

        // 상하좌우 이동
        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                if (forest[nx][ny] == 'D') {
                    return hedgehog_time[x][y] + 1;
                }
                if (forest[nx][ny] == '.' && hedgehog_time[nx][ny] == -1) {
                    if (water_time[nx][ny] == -1 || water_time[nx][ny] > hedgehog_time[x][y] + 1) {
                        hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1;
                        hedgehog_queue.push({nx, ny});
                    }
                }
            }
        }
    }

    return -1;
}

int main() {
    cin >> R >> C;

    forest.resize(R);
    water_time.assign(R, vector<int>(C, -1));
    hedgehog_time.assign(R, vector<int>(C, -1));

    for (int i = 0; i < R; i++) {
        cin >> forest[i];
        for (int j = 0; j < C; j++) {
            if (forest[i][j] == '*') {
                water_queue.push({i, j});
                water_time[i][j] = 0;
            } else if (forest[i][j] == 'S') {
                hedgehog_queue.push({i, j});
                hedgehog_time[i][j] = 0;
            }
        }
    }

    int result = bfs_escape();
    if (result == -1) {
        cout << "KAKTUS" << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}
