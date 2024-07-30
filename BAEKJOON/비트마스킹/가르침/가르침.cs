using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 특정 문자를 배울 때 읽을 수 있는 단어의 수를 계산하는 함수
    static int CountReadableWords(List<int> words, int learnedMask)
    {
        int count = 0;
        foreach (var word in words)
        {
            if ((word & learnedMask) == word) // 단어의 모든 문자가 배운 문자 집합에 포함되는지 확인
            {
                count++;
            }
        }
        return count; // 총 읽을 수 있는 단어 수를 반환
    }

    // 주어진 단어 수 N과 가르칠 수 있는 문자 수 K를 고려하여 읽을 수 있는 최대 단어 수를 계산하는 함수
    static int Solve(int N, int K, List<string> wordsInput)
    {
        if (K < 5) // K가 5 미만이면 기본 "antic" 문자를 배울 수 없음
        {
            return 0; // 읽을 수 있는 단어 수는 0
        }
        else if (K == 26) // K가 26이면 모든 알파벳을 배울 수 있음
        {
            return N; // 모든 단어를 읽을 수 있음
        }

        int basicMask = 0; // 기본적으로 알아야 하는 문자 집합
        foreach (char c in "antic")
        {
            basicMask |= (1 << (c - 'a'));
        }

        List<int> words = new List<int>(); // 단어 리스트
        foreach (var word in wordsInput)
        {
            int wordMask = 0;
            foreach (char c in word)
            {
                wordMask |= (1 << (c - 'a'));
            }
            words.Add(wordMask);
        }

        List<int> candidateMasks = new List<int>();
        for (int i = 0; i < (1 << 26); i++)
        {
            if ((i & basicMask) == basicMask && CountBits(i) == K)
            {
                candidateMasks.Add(i);
            }
        }

        int maxReadable = 0; // 최대 읽을 수 있는 단어 수를 저장하는 변수
        foreach (var mask in candidateMasks)
        {
            maxReadable = Math.Max(maxReadable, CountReadableWords(words, mask));
        }

        return maxReadable; // 최대 읽을 수 있는 단어 수를 반환
    }

    // 주어진 정수의 비트 수를 세는 함수
    static int CountBits(int n)
    {
        int count = 0;
        while (n > 0)
        {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int K = int.Parse(input[1]);
        List<string> words = new List<string>();
        for (int i = 0; i < N; i++)
        {
            words.Add(Console.ReadLine().Trim());
        }

        // 결과 출력
        Console.WriteLine(Solve(N, K, words)); // 계산된 최대 읽을 수 있는 단어 수를 출력
    }
}
