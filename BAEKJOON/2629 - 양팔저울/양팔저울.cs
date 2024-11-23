using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // 추의 개수를 입력받음
        int n = int.Parse(Console.ReadLine());
        
        // 추의 무게 리스트를 입력받음
        string[] weightsInput = Console.ReadLine().Split();
        int[] weights = new int[n];
        for (int i = 0; i < n; i++)
        {
            weights[i] = int.Parse(weightsInput[i]);
        }

        // 구슬의 개수를 입력받음
        int m = int.Parse(Console.ReadLine());

        // 구슬의 무게 리스트를 입력받음
        string[] marblesInput = Console.ReadLine().Split();
        int[] marbles = new int[m];
        for (int i = 0; i < m; i++)
        {
            marbles[i] = int.Parse(marblesInput[i]);
        }

        int maxWeight = 40000; // 구슬의 최대 무게
        bool[] dp = new bool[maxWeight + 1]; // DP 테이블
        dp[0] = true; // 무게 0은 항상 가능

        // 추를 이용해 가능한 무게 계산
        foreach (int weight in weights)
        {
            bool[] current = (bool[])dp.Clone(); // 기존 DP 테이블 복사

            for (int w = 0; w <= maxWeight; w++)
            {
                if (dp[w]) // 현재 무게가 가능한 경우
                {
                    if (w + weight <= maxWeight)
                    {
                        current[w + weight] = true; // 추를 왼쪽에 놓는 경우
                    }
                    if (Math.Abs(w - weight) <= maxWeight)
                    {
                        current[Math.Abs(w - weight)] = true; // 추를 오른쪽에 놓는 경우
                    }
                }
            }

            dp = current; // 갱신된 DP 테이블로 업데이트
        }

        // 결과 저장을 위한 리스트
        List<string> result = new List<string>();

        // 각 구슬의 무게가 DP 테이블에 포함되는지 확인
        foreach (int marble in marbles)
        {
            if (marble <= maxWeight && dp[marble])
            {
                result.Add("Y"); // 가능하면 Y
            }
            else
            {
                result.Add("N"); // 불가능하면 N
            }
        }

        // 결과 출력
        Console.WriteLine(string.Join(" ", result));
    }
}