using System;
using System.Collections.Generic;

class Program
{
    // 이분 탐색을 사용해 LIS에서 적절한 위치를 찾는 함수
    static int BinarySearch(List<int> dp, int target) {
        int low = 0, high = dp.Count;
        while (low < high) {
            int mid = (low + high) / 2;
            if (dp[mid] < target)
                low = mid + 1;  // target보다 작은 값은 제외
            else
                high = mid;     // target 이상인 값으로 범위를 좁힘
        }
        return low; // target이 들어갈 위치 반환
    }

    static void Main() {
        int n = int.Parse(Console.ReadLine()); // 전깃줄의 개수 입력
        var connections = new List<(int, int)>();

        for (int i = 0; i < n; i++) {
            var input = Console.ReadLine().Split(); // A, B 전봇대 연결 위치 입력
            int a = int.Parse(input[0]);
            int b = int.Parse(input[1]);
            connections.Add((a, b));
        }

        // A 전봇대 기준으로 정렬
        connections.Sort((x, y) => x.Item1.CompareTo(y.Item1));

        var dp = new List<int>(); // LIS를 저장하기 위한 리스트
        foreach (var conn in connections) {
            int b = conn.Item2; // B 전봇대의 연결 위치
            int idx = BinarySearch(dp, b); // LIS에서 b가 들어갈 위치 찾기
            if (idx == dp.Count)
                dp.Add(b); // LIS 끝에 추가
            else
                dp[idx] = b; // 기존 값을 갱신
        }

        // 제거해야 하는 전깃줄의 최소 개수 출력
        Console.WriteLine(n - dp.Count);
    }
}
