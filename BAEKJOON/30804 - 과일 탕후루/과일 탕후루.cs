using System;
using System.Collections.Generic;

class Program
{
    static int MaxFruitLength(int N, int[] fruits)
    {
        Dictionary<int, int> fruitCount = new Dictionary<int, int>(); // 과일 종류와 개수를 저장할 딕셔너리
        int left = 0; // 슬라이딩 윈도우의 시작 포인터
        int maxLength = 0; // 최대 길이를 저장할 변수

        for (int right = 0; right < N; right++) // 배열을 끝까지 탐색
        {
            if (!fruitCount.ContainsKey(fruits[right]))
                fruitCount[fruits[right]] = 0; // 새로운 과일 종류를 추가
            fruitCount[fruits[right]]++; // 현재 과일 개수를 증가

            while (fruitCount.Count > 2) // 윈도우 내 과일 종류가 2개를 초과하면
            {
                fruitCount[fruits[left]]--; // 왼쪽 포인터의 과일 개수를 감소
                if (fruitCount[fruits[left]] == 0) // 개수가 0이면 딕셔너리에서 삭제
                    fruitCount.Remove(fruits[left]);
                left++; // 왼쪽 포인터를 이동하여 윈도우 크기를 조정
            }

            maxLength = Math.Max(maxLength, right - left + 1); // 최대 길이를 갱신
        }

        return maxLength; // 가장 긴 길이를 반환
    }

    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()); // 과일 개수 입력
        int[] fruits = Array.ConvertAll(Console.ReadLine().Split(), int.Parse); // 과일 배열 입력

        Console.WriteLine(MaxFruitLength(N, fruits)); // 최대 과일 길이 출력
    }
}