using System;
using System.Collections.Generic;

class MarbleEscape {
    static int[] dx = { -1, 1, 0, 0 }; // 상, 하, 좌, 우 방향 벡터
    static int[] dy = { 0, 0, -1, 1 };

    // 구슬 이동 함수
    static (int, int, int) Move(int x, int y, int dx, int dy, char[,] board) {
        int count = 0; // 이동 거리
        while (board[x + dx, y + dy] != '#' && board[x, y] != 'O') { // 벽이나 구멍을 만나기 전까지 이동
            x += dx;
            y += dy;
            count++;
        }
        return (x, y, count); // 최종 위치와 이동 거리 반환
    }

    // BFS로 상태 탐색
    static int Bfs(char[,] board, int rx, int ry, int bx, int by) {
        Queue<(int, int, int, int, int)> queue = new(); // BFS 상태 저장 큐
        HashSet<(int, int, int, int)> visited = new();  // 방문한 상태 저장 집합
        queue.Enqueue((rx, ry, bx, by, 0)); // 초기 상태 추가
        visited.Add((rx, ry, bx, by));      // 초기 상태 방문 기록

        while (queue.Count > 0) {
            var (crx, cry, cbx, cby, depth) = queue.Dequeue(); // 큐에서 상태 꺼냄

            if (depth >= 10) return 0; // 10번 이상 기울인 경우 실패로 간주

            for (int i = 0; i < 4; i++) { // 네 방향으로 기울이기
                var (nrx, nry, rcnt) = Move(crx, cry, dx[i], dy[i], board); // 빨간 구슬 이동
                var (nbx, nby, bcnt) = Move(cbx, cby, dx[i], dy[i], board); // 파란 구슬 이동

                if (board[nbx, nby] == 'O') continue; // 파란 구슬이 구멍에 빠지면 실패
                if (board[nrx, nry] == 'O') return 1; // 빨간 구슬이 구멍에 빠지면 성공

                // 두 구슬이 같은 위치에 도달한 경우
                if (nrx == nbx && nry == nby) {
                    if (rcnt > bcnt) { // 빨간 구슬이 더 멀리 이동한 경우 뒤로 이동
                        nrx -= dx[i];
                        nry -= dy[i];
                    } else { // 파란 구슬이 더 멀리 이동한 경우 뒤로 이동
                        nbx -= dx[i];
                        nby -= dy[i];
                    }
                }

                // 방문하지 않은 상태만 큐에 추가
                if (!visited.Contains((nrx, nry, nbx, nby))) {
                    visited.Add((nrx, nry, nbx, nby)); // 새로운 상태 방문 기록
                    queue.Enqueue((nrx, nry, nbx, nby, depth + 1)); // 새로운 상태 큐에 추가
                }
            }
        }

        return 0; // 10번 이내에 성공하지 못한 경우 실패
    }

    // 문제 해결 함수
    static int Solve(char[,] board, int n, int m) {
        int rx = 0, ry = 0, bx = 0, by = 0;

        // 보드에서 빨간 구슬과 파란 구슬의 초기 위치 찾기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i, j] == 'R') {
                    rx = i; ry = j;
                }
                if (board[i, j] == 'B') {
                    bx = i; by = j;
                }
            }
        }

        return Bfs(board, rx, ry, bx, by); // BFS를 통해 문제 해결
    }

    // 메인 함수
    static void Main() {
        var input = Console.ReadLine().Split(); // 보드 크기 입력
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        char[,] board = new char[n, m]; // 2D 보드 배열 선언

        for (int i = 0; i < n; i++) { // 보드 상태 입력
            var line = Console.ReadLine();
            for (int j = 0; j < m; j++) {
                board[i, j] = line[j];
            }
        }

        Console.WriteLine(Solve(board, n, m)); // 결과 출력
    }
}
