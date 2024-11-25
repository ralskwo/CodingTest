using System;
using System.Collections.Generic;

class Program
{
    // 8방향 이동을 나타내는 방향 벡터
    static int[,] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };

    // BFS를 수행하는 함수
    static void BFS(int x, int y, int[,] grid, bool[,] visited, int h, int w)
    {
        Queue<(int, int)> queue = new Queue<(int, int)>(); // BFS를 위한 큐 선언
        queue.Enqueue((x, y)); // 시작점을 큐에 추가
        visited[x, y] = true; // 방문 처리

        while (queue.Count > 0) // 큐가 빌 때까지 반복
        {
            var (cx, cy) = queue.Dequeue(); // 현재 위치를 가져옴

            for (int i = 0; i < 8; i++) // 8방향을 확인
            {
                int nx = cx + directions[i, 0];
                int ny = cy + directions[i, 1];

                // 유효한 좌표인지 확인
                if (nx >= 0 && nx < h && ny >= 0 && ny < w)
                {
                    // 땅이고 방문하지 않았다면
                    if (grid[nx, ny] == 1 && !visited[nx, ny])
                    {
                        visited[nx, ny] = true; // 방문 처리
                        queue.Enqueue((nx, ny)); // 큐에 추가
                    }
                }
            }
        }
    }

    // 섬의 개수를 세는 함수
    static int CountIslands(int w, int h, int[,] grid)
    {
        bool[,] visited = new bool[h, w]; // 방문 여부를 저장할 배열
        int count = 0; // 섬의 개수 초기화

        for (int i = 0; i < h; i++) // 모든 칸을 순회
        {
            for (int j = 0; j < w; j++)
            {
                if (grid[i, j] == 1 && !visited[i, j]) // 땅이고 방문하지 않았다면
                {
                    BFS(i, j, grid, visited, h, w); // BFS 호출
                    count++; // 섬의 개수 증가
                }
            }
        }
        return count; // 최종 섬의 개수 반환
    }

    static void Main(string[] args)
    {
        while (true)
        {
            string[] dimensions = Console.ReadLine().Split(); // 너비와 높이 입력
            int w = int.Parse(dimensions[0]);
            int h = int.Parse(dimensions[1]);
            if (w == 0 && h == 0) break; // 종료 조건

            int[,] grid = new int[h, w]; // 지도 데이터
            for (int i = 0; i < h; i++) // 지도 입력
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < w; j++)
                {
                    grid[i, j] = int.Parse(line[j]);
                }
            }

            Console.WriteLine(CountIslands(w, h, grid)); // 결과 출력
        }
    }
}
