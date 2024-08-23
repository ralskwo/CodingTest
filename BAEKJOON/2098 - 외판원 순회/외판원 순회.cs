using System;
using System.Collections.Generic;

class TravelingSalesman
{
    // 도시의 수를 저장할 변수
    static int N;
    // 도시 간의 비용을 저장할 2차원 배열
    static int[,] W;
    // 동적 계획법을 위한 배열
    static int[,] dp;
    // 무한대를 나타내기 위한 큰 수
    static int INF = 1000000 * 16 + 1;

    // TSP (Traveling Salesman Problem)를 해결하기 위한 재귀 함수
    static int TSP(int current, int visited)
    {
        // 모든 도시를 방문한 경우
        if (visited == (1 << N) - 1)
        {
            // 시작 도시로 돌아갈 수 없는 경우 큰 값을 반환
            if (W[current, 0] == 0) return INF;
            // 시작 도시로 돌아가는 비용 반환
            return W[current, 0];
        }

        // 이미 계산된 값이 있는 경우 그 값을 반환
        if (dp[current, visited] != 0) return dp[current, visited];

        // 초기값을 무한대로 설정
        dp[current, visited] = INF;
        
        // 모든 도시를 순회
        for (int next = 0; next < N; next++)
        {
            // 이미 방문한 도시거나 갈 수 없는 경우 무시
            if ((visited & (1 << next)) != 0 || W[current, next] == 0) continue;
            // 다음 방문할 도시를 추가한 visited 값 계산
            int nextVisited = visited | (1 << next);
            // 재귀 호출을 통해 최소 비용 갱신
            dp[current, visited] = Math.Min(dp[current, visited], W[current, next] + TSP(next, nextVisited));
        }

        // 계산된 최소 비용 반환
        return dp[current, visited];
    }

    public static void Main()
    {
        // 입력을 받아 첫 번째 줄에서 도시의 수 N을 파싱
        string[] input = Console.ReadLine().Split();
        N = int.Parse(input[0]);

        // W 배열과 dp 배열 초기화
        W = new int[N, N];
        dp = new int[N, 1 << N];

        // N개의 줄에 걸쳐 도시 간의 비용 입력 받음
        for (int i = 0; i < N; i++)
        {
            input = Console.ReadLine().Split();
            for (int j = 0; j < N; j++)
            {
                W[i, j] = int.Parse(input[j]);
            }
        }

        // TSP 함수 호출하여 결과 계산 후 출력
        int result = TSP(0, 1);
        Console.WriteLine(result);
    }
}
