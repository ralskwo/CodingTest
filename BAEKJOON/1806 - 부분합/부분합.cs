using System;

class Program
{
    static void Main()
    {
        // 첫 번째 줄에서 N(수열의 길이)과 S(부분합의 최소 값)를 입력받아 각각 N과 S에 저장한다.
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]); // 수열의 길이
        int S = int.Parse(input[1]); // 목표 부분합

        // 두 번째 줄에서 수열의 각 원소를 입력받고, 배열로 변환하여 numbers에 저장한다.
        int[] numbers = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        // 시작 포인터(start)와 끝 포인터(end)를 0으로 초기화한다.
        int start = 0, end = 0;

        // 현재까지 계산한 부분합을 저장할 변수 current_sum을 0으로 초기화한다.
        int current_sum = 0;

        // 최소 길이를 저장할 변수 min_length를 수열의 길이 + 1로 설정한다. (최대보다 큰 값)
        int min_length = N + 1;

        // 슬라이딩 윈도우를 통해 부분합을 탐색한다.
        while (true)
        {
            // 현재 부분합이 S 이상인 경우
            if (current_sum >= S)
            {
                // 최소 길이를 갱신
                min_length = Math.Min(min_length, end - start);

                // 현재 시작점의 값을 부분합에서 제외하고, 슬라이딩 윈도우를 줄인다.
                current_sum -= numbers[start];
                start++;
            }
            // 끝 포인터가 수열의 끝에 도달한 경우 반복 종료
            else if (end == N)
            {
                break;
            }
            // 부분합이 S보다 작으면 끝 포인터 확장
            else
            {
                current_sum += numbers[end];
                end++;
            }
        }

        // 만약 최소 길이가 갱신되지 않았으면 0을 출력
        if (min_length == N + 1)
        {
            Console.WriteLine(0);
        }
        // 조건을 만족하는 최소 길이를 출력
        else
        {
            Console.WriteLine(min_length);
        }
    }
}
