using System;
using System.Collections.Generic;

class Program {
    static void Main(string[] args) {
        // 강의 개수 입력
        int N = int.Parse(Console.ReadLine());

        // 강의 정보를 저장할 리스트 선언
        List<(int start, int end)> lectures = new List<(int start, int end)>();

        // 강의 정보를 입력받아 리스트에 저장
        for (int i = 0; i < N; i++) {
            string[] input = Console.ReadLine().Split();
            int num = int.Parse(input[0]); // 강의 번호 (사용하지 않음)
            int start = int.Parse(input[1]); // 강의 시작 시간
            int end = int.Parse(input[2]); // 강의 종료 시간
            lectures.Add((start, end)); // (시작 시간, 종료 시간) 저장
        }

        // 강의 시작 시간을 기준으로 정렬
        lectures.Sort((a, b) => a.start == b.start ? a.end.CompareTo(b.end) : a.start.CompareTo(b.start));

        // 최소 강의실을 관리할 우선순위 큐 생성 (종료 시간 관리)
        PriorityQueue<int, int> minHeap = new PriorityQueue<int, int>();

        // 강의 정보를 순회하며 강의실 배정
        foreach (var lecture in lectures) {
            int start = lecture.start;
            int end = lecture.end;

            // 현재 강의 시작 시간이 가장 빨리 끝나는 강의실의 종료 시간 이후라면
            if (minHeap.Count > 0 && minHeap.Peek() <= start) {
                minHeap.Dequeue(); // 해당 강의실 재사용 가능하므로 종료 시간 제거
            }

            // 현재 강의의 종료 시간을 우선순위 큐에 추가
            minHeap.Enqueue(end, end);
        }

        // 최종적으로 우선순위 큐에 남아 있는 요소의 개수가 필요한 최소 강의실 개수
        Console.WriteLine(minHeap.Count);
    }
}
