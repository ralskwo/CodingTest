using System;

class Program
{
    // 연도를 찾는 함수 정의
    static int FindYear(int E, int S, int M)
    {
        int year = 1;  // year 변수를 1로 초기화 (1년부터 시작)
        
        // 조건을 만족하는 연도를 찾을 때까지 무한 반복
        while (true)
        {
            // year에서 E, S, M을 뺀 값이 각각 15, 28, 19로 나누어 떨어지면 그 year가 답
            if ((year - E) % 15 == 0 && (year - S) % 28 == 0 && (year - M) % 19 == 0)
            {
                return year;  // 조건을 만족하면 해당 year 반환
            }
            year++;  // 조건을 만족하지 않으면 year를 1 증가시키고 계속 탐색
        }
    }

    static void Main()
    {
        // 입력 받기: E, S, M 값을 사용자로부터 입력받음
        string[] input = Console.ReadLine().Split();
        int E = int.Parse(input[0]);
        int S = int.Parse(input[1]);
        int M = int.Parse(input[2]);

        // 조건을 만족하는 연도를 찾아 출력
        Console.WriteLine(FindYear(E, S, M));
    }
}
