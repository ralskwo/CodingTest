using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static char[,] grid = new char[5, 5];
    static int[] dx = { -1, 1, 0, 0 }; // 상하좌우 이동
    static int[] dy = { 0, 0, -1, 1 }; // 상하좌우 이동

    // 선택된 좌표들이 인접한지 확인하는 함수
    static bool IsAdjacent(List<(int, int)> selected)
    {
        var queue = new Queue<(int, int)>();
        var visited = new HashSet<(int, int)>();
        queue.Enqueue(selected[0]);
        visited.Add(selected[0]);
        int count = 1;

        // BFS 탐색
        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                var neighbor = (nx, ny);

                // 선택된 좌표에 포함되고 아직 방문하지 않았다면
                if (selected.Contains(neighbor) && !visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                    count++;
                }
            }
        }

        // 7개의 좌표가 모두 연결되어 있다면 true 반환
        return count == 7;
    }

    // 선택된 좌표 중 'S' 학생의 수를 세는 함수
    static int CountS(List<(int, int)> selected)
    {
        int count = 0;
        foreach (var (x, y) in selected)
        {
            if (grid[x, y] == 'S') count++;
        }
        return count;
    }

    static void Main(string[] args)
    {
        // 5x5 격자 입력 받기
        for (int i = 0; i < 5; i++)
        {
            var line = Console.ReadLine();
            if (line == null || line.Length != 5)
            {
                Console.WriteLine("Invalid input. Each line must be 5 characters.");
                return;
            }

            for (int j = 0; j < 5; j++)
            {
                grid[i, j] = line[j];
            }
        }

        // 모든 좌표 생성
        var positions = new List<(int, int)>();
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                positions.Add((i, j));
            }
        }

        int result = 0;

        // 25개의 좌표에서 7개의 조합 생성
        var combinations = GetCombinations(positions, 7);
        foreach (var selected in combinations)
        {
            // 조건 확인: 'S' 학생이 4명 이상이고 좌표들이 인접한 경우
            if (CountS(selected.ToList()) >= 4 && IsAdjacent(selected.ToList()))
            {
                result++;
            }
        }

        // 결과 출력
        Console.WriteLine(result);
    }

    // 조합을 생성하는 함수
    static IEnumerable<IEnumerable<T>> GetCombinations<T>(IEnumerable<T> list, int length)
    {
        if (length == 0) return new[] { Array.Empty<T>() };
        return list.SelectMany((item, index) =>
            GetCombinations(list.Skip(index + 1), length - 1).Select(combination => (new[] { item }).Concat(combination)));
    }
}
