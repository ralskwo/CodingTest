using System;
using System.Collections.Generic;

class DisjointSet {
    private int[] parent; // 각 원소의 부모를 저장하는 배열
    private int[] rank;   // 트리의 깊이를 저장하는 배열

    // 생성자: n개의 원소에 대해 초기화
    public DisjointSet(int n) {
        parent = new int[n]; // parent 배열 크기 초기화
        rank = new int[n];   // rank 배열 크기 초기화
        for (int i = 0; i < n; ++i) {
            parent[i] = i;   // 초기에는 각 원소가 자신의 부모가 됨
            rank[i] = 1;     // 초기 트리의 깊이는 1로 설정
        }
    }

    // 부모 찾기 (경로 압축)
    public int Find(int u) {
        if (parent[u] != u) { // 현재 원소가 자신의 부모가 아니라면
            parent[u] = Find(parent[u]); // 재귀적으로 부모를 찾아서 부모 갱신 (경로 압축)
        }
        return parent[u]; // 부모를 반환
    }

    // 두 집합 합치기 (Union by rank)
    public bool Union(int u, int v) {
        int root_u = Find(u); // u의 루트를 찾음
        int root_v = Find(v); // v의 루트를 찾음

        if (root_u != root_v) { // 루트가 다르다면, 즉 두 집합이 다르다면
            if (rank[root_u] > rank[root_v]) { // u의 트리 깊이가 더 크다면
                parent[root_v] = root_u; // v의 루트를 u의 루트로 설정
            } else if (rank[root_u] < rank[root_v]) { // v의 트리 깊이가 더 크다면
                parent[root_u] = root_v; // u의 루트를 v의 루트로 설정
            } else { // 트리 깊이가 같다면
                parent[root_v] = root_u; // v의 루트를 u의 루트로 설정하고
                rank[root_u]++; // u의 트리 깊이를 증가시킴
            }
            return true; // 두 집합이 합쳐졌으므로 true 반환
        }
        return false; // 이미 같은 집합이라면 false 반환
    }
}

class Program {
    static void Main(string[] args) {
        int n = int.Parse(Console.ReadLine()); // 행성의 수 입력 받기
        List<(int x, int y, int z, int index)> planets = new List<(int, int, int, int)>(); // 행성의 좌표와 인덱스를 저장할 리스트

        for (int i = 0; i < n; ++i) {
            var input = Console.ReadLine().Split(); // 행성의 좌표를 공백으로 분리하여 입력 받기
            int x = int.Parse(input[0]); // x 좌표
            int y = int.Parse(input[1]); // y 좌표
            int z = int.Parse(input[2]); // z 좌표
            planets.Add((x, y, z, i)); // 행성의 좌표와 인덱스를 튜플로 리스트에 저장
        }

        List<(int cost, int u, int v)> edges = new List<(int, int, int)>(); // 간선 목록 (비용, 행성1, 행성2)

        // x, y, z 좌표별로 정렬 후 인접 행성 간의 간선 추가
        for (int dim = 0; dim < 3; ++dim) {
            planets.Sort((a, b) => a.GetDim(dim).CompareTo(b.GetDim(dim))); // 각 좌표 축(dim) 별로 행성들을 정렬

            for (int i = 1; i < n; ++i) { // 인접한 행성 간의 간선을 생성
                int cost = Math.Abs(planets[i].GetDim(dim) - planets[i - 1].GetDim(dim)); // 비용 계산
                int u = planets[i].index; // 첫 번째 행성의 인덱스
                int v = planets[i - 1].index; // 두 번째 행성의 인덱스
                edges.Add((cost, u, v)); // 간선 목록에 추가
            }
        }

        edges.Sort((a, b) => a.cost.CompareTo(b.cost)); // 간선들을 비용 순으로 정렬

        DisjointSet dsu = new DisjointSet(n); // Disjoint Set 초기화
        int totalCost = 0; // 총 비용 초기화

        // Kruskal 알고리즘으로 최소 스패닝 트리 생성
        foreach (var (cost, u, v) in edges) { // 각 간선을 순회하며
            if (dsu.Union(u, v)) { // 두 집합이 합쳐지면 (사이클이 아니면)
                totalCost += cost; // 그 간선의 비용을 총 비용에 더함
            }
        }

        Console.WriteLine(totalCost); // 최종 최소 비용 출력
    }
}

// 확장 메서드: 특정 차원의 좌표 값을 반환하는 함수
static class Extensions {
    public static int GetDim(this (int x, int y, int z, int index) tuple, int dim) {
        return dim switch {
            0 => tuple.x, // dim이 0이면 x 좌표 반환
            1 => tuple.y, // dim이 1이면 y 좌표 반환
            _ => tuple.z  // 그 외에는 z 좌표 반환
        };
    }
}
