using System;
using System.Collections.Generic;

class Program {
    static int N, M;  // 보드의 세로, 가로 크기
    static List<string> board = new List<string>();  // 보드 상태 저장
    static int[] dx = { 1, -1, 0, 0 };  // 방향 배열 (상, 하, 좌, 우)
    static int[] dy = { 0, 0, 1, -1 };

    // 구슬 이동 함수: 특정 방향으로 이동하여 최종 위치와 이동 횟수 반환
    static (int, int, int) Move(int x, int y, int dx, int dy) {
        int count = 0;
        while (board[x + dx][y + dy] != '#' && board[x][y] != 'O') {
            x += dx;
            y += dy;
            count++;
        }
        return (x, y, count);
    }

    // BFS를 이용해 최소 이동 횟수를 찾는 함수
    static int Bfs(int rx, int ry, int bx, int by) {
        Queue<(int, int, int, int, int)> q = new Queue<(int, int, int, int, int)>();
        HashSet<(int, int, int, int)> visited = new HashSet<(int, int, int, int)>();
        q.Enqueue((rx, ry, bx, by, 1));
        visited.Add((rx, ry, bx, by));

        while (q.Count > 0) {
            var (crx, cry, cbx, cby, depth) = q.Dequeue();

            if (depth > 10)  // 이동 횟수가 10 초과 시 실패로 간주
                return -1;

            for (int i = 0; i < 4; i++) {  // 네 방향(상, 하, 좌, 우)으로 이동 시도
                var (nrx, nry, rCount) = Move(crx, cry, dx[i], dy[i]);
                var (nbx, nby, bCount) = Move(cbx, cby, dx[i], dy[i]);

                if (board[nbx][nby] == 'O')  // 파란 구슬이 구멍에 빠진 경우 실패
                    continue;
                if (board[nrx][nry] == 'O')  // 빨간 구슬이 구멍에 빠진 경우 성공
                    return depth;

                if (nrx == nbx && nry == nby) {  // 두 구슬이 같은 위치에 있는 경우
                    if (rCount > bCount) {
                        nrx -= dx[i];
                        nry -= dy[i];
                    } else {
                        nbx -= dx[i];
                        nby -= dy[i];
                    }
                }

                if (!visited.Contains((nrx, nry, nbx, nby))) {  // 방문하지 않은 상태면 큐에 추가
                    visited.Add((nrx, nry, nbx, nby));
                    q.Enqueue((nrx, nry, nbx, nby, depth + 1));
                }
            }
        }
        return -1;
    }

    static void Main() {
        var inputs = Console.ReadLine().Split();
        N = int.Parse(inputs[0]);
        M = int.Parse(inputs[1]);

        int rx = 0, ry = 0, bx = 0, by = 0;  // 빨간 구슬과 파란 구슬의 초기 위치
        for (int i = 0; i < N; i++) {
            board.Add(Console.ReadLine());
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 'R') {  // 빨간 구슬 위치 저장
                    rx = i;
                    ry = j;
                    board[i] = board[i].Remove(j, 1).Insert(j, ".");
                } else if (board[i][j] == 'B') {  // 파란 구슬 위치 저장
                    bx = i;
                    by = j;
                    board[i] = board[i].Remove(j, 1).Insert(j, ".");
                }
            }
        }

        Console.WriteLine(Bfs(rx, ry, bx, by));  // 결과 출력
    }
}