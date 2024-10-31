using System;
using System.Collections.Generic;

class Program
{
    const int MOD = 9901; // 나머지를 위한 상수 값

    static void Main()
    {
        // 격자판 크기 입력
        int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int N = input[0];
        int M = input[1];

        // 가능한 배치 수 계산 및 출력
        Console.WriteLine(CountWaysToFill(N, M));
    }

    // 가능한 경우의 수를 계산하는 함수
    static int CountWaysToFill(int N, int M)
    {
        // 격자판의 칸 수가 홀수이면 도미노로 완전히 채울 수 없음
        if ((N * M) % 2 != 0) return 0;

        // DP 배열 초기화: dp[col][state] 형태로 사용
        int[,] dp = new int[M + 1, 1 << N];
        dp[0, 0] = 1; // 초기 상태에서 가능한 배치 수는 1

        // 각 열을 순차적으로 탐색
        for (int col = 0; col < M; ++col)
        {
            for (int state = 0; state < (1 << N); ++state)
            {
                if (dp[col, state] == 0) continue; // 불가능한 상태는 건너뜀

                // 현재 상태로부터 다음 상태를 생성
                List<int> nextStates = new List<int>();
                GenerateNextStates(0, N, state, 0, nextStates);
                foreach (int nextState in nextStates)
                {
                    dp[col + 1, nextState] = (dp[col + 1, nextState] + dp[col, state]) % MOD;
                }
            }
        }
        return dp[M, 0]; // 마지막 열이 완전히 채워진 경우의 수 반환
    }

    // 현재 상태에서 다음 상태로 전이 가능한 상태 생성 함수
    static void GenerateNextStates(int pos, int N, int current_state, int next_state, List<int> nextStates)
    {
        if (pos == N)
        {
            nextStates.Add(next_state); // 완성된 다음 상태 추가
            return;
        }
        if ((current_state & (1 << pos)) != 0) // 현재 위치에 도미노가 이미 놓여 있으면
        {
            GenerateNextStates(pos + 1, N, current_state, next_state, nextStates); // 다음 칸으로 이동
        }
        else
        {
            GenerateNextStates(pos + 1, N, current_state, next_state | (1 << pos), nextStates); // 세로 배치
            if (pos + 1 < N && (current_state & (1 << (pos + 1))) == 0) // 가로 배치가 가능한지 확인
            {
                GenerateNextStates(pos + 2, N, current_state, next_state, nextStates);
            }
        }
    }
}