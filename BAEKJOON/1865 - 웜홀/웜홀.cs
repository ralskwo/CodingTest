using System;
using System.Collections.Generic;

class Program {
    const int INF = int.MaxValue;  // 무한대를 의미하는 상수 정의

    // 벨만-포드 알고리즘 함수: 음수 사이클이 존재하면 true, 없으면 false 반환
    static bool BellmanFord(int n, List<Tuple<int, int, int>> edges, int start) {
        int[] dist = new int[n + 1];
        for (int i = 1; i <= n; i++) dist[i] = INF;  // 각 지점까지의 최단 거리를 무한대로 초기화
        dist[start] = 0;  // 시작 지점의 거리를 0으로 설정

        for (int i = 0; i < n; i++) {  // 지점의 수만큼 반복
            bool updated = false;  // 이번 반복에서 갱신이 발생했는지 확인
            foreach (var edge in edges) {  // 모든 간선에 대해 반복
                int u = edge.Item1, v = edge.Item2, w = edge.Item3;
                if (dist[u] != INF && dist[u] + w < dist[v]) {  // u에서 v로의 경로가 최단 경로인지 확인
                    dist[v] = dist[u] + w;  // 최단 경로로 갱신
                    updated = true;  // 갱신이 발생했음을 표시
                    if (i == n - 1) return true;  // n번째 반복에서도 갱신이 있으면 음수 사이클 존재
                }
            }
            if (!updated) break;  // 더 이상 갱신이 없으면 반복 종료
        }
        return false;  // 음수 사이클이 없으면 false 반환
    }

    static void Main() {
        int TC = int.Parse(Console.ReadLine());  // 테스트 케이스 개수 입력
        while (TC-- > 0) {
            string[] parts = Console.ReadLine().Split();
            int n = int.Parse(parts[0]);  // 지점의 수
            int m = int.Parse(parts[1]);  // 도로의 개수
            int w = int.Parse(parts[2]);  // 웜홀의 개수

            var edges = new List<Tuple<int, int, int>>();  // 간선 정보를 저장할 리스트

            for (int i = 0; i < m; i++) {  // 도로 정보 입력
                parts = Console.ReadLine().Split();
                int s = int.Parse(parts[0]);
                int e = int.Parse(parts[1]);
                int t = int.Parse(parts[2]);
                edges.Add(Tuple.Create(s, e, t));  // 양방향 도로로 양쪽 추가
                edges.Add(Tuple.Create(e, s, t));
            }

            for (int i = 0; i < w; i++) {  // 웜홀 정보 입력
                parts = Console.ReadLine().Split();
                int s = int.Parse(parts[0]);
                int e = int.Parse(parts[1]);
                int t = int.Parse(parts[2]);
                edges.Add(Tuple.Create(s, e, -t));  // 음수 가중치로 단방향 웜홀 추가
            }

            bool hasNegativeCycle = false;
            for (int start = 1; start <= n; start++) {  // 모든 지점을 시작점으로 설정
                if (BellmanFord(n, edges, start)) {  // 음수 사이클이 있는지 확인
                    hasNegativeCycle = true;
                    break;  // 음수 사이클 발견 시 조기 종료
                }
            }

            Console.WriteLine(hasNegativeCycle ? "YES" : "NO");  // 결과 출력
        }
    }
}