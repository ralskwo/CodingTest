using System;
using System.Collections.Generic;

class Program
{
    static HashSet<int> Bfs(Dictionary<int, List<int>> graph, int start)
    {
        HashSet<int> visited = new HashSet<int>();
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(start);
        visited.Add(start);
        
        while (queue.Count > 0)
        {
            int v = queue.Dequeue();
            foreach (int neighbor in graph[v])
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                }
            }
        }
        return visited;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine().Trim());  // 컴퓨터의 수
        int m = int.Parse(Console.ReadLine().Trim());  // 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

        // 그래프 초기화
        Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
        for (int i = 1; i <= n; i++)
        {
            graph[i] = new List<int>();
        }

        // 간선 입력 받기
        for (int i = 0; i < m; i++)
        {
            string[] inputs = Console.ReadLine().Trim().Split();
            int a = int.Parse(inputs[0]);
            int b = int.Parse(inputs[1]);
            graph[a].Add(b);
            graph[b].Add(a);
        }

        // BFS를 통해 1번 컴퓨터와 연결된 모든 컴퓨터를 찾기
        HashSet<int> infectedComputers = Bfs(graph, 1);

        // 1번 컴퓨터 제외
        infectedComputers.Remove(1);

        // 결과 출력
        Console.WriteLine(infectedComputers.Count);
    }
}
