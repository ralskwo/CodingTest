using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 입력값 처리
        string[] firstLine = Console.ReadLine().Split();
        int n = int.Parse(firstLine[0]); // 가수의 수
        int m = int.Parse(firstLine[1]); // 보조 PD의 수

        List<int>[] graph = new List<int>[n + 1]; // 그래프를 인접 리스트로 표현
        for (int i = 1; i <= n; i++) graph[i] = new List<int>();

        int[] indegree = new int[n + 1]; // 각 노드의 진입 차수를 저장

        // 그래프 구성
        for (int i = 0; i < m; i++)
        {
            string[] input = Console.ReadLine().Split();
            int k = int.Parse(input[0]); // 현재 보조 PD가 담당하는 가수의 수
            int[] sequence = new int[k];
            for (int j = 0; j < k; j++)
            {
                sequence[j] = int.Parse(input[j + 1]); // 가수 순서를 배열에 저장
            }
            for (int j = 0; j < k - 1; j++)
            {
                graph[sequence[j]].Add(sequence[j + 1]); // 간선 추가
                indegree[sequence[j + 1]]++; // 진입 차수 증가
            }
        }

        // 위상 정렬
        Queue<int> q = new Queue<int>(); // 진입 차수가 0인 노드를 처리할 큐
        List<int> result = new List<int>(); // 정렬 결과를 저장할 리스트

        for (int i = 1; i <= n; i++)
        {
            if (indegree[i] == 0)
            {
                q.Enqueue(i); // 초기 진입 차수가 0인 노드를 큐에 추가
            }
        }

        while (q.Count > 0)
        {
            int current = q.Dequeue();
            result.Add(current); // 현재 노드를 결과 리스트에 추가

            foreach (int neighbor in graph[current])
            {
                indegree[neighbor]--; // 연결된 노드의 진입 차수를 감소
                if (indegree[neighbor] == 0)
                {
                    q.Enqueue(neighbor); // 진입 차수가 0이 된 노드를 큐에 추가
                }
            }
        }

        // 결과 검증
        if (result.Count != n)
        {
            Console.WriteLine(0); // 사이클이 발생한 경우 0 출력
        }
        else
        {
            foreach (int node in result)
            {
                Console.WriteLine(node); // 정렬된 결과 출력
            }
        }
    }
}
