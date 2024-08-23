using System;

class Program
{
    static void Main()
    {
        // 입력 받기
        string X = Console.ReadLine().Trim();
        string Y = Console.ReadLine().Trim();

        // 함수 호출 및 결과 출력
        var result = Lcs(X, Y);
        int length_of_lcs = result.Item1;
        string lcs_str = result.Item2;

        Console.WriteLine(length_of_lcs);  // LCS의 길이 출력
        if (length_of_lcs > 0)
        {
            Console.WriteLine(lcs_str);  // LCS 문자열 출력
        }
    }

    static Tuple<int, string> Lcs(string X, string Y)
    {
        int m = X.Length;  // 첫 번째 문자열의 길이
        int n = Y.Length;  // 두 번째 문자열의 길이

        // DP 테이블 생성 (0으로 초기화된 (m+1)x(n+1) 배열)
        int[,] L = new int[m + 1, n + 1];

        // DP 테이블 채우기
        for (int i = 1; i <= m; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
                if (X[i - 1] == Y[j - 1])
                {
                    L[i, j] = L[i - 1, j - 1] + 1;  // 문자가 같으면 대각선 위 + 1
                }
                else
                {
                    L[i, j] = Math.Max(L[i - 1, j], L[i, j - 1]);  // 문자가 다르면 위 또는 왼쪽 값 중 큰 값
                }
            }
        }

        // LCS의 길이
        int length_of_lcs = L[m, n];

        // LCS 문자열 구성 (역추적)
        int index = L[m, n];
        char[] lcs = new char[index];  // LCS 문자열을 저장할 배열
        int i2 = m, j2 = n;
        while (i2 > 0 && j2 > 0)
        {
            if (X[i2 - 1] == Y[j2 - 1])
            {
                lcs[index - 1] = X[i2 - 1];  // 공통 문자를 LCS 배열에 저장
                i2--;
                j2--;
                index--;
            }
            else if (L[i2 - 1, j2] > L[i2, j2 - 1])
            {
                i2--;  // 위쪽 값이 더 크면 위로 이동
            }
            else
            {
                j2--;  // 왼쪽 값이 더 크면 왼쪽으로 이동
            }
        }

        return Tuple.Create(length_of_lcs, new string(lcs));  // LCS의 길이와 LCS 문자열을 반환
    }
}
