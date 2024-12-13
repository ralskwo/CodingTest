#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

// 상하좌우 이동을 위한 방향 배열
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// 나무까지의 최단 거리를 계산하는 함수
vector<vector<int>> calculate_tree_distances(const vector<string>& forest, int N, int M) {
    vector<vector<int>> tree_distances(N, vector<int>(M, numeric_limits<int>::max())); // 거리 배열 초기화
    queue<pair<int, int>> q; // BFS를 위한 큐

    // 나무의 위치를 큐에 추가하고 거리를 0으로 설정
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (forest[i][j] == '+') {
                q.push({i, j}); // 나무의 위치를 큐에 추가
                tree_distances[i][j] = 0; // 나무의 거리는 0
            }
        }
    }

    // BFS 수행
    while (!q.empty()) {
        auto [x, y] = q.front(); // 큐에서 현재 위치 가져오기
        q.pop(); // 큐에서 제거

        for (int i = 0; i < 4; ++i) { // 상하좌우 탐색
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 유효한 범위 내에 있고 현재 거리보다 작으면 업데이트
            if (nx >= 0 && nx < N && ny >= 0 && ny < M && tree_distances[nx][ny] > tree_distances[x][y] + 1) {
                tree_distances[nx][ny] = tree_distances[x][y] + 1; // 거리 업데이트
                q.push({nx, ny}); // 새로운 위치를 큐에 추가
            }
        }
    }

    return tree_distances; // 최종 거리 배열 반환
}

// 가장 안전한 경로를 찾는 함수
int find_safest_path(const vector<string>& forest, int N, int M, pair<int, int> wolf_position, const vector<vector<int>>& tree_distances) {
    priority_queue<pair<int, pair<int, int>>> pq; // 우선순위 큐 (안전 거리 최대화)
    pq.push({tree_distances[wolf_position.first][wolf_position.second], wolf_position}); // 시작 위치 추가
    vector<vector<bool>> visited(N, vector<bool>(M, false)); // 방문 체크 배열
    visited[wolf_position.first][wolf_position.second] = true; // 시작 위치 방문 처리

    while (!pq.empty()) {
        auto [min_dist, pos] = pq.top(); // 안전 거리와 현재 위치 가져오기
        pq.pop(); // 큐에서 제거

        if (forest[pos.first][pos.second] == 'J') { // 오두막에 도착하면 안전 거리 반환
            return min_dist;
        }

        for (int i = 0; i < 4; ++i) { // 상하좌우 탐색
            int nx = pos.first + dx[i];
            int ny = pos.second + dy[i];
            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny]) {
                visited[nx][ny] = true; // 방문 처리
                int new_min_dist = min(min_dist, tree_distances[nx][ny]); // 새로운 최소 안전 거리 계산
                pq.push({new_min_dist, {nx, ny}}); // 우선순위 큐에 추가
            }
        }
    }

    return -1; // 오두막에 도달할 수 없는 경우 -1 반환
}

int main() {
    int N, M;
    cin >> N >> M; // 숲의 크기 입력받기
    vector<string> forest(N); // 숲의 상태 저장할 벡터

    for (int i = 0; i < N; ++i) {
        cin >> forest[i]; // 숲의 각 행 입력받기
    }

    pair<int, int> wolf_position; // 늑대의 위치 저장 변수

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (forest[i][j] == 'V') { 
                wolf_position = {i, j}; // 늑대의 위치 찾기
            }
        }
    }

    auto tree_distances = calculate_tree_distances(forest, N, M); // 나무까지의 거리 계산
    int result = find_safest_path(forest, N, M, wolf_position, tree_distances); // 가장 안전한 경로 찾기

    cout << result << endl; // 결과 출력

    return 0;
}
