using System;
using System.Collections.Generic;

class Program
{
    static int[] horse_dx = { -2, -1, 1, 2, 2, 1, -1, -2 }; // 말의 x방향 이동 배열
    static int[] horse_dy = { -1, -2, -2, -1, 1, 2, 2, 1 }; // 말의 y방향 이동 배열

    static int[] monkey_dx = { -1, 1, 0, 0 }; // 원숭이의 x방향 이동 배열
    static int[] monkey_dy = { 0, 0, -1, 1 }; // 원숭이의 y방향 이동 배열

    static void Main()
    {
        int K = int.Parse(Console.ReadLine()); // K 입력 받기
        string[] wh = Console.ReadLine().Split(); // W와 H 입력 받기
        int W = int.Parse(wh[0]);
        int H = int.Parse(wh[1]);

        int[,] grid = new int[H, W]; // 격자판 정보 저장
        for (int i = 0; i < H; i++)
        {
            string[] line = Console.ReadLine().Split();
            for (int j = 0; j < W; j++)
            {
                grid[i, j] = int.Parse(line[j]);
            }
        }

        bool[,,] visited = new bool[H, W, K + 1]; // 방문 여부 체크를 위한 3차원 배열

        Queue<Tuple<int, int, int, int>> q = new Queue<Tuple<int, int, int, int>>(); // BFS를 위한 큐
        q.Enqueue(new Tuple<int, int, int, int>(0, 0, 0, 0)); // 시작 위치 추가
        visited[0, 0, 0] = true; // 시작 위치 방문 처리

        while (q.Count > 0)
        {
            var current = q.Dequeue(); // 큐에서 현재 위치 가져오기
            int x = current.Item1;
            int y = current.Item2;
            int cnt = current.Item3;
            int k = current.Item4;

            if (x == W - 1 && y == H - 1) // 도착 지점에 도달한 경우
            {
                Console.WriteLine(cnt); // 이동 횟수 출력
                return; // 프로그램 종료
            }

            if (k < K) // 말의 이동을 더 사용할 수 있는 경우
            {
                for (int i = 0; i < 8; i++)
                {
                    int nx = x + horse_dx[i];
                    int ny = y + horse_dy[i];
                    int nk = k + 1;

                    if (nx >= 0 && nx < W && ny >= 0 && ny < H) // 격자판 범위 내인지 확인
                    {
                        if (!visited[ny, nx, nk] && grid[ny, nx] == 0) // 방문하지 않았고 평지인 경우
                        {
                            visited[ny, nx, nk] = true; // 방문 처리
                            q.Enqueue(new Tuple<int, int, int, int>(nx, ny, cnt + 1, nk)); // 큐에 추가
                        }
                    }
                }
            }

            for (int i = 0; i < 4; i++) // 원숭이의 일반 이동
            {
                int nx = x + monkey_dx[i];
                int ny = y + monkey_dy[i];
                int nk = k;

                if (nx >= 0 && nx < W && ny >= 0 && ny < H) // 격자판 범위 내인지 확인
                {
                    if (!visited[ny, nx, nk] && grid[ny, nx] == 0) // 방문하지 않았고 평지인 경우
                    {
                        visited[ny, nx, nk] = true; // 방문 처리
                        q.Enqueue(new Tuple<int, int, int, int>(nx, ny, cnt + 1, nk)); // 큐에 추가
                    }
                }
            }
        }

        Console.WriteLine(-1); // 도착 지점에 도달할 수 없는 경우 -1 출력
    }
}
