using System;
using System.Collections.Generic;

class Program
{
    static int MaxSequenceSum(List<int> nums)
    {
        List<int> positive = new List<int>();  // 양수를 저장하는 리스트
        List<int> negative = new List<int>();  // 음수와 0을 저장하는 리스트
        int result = 0;  // 최종 결과값을 저장하는 변수

        // 주어진 수열을 순회하며 분류
        foreach (int num in nums)
        {
            if (num > 1)
            {
                positive.Add(num);  // 1보다 큰 양수는 positive 리스트에 저장
            }
            else if (num == 1)
            {
                result += 1;  // 1은 바로 더하는 것이 유리
            }
            else
            {
                negative.Add(num);  // 음수와 0은 negative 리스트에 저장
            }
        }

        // 양수는 내림차순으로 정렬 (큰 것부터 묶기 위해)
        positive.Sort((a, b) => b.CompareTo(a));
        // 음수는 오름차순으로 정렬 (작은 것부터 묶기 위해)
        negative.Sort();

        // 양수 묶기
        int i = 0;
        while (i < positive.Count - 1)
        {
            result += positive[i] * positive[i + 1];  // 두 개씩 묶어 곱한 결과를 더함
            i += 2;  // 두 개씩 묶었으므로 인덱스를 2 증가
        }
        // 묶지 못하고 남은 양수 처리
        if (i < positive.Count)
        {
            result += positive[i];  // 남은 양수는 그대로 더함
        }

        // 음수 묶기
        i = 0;
        while (i < negative.Count - 1)
        {
            result += negative[i] * negative[i + 1];  // 두 개씩 묶어 곱한 결과를 더함
            i += 2;  // 두 개씩 묶었으므로 인덱스를 2 증가
        }
        // 묶지 못하고 남은 음수 처리
        if (i < negative.Count)
        {
            // 0이 있는 경우 음수와 묶어 상쇄
            if (nums.Contains(0))
            {
                result += 0;
            }
            else
            {
                result += negative[i];  // 0이 없으면 음수를 그대로 더함
            }
        }

        return result;  // 최종 결과 반환
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());  // 수열의 크기 입력
        List<int> nums = new List<int>();  // 수열을 저장할 리스트
        for (int i = 0; i < n; i++)
        {
            nums.Add(int.Parse(Console.ReadLine()));  // 수열의 각 수 입력
        }
        Console.WriteLine(MaxSequenceSum(nums));  // 결과 출력
    }
}
