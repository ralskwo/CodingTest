using System;
using System.Collections.Generic;

class Program
{
    static string MakeLargestNumber(int N, int K, string number)
    {
        // 결과를 저장할 스택을 초기화합니다.
        Stack<char> stack = new Stack<char>();

        // 입력된 숫자의 각 자릿수를 순서대로 처리합니다.
        foreach (char num in number)
        {
            // 스택이 비어있지 않고, 아직 제거할 수 있는 수가 남아 있으며,
            // 스택의 마지막 수가 현재 수보다 작으면 제거합니다.
            while (K > 0 && stack.Count > 0 && stack.Peek() < num)
            {
                stack.Pop(); // 더 큰 수를 만들기 위해 작은 수를 제거합니다.
                K--; // 제거한 수의 개수를 1 줄입니다.
            }
            // 현재 수를 스택에 추가합니다.
            stack.Push(num);
        }

        // 만약 K가 남아있다면, 뒤에서부터 K개의 수를 제거합니다.
        while (K > 0)
        {
            stack.Pop();
            K--;
        }

        // 스택의 내용을 배열로 변환한 뒤, 배열을 뒤집어 결과를 생성합니다.
        char[] resultArray = stack.ToArray();
        Array.Reverse(resultArray);
        // 배열을 문자열로 변환하여 반환합니다.
        return new string(resultArray);
    }

    static void Main()
    {
        // 첫째 줄에서 N과 K를 입력받습니다.
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int K = int.Parse(input[1]);

        // 둘째 줄에서 N자리 숫자를 입력받습니다.
        string number = Console.ReadLine().Trim();

        // K개의 수를 제거했을 때 얻을 수 있는 가장 큰 수를 출력합니다.
        Console.WriteLine(MakeLargestNumber(N, K, number));
    }
}