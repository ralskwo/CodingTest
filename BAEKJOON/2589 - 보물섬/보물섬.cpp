#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// 전역 변수로 지도 크기와 보물 지도를 저장할 변수들 선언
int n, m; // 지도 세로 크기(n)와 가로 크기(m)
vector<string> treasure_map; // 보물 지도를 저장할 벡터

// 상하좌우로 이동하기 위한 방향 벡터 (dx, dy)
int dx[4] = {-1, 1, 0, 0}; // x 좌표 이동: 상, 하
int dy[4] = {0, 0, -1, 1}; // y 좌표 이동: 좌, 우

// BFS 함수 정의 - 주어진 (x, y) 위치에서 출발해 최장 거리를 찾는 함수
int bfs(int x, int y) {
    vector<vector<bool>> visited(n, vector<bool>(m, false)); // 방문 여부를 체크할 2차원 배열
    queue<pair<int, int>> q; // 위치를 저장하는 큐
    queue<int> dist; // 현재 위치까지의 거리를 저장하는 큐
    
    visited[x][y] = true; // 시작 위치를 방문했다고 표시
    q.push({x, y}); // 시작 위치를 큐에 추가
    dist.push(0); // 시작 위치의 거리는 0으로 초기화

    int max_distance = 0; // 최장 거리를 저장할 변수

    // 큐가 빌 때까지 반복 (BFS 탐색)
    while (!q.empty()) {
        int cx = q.front().first; // 현재 x 좌표
        int cy = q.front().second; // 현재 y 좌표
        int current_dist = dist.front(); // 현재 위치까지의 거리
        q.pop(); // 큐에서 위치 제거
        dist.pop(); // 거리 큐에서 거리 제거

        max_distance = max(max_distance, current_dist); // 최장 거리 갱신

        // 네 방향으로 이동 가능한 위치 탐색
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i]; // 새로운 x 좌표
            int ny = cy + dy[i]; // 새로운 y 좌표

            // 지도 범위 내이고, 방문하지 않은 육지('L')인 경우
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && treasure_map[nx][ny] == 'L') {
                visited[nx][ny] = true; // 방문 여부 갱신
                q.push({nx, ny}); // 새 위치를 큐에 추가
                dist.push(current_dist + 1); // 거리 1 증가 후 큐에 추가
            }
        }
    }

    return max_distance; // 최장 거리 반환
}

int main() {
    // 지도 크기 입력받기
    cin >> n >> m;
    treasure_map.resize(n); // 지도 크기 설정

    // 보물 지도 입력받기
    for (int i = 0; i < n; i++) {
        cin >> treasure_map[i];
    }

    int max_treasure_distance = 0; // 최장 최단 거리 저장할 변수

    // 모든 육지 위치에서 BFS 수행
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (treasure_map[i][j] == 'L') { // 육지인 경우만 BFS 수행
                max_treasure_distance = max(max_treasure_distance, bfs(i, j)); // 최장 거리 갱신
            }
        }
    }

    cout << max_treasure_distance << endl; // 최장 최단 거리 출력
    return 0;
}