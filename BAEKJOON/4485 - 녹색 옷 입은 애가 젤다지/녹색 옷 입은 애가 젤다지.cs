using System;
using System.Collections.Generic;

class Program
{
    static readonly int INF = int.MaxValue;
    static readonly (int, int)[] directions = { (-1, 0), (1, 0), (0, -1), (0, 1) };

    static int Dijkstra(int[,] grid, int N)
    {
        var pq = new SortedSet<(int, int, int)>();
        pq.Add((grid[0, 0], 0, 0));
        int[,] minRupee = new int[N, N];
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                minRupee[i, j] = INF;
            }
        }
        minRupee[0, 0] = grid[0, 0];

        while (pq.Count > 0)
        {
            var current = pq.Min;
            pq.Remove(current);
            int currRupee = current.Item1, x = current.Item2, y = current.Item3;

            if (currRupee > minRupee[x, y])
            {
                continue;
            }

            foreach (var (dx, dy) in directions)
            {
                int nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < N && ny >= 0 && ny < N)
                {
                    int newRupee = currRupee + grid[nx, ny];
                    if (newRupee < minRupee[nx, ny])
                    {
                        minRupee[nx, ny] = newRupee;
                        pq.Add((newRupee, nx, ny));
                    }
                }
            }
        }

        return minRupee[N - 1, N - 1];
    }

    static List<string> SolveProblems(List<(int, int[,])> testCases)
    {
        var results = new List<string>();
        for (int idx = 0; idx < testCases.Count; idx++)
        {
            int N = testCases[idx].Item1;
            int[,] grid = testCases[idx].Item2;
            int minRupee = Dijkstra(grid, N);
            results.Add($"Problem {idx + 1}: {minRupee}");
        }
        return results;
    }

    static void Main()
    {
        var input = Console.In.ReadToEnd().Split(new[] { ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
        int index = 0;
        var testCases = new List<(int, int[,])>();

        while (true)
        {
            int N = int.Parse(input[index++]);
            if (N == 0) break;
            int[,] grid = new int[N, N];
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    grid[i, j] = int.Parse(input[index++]);
                }
            }
            testCases.Add((N, grid));
        }

        List<string> results = SolveProblems(testCases);
        foreach (var result in results)
        {
            Console.WriteLine(result);
        }
    }
}
