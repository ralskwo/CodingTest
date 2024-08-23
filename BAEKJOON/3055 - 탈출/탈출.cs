using System;
using System.Collections.Generic;

class Program
{
    static int R, C;
    static char[,] forest;
    static int[,] waterTime;
    static int[,] hedgehogTime;
    static Queue<(int, int)> waterQueue = new Queue<(int, int)>();
    static Queue<(int, int)> hedgehogQueue = new Queue<(int, int)>();

    static int BfsEscape()
    {
        // 물의 퍼짐 처리
        while (waterQueue.Count > 0)
        {
            var (x, y) = waterQueue.Dequeue();

            int[] dx = { -1, 1, 0, 0 };
            int[] dy = { 0, 0, -1, 1 };

            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < R && ny >= 0 && ny < C && forest[nx, ny] == '.' && waterTime[nx, ny] == -1)
                {
                    waterTime[nx, ny] = waterTime[x, y] + 1;
                    waterQueue.Enqueue((nx, ny));
                }
            }
        }

        // 고슴도치 이동 처리
        while (hedgehogQueue.Count > 0)
        {
            var (x, y) = hedgehogQueue.Dequeue();

            int[] dx = { -1, 1, 0, 0 };
            int[] dy = { 0, 0, -1, 1 };

            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < R && ny >= 0 && ny < C)
                {
                    if (forest[nx, ny] == 'D')
                    {
                        return hedgehogTime[x, y] + 1;
                    }
                    if (forest[nx, ny] == '.' && hedgehogTime[nx, ny] == -1)
                    {
                        if (waterTime[nx, ny] == -1 || waterTime[nx, ny] > hedgehogTime[x, y] + 1)
                        {
                            hedgehogTime[nx, ny] = hedgehogTime[x, y] + 1;
                            hedgehogQueue.Enqueue((nx, ny));
                        }
                    }
                }
            }
        }

        return -1;
    }

    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        R = int.Parse(input[0]);
        C = int.Parse(input[1]);

        forest = new char[R, C];
        waterTime = new int[R, C];
        hedgehogTime = new int[R, C];

        for (int i = 0; i < R; i++)
        {
            var row = Console.ReadLine();
            for (int j = 0; j < C; j++)
            {
                forest[i, j] = row[j];
                waterTime[i, j] = -1;
                hedgehogTime[i, j] = -1;

                if (forest[i, j] == '*')
                {
                    waterQueue.Enqueue((i, j));
                    waterTime[i, j] = 0;
                }
                else if (forest[i, j] == 'S')
                {
                    hedgehogQueue.Enqueue((i, j));
                    hedgehogTime[i, j] = 0;
                }
            }
        }

        int result = BfsEscape();
        if (result == -1)
        {
            Console.WriteLine("KAKTUS");
        }
        else
        {
            Console.WriteLine(result);
        }
    }
}
