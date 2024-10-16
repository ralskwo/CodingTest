using System;
using System.Collections.Generic;

class Program
{
    // 상하좌우 이동을 위한 방향 벡터
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    // BFS로 외부 공기와 치즈 접촉을 탐색하는 함수
    static void BFS(int[,] cheese, bool[,] visited, int n, int m)
    {
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>(); // BFS에 사용할 큐
        queue.Enqueue(new Tuple<int, int>(0, 0)); // 외부 공기를 (0, 0)에서 시작
        visited[0, 0] = true; // 방문 처리

        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue(); // 현재 좌표를 큐에서 꺼냄

            // 상하좌우 탐색
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 범위 내에 있고, 아직 방문하지 않은 칸이면
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx, ny])
                {
                    if (cheese[nx, ny] == 0) // 공기라면
                    {
                        visited[nx, ny] = true;
                        queue.Enqueue(new Tuple<int, int>(nx, ny)); // 계속 탐색하기 위해 큐에 추가
                    }
                    else if (cheese[nx, ny] == 1) // 치즈라면
                    {
                        visited[nx, ny] = true;
                        cheese[nx, ny] = 2; // 다음에 녹일 치즈로 표시
                    }
                }
            }
        }
    }

    // 공기와 접촉한 치즈를 녹이는 함수
    static int MeltCheese(int[,] cheese, int n, int m)
    {
        int melted = 0; // 녹은 치즈 개수를 저장할 변수
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (cheese[i, j] == 2) // 녹을 치즈는 2로 표시됨
                {
                    cheese[i, j] = 0; // 치즈를 녹임
                    melted++;
                }
            }
        }
        return melted; // 녹은 치즈 개수를 반환
    }

    static void Main()
    {
        // 세로(n), 가로(m) 입력 받기
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        // 치즈 상태 입력 받기
        int[,] cheese = new int[n, m];
        for (int i = 0; i < n; i++)
        {
            string[] line = Console.ReadLine().Split();
            for (int j = 0; j < m; j++)
            {
                cheese[i, j] = int.Parse(line[j]);
            }
        }

        int time = 0; // 치즈가 녹는 데 걸린 시간
        int lastCheese = 0; // 마지막 남은 치즈 개수

        while (true)
        {
            bool[,] visited = new bool[n, m]; // 방문 여부 체크 배열
            BFS(cheese, visited, n, m); // BFS로 외부 공기와 접촉한 치즈 찾기

            int melted = MeltCheese(cheese, n, m); // 치즈를 녹임
            if (melted == 0) break; // 녹을 치즈가 없으면 종료

            lastCheese = melted; // 마지막으로 남은 치즈 개수 기록
            time++; // 시간이 1시간 증가
        }

        Console.WriteLine(time); // 치즈가 모두 녹는 데 걸린 시간 출력
        Console.WriteLine(lastCheese); // 마지막으로 남은 치즈 개수 출력
    }
}