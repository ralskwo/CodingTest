using System;
using System.Collections.Generic;

class Program
{
    // Union-Find 자료구조에서 부모를 찾는 함수
    static int Find(int[] parent, int x)
    {
        if (parent[x] != x) // 부모가 자기 자신이 아니면, 재귀적으로 부모를 찾아감
        {
            parent[x] = Find(parent, parent[x]);
        }
        return parent[x];
    }

    // Union-Find 자료구조에서 두 집합을 합치는 함수
    static void Union(int[] parent, int[] rank, int x, int y)
    {
        int rootX = Find(parent, x);
        int rootY = Find(parent, y);

        if (rootX != rootY) // 두 집합이 다른 경우에만 합침
        {
            if (rank[rootX] > rank[rootY]) // rank를 기준으로 더 높은 쪽에 합침
            {
                parent[rootY] = rootX;
            }
            else if (rank[rootX] < rank[rootY])
            {
                parent[rootX] = rootY;
            }
            else
            {
                parent[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }

    // 최소 스패닝 트리를 구성하여 최소 비행기 종류 개수를 구하는 함수
    static int MinimumFlights(int n, List<Tuple<int, int, int>> edges)
    {
        int[] parent = new int[n + 1];
        int[] rank = new int[n + 1];

        for (int i = 1; i <= n; ++i)
        {
            parent[i] = i;
        }

        edges.Sort(); // 간선을 가중치 기준으로 정렬

        int mstWeight = 0;
        int mstEdges = 0;

        foreach (var edge in edges)
        {
            int weight = edge.Item1;
            int u = edge.Item2;
            int v = edge.Item3;

            if (Find(parent, u) != Find(parent, v)) // 사이클이 생기지 않도록 간선을 추가
            {
                Union(parent, rank, u, v);
                mstWeight += weight;
                mstEdges += 1;
                if (mstEdges == n - 1) // MST가 완성되면 종료
                {
                    break;
                }
            }
        }

        return mstEdges;
    }

    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스 수

        List<int> results = new List<int>();

        for (int t = 0; t < T; ++t)
        {
            string[] nm = Console.ReadLine().Split(' ');
            int n = int.Parse(nm[0]); // 나라의 수
            int m = int.Parse(nm[1]); // 비행기 종류의 수

            List<Tuple<int, int, int>> edges = new List<Tuple<int, int, int>>();

            for (int i = 0; i < m; ++i)
            {
                string[] uv = Console.ReadLine().Split(' ');
                int u = int.Parse(uv[0]);
                int v = int.Parse(uv[1]);
                edges.Add(Tuple.Create(1, u, v)); // 모든 가중치를 1로 설정 (문제 조건)
            }

            int result = MinimumFlights(n, edges);
            results.Add(result);
        }

        foreach (var result in results)
        {
            Console.WriteLine(result);
        }
    }
}
