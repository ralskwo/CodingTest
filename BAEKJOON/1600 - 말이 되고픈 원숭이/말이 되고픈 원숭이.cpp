#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int K; // 말처럼 이동할 수 있는 최대 횟수
int W, H; // 격자판의 가로(W), 세로(H) 크기
vector<vector<int>> grid; // 격자판 정보를 저장할 2차원 벡터
vector<vector<vector<bool>>> visited; // 방문 여부를 체크할 3차원 벡터

int horse_dx[8] = {-2, -1, 1, 2, 2, 1, -1, -2}; // 말의 x방향 이동 배열
int horse_dy[8] = {-1, -2, -2, -1, 1, 2, 2, 1}; // 말의 y방향 이동 배열

int monkey_dx[4] = {-1, 1, 0, 0}; // 원숭이의 x방향 이동 배열
int monkey_dy[4] = {0, 0, -1, 1}; // 원숭이의 y방향 이동 배열

int bfs() {
    queue<tuple<int, int, int, int>> q; // BFS를 위한 큐 선언 (x, y, 이동 횟수, 말 이동 횟수)
    q.push(make_tuple(0, 0, 0, 0)); // 시작 위치를 큐에 추가
    visited[0][0][0] = true; // 시작 위치 방문 처리

    while (!q.empty()) {
        int x, y, cnt, k;
        tie(x, y, cnt, k) = q.front(); // 큐의 맨 앞 요소를 가져옴
        q.pop(); // 큐에서 제거

        if (x == W - 1 && y == H - 1) { // 도착 지점에 도달한 경우
            return cnt; // 이동 횟수 반환
        }

        if (k < K) { // 말의 이동을 더 사용할 수 있는 경우
            for (int i = 0; i < 8; ++i) {
                int nx = x + horse_dx[i];
                int ny = y + horse_dy[i];
                int nk = k + 1;

                if (nx >= 0 && nx < W && ny >= 0 && ny < H) { // 격자판 범위 내인지 확인
                    if (!visited[ny][nx][nk] && grid[ny][nx] == 0) { // 방문하지 않았고 평지인 경우
                        visited[ny][nx][nk] = true; // 방문 처리
                        q.push(make_tuple(nx, ny, cnt + 1, nk)); // 큐에 추가
                    }
                }
            }
        }

        for (int i = 0; i < 4; ++i) { // 원숭이의 일반 이동
            int nx = x + monkey_dx[i];
            int ny = y + monkey_dy[i];
            int nk = k;

            if (nx >= 0 && nx < W && ny >= 0 && ny < H) { // 격자판 범위 내인지 확인
                if (!visited[ny][nx][nk] && grid[ny][nx] == 0) { // 방문하지 않았고 평지인 경우
                    visited[ny][nx][nk] = true; // 방문 처리
                    q.push(make_tuple(nx, ny, cnt + 1, nk)); // 큐에 추가
                }
            }
        }
    }

    return -1; // 도착 지점에 도달할 수 없는 경우 -1 반환
}

int main() {
    ios_base::sync_with_stdio(false); // 입출력 속도 향상을 위한 설정
    cin.tie(NULL);

    cin >> K; // 말처럼 이동할 수 있는 최대 횟수 입력
    cin >> W >> H; // 격자판의 가로(W), 세로(H) 크기 입력
    grid.resize(H, vector<int>(W));
    visited.resize(H, vector<vector<bool>>(W, vector<bool>(K + 1, false)));

    for (int i = 0; i < H; ++i) { // 격자판 정보 입력
        for (int j = 0; j < W; ++j) {
            cin >> grid[i][j];
        }
    }

    int result = bfs(); // BFS 탐색 시작
    cout << result << '\n'; // 결과 출력

    return 0;
}
