using System;
using System.Collections.Generic;

class Program {
    static (int minTime, int maxTime) AntTimes(int l, List<int> positions) {
        int minTime = 0; // 최소 시간을 저장할 변수
        int maxTime = 0; // 최대 시간을 저장할 변수
        
        foreach (int position in positions) { // 각 개미의 위치에 대해 반복
            // 최소 시간 계산: 개미가 왼쪽 끝 또는 오른쪽 끝 중 더 가까운 쪽으로 가는 시간
            minTime = Math.Max(minTime, Math.Min(position, l - position));
            
            // 최대 시간 계산: 개미가 왼쪽 끝 또는 오른쪽 끝 중 더 먼 쪽으로 가는 시간
            maxTime = Math.Max(maxTime, Math.Max(position, l - position));
        }
        
        return (minTime, maxTime); // 최소 시간과 최대 시간을 튜플로 반환
    }

    static void Main() {
        int testCases = int.Parse(Console.ReadLine()); // 테스트 케이스 수 입력
        
        while (testCases-- > 0) { // 각 테스트 케이스마다 반복
            string[] inputs = Console.ReadLine().Split();
            int l = int.Parse(inputs[0]); // 막대의 길이 l
            int n = int.Parse(inputs[1]); // 개미의 수 n
            
            List<int> positions = new List<int>(); // 개미의 위치를 저장할 리스트
            for (int i = 0; i < n; ++i) {
                positions.Add(int.Parse(Console.ReadLine())); // 개미의 위치 입력
            }
            
            var result = AntTimes(l, positions); // 최소, 최대 시간 계산
            Console.WriteLine($"{result.minTime} {result.maxTime}"); // 결과 출력
        }
    }
}
