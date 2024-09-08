#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// 상하좌우 이동을 위한 방향 벡터
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int R, C;  // 호수의 행과 열 크기
vector<string> lake;  // 호수 상태를 저장할 벡터
queue<pair<int, int>> water_queue, next_water_queue;  // 물의 위치를 저장할 큐
queue<pair<int, int>> swan_queue, next_swan_queue;  // 백조의 위치를 저장할 큐
bool visited_swan[1500][1500];  // 백조가 방문한 곳을 체크할 배열
pair<int, int> swans[2];  // 두 마리 백조의 위치 저장

// 얼음을 녹이는 함수
void melt_ice() {
    while (!water_queue.empty()) {
        int x = water_queue.front().first;
        int y = water_queue.front().second;
        water_queue.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < R && ny < C && lake[nx][ny] == 'X') {
                lake[nx][ny] = '.';  // 얼음을 물로 녹임
                next_water_queue.push({ nx, ny });  // 다음 날 녹을 물 위치 저장
            }
        }
    }
}

// 백조가 이동 가능한지 확인하는 함수
bool move_swan() {
    while (!swan_queue.empty()) {
        int x = swan_queue.front().first;
        int y = swan_queue.front().second;
        swan_queue.pop();

        // 두 번째 백조와 만나면 true 반환
        if (x == swans[1].first && y == swans[1].second)
            return true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < R && ny < C && !visited_swan[nx][ny]) {
                visited_swan[nx][ny] = true;
                if (lake[nx][ny] == '.') {
                    swan_queue.push({ nx, ny });  // 물인 경우 계속 이동 가능
                } else if (lake[nx][ny] == 'X') {
                    next_swan_queue.push({ nx, ny });  // 얼음인 경우 다음 날 이동
                }
            }
        }
    }
    return false;
}

// 문제를 해결하는 함수
int solve() {
    int days = 0;

    // 두 백조가 만날 때까지 매일 반복
    while (true) {
        // 백조가 만났다면 그 시점의 날짜 반환
        if (move_swan()) return days;

        // 얼음 녹이기
        melt_ice();

        // 다음 날 백조의 이동 큐 갱신
        swan_queue = next_swan_queue;
        next_swan_queue = queue<pair<int, int>>();

        // 다음 날 물 큐 갱신
        water_queue = next_water_queue;
        next_water_queue = queue<pair<int, int>>();

        days++;
    }
}

int main() {
    cin >> R >> C;
    lake.resize(R);

    // 호수 상태 입력
    for (int i = 0; i < R; i++) {
        cin >> lake[i];
        for (int j = 0; j < C; j++) {
            if (lake[i][j] == 'L') {
                if (swans[0].first == 0 && swans[0].second == 0) {
                    swans[0] = { i, j };  // 첫 번째 백조 위치 저장
                } else {
                    swans[1] = { i, j };  // 두 번째 백조 위치 저장
                }
                lake[i][j] = '.';  // 백조 위치를 물로 변경
            }
            if (lake[i][j] == '.') {
                water_queue.push({ i, j });  // 물의 위치 저장
            }
        }
    }

    // 첫 번째 백조의 위치를 BFS 시작점으로 설정
    swan_queue.push(swans[0]);
    visited_swan[swans[0].first][swans[0].second] = true;

    // 문제 해결 및 결과 출력
    cout << solve() << endl;
    return 0;
}
