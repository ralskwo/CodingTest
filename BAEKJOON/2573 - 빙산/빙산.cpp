#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 동서남북 방향을 나타내는 배열
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// BFS를 사용하여 빙산의 한 덩어리를 탐색하는 함수
void bfs(int x, int y, vector<vector<int>>& iceberg, vector<vector<bool>>& visited) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true; // 현재 위치를 방문 처리

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();
        
        // 동서남북 방향으로 인접한 칸을 탐색
        for (int i = 0; i < 4; ++i) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            
            // 배열 범위 내에 있고, 빙산이 있으며, 아직 방문하지 않은 경우
            if (nx >= 0 && nx < iceberg.size() && ny >= 0 && ny < iceberg[0].size()) {
                if (iceberg[nx][ny] > 0 && !visited[nx][ny]) {
                    visited[nx][ny] = true; // 방문 처리
                    q.push({nx, ny}); // 인접한 칸을 큐에 추가
                }
            }
        }
    }
}

// 빙산을 녹이는 함수
vector<pair<int, int>> melt_iceberg(vector<vector<int>>& iceberg, vector<pair<int, int>>& iceberg_positions) {
    vector<vector<int>> melt(iceberg.size(), vector<int>(iceberg[0].size(), 0)); // 각 칸의 녹을 양을 저장할 배열
    vector<pair<int, int>> new_iceberg_positions; // 녹은 후에도 남아 있는 빙산의 위치를 저장할 리스트
    
    for (auto& pos : iceberg_positions) {
        int x = pos.first;
        int y = pos.second;
        if (iceberg[x][y] > 0) {
            int sea_count = 0; // 주변의 바다 칸의 개수를 카운트
            for (int i = 0; i < 4; ++i) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (iceberg[nx][ny] == 0) // 바다(0)인 경우
                    sea_count++;
            }
            melt[x][y] = sea_count; // 현재 빙산 칸에 대해 녹을 양을 저장
        }
    }

    // 빙산 높이 감소
    for (auto& pos : iceberg_positions) {
        int x = pos.first;
        int y = pos.second;
        if (iceberg[x][y] > 0) {
            iceberg[x][y] = max(0, iceberg[x][y] - melt[x][y]); // 빙산의 높이를 줄임
            if (iceberg[x][y] > 0) // 녹은 후에도 남아 있는 경우
                new_iceberg_positions.push_back({x, y}); // 새로운 빙산 위치를 리스트에 추가
        }
    }
    
    return new_iceberg_positions; // 업데이트된 빙산 위치 반환
}

// 현재 빙산이 몇 개의 덩어리로 분리되어 있는지 계산하는 함수
int count_iceberg_parts(vector<vector<int>>& iceberg, vector<pair<int, int>>& iceberg_positions) {
    vector<vector<bool>> visited(iceberg.size(), vector<bool>(iceberg[0].size(), false));
    int count = 0; // 빙산 덩어리의 개수를 저장할 변수
    
    for (auto& pos : iceberg_positions) {
        int x = pos.first;
        int y = pos.second;
        if (iceberg[x][y] > 0 && !visited[x][y]) { // 빙산이고 아직 방문하지 않은 경우
            bfs(x, y, iceberg, visited); // BFS를 사용하여 하나의 덩어리를 탐색
            count++; // 덩어리의 개수 증가
        }
    }
    
    return count; // 빙산의 총 덩어리 개수 반환
}

// 시뮬레이션을 진행하여 빙산이 분리되는 시점을 찾는 함수
int simulate(vector<vector<int>>& iceberg) {
    int year = 0; // 경과한 시간을 나타내는 변수
    vector<pair<int, int>> iceberg_positions;

    // 초기 빙산의 위치 저장
    for (int i = 1; i < iceberg.size() - 1; ++i) {
        for (int j = 1; j < iceberg[0].size() - 1; ++j) {
            if (iceberg[i][j] > 0)
                iceberg_positions.push_back({i, j});
        }
    }
    
    while (!iceberg_positions.empty()) {
        // 빙산이 몇 덩어리로 분리되었는지 계산
        int parts = count_iceberg_parts(iceberg, iceberg_positions);
        
        if (parts >= 2) // 빙산이 두 덩어리 이상으로 분리되었을 때
            return year; // 경과한 시간을 반환
        
        // 빙산을 한 해 녹임
        iceberg_positions = melt_iceberg(iceberg, iceberg_positions);
        year++; // 시간이 1년 경과
    }
    
    return 0; // 모두 녹을 때까지 분리되지 않으면 0 반환
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> iceberg(n, vector<int>(m));

    // 빙산 높이 정보 입력
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> iceberg[i][j];
        }
    }

    // 시뮬레이션 시작
    int result = simulate(iceberg);
    cout << result << endl;

    return 0;
}
