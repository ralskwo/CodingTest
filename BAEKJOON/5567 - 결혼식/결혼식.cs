using System;
using System.Collections.Generic;

class Program
{
    static List<int>[] graph = new List<int>[501];  // 동기들의 친구 관계를 저장할 인접 리스트
    static bool[] visited = new bool[501];          // 각 동기의 방문 여부를 기록할 배열
    static int[] distance = new int[501];           // 상근이로부터 각 동기까지의 거리를 기록할 배열

    static int BFS(int start, int n)
    {
        Queue<int> queue = new Queue<int>();  // BFS 탐색을 위한 큐
        queue.Enqueue(start);                 // 시작점인 상근이(1번 학번)을 큐에 넣음
        visited[start] = true;                // 상근이의 방문 여부를 true로 설정
        distance[start] = 0;                  // 상근이의 거리는 0으로 설정

        while (queue.Count > 0)
        {
            int current = queue.Dequeue();  // 큐의 앞에서 현재 노드를 꺼냄

            foreach (int neighbor in graph[current])  // 현재 노드와 연결된 친구들을 확인
            {
                if (!visited[neighbor])  // 방문하지 않은 친구인 경우
                {
                    visited[neighbor] = true;  // 방문 처리
                    distance[neighbor] = distance[current] + 1;  // 친구의 거리는 현재 노드의 거리 + 1
                    queue.Enqueue(neighbor);  // 친구를 큐에 추가
                }
            }
        }

        int inviteCount = 0;  // 초대할 친구의 수를 세는 변수
        for (int i = 2; i <= n; i++)  // 상근이(1번 학번) 이외의 친구들에 대해
        {
            if (distance[i] > 0 && distance[i] <= 2)  // 상근이로부터 거리가 1 또는 2인 경우
            {
                inviteCount++;  // 초대할 수 있는 친구로 카운트
            }
        }
        return inviteCount;  // 초대할 친구 수 반환
    }

    static void Main(string[] args)
    {
        for (int i = 0; i < 501; i++)
        {
            graph[i] = new List<int>();  // 각 동기 리스트 초기화
        }

        int n = int.Parse(Console.ReadLine());  // 동기 수 입력
        int m = int.Parse(Console.ReadLine());  // 친구 관계 수 입력

        for (int i = 0; i < m; i++)
        {
            string[] input = Console.ReadLine().Split();  // 친구 관계 입력
            int a = int.Parse(input[0]);  // 첫 번째 친구
            int b = int.Parse(input[1]);  // 두 번째 친구
            graph[a].Add(b);  // a와 b는 서로 친구 관계이므로 양방향으로 저장
            graph[b].Add(a);
        }

        Console.WriteLine(BFS(1, n));  // 상근이(1번 학번)에서 BFS 탐색 시작하고, 초대할 친구 수 출력
    }
}