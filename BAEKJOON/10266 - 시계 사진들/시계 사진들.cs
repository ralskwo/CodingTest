using System;
using System.Collections.Generic;

class Program
{
    static List<int> CalculateGaps(List<int> angles)
    {
        angles.Sort();  // 각도를 정렬하여 순서 정리
        List<int> gaps = new List<int>();
        int n = angles.Count;
        
        for (int i = 1; i < n; i++)
        {
            gaps.Add(angles[i] - angles[i - 1]);  // 연속된 각도 간의 차이를 계산
        }
        gaps.Add(360000 - angles[n - 1] + angles[0]);  // 마지막과 첫 번째 각도 간의 차이 추가
        return gaps;
    }

    static bool KMPSearch(List<int> text, List<int> pattern)
    {
        int n = text.Count, m = pattern.Count;
        int[] lps = new int[m];
        int j = 0;

        for (int i = 1; i < m; i++)  // LPS 배열 생성
        {
            while (j > 0 && pattern[i] != pattern[j])
            {
                j = lps[j - 1];  // 일치 실패 시 이전 위치로 이동
            }
            if (pattern[i] == pattern[j])
            {
                lps[i] = ++j;  // 일치할 경우 LPS 배열을 업데이트
            }
        }

        j = 0;
        for (int i = 0; i < n; i++)
        {
            while (j > 0 && text[i] != pattern[j])
            {
                j = lps[j - 1];  // 불일치 시 LPS 배열을 참고해 위치 조정
            }
            if (text[i] == pattern[j])
            {
                j++;
                if (j == m) return true;  // 패턴을 찾으면 true 반환
            }
        }
        return false;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());  // 시계 바늘의 개수 입력
        List<int> angles1 = new List<int>(), angles2 = new List<int>();

        string[] input1 = Console.ReadLine().Split();
        foreach (var angle in input1) angles1.Add(int.Parse(angle));  // 첫 번째 시계 각도 입력

        string[] input2 = Console.ReadLine().Split();
        foreach (var angle in input2) angles2.Add(int.Parse(angle));  // 두 번째 시계 각도 입력

        List<int> gaps1 = CalculateGaps(angles1);  // 첫 번째 시계 간격 계산
        List<int> gaps2 = CalculateGaps(angles2);  // 두 번째 시계 간격 계산

        List<int> doubledGaps1 = new List<int>(gaps1);
        doubledGaps1.AddRange(gaps1);  // 두 배로 확장하여 회전 상태 검토 가능

        if (KMPSearch(doubledGaps1, gaps2))
        {
            Console.WriteLine("possible");  // 회전이 가능할 경우 출력
        }
        else
        {
            Console.WriteLine("impossible");  // 불가능할 경우 출력
        }
    }
}