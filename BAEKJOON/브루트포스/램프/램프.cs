using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // 입력 처리
        var inputs = Console.ReadLine().Split();
        int N = int.Parse(inputs[0]);
        int M = int.Parse(inputs[1]);

        List<string> lampStates = new List<string>();

        for (int i = 0; i < N; i++)
        {
            lampStates.Add(Console.ReadLine().Trim());
        }

        int K = int.Parse(Console.ReadLine().Trim());

        // 최대 켜진 행 수 계산
        int result = MaxOnRows(N, M, lampStates, K);
        Console.WriteLine(result);
    }

    static int MaxOnRows(int N, int M, List<string> lampStates, int K)
    {
        Dictionary<string, int> rowCount = new Dictionary<string, int>();
        int maxOn = 0;

        foreach (var row in lampStates)
        {
            if (rowCount.ContainsKey(row))
            {
                rowCount[row]++;
            }
            else
            {
                rowCount[row] = 1;
            }
        }

        foreach (var entry in rowCount)
        {
            string row = entry.Key;
            int count = entry.Value;

            int zeroCount = row.Count(c => c == '0');

            if (zeroCount <= K && (K - zeroCount) % 2 == 0)
            {
                maxOn = Math.Max(maxOn, count);
            }
        }

        return maxOn;
    }
}
