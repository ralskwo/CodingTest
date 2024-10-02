using System;         // 기본 입출력 처리를 위해 필요
using System.Collections.Generic;  // 리스트 및 힙 자료구조 사용을 위해 필요
using System.Linq;    // 정렬 함수 사용을 위해 필요

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());  // 문제의 개수를 입력받아 정수로 변환

        List<(int, int)> problems = new List<(int, int)>();  // 문제의 (데드라인, 컵라면 수) 저장할 리스트

        // 각 문제의 데드라인과 컵라면 수 입력 받기
        for (int i = 0; i < n; i++)
        {
            var inputs = Console.ReadLine().Split();  // 입력값을 공백으로 분리
            int deadline = int.Parse(inputs[0]);  // 데드라인 입력
            int ramen = int.Parse(inputs[1]);     // 컵라면 수 입력
            problems.Add((deadline, ramen));      // 리스트에 추가
        }

        // 데드라인을 기준으로 정렬
        problems.Sort((a, b) => a.Item1.CompareTo(b.Item1));

        // 우선순위 큐(최소 힙) 생성
        SortedSet<(int ramen, int index)> ramenHeap = new SortedSet<(int, int)>();
        int currentIndex = 0;

        // 문제를 하나씩 처리
        foreach (var problem in problems)
        {
            int deadline = problem.Item1;  // 데드라인 가져오기
            int ramen = problem.Item2;     // 컵라면 수 가져오기

            // 현재 문제를 힙에 추가
            ramenHeap.Add((ramen, currentIndex));
            currentIndex++;

            // 힙의 크기가 데드라인을 초과하면 가장 작은 컵라면 수 제거
            if (ramenHeap.Count > deadline)
            {
                ramenHeap.Remove(ramenHeap.First());  // 최소값(가장 적은 컵라면 수) 제거
            }
        }

        // 힙에 남아 있는 모든 컵라면 수 더하기
        int totalRamen = ramenHeap.Sum(item => item.ramen);

        // 최종 컵라면 수 출력
        Console.WriteLine(totalRamen);
    }
}
