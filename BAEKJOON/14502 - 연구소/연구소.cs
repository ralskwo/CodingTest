using System;  // 기본적인 입출력 기능을 사용하기 위해 System 네임스페이스를 포함
using System.Collections.Generic;  // List와 Queue 같은 컬렉션을 사용하기 위해 포함
using System.Linq;  // LINQ 기능을 사용하기 위해 포함

class Program
{
    static int n, m;  // 연구소의 세로 크기 n과 가로 크기 m
    static int[,] lab;  // 연구소의 상태를 저장하는 2차원 배열
    static List<(int, int)> emptySpaces = new List<(int, int)>();  // 빈 칸의 위치를 저장하는 리스트
    static List<(int, int)> viruses = new List<(int, int)>();  // 바이러스의 위치를 저장하는 리스트
    static int[] dx = { -1, 1, 0, 0 };  // 상하좌우 이동을 위한 x축 방향 벡터
    static int[] dy = { 0, 0, -1, 1 };  // 상하좌우 이동을 위한 y축 방향 벡터

    // 바이러스 확산을 시뮬레이션하는 함수
    static void SpreadVirus(int[,] tempLab)
    {
        Queue<(int, int)> queue = new Queue<(int, int)>();  // 바이러스의 위치를 저장할 큐 생성
        foreach (var virus in viruses)  // 모든 바이러스 위치를 큐에 추가
        {
            queue.Enqueue(virus);
        }

        while (queue.Count > 0)  // 큐가 빌 때까지 반복
        {
            var (x, y) = queue.Dequeue();  // 큐에서 좌표를 꺼내옴

            for (int i = 0; i < 4; i++)  // 상하좌우 4방향에 대해 반복
            {
                int nx = x + dx[i];  // 새로운 x 좌표 계산
                int ny = y + dy[i];  // 새로운 y 좌표 계산

                // 새로운 좌표가 연구소 범위 내에 있고, 빈 칸(0)인 경우
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && tempLab[nx, ny] == 0)
                {
                    tempLab[nx, ny] = 2;  // 바이러스를 퍼뜨림
                    queue.Enqueue((nx, ny));  // 새로 바이러스가 퍼진 위치를 큐에 추가
                }
            }
        }
    }

    // 안전 영역의 크기를 계산하는 함수
    static int GetSafeArea(int[,] tempLab)
    {
        int safeArea = 0;  // 안전 영역 크기를 저장할 변수
        for (int i = 0; i < n; i++)  // 연구소의 모든 칸을 확인
        {
            for (int j = 0; j < m; j++)
            {
                if (tempLab[i, j] == 0)  // 빈 칸(0)이면
                {
                    safeArea++;  // 안전 영역 크기 증가
                }
            }
        }
        return safeArea;  // 안전 영역 크기 반환
    }

    // 최대 안전 영역을 찾는 함수
    static int FindMaxSafeArea()
    {
        int maxSafeArea = 0;  // 최대 안전 영역 크기를 저장할 변수

        var combinations = GetCombinations(emptySpaces.Count, 3);  // 빈 칸 중에서 3개를 선택하는 모든 조합을 생성

        foreach (var walls in combinations)  // 각 조합에 대해 반복
        {
            int[,] tempLab = (int[,])lab.Clone();  // 연구소 상태를 깊은 복사

            foreach (var index in walls)  // 선택된 3개의 빈 칸 위치에 대해
            {
                var (x, y) = emptySpaces[index];  // 해당 위치의 좌표를 가져옴
                tempLab[x, y] = 1;  // 벽을 세움
            }

            SpreadVirus(tempLab);  // 바이러스를 확산시킴

            int safeArea = GetSafeArea(tempLab);  // 안전 영역 크기를 계산
            maxSafeArea = Math.Max(maxSafeArea, safeArea);  // 최대 안전 영역 크기를 갱신
        }

        return maxSafeArea;  // 최대 안전 영역 크기 반환
    }

    // n개 중 r개를 선택하는 조합을 생성하는 함수
    static IEnumerable<int[]> GetCombinations(int n, int r)
    {
        int[] indices = Enumerable.Range(0, r).ToArray();  // 0부터 r-1까지의 숫자로 초기화된 배열 생성
        while (true)
        {
            yield return (int[])indices.Clone();  // 현재 조합을 반환
            int i = r - 1;  // 가장 오른쪽부터 시작
            while (i >= 0 && indices[i] == i + n - r) i--;  // 가능한 위치를 찾을 때까지 왼쪽으로 이동
            if (i < 0) break;  // 더 이상 조합이 없으면 종료
            indices[i]++;  // 현재 위치에서 값을 증가
            for (int j = i + 1; j < r; j++) indices[j] = indices[j - 1] + 1;  // 그 이후의 위치를 재조정
        }
    }

    static void Main()
    {
        string[] inputs = Console.ReadLine().Split();  // 입력을 공백으로 분리하여 배열에 저장
        n = int.Parse(inputs[0]);  // 연구소의 세로 크기 n
        m = int.Parse(inputs[1]);  // 연구소의 가로 크기 m
        lab = new int[n, m];  // 연구소의 상태를 저장할 2차원 배열 초기화

        for (int i = 0; i < n; i++)  // 연구소 상태를 입력받음
        {
            inputs = Console.ReadLine().Split();  // 한 줄씩 입력받아 분리
            for (int j = 0; j < m; j++)
            {
                lab[i, j] = int.Parse(inputs[j]);  // 현재 칸의 상태 저장
                if (lab[i, j] == 0)  // 빈 칸(0)일 경우
                {
                    emptySpaces.Add((i, j));  // 빈 칸의 위치를 리스트에 추가
                }
                else if (lab[i, j] == 2)  // 바이러스(2)일 경우
                {
                    viruses.Add((i, j));  // 바이러스의 위치를 리스트에 추가
                }
            }
        }

        Console.WriteLine(FindMaxSafeArea());  // 최대 안전 영역 크기를 계산하고 출력
    }
}
