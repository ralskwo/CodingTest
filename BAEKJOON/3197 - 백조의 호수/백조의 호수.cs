using System;
using System.Collections.Generic;

class Program
{
    static int R, C;
    static char[,] lake;
    static Queue<(int, int)> waterQueue = new Queue<(int, int)>();
    static Queue<(int, int)> nextWaterQueue = new Queue<(int, int)>();
    static Queue<(int, int)> swanQueue = new Queue<(int, int)>();
    static Queue<(int, int)> nextSwanQueue = new Queue<(int, int)>();
    static bool[,] visitedSwan;
    static (int, int)[] swans = new (int, int)[2];
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    // 얼음을 녹이는 함수
    static void MeltIce()
    {
        while (waterQueue.Count > 0)
        {
            var (x, y) = waterQueue.Dequeue();
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < R && ny < C && lake[nx, ny] == 'X')
                {
                    lake[nx, ny] = '.';
                    nextWaterQueue.Enqueue((nx, ny));
                }
            }
        }
    }

    // 백조가 이동 가능한지 확인하는 함수
    static bool MoveSwan()
    {
        while (swanQueue.Count > 0)
        {
            var (x, y) = swanQueue.Dequeue();
            if (x == swans[1].Item1 && y == swans[1].Item2)
                return true;

            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < R && ny < C && !visitedSwan[nx, ny])
                {
                    visitedSwan[nx, ny] = true;
                    if (lake[nx, ny] == '.')
                        swanQueue.Enqueue((nx, ny));
                    else if (lake[nx, ny] == 'X')
                        nextSwanQueue.Enqueue((nx, ny));
                }
            }
        }
        return false;
    }

    // 문제 해결 함수
    static int Solve()
    {
        int days = 0;

        while (true)
        {
            if (MoveSwan())
                return days;

            MeltIce();

            swanQueue = nextSwanQueue;
            nextSwanQueue = new Queue<(int, int)>();

            waterQueue = nextWaterQueue;
            nextWaterQueue = new Queue<(int, int)>();

            days++;
        }
    }

    static void Main(string[] args)
    {
        var inputs = Console.ReadLine().Split();
        R = int.Parse(inputs[0]);
        C = int.Parse(inputs[1]);
        lake = new char[R, C];
        visitedSwan = new bool[R, C];

        int swanIndex = 0;

        // 호수 상태 입력
        for (int i = 0; i < R; i++)
        {
            var line = Console.ReadLine();
            for (int j = 0; j < C; j++)
            {
                lake[i, j] = line[j];
                if (lake[i, j] == 'L')
                {
                    swans[swanIndex++] = (i, j);
                    lake[i, j] = '.';
                }
                if (lake[i, j] == '.')
                {
                    waterQueue.Enqueue((i, j));
                }
            }
        }

        // 첫 번째 백조의 위치를 BFS 시작점으로 설정
        swanQueue.Enqueue(swans[0]);
        visitedSwan[swans[0].Item1, swans[0].Item2] = true;

        // 문제 해결 및 결과 출력
        Console.WriteLine(Solve());
    }
}
