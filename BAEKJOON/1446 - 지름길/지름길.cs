using System;
using System.Collections.Generic;

class Shortcut
{
    public int Start { get; set; }
    public int End { get; set; }
    public int Length { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        int N, D;  // N은 지름길의 개수, D는 고속도로의 길이
        string[] input = Console.ReadLine().Split();  // 첫 번째 줄 입력받기
        N = int.Parse(input[0]);  // N값 입력
        D = int.Parse(input[1]);  // D값 입력

        List<Shortcut> shortcuts = new List<Shortcut>();  // 지름길 리스트 생성

        for (int i = 0; i < N; i++)
        {
            input = Console.ReadLine().Split();  // 지름길 정보 입력
            int start = int.Parse(input[0]);
            int end = int.Parse(input[1]);
            int length = int.Parse(input[2]);
            shortcuts.Add(new Shortcut { Start = start, End = end, Length = length });  // 각 지름길 정보를 리스트에 추가
        }

        int[] dist = new int[D + 1];  // 각 지점까지의 최소 거리를 저장할 배열
        for (int i = 0; i <= D; i++)
            dist[i] = i;  // 처음에는 직선으로 이동한 거리를 초기화

        for (int i = 0; i <= D; i++)
        {
            if (i > 0)
            {
                dist[i] = Math.Min(dist[i], dist[i - 1] + 1);  // 직선 이동 경로 처리
            }

            foreach (var shortcut in shortcuts)
            {
                if (shortcut.Start == i && shortcut.End <= D)
                {
                    dist[shortcut.End] = Math.Min(dist[shortcut.End], dist[i] + shortcut.Length);  // 지름길을 이용한 경로 갱신
                }
            }
        }

        Console.WriteLine(dist[D]);  // 최종 결과 출력
    }
}
