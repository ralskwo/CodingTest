using System;
using System.Collections.Generic;

class Program
{
    // 주어진 좌표 (x, y)를 클릭했을 때 보드를 반전시키는 함수
    static void Flip(char[,] board, int x, int y)
    {
        int[] dx = { 0, 1, -1, 0, 0 };
        int[] dy = { 0, 0, 0, 1, -1 };

        for (int i = 0; i < 5; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3)
            {
                board[nx, ny] = (board[nx, ny] == '*') ? '.' : '*';
            }
        }
    }

    // 모든 가능한 클릭 조합을 시도하여 최소 클릭 수를 찾는 함수
    static int MinClicksToAllWhite(char[,] board)
    {
        int minClicks = int.MaxValue;

        for (int clicks = 0; clicks < (1 << 9); clicks++)
        {
            char[,] tempBoard = (char[,])board.Clone();
            int clickCount = 0;

            for (int idx = 0; idx < 9; idx++)
            {
                if ((clicks & (1 << idx)) != 0)
                {
                    int x = idx / 3;
                    int y = idx % 3;
                    Flip(tempBoard, x, y);
                    clickCount++;
                }
            }

            bool allWhite = true;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (tempBoard[i, j] == '*')
                    {
                        allWhite = false;
                        break;
                    }
                }
                if (!allWhite) break;
            }

            if (allWhite)
            {
                minClicks = Math.Min(minClicks, clickCount);
            }
        }

        return minClicks;
    }

    static void Main(string[] args)
    {
        int P = int.Parse(Console.ReadLine());
        List<int> results = new List<int>();

        for (int p = 0; p < P; p++)
        {
            char[,] board = new char[3, 3];
            for (int i = 0; i < 3; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < 3; j++)
                {
                    board[i, j] = line[j];
                }
            }
            results.Add(MinClicksToAllWhite(board));
        }

        foreach (int result in results)
        {
            Console.WriteLine(result);
        }
    }
}
