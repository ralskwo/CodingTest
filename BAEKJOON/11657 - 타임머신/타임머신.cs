using System;
using System.Collections.Generic;

class Program {
    const long INF = long.MaxValue; // 무한대를 표현하기 위한 상수

    // 벨만-포드 알고리즘 함수
    static bool BellmanFord(int n, List<Tuple<int, int, int>> edges, long[] distance) {
        distance[1] = 0; // 시작 도시의 거리를 0으로 초기화

        // n-1번 반복하여 최단 거리를 계산
        for (int i = 1; i < n; i++) {
            foreach (var edge in edges) { // 각 간선을 순회
                int u = edge.Item1;
                int v = edge.Item2;
                int cost = edge.Item3;

                if (distance[u] != INF && distance[u] + cost < distance[v]) {
                    distance[v] = distance[u] + cost; // 최단 거리 갱신
                }
            }
        }

        // n번째 반복에서 갱신이 발생하면 음수 사이클 존재
        foreach (var edge in edges) {
            int u = edge.Item1;
            int v = edge.Item2;
            int cost = edge.Item3;

            if (distance[u] != INF && distance[u] + cost < distance[v]) {
                return true; // 음수 사이클 존재
            }
        }

        return false; // 음수 사이클 없음
    }

    static void Main(string[] args) {
        string[] input = Console.ReadLine().Split(); // 첫 번째 줄 입력
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        var edges = new List<Tuple<int, int, int>>(); // 간선 정보를 저장할 리스트
        var distance = new long[n + 1]; // 최단 거리 배열
        for (int i = 1; i <= n; i++) {
            distance[i] = INF; // 최단 거리를 무한대로 초기화
        }

        for (int i = 0; i < m; i++) {
            string[] edgeInput = Console.ReadLine().Split(); // 각 간선 정보 입력
            int a = int.Parse(edgeInput[0]);
            int b = int.Parse(edgeInput[1]);
            int c = int.Parse(edgeInput[2]);
            edges.Add(Tuple.Create(a, b, c)); // 간선 추가
        }

        if (BellmanFord(n, edges, distance)) {
            Console.WriteLine(-1); // 음수 사이클이 존재하면 -1 출력
        } else {
            for (int i = 2; i <= n; i++) {
                if (distance[i] == INF) {
                    Console.WriteLine(-1); // 도달할 수 없는 경우 -1 출력
                } else {
                    Console.WriteLine(distance[i]); // 최단 거리 출력
                }
            }
        }
    }
}
