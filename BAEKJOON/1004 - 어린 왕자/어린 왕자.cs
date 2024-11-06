using System;
using System.Collections.Generic;

class Program
{
    // 특정 점이 행성계 내부에 있는지 판단하는 함수
    static bool IsInsideCircle(int x, int y, int cx, int cy, int r)
    {
        // 두 점 사이의 거리의 제곱이 반지름의 제곱보다 작은지 확인
        return (x - cx) * (x - cx) + (y - cy) * (y - cy) < r * r;
    }

    // 최소 진입/이탈 횟수를 계산하는 함수
    static int MinimumPlanetEntryExitCount(int x1, int y1, int x2, int y2, List<Tuple<int, int, int>> planets)
    {
        int count = 0;  // 진입/이탈 횟수를 저장할 변수
        foreach (var planet in planets)  // 각 행성계에 대해 반복
        {
            int cx = planet.Item1, cy = planet.Item2, r = planet.Item3;

            // 출발점과 도착점이 각각 행성계 내부에 있는지 확인
            bool startInside = IsInsideCircle(x1, y1, cx, cy, r);
            bool endInside = IsInsideCircle(x2, y2, cx, cy, r);

            // 출발점과 도착점 중 하나만 내부에 있는 경우 진입/이탈 발생
            if (startInside != endInside)
            {
                count++;
            }
        }
        return count;  // 최종 진입/이탈 횟수 반환
    }

    static void Main()
    {
        int T = int.Parse(Console.ReadLine());  // 테스트 케이스 개수 입력
        List<int> results = new List<int>();  // 결과를 저장할 리스트

        for (int t = 0; t < T; t++)  // 각 테스트 케이스에 대해 반복
        {
            var line1 = Console.ReadLine().Split();  // 출발점과 도착점 입력
            int x1 = int.Parse(line1[0]), y1 = int.Parse(line1[1]);
            int x2 = int.Parse(line1[2]), y2 = int.Parse(line1[3]);

            int n = int.Parse(Console.ReadLine());  // 행성계 개수 입력
            List<Tuple<int, int, int>> planets = new List<Tuple<int, int, int>>();  // 행성계 정보 리스트

            for (int i = 0; i < n; i++)  // 각 행성계에 대해 반복
            {
                var line2 = Console.ReadLine().Split();
                int cx = int.Parse(line2[0]), cy = int.Parse(line2[1]), r = int.Parse(line2[2]);
                planets.Add(Tuple.Create(cx, cy, r));  // 행성계 정보를 리스트에 추가
            }

            // 최소 진입/이탈 횟수를 계산하여 결과 리스트에 추가
            results.Add(MinimumPlanetEntryExitCount(x1, y1, x2, y2, planets));
        }

        foreach (var result in results)
        {
            Console.WriteLine(result);  // 각 테스트 케이스의 결과 출력
        }
    }
}