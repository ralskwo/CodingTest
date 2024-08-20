using System;
using System.Collections.Generic;

class Program
{
    static int N;
    static char[,] village;
    static int[,] altitude;
    static (int, int) postOffice;
    static List<int> heights = new List<int>();
    static int totalHouses = 0;

    static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};

    static bool CanDeliver(int minHeight, int maxHeight)
    {
        if (altitude[postOffice.Item1, postOffice.Item2] < minHeight || 
            altitude[postOffice.Item1, postOffice.Item2] > maxHeight)
        {
            return false;
        }

        bool[,] visited = new bool[N, N];
        Queue<(int, int)> queue = new Queue<(int, int)>();
        queue.Enqueue(postOffice);
        visited[postOffice.Item1, postOffice.Item2] = true;
        int delivered = 0;

        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();

            if (village[x, y] == 'K')
            {
                delivered++;
            }

            for (int i = 0; i < 8; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx, ny])
                {
                    if (altitude[nx, ny] >= minHeight && altitude[nx, ny] <= maxHeight)
                    {
                        visited[nx, ny] = true;
                        queue.Enqueue((nx, ny));
                    }
                }
            }
        }

        return delivered == totalHouses;
    }

    static void Main(string[] args)
    {
        N = int.Parse(Console.ReadLine());
        village = new char[N, N];
        altitude = new int[N, N];

        HashSet<int> heightSet = new HashSet<int>();

        for (int i = 0; i < N; i++)
        {
            string row = Console.ReadLine();
            for (int j = 0; j < N; j++)
            {
                village[i, j] = row[j];
            }
        }

        for (int i = 0; i < N; i++)
        {
            string[] altitudeRow = Console.ReadLine().Split(' ');
            for (int j = 0; j < N; j++)
            {
                altitude[i, j] = int.Parse(altitudeRow[j]);
                heightSet.Add(altitude[i, j]);

                if (village[i, j] == 'P')
                {
                    postOffice = (i, j);
                }
                if (village[i, j] == 'K')
                {
                    totalHouses++;
                }
            }
        }

        heights.AddRange(heightSet);
        heights.Sort();

        int left = 0, right = 0;
        int minFatigue = int.MaxValue;

        while (right < heights.Count)
        {
            if (left < heights.Count && CanDeliver(heights[left], heights[right]))
            {
                minFatigue = Math.Min(minFatigue, heights[right] - heights[left]);
                left++;
            }
            else
            {
                right++;
            }
        }

        Console.WriteLine(minFatigue);
    }
}
