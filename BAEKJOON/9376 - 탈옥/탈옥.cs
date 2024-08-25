using System;                           // 기본 입출력 및 기타 기능을 사용하기 위한 네임스페이스
using System.Collections.Generic;       // List와 LinkedList 등의 컬렉션을 사용하기 위한 네임스페이스

class Program
{
    static void Main()                  // 프로그램의 진입점
    {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스의 개수를 입력받음
        List<int> results = new List<int>();   // 각 테스트 케이스의 결과를 저장할 리스트 생성

        while (T-- > 0)                 // T가 0이 될 때까지 반복 (테스트 케이스 반복)
        {
            var dimensions = Console.ReadLine().Split(); // 감옥의 높이와 너비를 입력받아 분리
            int h = int.Parse(dimensions[0]);            // 감옥의 높이를 정수로 변환
            int w = int.Parse(dimensions[1]);            // 감옥의 너비를 정수로 변환

            string[] prisonMap = new string[h + 2];      // 감옥의 평면도를 저장할 배열 생성 (외부 공간 포함)
            prisonMap[0] = new string('.', w + 2);       // 맵의 상단을 빈 공간으로 초기화
            for (int i = 1; i <= h; i++)
            {
                prisonMap[i] = '.' + Console.ReadLine() + '.'; // 각 줄을 입력받아 양 옆에 빈 공간 추가
            }
            prisonMap[h + 1] = new string('.', w + 2);   // 맵의 하단을 빈 공간으로 초기화

            results.Add(Solve(prisonMap, h, w));         // 현재 테스트 케이스의 결과를 계산하여 리스트에 추가
        }

        foreach (int result in results)                  // 모든 테스트 케이스의 결과를 순차적으로 출력
        {
            Console.WriteLine(result);
        }
    }

    // BFS를 사용해 최단 거리를 계산하는 함수
    static int[,] Bfs((int, int) start, string[] prisonMap, int h, int w)
    {
        int[,] dist = new int[h + 2, w + 2];             // 거리 배열을 생성 (무한대 값으로 초기화)
        for (int i = 0; i < h + 2; i++)
            for (int j = 0; j < w + 2; j++)
                dist[i, j] = int.MaxValue;               // 모든 위치를 초기값인 MaxValue로 설정

        dist[start.Item1, start.Item2] = 0;              // 시작 위치의 거리를 0으로 설정
        var queue = new LinkedList<(int, int)>();        // BFS 탐색을 위한 큐(덱) 생성
        queue.AddLast(start);                            // 시작 위치를 큐에 추가

        int[] dx = { -1, 1, 0, 0 };                      // 상, 하, 좌, 우 방향 배열
        int[] dy = { 0, 0, -1, 1 };

        while (queue.Count > 0)                          // 큐가 빌 때까지 BFS 탐색을 수행
        {
            var (x, y) = queue.First.Value;              // 큐의 첫 번째 원소를 가져옴
            queue.RemoveFirst();                         // 큐에서 첫 번째 원소를 제거

            for (int i = 0; i < 4; i++)                  // 네 방향으로 이동 시도
            {
                int nx = x + dx[i];                      // 새로운 x 좌표
                int ny = y + dy[i];                      // 새로운 y 좌표

                if (nx >= 0 && nx < h + 2 && ny >= 0 && ny < w + 2) // 맵의 범위 내에 있는지 확인
                {
                    if (prisonMap[nx][ny] != '*' && dist[nx, ny] == int.MaxValue)
                    {
                        // 벽이 아니고 아직 방문하지 않은 경우
                        if (prisonMap[nx][ny] == '#')    // 만약 문을 만났다면
                        {
                            dist[nx, ny] = dist[x, y] + 1; // 문의 개수를 1 증가시켜 이동
                            queue.AddLast((nx, ny));    // 큐의 뒤에 추가
                        }
                        else                             // 빈 공간이라면
                        {
                            dist[nx, ny] = dist[x, y];  // 거리를 그대로 유지
                            queue.AddFirst((nx, ny));   // 큐의 앞에 추가 (우선적으로 처리)
                        }
                    }
                }
            }
        }

        return dist;                                    // 시작점으로부터 각 위치까지의 최소 거
