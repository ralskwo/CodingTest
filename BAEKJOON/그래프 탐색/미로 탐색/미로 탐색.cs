using System;
using System.Collections.Generic;

class MazeSolver
{
    public static int BfsMaze(int[][] maze, int n, int m)
    {
        // 이동 방향: 상, 하, 좌, 우
        int[][] directions = new int[][]
        {
            new int[] {-1, 0}, new int[] {1, 0},
            new int[] {0, -1}, new int[] {0, 1}
        };

        // BFS를 위한 큐 초기화
        Queue<Tuple<int, int, int>> queue = new Queue<Tuple<int, int, int>>(); // (x, y, 거리)
        queue.Enqueue(new Tuple<int, int, int>(0, 0, 1));
        bool[,] visited = new bool[n, m];
        visited[0, 0] = true;

        while (queue.Count > 0)
        {
            var current = queue.Dequeue();
            int x = current.Item1;
            int y = current.Item2;
            int dist = current.Item3;

            // 도착 지점에 도달했을 때
            if (x == n - 1 && y == m - 1)
            {
                return dist;
            }

            // 4방향 탐색
            foreach (var direction in directions)
            {
                int nx = x + direction[0];
                int ny = y + direction[1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx, ny] && maze[nx][ny] == 1)
                {
                    visited[nx, ny] = true;
                    queue.Enqueue(new Tuple<int, int, int>(nx, ny, dist + 1));
                }
            }
        }

        // 도착 지점에 도달할 수 없는 경우
        return -1;
    }

    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        int[][] maze = new int[n][];
        for (int i = 0; i < n; i++)
        {
            maze[i] = new int[m];
            var row = Console.ReadLine();
            for (int j = 0; j < m; j++)
            {
                maze[i][j] = row[j] - '0';
            }
        }

        Console.WriteLine(BfsMaze(maze, n, m));
    }
}
