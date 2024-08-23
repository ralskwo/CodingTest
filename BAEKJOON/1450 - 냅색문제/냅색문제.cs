using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 부분 집합의 합을 계산하는 함수
    static List<long> GetSubsets(List<int> weights)
    {
        int n = weights.Count;
        List<long> subsets = new List<long>();

        // 모든 부분 집합을 계산하여 그 합을 저장
        for (int i = 0; i < (1 << n); i++)
        {
            long sum = 0;
            for (int j = 0; j < n; j++)
            {
                if ((i & (1 << j)) != 0)
                {
                    sum += weights[j];
                }
            }
            subsets.Add(sum);
        }

        return subsets;
    }

    // 가능한 조합의 수를 계산하는 함수
    static long CountValidCombinations(int N, long C, List<int> weights)
    {
        // 리스트를 반으로 나누기
        List<int> leftWeights = weights.GetRange(0, N / 2);
        List<int> rightWeights = weights.GetRange(N / 2, N - N / 2);

        // 각각의 부분 집합의 합을 계산
        List<long> leftSubsets = GetSubsets(leftWeights);
        List<long> rightSubsets = GetSubsets(rightWeights);

        // 이진 탐색을 위한 정렬
        rightSubsets.Sort();

        long count = 0;

        // 왼쪽 부분 집합의 합을 순회하면서, C를 넘지 않는 조합을 찾기
        foreach (long leftSum in leftSubsets)
        {
            if (leftSum <= C)
            {
                // C - leftSum 보다 작거나 같은 값을 갖는 오른쪽 부분 집합의 개수를 구함
                int index = rightSubsets.BinarySearch(C - leftSum);
                
                if (index < 0)
                {
                    index = ~index; // BinarySearch가 실패하면 위치를 반환하기 위해 인덱스 변환
                }
                else
                {
                    // 정확히 C - leftSum인 값이 있는 경우, 동일한 값까지 포함시키기 위한 로직
                    while (index < rightSubsets.Count && rightSubsets[index] == C - leftSum)
                    {
                        index++;
                    }
                }

                count += index;
            }
        }

        return count;
    }

    static void Main()
    {
        // 한 줄에서 입력 받도록 수정
        var input = Console.ReadLine().Split(' ');
        int N = int.Parse(input[0]);
        long C = long.Parse(input[1]);

        List<int> weights = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

        // 가능한 조합의 수를 계산하여 출력
        Console.WriteLine(CountValidCombinations(N, C, weights));
    }
}
