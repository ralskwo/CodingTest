using System;
using System.Collections.Generic;

class Program
{
    // 최대 이익을 계산하는 함수
    static long MaxProfit(int n, int[] wages)
    {
        int[] left = new int[n];  // 각 날에 대해 왼쪽으로 확장 가능한 최대 범위를 저장할 배열
        int[] right = new int[n]; // 각 날에 대해 오른쪽으로 확장 가능한 최대 범위를 저장할 배열
        Stack<int> stack = new Stack<int>(); // 스택을 이용하여 확장 가능한 범위를 계산하기 위한 스택

        // 왼쪽으로 확장 가능한 최대 범위를 계산
        for (int i = 0; i < n; i++)
        {
            while (stack.Count > 0 && wages[stack.Peek()] >= wages[i]) // 현재 일급이 스택의 마지막 일급보다 작거나 같으면
            {
                stack.Pop(); // 스택에서 제거하여 왼쪽 확장 불가능한 범위로 설정
            }
            left[i] = stack.Count > 0 ? stack.Peek() + 1 : 0; // 왼쪽 확장 가능한 최대 범위 설정
            stack.Push(i); // 현재 위치를 스택에 추가
        }

        stack.Clear(); // 스택 초기화

        // 오른쪽으로 확장 가능한 최대 범위를 계산
        for (int i = n - 1; i >= 0; i--)
        {
            while (stack.Count > 0 && wages[stack.Peek()] >= wages[i]) // 현재 일급이 스택의 마지막 일급보다 작거나 같으면
            {
                stack.Pop(); // 스택에서 제거하여 오른쪽 확장 불가능한 범위로 설정
            }
            right[i] = stack.Count > 0 ? stack.Peek() - 1 : n - 1; // 오른쪽 확장 가능한 최대 범위 설정
            stack.Push(i); // 현재 위치를 스택에 추가
        }

        long maxProfit = 0; // 최대 이익을 저장할 변수 초기화

        // 각 날에 대해 최대 이익을 계산
        for (int i = 0; i < n; i++)
        {
            long currentProfit = (long)wages[i] * (right[i] - left[i] + 1); // 현재 날의 일급과 최대 일수로 이익 계산
            maxProfit = Math.Max(maxProfit, currentProfit); // 최대 이익을 갱신
        }

        return maxProfit; // 최종 최대 이익 반환
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine()); // 일을 할 수 있는 날의 수 입력
        int[] wages = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse); // 각 날의 일급을 배열로 입력

        Console.WriteLine(MaxProfit(n, wages)); // 최대 이익 계산 및 출력
    }
}
