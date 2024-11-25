using System;

class Program
{
    const int MOD = 1000000007; // 결과를 나눌 모듈러 값 설정

    static int CountBuildingArrangements(int N, int L, int R)
    {
        // 3D DP 배열 초기화
        int[,,] dp = new int[N + 1, L + 1, R + 1];

        dp[1, 1, 1] = 1; // 초기 조건: 빌딩 1개일 때 왼쪽과 오른쪽에서 각각 1개씩 보이는 경우

        // DP 계산
        for (int n = 2; n <= N; n++) // 빌딩의 개수를 2부터 N까지 반복
        {
            for (int l = 1; l <= L; l++) // 왼쪽에서 보이는 빌딩 개수를 1부터 L까지 반복
            {
                for (int r = 1; r <= R; r++) // 오른쪽에서 보이는 빌딩 개수를 1부터 R까지 반복
                {
                    // 가장 높은 빌딩이 왼쪽에서 보이게 추가된 경우
                    if (l > 1)
                        dp[n, l, r] = (dp[n, l, r] + dp[n - 1, l - 1, r]) % MOD;

                    // 가장 높은 빌딩이 오른쪽에서 보이게 추가된 경우
                    if (r > 1)
                        dp[n, l, r] = (dp[n, l, r] + dp[n - 1, l, r - 1]) % MOD;

                    // 가장 높은 빌딩이 중간에 추가된 경우
                    dp[n, l, r] = (dp[n, l, r] + (int)((long)(n - 2) * dp[n - 1, l, r] % MOD)) % MOD;
                }
            }
        }

        return dp[N, L, R]; // 최종 결과 반환
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split(); // 입력값 읽기
        int N = int.Parse(input[0]);
        int L = int.Parse(input[1]);
        int R = int.Parse(input[2]);

        Console.WriteLine(CountBuildingArrangements(N, L, R)); // 결과 출력
    }
}
