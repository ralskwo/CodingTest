#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

// BFS를 사용하여 미로의 최단 경로를 찾는 함수
int bfs_maze(vector<vector<int>>& maze, int n, int m) {
    // 이동 방향: 상(위), 하(아래), 좌(왼쪽), 우(오른쪽)
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    // BFS를 위한 큐 초기화
    queue<tuple<int, int, int>> q;  // (x, y, 거리)를 저장하는 큐
    q.push(make_tuple(0, 0, 1));  // 시작점 (0, 0)에서 시작, 거리 1
    vector<vector<bool>> visited(n, vector<bool>(m, false));  // 방문 체크를 위한 2차원 벡터
    visited[0][0] = true;  // 시작점 방문 처리
    
    // 큐가 빌 때까지 반복
    while (!q.empty()) {
        int x, y, dist;  // 현재 위치와 거리
        tie(x, y, dist) = q.front();  // 큐의 맨 앞 요소를 꺼내옴
        q.pop();  // 큐에서 제거
        
        // 도착 지점에 도달했을 때
        if (x == n - 1 && y == m - 1) {
            return dist;  // 현재까지의 거리를 반환
        }
        
        // 4방향 탐색
        for (int i = 0; i < 4; ++i) {
            int nx = x + directions[i][0];  // 새로운 x 좌표
            int ny = y + directions[i][1];  // 새로운 y 좌표
            
            // 새 위치가 미로 범위 내에 있고, 방문하지 않았으며, 길(1)이 있을 때
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maze[nx][ny] == 1) {
                visited[nx][ny] = true;  // 방문 처리
                q.push(make_tuple(nx, ny, dist + 1));  // 큐에 새 위치와 거리를 추가
            }
        }
    }
    
    // 도착 지점에 도달할 수 없는 경우
    return -1;  // -1을 반환
}

int main() {
    int n, m;  // 미로의 크기 (n: 행, m: 열)
    cin >> n >> m;
    vector<vector<int>> maze(n, vector<int>(m));  // n x m 크기의 미로를 저장할 벡터
    
    // 미로의 각 행을 입력받아 2차원 벡터에 저장
    for (int i = 0; i < n; ++i) {
        string row;  // 한 줄씩 입력받기 위한 문자열 변수
        cin >> row;
        for (int j = 0; j < m; ++j) {
            maze[i][j] = row[j] - '0';  // 문자 '0' 또는 '1'을 정수 0 또는 1로 변환하여 저장
        }
    }
    
    // BFS를 통해 최단 거리를 출력
    cout << bfs_maze(maze, n, m) << endl;
    
    return 0;  // 프로그램 종료
}
