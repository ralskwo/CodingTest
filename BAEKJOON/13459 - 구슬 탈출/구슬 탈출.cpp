#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <set>

using namespace std;

// 방향 벡터 (상, 하, 좌, 우)
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// 구슬 이동 함수
tuple<int, int, int> move(int x, int y, int dx, int dy, vector<string> &board) {
    int count = 0; // 이동 거리
    while (board[x + dx][y + dy] != '#' && board[x][y] != 'O') { // 벽이나 구멍에 도달할 때까지 이동
        x += dx;
        y += dy;
        count++;
    }
    return {x, y, count}; // 최종 위치와 이동 거리 반환
}

// BFS로 상태 탐색
int bfs(vector<string> &board, int rx, int ry, int bx, int by) {
    queue<tuple<int, int, int, int, int>> q;  // 상태(빨간 구슬, 파란 구슬 위치, 이동 횟수)를 저장하는 큐
    set<tuple<int, int, int, int>> visited;   // 방문한 상태를 저장하는 집합
    q.push({rx, ry, bx, by, 0});              // 초기 상태 추가
    visited.insert({rx, ry, bx, by});         // 초기 상태 방문 기록

    while (!q.empty()) {
        auto [rx, ry, bx, by, depth] = q.front(); // 현재 상태 추출
        q.pop();

        if (depth >= 10) return 0; // 10번 이상 기울인 경우 실패

        for (int i = 0; i < 4; i++) { // 네 방향으로 기울이기
            auto [nrx, nry, rcnt] = move(rx, ry, dx[i], dy[i], board); // 빨간 구슬 이동
            auto [nbx, nby, bcnt] = move(bx, by, dx[i], dy[i], board); // 파란 구슬 이동

            if (board[nbx][nby] == 'O') continue;  // 파란 구슬이 구멍에 빠지면 실패
            if (board[nrx][nry] == 'O') return 1;  // 빨간 구슬이 구멍에 빠지면 성공

            // 두 구슬이 같은 위치에 있으면 조정
            if (nrx == nbx && nry == nby) {
                if (rcnt > bcnt) {  // 빨간 구슬이 더 많이 이동했다면 뒤로 한 칸
                    nrx -= dx[i];
                    nry -= dy[i];
                } else {  // 파란 구슬이 더 많이 이동했다면 뒤로 한 칸
                    nbx -= dx[i];
                    nby -= dy[i];
                }
            }

            // 방문하지 않은 상태라면 큐에 추가
            if (!visited.count({nrx, nry, nbx, nby})) {
                visited.insert({nrx, nry, nbx, nby});
                q.push({nrx, nry, nbx, nby, depth + 1});
            }
        }
    }
    return 0;  // 10번 내에 성공하지 못한 경우
}

// 문제 해결 함수
int solve(vector<string> &board) {
    int N = board.size(), M = board[0].size();
    int rx, ry, bx, by;

    // 보드에서 빨간 구슬과 파란 구슬 위치 찾기
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 'R') {
                rx = i;
                ry = j;
            }
            if (board[i][j] == 'B') {
                bx = i;
                by = j;
            }
        }
    }

    return bfs(board, rx, ry, bx, by);  // BFS로 문제 해결
}

// 메인 함수
int main() {
    int N, M;
    cin >> N >> M;
    vector<string> board(N);

    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    cout << solve(board) << endl;
    return 0;
}
