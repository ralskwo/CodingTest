using System;
using System.Collections.Generic;

class TreasureIsland
{
    static int n, m; // 지도 크기 (세로 n, 가로 m)
    static List<string> treasure_map = new List<string>(); // 보물 지도를 저장할 리스트
    static int[] dx = { -1, 1, 0, 0 }; // x 좌표 이동: 상하
    static int[] dy = { 0, 0, -1, 1 }; // y 좌표 이동: 좌우

    // BFS 함수 정의 - 특정 위치 (x, y)에서 시작하여 최장 거리를 계산하는 함수
    static int BFS(int x, int y)
    {
        bool[,] visited = new bool[n, m]; // 방문 여부를 체크할 2차원 배열
        Queue<(int, int, int)> queue = new Queue<(int, int, int)>(); // 위치와 거리 정보를 담는 큐

        visited[x, y] = true; // 시작 위치 방문 처리
        queue.Enqueue((x, y, 0)); // 시작 위치와 거리(0)를 큐에 삽입

        int maxDistance = 0; // 최장 거리를 저장할 변수

        // 큐가 빌 때까지 반복 (BFS 탐색)
        while (queue.Count > 0)
        {
            var (cx, cy, dist) = queue.Dequeue(); // 현재 위치와 거리 정보를 큐에서 꺼내기
            maxDistance = Math.Max(maxDistance, dist); // 최장 거리 갱신

            // 네 방향으로 이동 가능한 위치 탐색
            for (int i = 0; i < 4; i++)
            {
                int nx = cx + dx[i]; // 새로운 x 좌표
                int ny = cy + dy[i]; // 새로운 y 좌표

                // 지도 범위 내이며, 방문하지 않은 육지('L')인 경우
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx, ny] && treasure_map[nx][ny] == 'L')
                {
                    visited[nx, ny] = true; // 방문 표시
                    queue.Enqueue((nx, ny, dist + 1)); // 새 위치와 거리 증가하여 큐에 삽입
                }
            }
        }

        return maxDistance; // 최장 거리 반환
    }

    static void Main()
    {
        // 지도 크기 입력받기
        var input = Console.ReadLine().Split();
        n = int.Parse(input[0]); // 세로 크기 n
        m = int.Parse(input[1]); // 가로 크기 m

        // 보물 지도 입력받기
        for (int i = 0; i < n; i++)
        {
            treasure_map.Add(Console.ReadLine().Trim()); // 각 줄을 입력받아 리스트에 저장
        }

        int maxTreasureDistance = 0; // 최장 최단 거리 저장 변수 초기화

        // 모든 육지 위치에서 BFS 수행
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (treasure_map[i][j] == 'L') // 육지인 경우만 BFS 수행
                {
                    maxTreasureDistance = Math.Max(maxTreasureDistance, BFS(i, j)); // 최장 거리 갱신
                }
            }
        }

        Console.WriteLine(maxTreasureDistance); // 최장 최단 거리 출력
    }
}