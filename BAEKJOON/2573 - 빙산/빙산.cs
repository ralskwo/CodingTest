using System;
using System.Collections.Generic;

class Iceberg
{
    // 동서남북 방향을 나타내는 배열
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    // BFS를 사용하여 빙산의 한 덩어리를 탐색하는 함수
    static void BFS(int x, int y, int[,] iceberg, bool[,] visited)
    {
        Queue<(int, int)> queue = new Queue<(int, int)>();
        queue.Enqueue((x, y));
        visited[x, y] = true; // 현재 위치를 방문 처리

        while (queue.Count > 0)
        {
            var (cx, cy) = queue.Dequeue();

            // 동서남북 방향으로 인접한 칸을 탐색
            for (int i = 0; i < 4; ++i)
            {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 배열 범위 내에 있고, 빙산이 있으며, 아직 방문하지 않은 경우
                if (nx >= 0 && nx < iceberg.GetLength(0) && ny >= 0 && ny < iceberg.GetLength(1))
                {
                    if (iceberg[nx, ny] > 0 && !visited[nx, ny])
                    {
                        visited[nx, ny] = true; // 방문 처리
                        queue.Enqueue((nx, ny)); // 인접한 칸을 큐에 추가
                    }
                }
            }
        }
    }

    // 빙산을 녹이는 함수
    static List<(int, int)> MeltIceberg(int[,] iceberg, List<(int, int)> icebergPositions)
    {
        int[,] melt = new int[iceberg.GetLength(0), iceberg.GetLength(1)]; // 각 칸의 녹을 양을 저장할 배열
        List<(int, int)> newIcebergPositions = new List<(int, int)>(); // 녹은 후에도 남아 있는 빙산의 위치를 저장할 리스트

        foreach (var pos in icebergPositions)
        {
            int x = pos.Item1;
            int y = pos.Item2;
            if (iceberg[x, y] > 0)
            {
                int seaCount = 0; // 주변의 바다 칸의 개수를 카운트
                for (int i = 0; i < 4; ++i)
                {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (iceberg[nx, ny] == 0) // 바다(0)인 경우
                        seaCount++;
                }
                melt[x, y] = seaCount; // 현재 빙산 칸에 대해 녹을 양을 저장
            }
        }

        // 빙산 높이 감소
        foreach (var pos in icebergPositions)
        {
            int x = pos.Item1;
            int y = pos.Item2;
            if (iceberg[x, y] > 0)
            {
                iceberg[x, y] = Math.Max(0, iceberg[x, y] - melt[x, y]); // 빙산의 높이를 줄임
                if (iceberg[x, y] > 0) // 녹은 후에도 남아 있는 경우
                    newIcebergPositions.Add((x, y)); // 새로운 빙산 위치를 리스트에 추가
            }
        }

        return newIcebergPositions; // 업데이트된 빙산 위치 반환
    }

    // 현재 빙산이 몇 개의 덩어리로 분리되어 있는지 계산하는 함수
    static int CountIcebergParts(int[,] iceberg, List<(int, int)> icebergPositions)
    {
        bool[,] visited = new bool[iceberg.GetLength(0), iceberg.GetLength(1)];
        int count = 0; // 빙산 덩어리의 개수를 저장할 변수

        foreach (var pos in icebergPositions)
        {
            int x = pos.Item1;
            int y = pos.Item2;
            if (iceberg[x, y] > 0 && !visited[x, y]) // 빙산이고 아직 방문하지 않은 경우
            {
                BFS(x, y, iceberg, visited); // BFS를 사용하여 하나의 덩어리를 탐색
                count++; // 덩어리의 개수 증가
            }
        }

        return count; // 빙산의 총 덩어리 개수 반환
    }

    // 시뮬레이션을 진행하여 빙산이 분리되는 시점을 찾는 함수
    static int Simulate(int[,] iceberg)
    {
        int year = 0; // 경과한 시간을 나타내는 변수
        List<(int, int)> icebergPositions = new List<(int, int)>();

        // 초기 빙산의 위치 저장
        for (int i = 1; i < iceberg.GetLength(0) - 1; ++i)
        {
            for (int j = 1; j < iceberg.GetLength(1) - 1; ++j)
            {
                if (iceberg[i, j] > 0)
                    icebergPositions.Add((i, j));
            }
        }

        while (icebergPositions.Count > 0)
        {
            // 빙산이 몇 덩어리로 분리되었는지 계산
            int parts = CountIcebergParts(iceberg, icebergPositions);

            if (parts >= 2) // 빙산이 두 덩어리 이상으로 분리되었을 때
                return year; // 경과한 시간을 반환

            // 빙산을 한 해 녹임
            icebergPositions = MeltIceberg(iceberg, icebergPositions);
            year++; // 시간이 1년 경과
        }

        return 0; // 모두 녹을 때까지 분리되지 않으면 0 반환
    }

    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        int[,] iceberg = new int[n, m];

        // 빙산 높이 정보 입력
        for (int i = 0; i < n; ++i)
        {
            input = Console.ReadLine().Split();
            for (int j = 0; j < m; ++j)
            {
                iceberg[i, j] = int.Parse(input[j]);
            }
        }

        // 시뮬레이션 시작
        int result = Simulate(iceberg);
        Console.WriteLine(result);
    }
}
