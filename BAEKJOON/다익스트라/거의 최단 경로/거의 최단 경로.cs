using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    const int INF = int.MaxValue;

    static void Main()
    {
        while (true)
        {
            var input = Console.ReadLine().Split();
            int N = int.Parse(input[0]);
            int M = int.Parse(input[1]);

            if (N == 0 && M == 0)
                break;

            input = Console.ReadLine().Split();
            int S = int.Parse(input[0]);
            int D = int.Parse(input[1]);

            var graph = new List<(int, int)>[N];
            var reverseGraph = new List<(int, int)>[N];
            for (int i = 0; i < N; i++)
            {
                graph[i] = new List<(int, int)>();
                reverseGraph[i] = new List<(int, int)>();
            }

            for (int i = 0; i < M; i++)
            {
                input = Console.ReadLine().Split();
                int U = int.Parse(input[0]);
                int V = int.Parse(input[1]);
                int P = int.Parse(input[2]);
                graph[U].Add((V, P));
                reverseGraph[V].Add((U, P));
            }

            var shortestDistances = Dijkstra(graph, S, N);
            int shortestDistance = shortestDistances[D];

            if (shortestDistance == INF)
            {
                Console.WriteLine(-1);
                continue;
            }

            RemoveShortestPaths(graph, reverseGraph, shortestDistances, D);

            var newDistances = Dijkstra(graph, S, N);
            int newDistance = newDistances[D];

            if (newDistance == INF)
            {
                Console.WriteLine(-1);
            }
            else
            {
                Console.WriteLine(newDistance);
            }
        }
    }

    static int[] Dijkstra(List<(int, int)>[] graph, int start, int n)
    {
        var distances = new int[n];
        for (int i = 0; i < n; i++)
            distances[i] = INF;
        distances[start] = 0;

        var pq = new SortedSet<(int, int)>();
        pq.Add((0, start));

        while (pq.Count > 0)
        {
            var (currentDistance, currentNode) = pq.Min;
            pq.Remove(pq.Min);

            if (currentDistance > distances[currentNode])
                continue;

            foreach (var (adjacent, weight) in graph[currentNode])
            {
                int distance = currentDistance + weight;
                if (distance < distances[adjacent])
                {
                    pq.Remove((distances[adjacent], adjacent));
                    distances[adjacent] = distance;
                    pq.Add((distance, adjacent));
                }
            }
        }
        return distances;
    }

    static void RemoveShortestPaths(List<(int, int)>[] graph, List<(int, int)>[] reverseGraph, int[] shortestDistances, int D)
    {
        var queue = new Queue<int>();
        queue.Enqueue(D);
        var removed = new HashSet<(int, int)>();

        while (queue.Count > 0)
        {
            int node = queue.Dequeue();
            foreach (var (prev, weight) in reverseGraph[node])
            {
                if (shortestDistances[prev] + weight == shortestDistances[node])
                {
                    if (!removed.Contains((prev, node)))
                    {
                        graph[prev].Remove((node, weight));
                        removed.Add((prev, node));
                        queue.Enqueue(prev);
                    }
                }
            }
        }
    }
}
