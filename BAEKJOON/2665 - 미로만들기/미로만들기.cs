using System;
using System.Collections.Generic;  // List와 LinkedList를 사용하기 위한 라이브러리

class Program
{
    // 상, 하, 좌, 우 방향 이동을 위한 델타값
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    // 최소 검은 방을 바꾸는 횟수를 계산하는 BFS 함수
    static int BfsMinChange(int n, int[][] grid)
    {
        // 각 방까지 도달할 때 바꾼 검은 방의 최소 횟수를 저장하는 배열
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++)
        {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++)
            {
                dist[i][j] = int.MaxValue;  // 무한대로 초기화
            }
        }
        dist[0][0] = 0;  // 시작점은 비용 0

        // BFS 탐색을 위한 LinkedList 선언
        LinkedList<(int, int)> dq = new LinkedList<(int, int)>();
        dq.AddLast((0, 0));  // 시작점 삽입

        while (dq.Count > 0)
        {
            // 덱에서 현재 좌표를 꺼냄
            (int x, int y) = dq.First.Value;
            dq.RemoveFirst();

            // 4방향으로 이동
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 좌표가 유효한지 확인
                if (nx >= 0 && nx < n && ny >= 0 && ny < n)
                {
                    // 흰 방일 경우
                    if (grid[nx][ny] == 1 && dist[nx][ny] > dist[x][y])
                    {
                        dist[nx][ny] = dist[x][y];  // 비용 업데이트
                        dq.AddFirst((nx, ny));  // 앞에 삽입
                    }
                    // 검은 방일 경우
                    else if (grid[nx][ny] == 0 && dist[nx][ny] > dist[x][y] + 1)
                    {
                        dist[nx][ny] = dist[x][y] + 1;  // 비용 1 추가
                        dq.AddLast((nx, ny));  // 뒤에 삽입
                    }
                }
            }
        }

        // 도착점의 최소 검은 방 변경 횟수 반환
        return dist[n - 1][n - 1];
    }

    static void Main(string[] args)
    {
        // 방 크기 입력
        int n = int.Parse(Console.ReadLine());

        // 방 상태 입력
        int[][] grid = new int[n][];
        for (int i = 0; i < n; i++)
        {
            grid[i] = new int[n];
            string line = Console.ReadLine();
            for (int j = 0; j < n; j++)
            {
                grid[i][j] = line[j] - '0';  // 문자열을 숫자로 변환하여 저장
            }
        }

        // BFS 함수 호출 및 결과 출력
        Console.WriteLine(BfsMinChange(n, grid));
    }
}
