using System;
using System.Collections.Generic;

class Flower
{
    public int Start; // 꽃의 시작 날짜 (MMDD 형식)
    public int End;   // 꽃의 종료 날짜 (MMDD 형식)

    // 생성자: 시작일과 종료일을 받아 Flower 객체 생성
    public Flower(int start, int end)
    {
        Start = start;
        End = end;
    }
}

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine()); // 첫 번째 줄에서 꽃의 개수를 입력받음
        List<Flower> flowers = new List<Flower>(); // 꽃의 정보를 저장할 리스트

        // 꽃의 정보를 입력받아 MMDD 형식으로 리스트에 추가
        for (int i = 0; i < N; ++i)
        {
            string[] input = Console.ReadLine().Split();
            int sm = int.Parse(input[0]);
            int sd = int.Parse(input[1]);
            int em = int.Parse(input[2]);
            int ed = int.Parse(input[3]);

            int start = sm * 100 + sd; // 시작 날짜를 MMDD 형식으로 변환
            int end = em * 100 + ed;   // 종료 날짜를 MMDD 형식으로 변환
            flowers.Add(new Flower(start, end)); // 리스트에 꽃 정보 추가
        }

        // 꽃을 시작 날짜 오름차순, 종료 날짜 내림차순으로 정렬
        flowers.Sort((a, b) =>
        {
            if (a.Start == b.Start) return b.End.CompareTo(a.End);
            return a.Start.CompareTo(b.Start);
        });

        int START = 301; // 3월 1일을 MMDD 형식으로 설정
        int END = 1130;  // 11월 30일을 MMDD 형식으로 설정

        int currentEnd = START; // 현재 커버할 수 있는 마지막 날짜를 START로 초기화
        int maxEnd = 0;         // 선택된 꽃들이 커버할 수 있는 최대 종료 날짜
        int count = 0;          // 선택된 꽃의 수
        int index = 0;          // flowers 리스트의 인덱스를 추적할 변수

        // 모든 꽃을 순회하거나, 커버할 수 있는 날짜가 END를 넘어갈 때까지 반복
        while (index < N && currentEnd <= END)
        {
            bool found = false; // 현재 커버할 수 있는 꽃을 찾았는지 여부

            // 현재 커버할 수 있는 날짜 이하에서 피는 꽃들 중 가장 늦게 지는 꽃을 선택
            while (index < N && flowers[index].Start <= currentEnd)
            {
                if (flowers[index].End > maxEnd)
                {
                    maxEnd = flowers[index].End;
                    found = true; // 유효한 꽃을 찾았음을 표시
                }
                index++; // 다음 꽃으로 이동
            }

            if (!found) // 더 이상 연장할 수 없는 경우, 반복 종료
                break;

            currentEnd = maxEnd; // 현재 커버 가능한 마지막 날짜를 갱신
            count++; // 꽃을 하나 선택했으므로 count 증가
        }

        // 11월 30일을 커버하지 못했으면 0을 출력
        if (currentEnd <= END)
            Console.WriteLine(0);
        else
            Console.WriteLine(count); // 선택한 꽃의 개수 출력
    }
}
