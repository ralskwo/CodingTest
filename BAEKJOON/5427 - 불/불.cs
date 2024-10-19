using System;
using System.Collections.Generic;

class Program
{
    // 방향 벡터 (동, 서, 남, 북)
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, 1, -1 };

    // 빌딩 탈출 함수
    static string EscapeBuilding(int w, int h, string[] building)
    {
        var fireQueue = new Queue<(int, int)>(); // 불의 위치를 저장할 큐
        var personQueue = new Queue<(int, int)>(); // 상근이의 위치를 저장할 큐
        var fireTimes = new int[h, w]; // 불이 각 위치에 도달하는 시간을 저장하는 배열
        var personTimes = new int[h, w]; // 상근이가 각 위치에 도달하는 시간을 저장하는 배열

        // 배열을 초기화하여 모든 값을 -1로 설정합니다 (도달하지 않았음을 의미).
        for (int y = 0; y < h; y++)
        {
            for (int x = 0; x < w; x++)
            {
                fireTimes[y, x] = -1;
                personTimes[y, x] = -1;
            }
        }

        // 초기 위치 설정
        for (int y = 0; y < h; y++)
        {
            for (int x = 0; x < w; x++)
            {
                if (building[y][x] == '*')
                {
                    fireQueue.Enqueue((x, y)); // 불의 위치를 큐에 추가합니다.
                    fireTimes[y, x] = 0; // 불이 시작된 위치의 시간을 0으로 설정합니다.
                }
                if (building[y][x] == '@')
                {
                    personQueue.Enqueue((x, y)); // 상근이의 시작 위치를 큐에 추가합니다.
                    personTimes[y, x] = 0; // 상근이가 시작된 위치의 시간을 0으로 설정합니다.
                }
            }
        }

        // 불의 확산을 BFS로 처리합니다.
        while (fireQueue.Count > 0)
        {
            var (x, y) = fireQueue.Dequeue(); // 현재 위치의 불을 큐에서 꺼냅니다.
            for (int i = 0; i < 4; i++) // 동서남북 네 방향을 확인합니다.
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 다음 위치가 지도 범위 내에 있고, 아직 불이 도달하지 않은 빈 공간일 때
                if (nx >= 0 && nx < w && ny >= 0 && ny < h && fireTimes[ny, nx] == -1 && building[ny][nx] == '.')
                {
                    fireTimes[ny, nx] = fireTimes[y, x] + 1; // 현재 시간에서 1초 뒤에 불이 도달합니다.
                    fireQueue.Enqueue((nx, ny)); // 새로운 불의 위치를 큐에 추가합니다.
                }
            }
        }

        // 상근이의 이동을 BFS로 처리합니다.
        while (personQueue.Count > 0)
        {
            var (x, y) = personQueue.Dequeue(); // 현재 위치의 상근이를 큐에서 꺼냅니다.
            for (int i = 0; i < 4; i++) // 동서남북 네 방향을 확인합니다.
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 상근이가 지도 밖으로 나가는 경우 탈출 성공입니다.
                if (nx < 0 || nx >= w || ny < 0 || ny >= h)
                {
                    return (personTimes[y, x] + 1).ToString(); // 탈출하는 데 걸린 시간을 반환합니다.
                }

                // 다음 위치가 지도 범위 내에 있고, 이동 가능한 빈 공간이며, 아직 방문하지 않은 경우
                if (nx >= 0 && nx < w && ny >= 0 && ny < h && personTimes[ny, nx] == -1 && building[ny][nx] == '.')
                {
                    // 불이 도달하지 않았거나 상근이가 먼저 도달할 수 있는 경우에만 이동합니다.
                    if (fireTimes[ny, nx] == -1 || fireTimes[ny, nx] > personTimes[y, x] + 1)
                    {
                        personTimes[ny, nx] = personTimes[y, x] + 1; // 이동 시간을 기록합니다.
                        personQueue.Enqueue((nx, ny)); // 상근이의 새로운 위치를 큐에 추가합니다.
                    }
                }
            }
        }

        return "IMPOSSIBLE"; // 상근이가 탈출할 수 없는 경우 "IMPOSSIBLE"을 반환합니다.
    }

    static void Main()
    {
        int t = int.Parse(Console.ReadLine()); // 테스트 케이스의 개수를 입력받습니다.
        
        while (t-- > 0)
        {
            var inputs = Console.ReadLine().Split(); // 너비와 높이를 입력받습니다.
            int w = int.Parse(inputs[0]);
            int h = int.Parse(inputs[1]);

            string[] building = new string[h]; // 빌딩의 지도를 저장할 배열입니다.
            for (int i = 0; i < h; i++)
            {
                building[i] = Console.ReadLine(); // 빌딩의 지도를 입력받습니다.
            }

            // 빌딩 탈출 함수의 결과를 출력합니다.
            Console.WriteLine(EscapeBuilding(w, h, building));
        }
    }
}