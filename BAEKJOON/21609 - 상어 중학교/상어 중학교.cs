using System;
using System.Collections.Generic;

class Program
{
    const int EMPTY = -2; // 빈 공간을 나타내는 상수
    const int BLACK = -1; // 검은색 블록을 나타내는 상수
    const int RAINBOW = 0; // 무지개 블록을 나타내는 상수

    // 네 방향 탐색을 위한 벡터 (상, 하, 좌, 우)
    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    // BFS를 사용하여 블록 그룹을 찾는 함수
    static (int size, int rainbowCount, (int, int) standardBlock, List<(int, int)> group) Bfs(int N, int[,] grid, int startR, int startC, int color)
    {
        Queue<(int, int)> q = new Queue<(int, int)>();
        bool[,] visited = new bool[N, N];

        List<(int, int)> group = new List<(int, int)>();
        int rainbowCount = 0;
        (int, int) standardBlock = (startR, startC); // 기준 블록

        q.Enqueue((startR, startC));
        group.Add((startR, startC));
        visited[startR, startC] = true;

        while (q.Count > 0)
        {
            var (r, c) = q.Dequeue();

            // 네 방향 탐색
            for (int i = 0; i < 4; i++)
            {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // 격자 범위 내에 있고 방문하지 않은 경우
                if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr, nc])
                {
                    // 같은 색상 블록이나 무지개 블록인 경우
                    if (grid[nr, nc] == color || grid[nr, nc] == RAINBOW)
                    {
                        visited[nr, nc] = true;
                        q.Enqueue((nr, nc));
                        group.Add((nr, nc));

                        // 무지개 블록인 경우 카운트 증가
                        if (grid[nr, nc] == RAINBOW)
                        {
                            rainbowCount++;
                        }
                        else
                        {
                            // 일반 블록인 경우 기준 블록 업데이트
                            if ((nr, nc).CompareTo(standardBlock) < 0)
                            {
                                standardBlock = (nr, nc);
                            }
                        }
                    }
                }
            }
        }

        // 무지개 블록은 다른 그룹에서도 사용할 수 있도록 방문 표시 초기화
        foreach (var (r, c) in group)
        {
            if (grid[r, c] == RAINBOW)
            {
                visited[r, c] = false;
            }
        }

        return (group.Count, rainbowCount, standardBlock, group);
    }

    // 격자에서 가장 큰 블록 그룹을 찾는 함수
    static List<(int, int)> FindLargestBlockGroup(int N, int[,] grid)
    {
        List<(int, int)> largestGroup = new List<(int, int)>();
        (int size, int rainbowCount, (int, int) standardBlock, List<(int, int)> group) best = (0, 0, (0, 0), new List<(int, int)>());

        // 격자의 각 칸을 순회
        for (int r = 0; r < N; r++)
        {
            for (int c = 0; c < N; c++)
            {
                // 일반 블록이면 BFS 실행
                if (grid[r, c] > 0)
                {
                    var result = Bfs(N, grid, r, c, grid[r, c]);
                    var (size, rainbowCount, standardBlock, group) = result;

                    // 그룹의 크기가 2 이상이어야 함
                    if (size >= 2)
                    {
                        // 조건에 따라 가장 큰 그룹 선택
                        if ((size, rainbowCount, standardBlock).CompareTo((best.size, best.rainbowCount, best.standardBlock)) > 0)
                        {
                            best = result;
                        }
                    }
                }
            }
        }

        // 가장 큰 그룹 반환
        return best.group;
    }

    // 중력을 적용하여 블록을 아래로 떨어뜨리는 함수
    static void ApplyGravity(int N, int[,] grid)
    {
        // 각 열에 대해 아래에서 위로 탐색
        for (int col = 0; col < N; col++)
        {
            int emptyRow = N - 1; // 블록이 내려올 빈 공간의 행 인덱스
            for (int row = N - 1; row >= 0; row--)
            {
                // 검은색 블록이면 빈 공간 업데이트
                if (grid[row, col] == BLACK)
                {
                    emptyRow = row - 1;
                }
                // 일반 블록이나 무지개 블록인 경우
                else if (grid[row, col] >= 0)
                {
                    // 블록을 아래로 이동
                    if (emptyRow != row)
                    {
                        grid[emptyRow, col] = grid[row, col];
                        grid[row, col] = EMPTY;
                    }
                    emptyRow--;
                }
            }
        }
    }

    // 격자를 90도 반시계 방향으로 회전하는 함수
    static int[,] RotateCounterClockwise(int N, int[,] grid)
    {
        int[,] newGrid = new int[N, N]; // 새로운 격자 생성
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                newGrid[N - j - 1, i] = grid[i, j];
            }
        }
        return newGrid;
    }

    // 게임을 진행하여 총 점수를 계산하는 함수
    static int PlayGame(int N, int[,] grid)
    {
        int totalScore = 0;

        while (true)
        {
            // 1. 가장 큰 블록 그룹 찾기
            var largestGroup = FindLargestBlockGroup(N, grid);
            if (largestGroup.Count == 0)
            {
                break; // 더 이상 블록 그룹이 없으면 종료
            }

            // 2. 블록 그룹 제거 및 점수 계산
            foreach (var (r, c) in largestGroup)
            {
                grid[r, c] = EMPTY; // 블록 제거
            }
            totalScore += largestGroup.Count * largestGroup.Count; // 점수 누적

            // 3. 중력 적용
            ApplyGravity(N, grid);

            // 4. 격자를 90도 반시계 방향으로 회전
            grid = RotateCounterClockwise(N, grid);

            // 5. 중력 재적용
            ApplyGravity(N, grid);
        }

        return totalScore;
    }

    static void Main()
    {
        string[] inputs = Console.ReadLine().Split();
        int N = int.Parse(inputs[0]);
        int M = int.Parse(inputs[1]);

        // 격자 입력
        int[,] grid = new int[N, N];
        for (int i = 0; i < N; i++)
        {
            string[] rowInput = Console.ReadLine().Split();
            for (int j = 0; j < N; j++)
            {
                grid[i, j] = int.Parse(rowInput[j]);
            }
        }

        // 게임 진행 및 결과 출력
        int result = PlayGame(N, grid);
        Console.WriteLine(result);
    }
}
