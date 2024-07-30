using System;

class Program
{
    // 이진수로 변환된 숫자에서 1의 개수를 세는 함수
    static int CountSetBits(int x)
    {
        int count = 0;
        while (x > 0)
        {
            if ((x & 1) == 1)
                count++;
            x >>= 1;
        }
        return count;
    }

    // 최소 추가 물병의 수를 계산하는 함수
    static int MinBottlePurchase(int N, int K)
    {
        // 추가로 구매할 물병의 수 초기화
        int purchaseCount = 0;

        // N의 물병 개수에서 1의 개수가 K 이하가 될 때까지 반복
        while (CountSetBits(N) > K)
        {
            // 물병을 하나 추가 구매하여 N을 1 증가
            N += 1;
            // 구매한 물병의 수를 증가
            purchaseCount += 1;
        }

        // 필요한 최소 추가 물병의 수를 반환
        return purchaseCount;
    }

    static void Main(string[] args)
    {
        // 입력 값을 받아 N과 K로 분리
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int K = int.Parse(input[1]);

        // 결과를 계산하여 출력
        int result = MinBottlePurchase(N, K);
        Console.WriteLine(result);
    }
}
