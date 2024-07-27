#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

struct Fish {
    int dist;
    int x;
    int y;
};

bool compare(const Fish &a, const Fish &b) {
    if (a.dist == b.dist) {
        if (a.x == b.x) {
            return a.y < b.y;
        }
        return a.x < b.x;
    }
    return a.dist < b.dist;
}

vector<Fish> bfs(int start_x, int start_y, int size, vector<vector<int>> &grid) {
    int N = grid.size();
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(start_x, start_y, 0));
    visited[start_x][start_y] = true;
    vector<Fish> fish;

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    while (!q.empty()) {
        int x, y, dist;
        tie(x, y, dist) = q.front();
        q.pop();

        for (auto direction : directions) {
            int nx = x + direction[0];
            int ny = y + direction[1];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                if (grid[nx][ny] <= size) {
                    visited[nx][ny] = true;
                    q.push(make_tuple(nx, ny, dist + 1));
                    if (grid[nx][ny] > 0 && grid[nx][ny] < size) {
                        fish.push_back({dist + 1, nx, ny});
                    }
                }
            }
        }
    }

    sort(fish.begin(), fish.end(), compare);
    return fish;
}

int baby_shark(vector<vector<int>> &grid) {
    int N = grid.size();
    int shark_x, shark_y;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j] == 9) {
                shark_x = i;
                shark_y = j;
                grid[i][j] = 0;
            }
        }
    }

    int size = 2;
    int eaten = 0;
    int time = 0;

    while (true) {
        vector<Fish> result = bfs(shark_x, shark_y, size, grid);
        if (result.empty()) {
            break;
        }

        Fish nearest = result[0];
        time += nearest.dist;
        shark_x = nearest.x;
        shark_y = nearest.y;
        grid[shark_x][shark_y] = 0;
        eaten++;

        if (eaten == size) {
            size++;
            eaten = 0;
        }
    }

    return time;
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    cout << baby_shark(grid) << endl;
    return 0;
}
