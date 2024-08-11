using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    const int INF = int.MaxValue;

    static List<List<(int, int)>> graph;

    static List<int> Dijkstra(int start, int numNodes)
    {
        var distances = Enumerable.Repeat(INF, numNodes + 1).ToList();
        var priorityQueue = new SortedSet<(int distance, int node)>();

        priorityQueue.Add((0, start));
        distances[start] = 0;

        while (priorityQueue.Any())
        {
            var (currentDistance, currentNode) = priorityQueue.First();
            priorityQueue.Remove(priorityQueue.First());

            if (distances[currentNode] < currentDistance)
                continue;

            foreach (var (adjacent, weight) in graph[currentNode])
            {
                int distance = currentDistance + weight;

                if (distance < distances[adjacent])
                {
                    priorityQueue.Remove((distances[adjacent], adjacent)); // 기존에 있는 거리는 삭제
                    distances[adjacent] = distance;
                    priorityQueue.Add((distance, adjacent));
                }
            }
        }

        return distances;
    }

    static void Main()
    {
        int numTestCases = int.Parse(Console.ReadLine());

        while (numTestCases-- > 0)
        {
            var parts = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int numNodes = parts[0];
            int numEdges = parts[1];
            int numDestCandidates = parts[2];

            parts = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int startNode = parts[0];
            int mustPass1 = parts[1];
            int mustPass2 = parts[2];

            graph = new List<List<(int, int)>>();
            for (int i = 0; i <= numNodes; i++)
            {
                graph.Add(new List<(int, int)>());
            }

            for (int i = 0; i < numEdges; i++)
            {
                parts = Console.ReadLine().Split().Select(int.Parse).ToArray();
                int node1 = parts[0];
                int node2 = parts[1];
                int weight = parts[2];
                graph[node1].Add((node2, weight));
                graph[node2].Add((node1, weight));
            }

            var destCandidates = new List<int>();
            for (int i = 0; i < numDestCandidates; i++)
            {
                destCandidates.Add(int.Parse(Console.ReadLine()));
            }

            var startToAll = Dijkstra(startNode, numNodes);
            var gToAll = Dijkstra(mustPass1, numNodes);
            var hToAll = Dijkstra(mustPass2, numNodes);

            var result = new List<int>();
            foreach (var candidate in destCandidates)
            {
                if ((startToAll[mustPass1] + gToAll[mustPass2] + hToAll[candidate] == startToAll[candidate]) ||
                    (startToAll[mustPass2] + hToAll[mustPass1] + gToAll[candidate] == startToAll[candidate]))
                {
                    result.Add(candidate);
                }
            }

            result.Sort();
            Console.WriteLine(string.Join(" ", result));
        }
    }
}
