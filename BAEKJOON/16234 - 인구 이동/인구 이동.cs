using System;
using System.Collections.Generic;

class Program
{
    static int N, L, R;  // 땅의 크기 N, 인구 차이 하한선 L, 상한선 R
    static int[,] population;  // 각 나라의 인구수를 저장하는 2차원 배열
    static bool[,] visited;    // 방문 여부를 체크하는 2차원 배열
    static int[][] directions = new int[][] { new int[] {-1, 0}, new int[] {1, 0}, new int[] {0, -1}, new int[] {0, 1} };  // 상, 하, 좌, 우 네 방향을 나타내는 배열

    static bool BFS(int startRow, int startCol)
    {
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();  // BFS를 위한 큐
        List<Tuple<int, int>> unionList = new List<Tuple<int, int>>();  // 연합에 속한 나라들의 좌표를 저장하는 리스트

        queue.Enqueue(Tuple.Create(startRow, startCol));  // 시작 좌표를 큐에 추가
        visited[startRow, startCol] = true;  // 시작 좌표를 방문 처리
        unionList.Add(Tuple.Create(startRow, startCol));  // 연합에 시작 좌표 추가

        int totalPopulation = population[startRow, startCol];  // 연합의 총 인구수
        int countryCount = 1;  // 연합에 속한 나라의 수

        while (queue.Count > 0)  // 큐가 빌 때까지 반복
        {
            var current = queue.Dequeue();
            int row = current.Item1;
            int col = current.Item2;

            for (int i = 0; i < 4; i++)  // 네 방향에 대해 반복
            {
                int newRow = row + directions[i][0];
                int newCol = col + directions[i][1];

                if (newRow >= 0 && newRow < N && newCol >= 0 && newCol < N && !visited[newRow, newCol])
                {
                    int populationDiff = Math.Abs(population[row, col] - population[newRow, newCol]);

                    if (L <= populationDiff && populationDiff <= R)  // 인구 차이가 L 이상, R 이하일 때
                    {
                        visited[newRow, newCol] = true;  // 새로운 좌표를 방문 처리
                        queue.Enqueue(Tuple.Create(newRow, newCol));  // 큐에 새로운 좌표 추가
                        unionList.Add(Tuple.Create(newRow, newCol));  // 연합에 새로운 좌표 추가
                        totalPopulation += population[newRow, newCol];  // 연합의 총 인구수 증가
                        countryCount++;  // 연합의 나라 수 증가
                    }
                }
            }
        }

        if (countryCount > 1)  // 연합이 2개 이상의 나라로 이루어진 경우
        {
            int newPopulation = totalPopulation / countryCount;  // 새로운 인구수 계산

            foreach (var country in unionList)  // 연합에 속한 모든 나라의 인구수 갱신
            {
                population[country.Item1, country.Item2] = newPopulation;
            }
            return true;  // 인구 이동이 발생했음을 반환
        }
        return false;  // 인구 이동이 발생하지 않았음을 반환
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split();  // N, L, R 입력
        N = int.Parse(input[0]);
        L = int.Parse(input[1]);
        R = int.Parse(input[2]);

        population = new int[N, N];  // N x N 크기의 인구수 배열 초기화

        for (int i = 0; i < N; i++)  // 인구수 입력
        {
            input = Console.ReadLine().Split();
            for (int j = 0; j < N; j++)
            {
                population[i, j] = int.Parse(input[j]);
            }
        }

        int days = 0;  // 인구 이동이 발생한 일수 초기화

        while (true)  // 무한 반복
        {
            visited = new bool[N, N];  // 방문 여부 배열 초기화
            bool movementOccurred = false;  // 인구 이동 발생 여부 초기화

            for (int i = 0; i < N; i++)  // 모든 나라에 대해 반복
            {
                for (int j = 0; j < N; j++)
                {
                    if (!visited[i, j])  // 방문하지 않은 나라에 대해 BFS 수행
                    {
                        if (BFS(i, j))
                        {
                            movementOccurred = true;  // 인구 이동 발생 표시
                        }
                    }
                }
            }

            if (!movementOccurred) break;  // 더 이상 인구 이동이 발생하지 않으면 종료
            days++;  // 인구 이동이 발생한 날 수 증가
        }

        Console.WriteLine(days);  // 결과 출력
    }
}
