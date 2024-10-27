#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// 방향 벡터 설정 (서, 북, 동, 남 순서)
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};

// 벽의 방향을 비트마스킹으로 나타내는 값 (서쪽: 1, 북쪽: 2, 동쪽: 4, 남쪽: 8)
int DIRECTION_WALL[4] = {1, 2, 4, 8};

// BFS를 통해 방을 탐색하고 방의 크기를 반환하는 함수
int bfs(int start_x, int start_y, int room_id, vector<vector<int>>& castle, vector<vector<int>>& visited) {
    queue<pair<int, int>> q; // BFS를 위한 큐
    q.push({start_x, start_y}); // 시작 위치를 큐에 추가
    visited[start_x][start_y] = room_id; // 시작 위치를 현재 방 ID로 방문 표시
    int room_size = 1; // 현재 방의 크기 (칸 수)

    // 큐가 빌 때까지 BFS 탐색을 수행
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // 4방향(서, 북, 동, 남)을 순회하며 이동할 수 있는지 확인
        for (int direction = 0; direction < 4; ++direction) {
            int nx = x + dx[direction];
            int ny = y + dy[direction];

            // 성곽 크기 내에 있고, 아직 방문하지 않은 위치인지 확인
            if (nx >= 0 && nx < castle.size() && ny >= 0 && ny < castle[0].size() && visited[nx][ny] == 0) {
                // 현재 위치에서 해당 방향에 벽이 없을 때만 이동
                if ((castle[x][y] & DIRECTION_WALL[direction]) == 0) {
                    visited[nx][ny] = room_id; // 이동할 위치를 현재 방 ID로 표시
                    q.push({nx, ny}); // 큐에 이동할 위치 추가
                    room_size++; // 방 크기 증가
                }
            }
        }
    }
    return room_size; // 최종 방 크기 반환
}

int main() {
    int N, M;
    cin >> N >> M; // 성곽의 너비와 높이 입력 받기

    vector<vector<int>> castle(M, vector<int>(N)); // 성곽의 벽 정보 저장
    vector<vector<int>> visited(M, vector<int>(N, 0)); // 방문 여부와 방 ID 저장

    // 성곽의 각 칸의 벽 정보 입력
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> castle[i][j];
        }
    }

    vector<int> room_sizes; // 각 방의 크기를 저장
    int room_count = 0; // 방의 개수를 저장

    // 성곽의 각 칸을 순회하며 방 탐색 수행
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            // 아직 방문하지 않은 칸이면 새로운 방으로 간주하고 탐색
            if (visited[i][j] == 0) {
                room_count++; // 방의 개수 증가
                int room_size = bfs(i, j, room_count, castle, visited); // BFS로 방 크기 계산
                room_sizes.push_back(room_size); // 방 크기를 리스트에 추가
            }
        }
    }

    // 가장 넓은 방의 크기 계산
    int max_room_size = *max_element(room_sizes.begin(), room_sizes.end());

    // 벽을 하나 제거하여 얻을 수 있는 최대 방 크기 계산
    int max_combined_room_size = 0;

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            int current_room_id = visited[i][j]; // 현재 칸의 방 ID 저장

            // 4방향을 확인하여 인접 방과의 연결 시도
            for (int direction = 0; direction < 4; ++direction) {
                int ni = i + dx[direction];
                int nj = j + dy[direction];

                if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
                    int neighbor_room_id = visited[ni][nj]; // 인접 방의 ID 저장

                    // 인접 방이 다른 방일 경우에만 벽을 제거하고 방을 합친 크기 계산
                    if (current_room_id != neighbor_room_id) {
                        int combined_size = room_sizes[current_room_id - 1] + room_sizes[neighbor_room_id - 1];
                        max_combined_room_size = max(max_combined_room_size, combined_size); // 최대 크기 갱신
                    }
                }
            }
        }
    }

    // 결과 출력: 방의 개수, 가장 넓은 방의 크기, 벽을 제거하여 얻을 수 있는 최대 방 크기
    cout << room_count << endl;
    cout << max_room_size << endl;
    cout << max_combined_room_size << endl;

    return 0;
}