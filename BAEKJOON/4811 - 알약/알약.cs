using System;
using System.Collections.Generic;

class Program {
    // 동적 프로그래밍을 위한 메모이제이션 딕셔너리
    static Dictionary<(int, int), long> dp = new Dictionary<(int, int), long>();

    // 재귀 함수: 전체 조각(whole)과 반 조각(half)의 상태에서 가능한 경우의 수를 계산
    static long CountWays(int whole, int half) {
        // 전체 조각과 반 조각이 모두 0인 경우, 가능한 문자열 한 가지가 완성되었음을 의미하므로 1 반환
        if (whole == 0 && half == 0)
            return 1;

        // 이미 계산된 상태가 dp에 있으면 저장된 값을 반환하여 중복 계산 방지
        if (dp.ContainsKey((whole, half)))
            return dp[(whole, half)];

        long ways = 0; // 가능한 경우의 수를 저장할 변수

        // 전체 조각이 하나라도 있으면 하나를 꺼내서 반 조각을 추가하는 경우를 고려
        if (whole > 0)
            ways += CountWays(whole - 1, half + 1);

        // 반 조각이 하나라도 있으면 반 조각을 복용하는 경우를 고려
        if (half > 0)
            ways += CountWays(whole, half - 1);

        // 현재 상태의 경우의 수를 dp에 저장하여 다음에 동일 상태가 발생하면 빠르게 반환할 수 있게 함
        dp[(whole, half)] = ways;
        return ways;
    }

    static void Main() {
        while (true) {
            int N = int.Parse(Console.ReadLine()); // 약의 개수 N을 입력받음
            if (N == 0) break; // 입력이 0이면 종료 조건으로 판단하여 반복문 탈출
            Console.WriteLine(CountWays(N, 0)); // 가능한 문자열의 개수를 출력
        }
    }
}