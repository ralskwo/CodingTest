using System;
using System.Collections.Generic;

class Program
{
    static int MaxPeopleInSegment(int n, List<Tuple<int, int>> positions, int d)
    {
        // 각 사람의 집과 사무실 위치에서 시작점과 끝점을 계산
        List<Tuple<int, int>> segments = new List<Tuple<int, int>>();
        foreach (var pos in positions)
        {
            int start = Math.Min(pos.Item1, pos.Item2);
            int end = Math.Max(pos.Item1, pos.Item2);
            segments.Add(Tuple.Create(start, end));
        }

        // 끝점을 기준으로 정렬
        segments.Sort((a, b) => a.Item2.CompareTo(b.Item2));

        int maxCount = 0;  // 최대 사람 수를 저장할 변수 초기화
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();  // 우선순위 큐 초기화

        foreach (var seg in segments)
        {
            int start = seg.Item1;
            int end = seg.Item2;

            // 현재 사람의 시작점을 우선순위 큐에 삽입
            pq.Enqueue(start, start);

            // 우선순위 큐의 첫 번째 요소가 현재 끝점에서 d를 뺀 값보다 작으면 큐에서 제거
            while (pq.Count > 0 && pq.Peek() < end - d)
            {
                pq.Dequeue();
            }

            // 현재 우선순위 큐의 크기를 최대 사람 수와 비교하여 갱신
            maxCount = Math.Max(maxCount, pq.Count);
        }

        return maxCount;  // 최대 사람 수 반환
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());  // 첫 번째 줄에서 사람 수를 입력 받음

        List<Tuple<int, int>> positions = new List<Tuple<int, int>>();
        for (int i = 0; i < n; i++)
        {
            string[] input = Console.ReadLine().Split();
            int h = int.Parse(input[0]);
            int o = int.Parse(input[1]);
            positions.Add(Tuple.Create(h, o));  // 각 사람의 집과 사무실 위치를 입력 받음
        }

        int d = int.Parse(Console.ReadLine());  // 마지막 줄에서 선분의 길이를 입력 받음

        // 최대 사람 수를 계산하여 출력
        Console.WriteLine(MaxPeopleInSegment(n, positions, d));
    }
}
