using System;
using System.Linq;

class Program
{
    const int INF = int.MaxValue;

    static int FloydWarshallMinCycle(int V, int[][] edges)
    {
        // 거리 행렬 초기화
        int[,] dist = new int[V, V];
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                dist[i, j] = INF;

        // 주어진 간선 정보로 거리 행렬 초기화
        foreach (var edge in edges)
        {
            int a = edge[0] - 1, b = edge[1] - 1, c = edge[2];
            dist[a, b] = Math.Min(dist[a, b], c);
        }

        // Floyd-Warshall 알고리즘 실행
        for (int k = 0; k < V; k++)
        {
            for (int i = 0; i < V; i++)
            {
                for (int j = 0; j < V; j++)
                {
                    // 오버플로우 방지
                    if (dist[i, k] != INF && dist[k, j] != INF)
                    {
                        dist[i, j] = Math.Min(dist[i, j], dist[i, k] + dist[k, j]);
                    }
                }
            }
        }

        // 최소 사이클 찾기
        int minCycle = INF;
        for (int i = 0; i < V; i++)
        {
            minCycle = Math.Min(minCycle, dist[i, i]);
        }

        // 결과 반환 (사이클이 없으면 -1 반환)
        return minCycle == INF ? -1 : minCycle;
    }

    static void Main(string[] args)
    {
        // 마을 수와 도로 수 입력
        int[] VE = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int V = VE[0], E = VE[1];

        // 도로 정보 입력
        int[][] edges = new int[E][];
        for (int i = 0; i < E; i++)
        {
            edges[i] = Console.ReadLine().Split().Select(int.Parse).ToArray();
        }

        // 최소 사이클 계산 및 결과 출력
        int result = FloydWarshallMinCycle(V, edges);
        Console.WriteLine(result);
    }
}