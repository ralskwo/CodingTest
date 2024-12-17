using System;
using System.Collections.Generic;

class Program
{
    // BFS 함수: 목표 이모티콘 개수 S를 만드는 최소 시간을 반환
    static int BFS(int S)
    {
        var queue = new Queue<(int screen, int clipboard, int time)>(); // 상태를 저장하는 큐
        bool[,] visited = new bool[S + 1, S + 1]; // 방문 여부 체크 (화면, 클립보드)

        queue.Enqueue((1, 0, 0)); // 초기 상태: 화면에 1개, 클립보드 비어있음, 시간 0초
        visited[1, 0] = true; // 초기 상태 방문 처리

        while (queue.Count > 0)
        {
            var (screen, clipboard, time) = queue.Dequeue(); // 현재 상태를 큐에서 꺼냄

            if (screen == S) // 화면에 있는 이모티콘 개수가 목표 S에 도달하면 시간 반환
                return time;

            // 연산 1: 화면 이모티콘을 클립보드에 복사
            if (!visited[screen, screen]) // 방문하지 않은 상태라면
            {
                visited[screen, screen] = true;
                queue.Enqueue((screen, screen, time + 1)); // (현재 화면, 클립보드에 저장된 화면, 시간 + 1)
            }

            // 연산 2: 클립보드 이모티콘을 화면에 붙여넣기
            if (clipboard > 0 && screen + clipboard <= S && !visited[screen + clipboard, clipboard])
            {
                visited[screen + clipboard, clipboard] = true;
                queue.Enqueue((screen + clipboard, clipboard, time + 1)); // 화면에 붙여넣기한 상태 추가
            }

            // 연산 3: 화면 이모티콘 중 하나 삭제
            if (screen > 0 && !visited[screen - 1, clipboard])
            {
                visited[screen - 1, clipboard] = true;
                queue.Enqueue((screen - 1, clipboard, time + 1)); // 화면 이모티콘을 1개 삭제한 상태 추가
            }
        }
        return -1; // 실패하는 경우는 없지만 안전 처리
    }

    static void Main()
    {
        int S = int.Parse(Console.ReadLine()); // 목표 이모티콘 개수 입력
        Console.WriteLine(BFS(S)); // BFS를 통해 최소 시간 출력
    }
}
