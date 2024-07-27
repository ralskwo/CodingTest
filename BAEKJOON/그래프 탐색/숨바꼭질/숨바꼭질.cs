using System;
using System.Collections.Generic;

class Program
{
    static int Bfs(int N, int K)
    {
        // 문제에서 주어진 위치의 최대값을 설정합니다.
        const int maxLimit = 100000;
        
        // 방문한 위치를 추적하기 위한 배열을 만듭니다. 인덱스는 위치를 나타내고 값은 방문 여부를 나타냅니다.
        bool[] visited = new bool[maxLimit + 1];
        
        // 큐를 초기화합니다. 시작 위치 N과 현재 시간을 튜플로 넣습니다.
        Queue<(int position, int time)> queue = new Queue<(int position, int time)>();
        queue.Enqueue((N, 0));
        
        // 큐가 비어 있지 않는 동안 반복합니다.
        while (queue.Count > 0)
        {
            // 큐의 맨 앞 요소를 가져와 현재 위치와 시간을 얻습니다.
            var current = queue.Dequeue();
            int position = current.position;
            int time = current.time;
            
            // 현재 위치가 동생의 위치와 같다면,
            if (position == K)
            {
                // 현재 시간을 반환합니다. (최단 시간)
                return time;
            }
            
            // 현재 위치에서 이동할 수 있는 세 가지 경우를 모두 확인합니다.
            int[] nextPositions = { position - 1, position + 1, position * 2 };
            foreach (int nextPos in nextPositions)
            {
                // 다음 위치가 범위 내에 있고 방문하지 않은 경우
                if (nextPos >= 0 && nextPos <= maxLimit && !visited[nextPos])
                {
                    // 위치를 방문한 것으로 표시합니다.
                    visited[nextPos] = true;
                    
                    // 다음 위치와 시간을 큐에 추가합니다.
                    queue.Enqueue((nextPos, time + 1));
                }
            }
        }
        
        return -1; // 만약 동생을 찾을 수 없는 경우
    }

    static void Main(string[] args)
    {
        // 표준 입력에서 수빈이의 위치 N과 동생의 위치 K를 읽습니다.
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int K = int.Parse(input[1]);
        
        // BFS 함수의 결과를 출력합니다.
        Console.WriteLine(Bfs(N, K));
    }
}
