using System;
using System.Collections.Generic;

class Program {
    // 최소 수신 가능 거리의 합을 계산하는 함수
    static int MinTotalDistance(int N, int K, List<int> sensors) {
        // 집중국의 수가 센서의 수 이상인 경우, 모든 센서를 개별적으로 커버 가능
        if (K >= N) return 0;

        // 센서 좌표를 오름차순으로 정렬
        sensors.Sort();

        // 인접 센서 간의 거리를 저장할 리스트
        List<int> distances = new List<int>();
        for (int i = 1; i < N; i++) {
            // 센서 간 거리 계산
            distances.Add(sensors[i] - sensors[i - 1]);
        }

        // 거리 리스트를 내림차순으로 정렬
        distances.Sort((a, b) => b.CompareTo(a));

        // 가장 큰 K-1 개의 간격을 제거
        for (int i = 0; i < K - 1; i++) {
            distances[i] = 0; // 큰 간격 제거
        }

        // 남은 거리의 합을 계산
        int result = 0;
        foreach (int distance in distances) {
            result += distance;
        }
        return result;
    }

    static void Main(string[] args) {
        // 입력 처리
        int N = int.Parse(Console.ReadLine());
        int K = int.Parse(Console.ReadLine());

        string[] input = Console.ReadLine().Split();
        List<int> sensors = new List<int>();
        foreach (string s in input) {
            sensors.Add(int.Parse(s));
        }

        // 최소 거리 합 계산 및 출력
        Console.WriteLine(MinTotalDistance(N, K, sensors));
    }
}