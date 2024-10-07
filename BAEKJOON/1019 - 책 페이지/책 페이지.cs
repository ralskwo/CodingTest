using System;
using System.Collections.Generic;

class Program
{
    // 0부터 9까지의 숫자가 1부터 n까지 몇 번 등장하는지 세는 함수
    static List<int> CountDigits(long n)
    {
        // n이 0 이하일 경우, 모든 숫자 등장 횟수를 0으로 초기화한 리스트 반환
        if (n <= 0) return new List<int>(new int[10]);

        // n을 문자열로 변환하여 자리수 확인
        string strN = n.ToString();
        int length = strN.Length;

        // 각 숫자(0~9)의 등장 횟수를 저장할 리스트 초기화
        List<int> counts = new List<int>(new int[10]);

        // n의 각 자리수에 대해 등장 빈도를 계산
        for (int i = 0; i < length; i++)
        {
            // 현재 자리의 숫자를 정수형으로 변환하여 저장
            int curr = strN[i] - '0';  // 문자에서 숫자로 변환

            // 현재 자리의 자릿값을 계산 (예: 천의 자리면 1000)
            long placeValue = (long)Math.Pow(10, length - i - 1);

            // 현재 자리보다 앞의 모든 완전한 세트에서의 숫자 빈도 계산
            for (int digit = 0; digit < 10; digit++)
            {
                counts[digit] += (int)(n / (placeValue * 10)) * (int)placeValue;
            }

            // 현재 자리의 숫자보다 작은 숫자들의 등장 횟수 추가
            for (int digit = 0; digit < curr; digit++)
            {
                counts[digit] += (int)placeValue;
            }

            // 현재 자리의 숫자가 등장하는 횟수를 더해줌
            counts[curr] += (int)(n % placeValue) + 1;

            // 0은 맨 앞자리에 올 수 없으므로, 보정 작업을 수행
            counts[0] -= (int)placeValue;
        }

        // 최종적으로 0부터 9까지의 숫자 빈도 리스트 반환
        return counts;
    }

    static void Main(string[] args)
    {
        // 사용자로부터 숫자 입력 받기
        long N = long.Parse(Console.ReadLine());

        // 0부터 9까지의 숫자 등장 횟수 계산
        List<int> result = CountDigits(N);

        // 결과를 공백으로 구분하여 출력
        Console.WriteLine(string.Join(" ", result));
    }
}
