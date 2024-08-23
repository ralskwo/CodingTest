using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        ACMCraft();
    }

    static void ACMCraft()
    {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스의 수

        while (T-- > 0)
        {
            var input = Console.ReadLine().Split();
            int N = int.Parse(input[0]); // 건물의 수
            int K = int.Parse(input[1]); // 규칙의 수

            int[] buildTimes = new int[N + 1]; // 각 건물을 짓는 데 걸리는 시간
            int[] indegree = new int[N + 1]; // 각 건물의 진입 차수
            List<int>[] graph = new List<int>[N + 1]; // 그래프 초기화
            int[] dp = new int[N + 1]; // 각 건물을 짓는 데 걸리는 최소 시간을 저장할 배열

            for (int i = 1; i <= N; i++)
            {
                graph[i] = new List<int>();
            }

            // 각 건물의 건설 시간을 설정합니다.
            input = Console.ReadLine().Split();
            for (int i = 1; i <= N; i++)
            {
                buildTimes[i] = int.Parse(input[i - 1]);
            }

            // 그래프를 구성하고 진입 차수를 설정합니다.
            for (int i = 0; i < K; i++)
            {
                input = Console.ReadLine().Split();
                int X = int.Parse(input[0]);
                int Y = int.Parse(input[1]);
                graph[X].Add(Y);
                indegree[Y]++;
            }

            int target = int.Parse(Console.ReadLine()); // 목표 건물

            Queue<int> queue = new Queue<int>();

            // 진입 차수가 0인 건물들을 큐에 추가하고, 초기 시간을 설정합니다.
            for (int i = 1; i <= N; i++)
            {
                if (indegree[i] == 0)
                {
                    queue.Enqueue(i);
                    dp[i] = buildTimes[i];
                }
            }

            // 위상 정렬을 수행하면서 각 건물을 짓는 데 걸리는 최소 시간을 계산합니다.
            while (queue.Count > 0)
            {
                int current = queue.Dequeue();
                foreach (int neighbor in graph[current])
                {
                    indegree[neighbor]--;
                    dp[neighbor] = Math.Max(dp[neighbor], dp[current] + buildTimes[neighbor]);
                    if (indegree[neighbor] == 0)
                    {
                        queue.Enqueue(neighbor);
                    }
                }
            }

            // 목표 건물을 짓는 데 걸리는 최소 시간을 출력합니다.
            Console.WriteLine(dp[target]);
        }
    }
}
