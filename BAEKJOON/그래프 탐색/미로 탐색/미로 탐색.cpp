#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int bfs_maze(vector<vector<int>>& maze, int n, int m) {
    // 이동 방향: 상, 하, 좌, 우
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    // BFS를 위한 큐 초기화
    queue<tuple<int, int, int>> q;  // (x, y, 거리)
    q.push(make_tuple(0, 0, 1));
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    visited[0][0] = true;
    
    while (!q.empty()) {
        int x, y, dist;
        tie(x, y, dist) = q.front();
        q.pop();
        
        // 도착 지점에 도달했을 때
        if (x == n - 1 && y == m - 1) {
            return dist;
        }
        
        // 4방향 탐색
        for (int i = 0; i < 4; ++i) {
            int nx = x + directions[i][0];
            int ny = y + directions[i][1];
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maze[nx][ny] == 1) {
                visited[nx][ny] = true;
                q.push(make_tuple(nx, ny, dist + 1));
            }
        }
    }
    
    // 도착 지점에 도달할 수 없는 경우
    return -1;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> maze(n, vector<int>(m));
    
    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < m; ++j) {
            maze[i][j] = row[j] - '0';
        }
    }
    
    cout << bfs_maze(maze, n, m) << endl;
    
    return 0;
}
