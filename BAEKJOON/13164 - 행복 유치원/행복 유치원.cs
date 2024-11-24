using System;
using System.Collections.Generic;

class Program
{
    static int MinimumCost(int N, int K, List<int> heights)
    {
        // 인접한 키 차이를 저장할 리스트
        List<int> differences = new List<int>();

        // 인접한 키 차이를 계산하여 differences 리스트에 추가
        for (int i = 0; i < N - 1; i++)
        {
            differences.Add(heights[i + 1] - heights[i]);
        }

        // 키 차이를 내림차순으로 정렬
        differences.Sort((a, b) => b - a);

        // K-1개의 큰 차이를 제거한 뒤 남은 차이들의 합 계산
        int totalCost = 0;
        for (int i = K - 1; i < differences.Count; i++)
        {
            totalCost += differences[i];
        }

        // 최소 비용 반환
        return totalCost;
    }

    static void Main(string[] args)
    {
        // 원생 수 N과 조의 개수 K 입력
        string[] inputs = Console.ReadLine().Split(' ');
        int N = int.Parse(inputs[0]);
        int K = int.Parse(inputs[1]);

        // 원생들의 키를 저장할 리스트 heights
        List<int> heights = new List<int>(Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse));

        // 최소 비용 계산 및 출력
        Console.WriteLine(MinimumCost(N, K, heights));
    }
}