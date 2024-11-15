using System;
using System.Collections.Generic;

class Program
{
    static int[] dx = { -1, 1, 0, 0 }; // 상하좌우 이동을 위한 방향 벡터
    static int[] dy = { 0, 0, -1, 1 };

    // BFS를 사용하여 연결된 배추를 탐색
    static void BFS(int x, int y, int[,] field, bool[,] visited, int M, int N)
    {
        Queue<(int, int)> queue = new Queue<(int, int)>();
        queue.Enqueue((x, y));
        visited[y, x] = true; // 현재 위치 방문 처리

        while (queue.Count > 0)
        {
            var (cx, cy) = queue.Dequeue();

            // 상하좌우로 이동하며 연결된 배추 탐색
            for (int i = 0; i < 4; i++)
            {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 범위 내에 있고, 방문하지 않았으며, 배추가 있는 경우
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && !visited[ny, nx] && field[ny, nx] == 1)
                {
                    visited[ny, nx] = true; // 방문 처리
                    queue.Enqueue((nx, ny)); // 다음 탐색 위치 추가
                }
            }
        }
    }

    static void Main()
    {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스 수

        for (int t = 0; t < T; t++)
        {
            var inputs = Console.ReadLine().Split();
            int M = int.Parse(inputs[0]); // 가로 길이
            int N = int.Parse(inputs[1]); // 세로 길이
            int K = int.Parse(inputs[2]); // 배추의 개수

            int[,] field = new int[N, M]; // 배추밭 정보
            bool[,] visited = new bool[N, M]; // 방문 여부

            // 배추의 위치 입력
            for (int i = 0; i < K; i++)
            {
                var position = Console.ReadLine().Split();
                int x = int.Parse(position[0]);
                int y = int.Parse(position[1]);
                field[y, x] = 1; // 배추가 있는 곳을 1로 표시
            }

            int wormCount = 0; // 필요한 지렁이 수
            for (int y = 0; y < N; y++)
            {
                for (int x = 0; x < M; x++)
                {
                    // 배추가 있고 방문하지 않은 경우
                    if (field[y, x] == 1 && !visited[y, x])
                    {
                        BFS(x, y, field, visited, M, N); // BFS를 통해 연결된 배추 탐색
                        wormCount++; // 새로운 군집 발견
                    }
                }
            }

            Console.WriteLine(wormCount); // 결과 출력
        }
    }
}