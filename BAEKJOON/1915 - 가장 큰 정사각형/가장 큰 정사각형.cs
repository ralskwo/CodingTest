using System;
using System.Collections.Generic;

class Program
{
    static int MaximalSquare(int n, int m, List<string> matrixStr)
    {
        if (matrixStr.Count == 0)
        {
            return 0;
        }

        int[,] dp = new int[n, m];
        int maxSide = 0;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (matrixStr[i][j] == '1')
                {
                    if (i == 0 || j == 0)
                    {
                        dp[i, j] = 1;  // 첫 행 또는 첫 열인 경우
                    }
                    else
                    {
                        // 이전 행, 이전 열, 대각선 값을 참고하여 최소값에 1을 더함
                        dp[i, j] = Math.Min(Math.Min(dp[i - 1, j], dp[i, j - 1]), dp[i - 1, j - 1]) + 1;
                    }
                    // 최대 변의 길이 갱신
                    maxSide = Math.Max(maxSide, dp[i, j]);
                }
            }
        }

        // 최대 변의 길이의 제곱이 가장 큰 정사각형의 넓이
        return maxSide * maxSide;
    }

    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();  // 첫 줄에서 n과 m을 입력 받음
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        List<string> matrixStr = new List<string>();
        for (int i = 0; i < n; ++i)
        {
            matrixStr.Add(Console.ReadLine().Trim());  // 다음 n개의 줄에서 문자열 리스트를 입력 받음
        }

        // 함수 호출 및 결과 출력
        Console.WriteLine(MaximalSquare(n, m, matrixStr));
    }
}
