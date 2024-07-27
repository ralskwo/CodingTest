using System;
using System.Collections.Generic;

class Program
{
    static string Elevator(int F, int S, int G, int U, int D)
    {
        int[] visited = new int[F + 1]; // 방문 여부와 버튼 누름 횟수를 저장할 배열을 초기화합니다. 초기값은 -1로 설정하여 방문하지 않음을 표시합니다.
        for (int i = 0; i <= F; i++)
        {
            visited[i] = -1;
        }
        
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>(); // 현재 층과 버튼 누름 횟수를 저장하는 큐를 초기화합니다.
        queue.Enqueue(new Tuple<int, int>(S, 0)); // 시작 층 S와 누름 횟수 0을 추가합니다.
        visited[S] = 0; // 시작 층은 방문했으므로 0으로 설정합니다.

        while (queue.Count > 0) // 큐가 빌 때까지 반복합니다.
        {
            var current = queue.Dequeue(); // 큐에서 현재 층과 버튼 누름 횟수를 가져옵니다.
            int currentFloor = current.Item1;
            int presses = current.Item2;

            if (currentFloor == G) // 현재 층이 목표 층과 같으면
            {
                return presses.ToString(); // 버튼 누름 횟수를 반환합니다.
            }

            // 위로 이동
            if (currentFloor + U <= F && visited[currentFloor + U] == -1) // 위로 이동한 층이 총 층 수를 넘지 않고 아직 방문하지 않았다면
            {
                visited[currentFloor + U] = presses + 1; // 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
                queue.Enqueue(new Tuple<int, int>(currentFloor + U, presses + 1)); // 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
            }

            // 아래로 이동
            if (currentFloor - D > 0 && visited[currentFloor - D] == -1) // 아래로 이동한 층이 1층 이상이고 아직 방문하지 않았다면
            {
                visited[currentFloor - D] = presses + 1; // 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
                queue.Enqueue(new Tuple<int, int>(currentFloor - D, presses + 1)); // 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
            }
        }

        return "use the stairs"; // 큐가 비고도 목표 층에 도달하지 못하면 "use the stairs"를 반환합니다.
    }

    static void Main()
    {
        // 입력을 읽습니다.
        string[] inputs = Console.ReadLine().Split();
        int F = int.Parse(inputs[0]);
        int S = int.Parse(inputs[1]);
        int G = int.Parse(inputs[2]);
        int U = int.Parse(inputs[3]);
        int D = int.Parse(inputs[4]);

        // 함수 호출 및 결과 출력
        string result = Elevator(F, S, G, U, D); // elevator 함수를 호출하고 결과를 result에 저장합니다.
        Console.WriteLine(result); // 결과를 출력합니다.
    }
}
