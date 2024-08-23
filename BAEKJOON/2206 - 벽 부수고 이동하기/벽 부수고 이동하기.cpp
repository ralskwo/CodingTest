#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

struct State {
    int x, y, wall_broken;
};

int bfs(const vector<vector<int>>& maze, int n, int m) {
    // 이동 방향: 상, 하, 좌, 우
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    // BFS를 위한 큐 초기화: (x, y, 벽을 부쉈는지 여부)
    queue<State> q;
    q.push({0, 0, 0});
    
    // 방문 체크 리스트 초기화
    vector<vector<vector<bool>>> visited(n, vector<vector<bool>>(m, vector<bool>(2, false)));
    visited[0][0][0] = true;
    
    // 거리 리스트 초기화
    vector<vector<vector<int>>> distance(n, vector<vector<int>>(m, vector<int>(2, 0)));
    distance[0][0][0] = 1;
    
    while (!q.empty()) {
        State current = q.front();
        q.pop();
        int x = current.x;
        int y = current.y;
        int wall_broken = current.wall_broken;
        
        // 도착 지점에 도달했을 때
        if (x == n - 1 && y == m - 1) {
            return distance[x][y][wall_broken];
        }
        
        // 4방향 탐색
        for (const auto& direction : directions) {
            int nx = x + direction.first;
            int ny = y + direction.second;
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (maze[nx][ny] == 0 && !visited[nx][ny][wall_broken]) {
                    // 벽이 아니고, 방문하지 않은 위치일 때
                    visited[nx][ny][wall_broken] = true;
                    distance[nx][ny][wall_broken] = distance[x][y][wall_broken] + 1;
                    q.push({nx, ny, wall_broken});
                }
                
                if (maze[nx][ny] == 1 && wall_broken == 0 && !visited[nx][ny][1]) {
                    // 벽이지만, 아직 벽을 부수지 않은 경우
                    visited[nx][ny][1] = true;
                    distance[nx][ny][1] = distance[x][y][wall_broken] + 1;
                    q.push({nx, ny, 1});
                }
            }
        }
    }
    
    return -1;  // 도착 지점에 도달할 수 없는 경우
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> maze(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < m; j++) {
            maze[i][j] = row[j] - '0';
        }
    }
    
    cout << bfs(maze, n, m) << endl;
    
    return 0;
}
