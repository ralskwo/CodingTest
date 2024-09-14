using System;
using System.Collections.Generic;

class Program
{
    // 톱니바퀴 회전 함수
    static List<int> RotateGear(List<int> gear, int direction)
    {
        // 시계 방향 회전
        if (direction == 1)
        {
            // 마지막 원소를 맨 앞으로 이동
            int last = gear[gear.Count - 1];
            gear.RemoveAt(gear.Count - 1);
            gear.Insert(0, last);
        }
        // 반시계 방향 회전
        else if (direction == -1)
        {
            // 첫 번째 원소를 맨 뒤로 이동
            int first = gear[0];
            gear.RemoveAt(0);
            gear.Add(first);
        }
        return gear;
    }

    // 톱니바퀴 회전 시뮬레이션 함수
    static void SimulateGears(List<List<int>> gears, List<Tuple<int, int>> rotations)
    {
        foreach (var rotation in rotations)
        {
            int gearIndex = rotation.Item1 - 1;
            int direction = rotation.Item2;

            // 각 톱니바퀴의 회전 방향을 기록하는 배열
            int[] rotationDirections = new int[4];
            rotationDirections[gearIndex] = direction;

            // 현재 톱니바퀴의 왼쪽으로 영향 전파
            for (int i = gearIndex; i > 0; i--)
            {
                if (gears[i][6] != gears[i - 1][2])
                {
                    rotationDirections[i - 1] = -rotationDirections[i];
                }
                else
                {
                    break;
                }
            }

            // 현재 톱니바퀴의 오른쪽으로 영향 전파
            for (int i = gearIndex; i < 3; i++)
            {
                if (gears[i][2] != gears[i + 1][6])
                {
                    rotationDirections[i + 1] = -rotationDirections[i];
                }
                else
                {
                    break;
                }
            }

            // 기록된 회전 방향에 따라 톱니바퀴 회전
            for (int i = 0; i < 4; i++)
            {
                if (rotationDirections[i] != 0)
                {
                    gears[i] = RotateGear(gears[i], rotationDirections[i]);
                }
            }
        }
    }

    // 점수 계산 함수
    static int CalculateScore(List<List<int>> gears)
    {
        int score = 0;
        for (int i = 0; i < 4; i++)
        {
            // 12시 방향이 S극인 경우
            if (gears[i][0] == 1)
            {
                score += (1 << i); // 2의 i승 더하기
            }
        }
        return score;
    }

    static void Main()
    {
        List<List<int>> gears = new List<List<int>>();
        List<Tuple<int, int>> rotations = new List<Tuple<int, int>>();

        // 톱니바퀴 초기 상태 입력
        for (int i = 0; i < 4; i++)
        {
            string input = Console.ReadLine();
            List<int> gear = new List<int>();
            foreach (char c in input)
            {
                gear.Add(c - '0'); // 문자열을 숫자로 변환하여 저장
            }
            gears.Add(gear);
        }

        int K = int.Parse(Console.ReadLine()); // 회전 횟수 입력

        // 회전 명령 입력
        for (int i = 0; i < K; i++)
        {
            string[] rotationInfo = Console.ReadLine().Split();
            int gearIndex = int.Parse(rotationInfo[0]);
            int direction = int.Parse(rotationInfo[1]);
            rotations.Add(Tuple.Create(gearIndex, direction));
        }

        // 시뮬레이션 실행
        SimulateGears(gears, rotations);

        // 점수 계산 및 출력
        int score = CalculateScore(gears);
        Console.WriteLine(score);
    }
}
