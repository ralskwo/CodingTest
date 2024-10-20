using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 4방향 이동을 위한 배열 (상, 우, 하, 좌)
    static readonly int[] dx = { -1, 0, 1, 0 };
    static readonly int[] dy = { 0, 1, 0, -1 };

    // BFS 함수 정의
    static int OptimizedBfs(int h, int w, string[] building, string initialKeys)
    {
        // 빌딩 주변에 패딩 추가
        var extendedBuilding = new char[h + 2][];
        extendedBuilding[0] = new string('.', w + 2).ToCharArray();
        extendedBuilding[h + 1] = new string('.', w + 2).ToCharArray();
        for (int i = 0; i < h; i++)
        {
            extendedBuilding[i + 1] = ('.' + building[i] + '.').ToCharArray();
        }

        // 초기 열쇠 설정
        var keys = new HashSet<char>(initialKeys.Where(k => k != '0').Select(char.ToUpper));

        // BFS를 위한 큐와 방문 배열 초기화
        var queue = new Queue<(int, int)>();
        var visited = new bool[h + 2, w + 2];
        queue.Enqueue((0, 0));
        visited[0, 0] = true;

        // 접근 불가능한 문들을 저장할 딕셔너리
        var inaccessibleDoors = new Dictionary<char, List<(int, int)>>();
        int documentsCollected = 0;

        // BFS 시작
        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();

            // 4방향 탐색
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i], ny = y + dy[i];

                // 범위 체크 및 방문 여부 확인
                if (nx >= 0 && nx < h + 2 && ny >= 0 && ny < w + 2 && !visited[nx, ny])
                {
                    char cell = extendedBuilding[nx][ny];

                    // 벽인 경우 스킵
                    if (cell == '*') continue;

                    visited[nx, ny] = true;

                    // 문서 발견
                    if (cell == '$')
                    {
                        documentsCollected++;
                    }
                    // 열쇠 발견
                    else if (char.IsLower(cell))
                    {
                        char key = char.ToUpper(cell);
                        if (!keys.Contains(key))
                        {
                            keys.Add(key);
                            // 해당 열쇠로 열 수 있는 문들 처리
                            if (inaccessibleDoors.TryGetValue(key, out var doors))
                            {
                                foreach (var door in doors)
                                {
                                    queue.Enqueue(door);
                                }
                                inaccessibleDoors.Remove(key);
                            }
                        }
                    }
                    // 문 발견
                    else if (char.IsUpper(cell))
                    {
                        if (!keys.Contains(cell))
                        {
                            if (!inaccessibleDoors.ContainsKey(cell))
                                inaccessibleDoors[cell] = new List<(int, int)>();
                            inaccessibleDoors[cell].Add((nx, ny));
                            continue;
                        }
                    }

                    // 다음 위치 큐에 추가
                    queue.Enqueue((nx, ny));
                }
            }
        }

        return documentsCollected;
    }

    // 각 테스트 케이스 해결 함수
    static int Solve()
    {
        var input = Console.ReadLine().Split();
        int h = int.Parse(input[0]);
        int w = int.Parse(input[1]);

        string[] building = new string[h];
        for (int i = 0; i < h; i++)
        {
            building[i] = Console.ReadLine();
        }

        string initialKeys = Console.ReadLine();

        return OptimizedBfs(h, w, building, initialKeys);
    }

    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());

        // 각 테스트 케이스에 대해 Solve 함수 호출
        for (int i = 0; i < T; i++)
        {
            Console.WriteLine(Solve());
        }
    }
}