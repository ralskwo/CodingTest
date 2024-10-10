using System;
using System.Collections.Generic;

class Program
{
    static int M, N, H; // 상자의 가로, 세로, 높이 크기
    static int[,,] box; // 3차원 배열 선언
    static int[][] directions = new int[6][] {
        new int[] {1, 0, 0}, new int[] {-1, 0, 0}, new int[] {0, 1, 0}, new int[] {0, -1, 0}, new int[] {0, 0, 1}, new int[] {0, 0, -1}
    }; // 6방향 탐색을 위한 배열
    static Queue<Tuple<int, int, int, int>> queue = new Queue<Tuple<int, int, int, int>>(); // BFS 탐색을 위한 큐 선언

    static void Main()
    {
        string[] sizes = Console.ReadLine().Split();
        M = int.Parse(sizes[0]);
        N = int.Parse(sizes[1]);
        H = int.Parse(sizes[2]);

        box = new int[H, N, M]; // 입력 크기만큼 3차원 배열 초기화
        int totalTomatoes = 0; // 전체 토마토 개수
        int ripeTomatoes = 0;  // 익은 토마토 개수
        int result = 0;        // 최종 최소 일수

        // 3차원 배열 입력 받기
        for (int h = 0; h < H; h++)
        {
            for (int n = 0; n < N; n++)
            {
                string[] line = Console.ReadLine().Split();
                for (int m = 0; m < M; m++)
                {
                    box[h, n, m] = int.Parse(line[m]); // 현재 칸의 상태 입력
                    if (box[h, n, m] == 1)
                    {
                        queue.Enqueue(new Tuple<int, int, int, int>(h, n, m, 0)); // 익은 토마토 위치 큐에 추가
                        ripeTomatoes++;
                    }
                    if (box[h, n, m] != -1) totalTomatoes++; // 전체 토마토 개수 증가
                }
            }
        }

        // 처음부터 모든 토마토가 익어 있는 경우 처리
        if (ripeTomatoes == totalTomatoes)
        {
            Console.WriteLine(0);
            return;
        }

        // BFS 탐색 시작
        while (queue.Count > 0)
        {
            var current = queue.Dequeue(); // 큐에서 현재 위치 꺼내기
            int z = current.Item1;
            int x = current.Item2;
            int y = current.Item3;
            int days = current.Item4;

            // 6방향으로 탐색
            foreach (var direction in directions)
            {
                int nz = z + direction[0];
                int nx = x + direction[1];
                int ny = y + direction[2];

                // 상자 범위 내이고, 익지 않은 토마토가 있을 때
                if (nz >= 0 && nz < H && nx >= 0 && nx < N && ny >= 0 && ny < M && box[nz, nx, ny] == 0)
                {
                    box[nz, nx, ny] = 1; // 익은 토마토로 변경
                    queue.Enqueue(new Tuple<int, int, int, int>(nz, nx, ny, days + 1)); // 새로운 위치 큐에 추가
                    result = days + 1; // 최소 일수 갱신
                }
            }
        }

        // 익지 않은 토마토가 남아 있는지 확인
        for (int h = 0; h < H; h++)
        {
            for (int n = 0; n < N; n++)
            {
                for (int m = 0; m < M; m++)
                {
                    if (box[h, n, m] == 0) // 익지 않은 토마토가 있는 경우
                    {
                        Console.WriteLine(-1);
                        return;
                    }
                }
            }
        }

        // 최소 일수 출력
        Console.WriteLine(result);
    }
}
