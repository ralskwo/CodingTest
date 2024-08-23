using System;
using System.Collections.Generic;

class Program
{
    const int INF = int.MaxValue;

    // 플로이드-워셜 알고리즘을 수행하는 함수
    static void FloydWarshall(int n, int[,] dist, int[,] next)
    {
        for (int k = 0; k < n; ++k)
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    if (dist[i, k] != INF && dist[k, j] != INF && dist[i, k] + dist[k, j] < dist[i, j])
                    {
                        dist[i, j] = dist[i, k] + dist[k, j];
                        next[i, j] = next[i, k];
                    }
                }
            }
        }
    }

    // 경로를 재구성하는 함수
    static List<int> ConstructPath(int start, int end, int[,] next)
    {
        if (next[start, end] == -1)
        {
            return null; // 경로가 존재하지 않음
        }
        List<int> path = new List<int> { start };
        while (start != end)
        {
            start = next[start, end];
            // 경로가 없을 때 무한 루프 방지를 위해 체크
            if (start == -1) return null;
            path.Add(start);
        }
        return path;
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        int m = int.Parse(Console.ReadLine());

        int[,] dist = new int[n, n];
        int[,] next = new int[n, n];

        // 초기화
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (i == j)
                    dist[i, j] = 0;
                else
                    dist[i, j] = INF;

                next[i, j] = -1; // 초기 경로는 -1로 설정
            }
        }

        // 버스 정보 입력받기
        for (int i = 0; i < m; ++i)
        {
            string[] input = Console.ReadLine().Split();
            int a = int.Parse(input[0]) - 1;
            int b = int.Parse(input[1]) - 1;
            int c = int.Parse(input[2]);

            if (c < dist[a, b])
            {
                dist[a, b] = c;
                next[a, b] = b;
            }
        }

        // 플로이드-워셜 알고리즘 수행
        FloydWarshall(n, dist, next);

        // 모든 쌍에 대한 최단 거리 출력
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (dist[i, j] == INF)
                    Console.Write("0 ");
                else
                    Console.Write(dist[i, j] + " ");
            }
            Console.WriteLine();
        }

        // 경로 재구성 및 출력
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (dist[i, j] == INF)
                {
                    Console.WriteLine(0);
                }
                else
                {
                    List<int> path = ConstructPath(i, j, next);
                    if (path == null)
                    {
                        Console.WriteLine(0);
                    }
                    else
                    {
                        Console.Write(path.Count + " ");
                        foreach (int v in path)
                        {
                            Console.Write((v + 1) + " "); // 1-index로 변환하여 출력
                        }
                        Console.WriteLine();
                    }
                }
            }
        }
    }
}
