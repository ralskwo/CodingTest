using System;
using System.Collections.Generic;

class Program
{
    struct Fish
    {
        public int Dist;
        public int X;
        public int Y;

        public Fish(int dist, int x, int y)
        {
            Dist = dist;
            X = x;
            Y = y;
        }
    }

    static List<Fish> Bfs(int startX, int startY, int size, int[,] grid)
    {
        int N = grid.GetLength(0);
        bool[,] visited = new bool[N, N];
        Queue<Tuple<int, int, int>> queue = new Queue<Tuple<int, int, int>>();
        queue.Enqueue(Tuple.Create(startX, startY, 0));
        visited[startX, startY] = true;
        List<Fish> fish = new List<Fish>();

        int[,] directions = new int[,] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        while (queue.Count > 0)
        {
            var current = queue.Dequeue();
            int x = current.Item1;
            int y = current.Item2;
            int dist = current.Item3;

            for (int i = 0; i < directions.GetLength(0); i++)
            {
                int nx = x + directions[i, 0];
                int ny = y + directions[i, 1];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx, ny])
                {
                    if (grid[nx, ny] <= size)
                    {
                        visited[nx, ny] = true;
                        queue.Enqueue(Tuple.Create(nx, ny, dist + 1));
                        if (grid[nx, ny] > 0 && grid[nx, ny] < size)
                        {
                            fish.Add(new Fish(dist + 1, nx, ny));
                        }
                    }
                }
            }
        }

        fish.Sort((a, b) => 
        {
            if (a.Dist == b.Dist)
            {
                if (a.X == b.X)
                {
                    return a.Y.CompareTo(b.Y);
                }
                return a.X.CompareTo(b.X);
            }
            return a.Dist.CompareTo(b.Dist);
        });

        return fish;
    }

    static int BabyShark(int[,] grid)
    {
        int N = grid.GetLength(0);
        int sharkX = 0, sharkY = 0;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (grid[i, j] == 9)
                {
                    sharkX = i;
                    sharkY = j;
                    grid[i, j] = 0;
                }
            }
        }

        int size = 2;
        int eaten = 0;
        int time = 0;

        while (true)
        {
            List<Fish> result = Bfs(sharkX, sharkY, size, grid);
            if (result.Count == 0)
            {
                break;
            }

            Fish nearest = result[0];
            time += nearest.Dist;
            sharkX = nearest.X;
            sharkY = nearest.Y;
            grid[sharkX, sharkY] = 0;
            eaten++;

            if (eaten == size)
            {
                size++;
                eaten = 0;
            }
        }

        return time;
    }

    static void Main()
    {
        int N = int.Parse(Console.ReadLine().Trim());
        int[,] grid = new int[N, N];

        for (int i = 0; i < N; i++)
        {
            string[] line = Console.ReadLine().Trim().Split();
            for (int j = 0; j < N; j++)
            {
                grid[i, j] = int.Parse(line[j]);
            }
        }

        Console.WriteLine(BabyShark(grid));
    }
}
