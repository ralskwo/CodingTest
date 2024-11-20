using System;
using System.Collections.Generic;
using System.Linq;

class Program {
    static List<int> MaxStickerScore(List<List<int[]>> testCases) {
        List<int> results = new List<int>(); // 결과를 저장할 리스트

        foreach (var stickers in testCases) {
            int n = stickers[0].Length; // 열의 개수
            if (n == 1) {
                // 열이 1개인 경우, 두 행의 첫 번째 값 중 큰 값을 결과에 추가
                results.Add(Math.Max(stickers[0][0], stickers[1][0]));
                continue;
            }

            // 두 열 전과 한 열 전의 결과를 저장할 변수 초기화
            int[] dpPrev = new int[2]; // dp[i-2]
            int[] dpCurr = new int[] { stickers[0][0], stickers[1][0] }; // dp[i-1]

            // 두 번째 열부터 마지막 열까지 반복
            for (int i = 1; i < n; i++) {
                int[] newDp = new int[] {
                    Math.Max(dpCurr[1], dpPrev[1]) + stickers[0][i], // 위쪽 행의 현재 열
                    Math.Max(dpCurr[0], dpPrev[0]) + stickers[1][i]  // 아래쪽 행의 현재 열
                };
                dpPrev = dpCurr; // 이전 값을 갱신
                dpCurr = newDp; // 현재 값을 갱신
            }

            // 마지막 열에서의 최대값을 결과에 추가
            results.Add(Math.Max(dpCurr[0], dpCurr[1]));
        }

        return results; // 모든 테스트 케이스의 결과 반환
    }

    static void Main(string[] args) {
        int t = int.Parse(Console.ReadLine()); // 테스트 케이스 개수 입력
        List<List<int[]>> testCases = new List<List<int[]>>(); // 각 테스트 케이스 저장

        for (int i = 0; i < t; i++) {
            int n = int.Parse(Console.ReadLine()); // 열의 개수 입력
            int[] row1 = Console.ReadLine().Split().Select(int.Parse).ToArray(); // 위쪽 행 입력
            int[] row2 = Console.ReadLine().Split().Select(int.Parse).ToArray(); // 아래쪽 행 입력
            testCases.Add(new List<int[]> { row1, row2 }); // 두 행을 묶어서 저장
        }

        List<int> results = MaxStickerScore(testCases); // 최대 점수 계산

        foreach (int result in results) {
            Console.WriteLine(result); // 각 테스트 케이스의 결과 출력
        }
    }
}
