using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // 단어 W의 길이 g와 문자열 S의 길이 s_len 입력
        string[] input = Console.ReadLine().Split();
        int g = int.Parse(input[0]);
        int s_len = int.Parse(input[1]);

        // 단어 W와 문자열 S 입력
        string W = Console.ReadLine();
        string S = Console.ReadLine();

        // 단어 W의 문자 빈도 계산
        Dictionary<char, int> wCount = new Dictionary<char, int>();
        foreach (char c in W)
        {
            if (wCount.ContainsKey(c))
                wCount[c]++;
            else
                wCount[c] = 1;
        }

        // 문자열 S의 첫 g개의 문자 빈도 계산
        Dictionary<char, int> windowCount = new Dictionary<char, int>();
        for (int i = 0; i < g; i++)
        {
            if (windowCount.ContainsKey(S[i]))
                windowCount[S[i]]++;
            else
                windowCount[S[i]] = 1;
        }

        int count = 0; // 조건을 만족하는 경우의 수 저장 변수

        // 첫 번째 윈도우 검사
        if (AreDictionariesEqual(wCount, windowCount))
            count++;

        // 슬라이딩 윈도우 탐색
        for (int i = g; i < s_len; i++)
        {
            char startChar = S[i - g]; // 윈도우에서 빠지는 문자
            char endChar = S[i];      // 윈도우에서 추가되는 문자

            // 새로 추가된 문자의 빈도 증가
            if (windowCount.ContainsKey(endChar))
                windowCount[endChar]++;
            else
                windowCount[endChar] = 1;

            // 제외된 문자의 빈도 감소
            windowCount[startChar]--;
            if (windowCount[startChar] == 0)
                windowCount.Remove(startChar); // 빈도가 0이 되면 딕셔너리에서 제거

            // 현재 윈도우가 조건을 만족하면 count 증가
            if (AreDictionariesEqual(wCount, windowCount))
                count++;
        }

        // 조건을 만족하는 부분 문자열 개수 출력
        Console.WriteLine(count);
    }

    // 두 딕셔너리 비교를 위한 메서드
    static bool AreDictionariesEqual(Dictionary<char, int> d1, Dictionary<char, int> d2)
    {
        if (d1.Count != d2.Count)
            return false;

        foreach (var kvp in d1)
        {
            if (!d2.ContainsKey(kvp.Key) || d2[kvp.Key] != kvp.Value)
                return false;
        }

        return true;
    }
}
