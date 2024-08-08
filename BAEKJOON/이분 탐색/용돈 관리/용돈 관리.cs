using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 도우미 함수: 주어진 금액 k로 M번 이하로 인출이 가능한지 확인
    static bool CanWithdrawWithK(int k, List<int> dailyUsage, int N, int M)
    {
        int count = 1;  // 인출 횟수
        int currentSum = 0;  // 현재 인출한 금액의 합

        foreach (int usage in dailyUsage)
        {
            if (currentSum + usage > k)  // 현재 인출 금액에 오늘 사용할 금액을 더했을 때 k를 초과하면
            {
                count++;  // 인출 횟수를 증가시킨다
                currentSum = usage;  // 현재 인출 금액을 오늘 사용할 금액으로 초기화
                if (count > M)  // 인출 횟수가 M을 초과하면
                {
                    return false;  // false를 반환하여 주어진 k로 인출이 불가능함을 알린다
                }
            }
            else
            {
                currentSum += usage;  // k를 초과하지 않으면 현재 인출 금액에 오늘 사용할 금액을 더한다
            }
        }

        return true;  // 모든 사용 금액을 k 이내에서 M번 이하로 인출할 수 있으면 true를 반환
    }

    // 이분 탐색 함수: 최소 금액 K를 찾음
    static int FindMinimumK(int N, int M, List<int> dailyUsage)
    {
        int low = dailyUsage.Max();  // 최소 금액 K의 초기값은 매일 사용하는 금액 중 최대값으로 설정
        int high = dailyUsage.Sum();  // 최대 금액 K의 초기값은 모든 날의 사용 금액의 합으로 설정

        while (low < high)  // 이분 탐색을 통해 적절한 K를 찾는다
        {
            int mid = (low + high) / 2;  // 중간값을 계산
            if (CanWithdrawWithK(mid, dailyUsage, N, M))  // 중간값으로 인출이 가능한지 확인
            {
                high = mid;  // 가능하면 상한값을 중간값으로 설정
            }
            else
            {
                low = mid + 1;  // 불가능하면 하한값을 중간값+1로 설정
            }
        }

        return low;  // 최소 금액 K를 반환
    }

    static void Main()
    {
        // 입력 처리
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);  // 첫 번째 줄의 첫 번째 숫자는 N
        int M = int.Parse(input[1]);  // 첫 번째 줄의 두 번째 숫자는 M
        List<int> dailyUsage = new List<int>();

        for (int i = 0; i < N; i++)
        {
            dailyUsage.Add(int.Parse(Console.ReadLine()));  // 나머지 숫자들은 매일 사용할 금액
        }

        // 최소 금액 K 계산
        int minimumK = FindMinimumK(N, M, dailyUsage);

        // 출력
        Console.WriteLine(minimumK);  // 최소 금액 K를 출력
    }
}
