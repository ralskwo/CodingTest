using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 유효한 문제 조합을 세는 함수
    static int CountValidCombinations(int N, int L, int R, int X, int[] A)
    {
        int count = 0;  // 조건을 만족하는 조합의 개수를 저장하는 변수 초기화

        // 부분 집합을 구하기 위한 비트 마스크 방식
        for (int i = 1; i < (1 << N); i++)
        {
            List<int> subset = new List<int>();  // 부분 집합을 저장할 리스트

            // 비트 마스크를 사용해 부분 집합 생성
            for (int j = 0; j < N; j++)
            {
                if ((i & (1 << j)) != 0)
                {
                    subset.Add(A[j]);  // j번째 요소를 부분 집합에 추가
                }
            }

            // 부분 집합이 두 개 이상의 문제를 포함해야 함
            if (subset.Count < 2) continue;

            // 부분 집합의 난이도 총합 계산
            int total = subset.Sum();

            // 가장 어려운 문제와 쉬운 문제의 난이도 차이 계산
            int maxDiff = subset.Max() - subset.Min();

            // 난이도 총합과 난이도 차이 조건 확인
            if (L <= total && total <= R && maxDiff >= X)
            {
                count++;  // 조건을 만족하면 카운트 증가
            }
        }
        return count;  // 조건을 만족하는 조합의 개수 반환
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int L = int.Parse(input[1]);
        int R = int.Parse(input[2]);
        int X = int.Parse(input[3]);

        int[] A = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        // 유효한 문제 조합의 개수 계산 및 출력
        Console.WriteLine(CountValidCombinations(N, L, R, X, A));
    }
}
