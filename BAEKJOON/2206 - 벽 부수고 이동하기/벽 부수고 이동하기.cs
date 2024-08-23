using System;
using System.Collections.Generic;

class Program
{
    struct State
    {
        public int X, Y, WallBroken;
        public State(int x, int y, int wallBroken)
        {
            X = x;
            Y = y;
            WallBroken = wallBroken;
        }
    }

    static int Bfs(int[][] maze, int n, int m)
    {
        // 이동 방향: 상, 하, 좌, 우
        int[][] directions = new int[][]
        {
            new int[] {-1, 0}, new int[] {1, 0},
            new int[] {0, -1}, new int[] {0, 1}
        };

        // BFS를 위한 큐 초기화: (x, y, 벽을 부쉈는지 여부)
        Queue<State> queue = new Queue<State>();
        queue.Enqueue(new State(0, 0, 0));
        
        // 방문 체크 리스트 초기화
        bool[,,] visited = new bool[n, m, 2];
        visited[0, 0, 0] = true;

        // 거리 리스트 초기화
        int[,,] distance = new int[n, m, 2];
        distance[0, 0, 0] = 1;

        while (queue.Count > 0)
        {
            State current = queue.Dequeue();
            int x = current.X;
            int y = current.Y;
            int wallBroken = current.WallBroken;

            // 도착 지점에 도달했을 때
            if (x == n - 1 && y == m - 1)
            {
                return distance[x, y, wallBroken];
            }

            // 4방향 탐색
            foreach (var direction in directions)
            {
                int nx = x + direction[0];
                int ny = y + direction[1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m)
                {
                    if (maze[nx][ny] == 0 && !visited[nx, ny, wallBroken])
                    {
                        // 벽이 아니고, 방문하지 않은 위치일 때
                        visited[nx, ny, wallBroken] = true;
                        distance[nx, ny, wallBroken] = distance[x, y, wallBroken] + 1;
                        queue.Enqueue(new State(nx, ny, wallBroken));
                    }

                    if (maze[nx][ny] == 1 && wallBroken == 0 && !visited[nx, ny, 1])
                    {
                        // 벽이지만, 아직 벽을 부수지 않은 경우
                        visited[nx, ny, 1] = true;
                        distance[nx, ny, 1] = distance[x, y, wallBroken] + 1;
                        queue.Enqueue(new State(nx, ny, 1));
                    }
                }
            }
        }

        return -1; // 도착 지점에 도달할 수 없는 경우
    }

    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        int[][] maze = new int[n][];
        for (int i = 0; i < n; i++)
        {
            string row = Console.ReadLine();
            maze[i] = new int[m];
            for (int j = 0; j < m; j++)
            {
                maze[i][j] = row[j] - '0';
            }
        }

        Console.WriteLine(Bfs(maze, n, m));
    }
}
