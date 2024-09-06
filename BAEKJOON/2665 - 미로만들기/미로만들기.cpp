#include <iostream>  // 입출력 처리를 위한 라이브러리
#include <deque>     // 0-1 BFS에서 사용할 덱(deque)을 위한 라이브러리
#include <vector>    // 2차원 벡터를 사용하기 위한 라이브러리
#include <climits>   // 무한대 값을 설정하기 위한 라이브러리

using namespace std;

// 상, 하, 좌, 우 방향으로 이동하기 위한 델타값
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

// 최소 검은 방을 바꾸는 횟수를 계산하는 BFS 함수
int bfs_min_change(int n, vector<vector<int>>& grid) {
    // 각 방까지 도달할 때 바꾼 검은 방의 최소 횟수를 저장하는 배열
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    dist[0][0] = 0;  // 시작점은 비용 0으로 초기화

    deque<pair<int, int>> dq;  // BFS를 위한 덱 선언
    dq.push_back({0, 0});  // 시작점을 덱에 추가

    while (!dq.empty()) {
        // 덱의 앞에서 좌표를 꺼내옴
        int x = dq.front().first;
        int y = dq.front().second;
        dq.pop_front();

        // 4방향으로 이동
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 좌표가 유효한 범위 내에 있는지 확인
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                // 흰 방일 경우
                if (grid[nx][ny] == 1 && dist[nx][ny] > dist[x][y]) {
                    dist[nx][ny] = dist[x][y];  // 비용 업데이트
                    dq.push_front({nx, ny});  // 비용이 0이므로 앞에 삽입
                }
                // 검은 방일 경우
                else if (grid[nx][ny] == 0 && dist[nx][ny] > dist[x][y] + 1) {
                    dist[nx][ny] = dist[x][y] + 1;  // 비용 1 추가 후 업데이트
                    dq.push_back({nx, ny});  // 비용이 추가되므로 뒤에 삽입
                }
            }
        }
    }

    // 도착점까지의 최소 검은 방 변경 횟수 반환
    return dist[n-1][n-1];
}

int main() {
    int n;
    cin >> n;  // 방의 크기 입력

    vector<vector<int>> grid(n, vector<int>(n));  // 방의 상태 저장할 2차원 배열
    for (int i = 0; i < n; ++i) {
        string line;
        cin >> line;  // 방의 상태 입력
        for (int j = 0; j < n; ++j) {
            grid[i][j] = line[j] - '0';  // 문자열을 숫자로 변환하여 저장
        }
    }

    // BFS 함수 호출 및 결과 출력
    cout << bfs_min_change(n, grid) << endl;

    return 0;
}
