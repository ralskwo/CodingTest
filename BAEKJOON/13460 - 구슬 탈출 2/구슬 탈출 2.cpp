#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <set>

using namespace std;

int N, M;  // 보드의 세로, 가로 크기
vector<string> board;  // 보드 상태 저장
int dx[4] = {1, -1, 0, 0};  // 방향 배열 (상, 하, 좌, 우)
int dy[4] = {0, 0, 1, -1};

// 구슬 이동 함수: 특정 방향으로 이동하여 최종 위치와 이동 횟수 반환
tuple<int, int, int> move(int x, int y, int dx, int dy) {
    int count = 0;  // 이동 거리 기록
    while (board[x + dx][y + dy] != '#' && board[x][y] != 'O') {  // 벽이나 구멍에 도달할 때까지 이동
        x += dx;
        y += dy;
        count++;
    }
    return {x, y, count};  // 최종 위치와 이동 횟수 반환
}

// BFS를 이용해 최소 이동 횟수를 찾는 함수
int bfs(int rx, int ry, int bx, int by) {
    queue<tuple<int, int, int, int, int>> q;  // 빨간 구슬, 파란 구슬 위치 및 깊이 저장
    set<tuple<int, int, int, int>> visited;  // 방문 상태 기록
    q.push({rx, ry, bx, by, 1});
    visited.insert({rx, ry, bx, by});

    while (!q.empty()) {  // 큐가 빌 때까지 탐색
        int crx, cry, cbx, cby, depth;
        tie(crx, cry, cbx, cby, depth) = q.front();
        q.pop();

        if (depth > 10)  // 이동 횟수가 10 초과 시 실패로 간주
            return -1;

        for (int i = 0; i < 4; i++) {  // 네 방향(상, 하, 좌, 우)으로 이동 시도
            int nrx, nry, r_count;
            int nbx, nby, b_count;

            tie(nrx, nry, r_count) = move(crx, cry, dx[i], dy[i]);  // 빨간 구슬 이동
            tie(nbx, nby, b_count) = move(cbx, cby, dx[i], dy[i]);  // 파란 구슬 이동

            if (board[nbx][nby] == 'O')  // 파란 구슬이 구멍에 빠진 경우 실패
                continue;
            if (board[nrx][nry] == 'O')  // 빨간 구슬이 구멍에 빠진 경우 성공
                return depth;

            if (nrx == nbx && nry == nby) {  // 두 구슬이 같은 위치에 있는 경우
                if (r_count > b_count) {  // 이동 거리가 더 긴 구슬을 뒤로 조정
                    nrx -= dx[i];
                    nry -= dy[i];
                } else {
                    nbx -= dx[i];
                    nby -= dy[i];
                }
            }

            if (visited.find({nrx, nry, nbx, nby}) == visited.end()) {  // 방문하지 않은 상태면 큐에 추가
                visited.insert({nrx, nry, nbx, nby});
                q.push({nrx, nry, nbx, nby, depth + 1});
            }
        }
    }
    return -1;  // 10번 이하의 이동으로 빨간 구슬을 구멍에 넣을 수 없는 경우
}

int main() {
    cin >> N >> M;  // 보드 크기 입력
    board.resize(N);  // 보드 크기 할당
    int rx, ry, bx, by;  // 빨간 구슬과 파란 구슬의 초기 위치

    for (int i = 0; i < N; i++) {
        cin >> board[i];
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 'R') {  // 빨간 구슬 위치 저장
                rx = i;
                ry = j;
                board[i][j] = '.';
            } else if (board[i][j] == 'B') {  // 파란 구슬 위치 저장
                bx = i;
                by = j;
                board[i][j] = '.';
            }
        }
    }

    cout << bfs(rx, ry, bx, by) << endl;  // 결과 출력
    return 0;
}