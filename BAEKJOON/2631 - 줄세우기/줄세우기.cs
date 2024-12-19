using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()); // 아이들의 수를 입력받습니다.
        int[] children = new int[n]; // 아이들의 번호를 저장할 배열을 선언합니다.

        for (int i = 0; i < n; i++)
        {
            children[i] = int.Parse(Console.ReadLine()); // 아이들의 번호를 입력받아 배열에 저장합니다.
        }

        List<int> lis = new List<int>(); // 최장 증가 부분 수열(LIS)을 저장할 리스트를 선언합니다.

        foreach (int num in children)
        {
            // 현재 숫자가 LIS에 들어갈 위치를 이진 탐색으로 찾습니다.
            int pos = lis.BinarySearch(num);
            if (pos < 0) pos = ~pos; // BinarySearch는 음수를 반환하면 해당 위치를 계산하기 위해 ~를 사용합니다.

            if (pos == lis.Count)
            {
                // 위치가 LIS의 끝이라면 현재 숫자를 추가합니다.
                lis.Add(num);
            }
            else
            {
                // 그렇지 않으면 해당 위치 값을 현재 숫자로 대체합니다.
                lis[pos] = num;
            }
        }

        // 최소 이동 수는 전체 아이들 수에서 LIS 길이를 뺀 값입니다.
        Console.WriteLine(n - lis.Count);
    }
}
