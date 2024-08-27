using System;

class Program
{
    // 에라토스테네스의 체를 사용하여 1000 이하의 소수를 구하는 함수
    static bool[] SieveOfEratosthenes(int maxNum)
    {
        bool[] sieve = new bool[maxNum + 1]; // maxNum + 1 크기의 배열을 생성
        for (int i = 2; i <= maxNum; i++)
            sieve[i] = true; // 모든 값을 true로 초기화 (0과 1은 false로 남음)

        // 2부터 시작하여 maxNum의 제곱근까지 반복
        for (int i = 2; i * i <= maxNum; i++)
        {
            if (sieve[i]) // i가 소수인 경우
            {
                // i의 배수들을 false로 설정 (즉, 소수가 아님)
                for (int j = i * i; j <= maxNum; j += i)
                    sieve[j] = false;
            }
        }
        return sieve; // 소수 여부를 나타내는 배열 반환
    }

    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()); // N개의 수를 입력받음
        string[] inputs = Console.ReadLine().Split(); // N개의 수를 문자열 배열로 입력받음
        int[] numbers = Array.ConvertAll(inputs, int.Parse); // 문자열 배열을 정수 배열로 변환

        int maxNum = 1000; // 문제에서 주어진 수의 최대값 1000
        bool[] sieve = SieveOfEratosthenes(maxNum); // 1000 이하의 소수 구하기

        int primeCount = 0; // 소수의 개수를 세기 위한 변수
        for (int i = 0; i < N; i++)
        {
            if (sieve[numbers[i]]) // 주어진 수가 소수라면
                primeCount++; // 소수의 개수를 증가시킴
        }

        Console.WriteLine(primeCount); // 소수의 개수를 출력
    }
}
