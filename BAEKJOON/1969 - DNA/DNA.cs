using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 최소 Hamming Distance를 계산하는 함수
    static (string, int) FindMinHammingDNA(int N, int M, List<string> dnaList)
    {
        string minDistanceDNA = ""; // 최소 거리 DNA를 저장할 변수
        int totalHammingDistance = 0; // Hamming Distance 총합을 저장할 변수

        // 각 열(column)에 대해 반복
        for (int col = 0; col < M; col++)
        {
            Dictionary<char, int> freq = new Dictionary<char, int>(); // 각 문자(A, T, G, C)의 빈도 저장

            // 현재 열의 모든 DNA 문자열에서 문자 빈도 계산
            for (int row = 0; row < N; row++)
            {
                char nucleotide = dnaList[row][col];
                if (!freq.ContainsKey(nucleotide))
                    freq[nucleotide] = 0;
                freq[nucleotide]++;
            }

            // 가장 빈번한 문자를 선택. 빈도가 같으면 사전순으로 선택
            char mostCommon = 'A';
            int maxFreq = 0;
            foreach (var entry in freq)
            {
                if (entry.Value > maxFreq || (entry.Value == maxFreq && entry.Key < mostCommon))
                {
                    mostCommon = entry.Key;
                    maxFreq = entry.Value;
                }
            }

            // 최소 거리 DNA에 가장 빈번한 문자 추가
            minDistanceDNA += mostCommon;

            // Hamming Distance 계산: 전체 문자 개수 - 가장 빈번한 문자 개수
            totalHammingDistance += N - maxFreq;
        }

        return (minDistanceDNA, totalHammingDistance); // 최소 거리 DNA와 Hamming Distance 총합 반환
    }

    static void Main(string[] args)
    {
        // DNA 개수와 문자열 길이를 입력받음
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);

        // DNA 문자열 리스트 입력받기
        List<string> dnaList = new List<string>();
        for (int i = 0; i < N; i++)
        {
            dnaList.Add(Console.ReadLine());
        }

        // 최소 거리 DNA와 Hamming Distance 계산
        var result = FindMinHammingDNA(N, M, dnaList);

        // 결과 출력
        Console.WriteLine(result.Item1); // 최소 거리 DNA 출력
        Console.WriteLine(result.Item2); // Hamming Distance 총합 출력
    }
}