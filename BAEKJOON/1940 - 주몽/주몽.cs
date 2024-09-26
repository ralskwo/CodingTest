using System;
using System.Linq;

class Program
{
    static int CountArmors(int N, int M, int[] materials)
    {
        // 재료 번호 배열 정렬
        Array.Sort(materials);

        // 투 포인터 초기화
        int left = 0;
        int right = N - 1;
        int count = 0;

        // 투 포인터 방식으로 갑옷을 만들 수 있는 경우의 수를 셈
        while (left < right)
        {
            int sum_value = materials[left] + materials[right];

            if (sum_value == M)
            {
                count++;
                left++;
                right--;
            }
            else if (sum_value < M)
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return count;
    }

    static void Main(string[] args)
    {
        // 재료의 개수 입력
        int N = int.Parse(Console.ReadLine());
        // 갑옷을 만들기 위해 필요한 수 입력
        int M = int.Parse(Console.ReadLine());

        // 재료 번호 입력
        int[] materials = Console.ReadLine().Split().Select(int.Parse).ToArray();

        // 갑옷을 만들 수 있는 개수 출력
        Console.WriteLine(CountArmors(N, M, materials));
    }
}
