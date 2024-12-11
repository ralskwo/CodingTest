using System;

class Program {
    static int LongestCommonSubsequence(string str1, string str2, string str3) {
        // 각 문자열의 길이를 저장
        int len1 = str1.Length;
        int len2 = str2.Length;
        int len3 = str3.Length;

        // 3차원 DP 테이블 초기화
        int[,,] dp = new int[len1 + 1, len2 + 1, len3 + 1];

        // DP 테이블 채우기
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                for (int k = 1; k <= len3; k++) {
                    // 현재 문자가 모두 같으면 이전 상태에서 1을 더함
                    if (str1[i - 1] == str2[j - 1] && str2[j - 1] == str3[k - 1]) {
                        dp[i, j, k] = dp[i - 1, j - 1, k - 1] + 1;
                    }
                    // 그렇지 않으면 세 가지 경우 중 최대값을 선택
                    else {
                        dp[i, j, k] = Math.Max(dp[i - 1, j, k], 
                                    Math.Max(dp[i, j - 1, k], dp[i, j, k - 1]));
                    }
                }
            }
        }

        // 결과 반환: 세 문자열의 LCS 길이
        return dp[len1, len2, len3];
    }

    static void Main() {
        // 문자열 입력
        string str1 = Console.ReadLine();
        string str2 = Console.ReadLine();
        string str3 = Console.ReadLine();

        // LCS 계산 및 출력
        Console.WriteLine(LongestCommonSubsequence(str1, str2, str3));
    }
}
