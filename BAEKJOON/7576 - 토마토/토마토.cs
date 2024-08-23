using System;
using System.Collections.Generic;

class Program
{
    // BFS를 수행하기 위한 방향 벡터 (상, 하, 좌, 우)
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    static void Main(string[] args)
    {
        // 입력 처리
        string[] input = Console.ReadLine().Split();
        int M = int.Parse(input[0]); // 가로 크기
        int N = int.Parse(input[1]); // 세로 크기

        int[,] farm = new int[N, M];
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();
        int days = 0;

        // 농장의 상태를 입력받고 익은 토마토를 큐에 추가
        for (int i = 0; i < N; i++)
        {
            input = Console.ReadLine().Split();
            for (int j = 0; j < M; j++)
            {
                farm[i, j] = int.Parse(input[j]);
                if (farm[i, j] == 1)
                {
                    queue.Enqueue(new Tuple<int, int>(i, j));
                }
            }
        }

        // BFS 탐색 시작
        while (queue.Count > 0)
        {
            int size = queue.Count;
            bool changed = false;

            for (int i = 0; i < size; i++)
            {
                var current = queue.Dequeue();
                int x = current.Item1;
                int y = current.Item2;

                // 네 방향으로 이동
                for (int dir = 0; dir < 4; dir++)
                {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];

                    // 유효한 위치인지와 익지 않은 토마토인지 확인
                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && farm[nx, ny] == 0)
                    {
                        farm[nx, ny] = 1;  // 토마토를 익게 함
                        queue.Enqueue(new Tuple<int, int>(nx, ny));
                        changed = true;
                    }
                }
            }

            // 이번 단계에서 토마토가 익었다면 경과 일수를 증가
            if (changed)
            {
                days++;
            }
        }

        // 모든 토마토가 익었는지 확인
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (farm[i, j] == 0)
                {
                    Console.WriteLine(-1);
                    return;
                }
            }
        }

        // 모든 토마토가 익은 최소 일수를 출력
        Console.WriteLine(days);
    }
}
