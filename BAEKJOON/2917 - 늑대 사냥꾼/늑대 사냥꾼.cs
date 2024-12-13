using System;
using System.Collections.Generic;

class Program {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static int[,] CalculateTreeDistances(char[,] forest, int N, int M) {
        int[,] treeDistances = new int[N,M];
        Queue<(int x, int y)> queue = new Queue<(int x, int y)>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                treeDistances[i,j] = int.MaxValue;
                if (forest[i,j] == '+') {
                    queue.Enqueue((i,j));
                    treeDistances[i,j] = 0;
                }
            }
        }

        while (queue.Count > 0) {
            var (x,y) = queue.Dequeue();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < M && treeDistances[nx,ny] > treeDistances[x,y] + 1) {
                    treeDistances[nx,ny] = treeDistances[x,y] + 1;
                    queue.Enqueue((nx,ny));
                }
            }
        }

        return treeDistances;
    }

    static int FindSafestPath(char[,] forest, int N, int M, (int x,int y) wolfPosition, int[,] treeDistances) {
        PriorityQueue<(int x, int y), int> pq = new PriorityQueue<(int x, int y), int>();
        pq.Enqueue(wolfPosition, -treeDistances[wolfPosition.x,wolfPosition.y]);
        bool[,] visited = new bool[N,M];
        visited[wolfPosition.x,wolfPosition.y] = true;

        while (pq.TryDequeue(out var pos, out var negMinDist)) {
            int minDist = -negMinDist;

            if (forest[pos.x,pos.y] == 'J') {
                return minDist;
            }

            for (int i = 0; i < 4; i++) {
                int nx = pos.x + dx[i];
                int ny = pos.y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx,ny]) {
                    visited[nx,ny] = true;
                    int newMinDist = Math.Min(minDist, treeDistances[nx,ny]);
                    pq.Enqueue((nx,ny), -newMinDist);
                }
            }
        }

        return -1;
    }

    static void Main() {
        string[] inputLine = Console.ReadLine().Split();
        int N = int.Parse(inputLine[0]);
        int M = int.Parse(inputLine[1]);
        char[,] forest = new char[N,M];

        for (int i = 0; i < N; i++) {
            string line = Console.ReadLine();
            for (int j = 0; j < M; j++) {
                forest[i,j] = line[j];
            }
        }

        (int x, int y) wolfPosition = (-1,-1);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (forest[i,j] == 'V') {
                    wolfPosition = (i,j);
                    break;
                }
            }
            if (wolfPosition != (-1,-1)) break;
        }

        var treeDistances = CalculateTreeDistances(forest, N, M);
        var result = FindSafestPath(forest, N, M, wolfPosition, treeDistances);

        Console.WriteLine(result);
    }
}
