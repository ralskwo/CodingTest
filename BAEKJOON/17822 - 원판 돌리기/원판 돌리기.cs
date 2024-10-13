using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 입력을 위한 변수 선언
    static int N, M, T;
    static List<List<int>> board;
    static List<(int, int, int)> commands;  // 회전 명령을 저장할 튜플 리스트

    // 인접한 수를 제거하는 함수
    static bool RemoveAdjacent()
    {
        bool[,] toRemove = new bool[N, M];  // 삭제할 좌표를 표시
        bool removed = false;  // 인접한 수가 삭제되었는지 여부
        
        // 모든 원판과 그 안의 수를 순회
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                if (board[i][j] == 0) continue;  // 0이면 이미 삭제된 수
                int cur = board[i][j];  // 현재 수
                
                // 같은 원판에서 좌우로 인접한 수 비교
                if (board[i][j] == board[i][(j + 1) % M])
                {
                    toRemove[i, j] = toRemove[i, (j + 1) % M] = true;
                    removed = true;
                }
                if (board[i][j] == board[i][(j + M - 1) % M])
                {
                    toRemove[i, j] = toRemove[i, (j + M - 1) % M] = true;
                    removed = true;
                }

                // 다른 원판과 상하로 인접한 수 비교
                if (i > 0 && board[i][j] == board[i - 1][j])
                {
                    toRemove[i, j] = toRemove[i - 1, j] = true;
                    removed = true;
                }
                if (i < N - 1 && board[i][j] == board[i + 1][j])
                {
                    toRemove[i, j] = toRemove[i + 1, j] = true;
                    removed = true;
                }
            }
        }

        // 인접한 수를 모두 0으로 변경
        if (removed)
        {
            for (int i = 0; i < N; ++i)
            {
                for (int j = 0; j < M; ++j)
                {
                    if (toRemove[i, j]) board[i][j] = 0;
                }
            }
        }
        
        return removed;
    }

    // 평균에 따른 수 조정 함수
    static void AdjustByAverage()
    {
        int totalSum = 0, totalCount = 0;

        // 모든 원판의 수를 합산하고 개수를 셈
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                if (board[i][j] != 0)
                {
                    totalSum += board[i][j];
                    totalCount++;
                }
            }
        }

        if (totalCount == 0) return;  // 남은 수가 없으면 함수 종료

        double average = (double)totalSum / totalCount;  // 평균 계산

        // 평균에 따라 수를 조정
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                if (board[i][j] != 0)
                {
                    if (board[i][j] > average) board[i][j]--;  // 평균보다 크면 1 감소
                    else if (board[i][j] < average) board[i][j]++;  // 평균보다 작으면 1 증가
                }
            }
        }
    }

    // 원판을 회전시키는 함수
    static void Rotate(int x, int d, int k)
    {
        for (int i = x - 1; i < N; i += x)
        {
            if (d == 0)  // 시계 방향
            {
                for (int j = 0; j < k; ++j)
                {
                    board[i].Insert(0, board[i][M - 1]);  // 마지막 원소를 맨 앞에 추가
                    board[i].RemoveAt(M);  // 마지막 원소 제거
                }
            }
            else  // 반시계 방향
            {
                for (int j = 0; j < k; ++j)
                {
                    board[i].Add(board[i][0]);  // 첫 원소를 맨 뒤에 추가
                    board[i].RemoveAt(0);  // 첫 원소 제거
                }
            }
        }
    }

    static void Main(string[] args)
    {
        // 입력 받기
        string[] input = Console.ReadLine().Split();
        N = int.Parse(input[0]);
        M = int.Parse(input[1]);
        T = int.Parse(input[2]);

        board = new List<List<int>>();  // N개의 원판 공간 할당
        for (int i = 0; i < N; ++i)
        {
            input = Console.ReadLine().Split();
            board.Add(input.Select(int.Parse).ToList());  // 각 원판의 숫자 저장
        }

        commands = new List<(int, int, int)>();
        for (int i = 0; i < T; ++i)
        {
            input = Console.ReadLine().Split();
            int x = int.Parse(input[0]);
            int d = int.Parse(input[1]);
            int k = int.Parse(input[2]);
            commands.Add((x, d, k));  // 회전 명령 저장
        }

        // 회전 명령을 처리
        foreach (var command in commands)
        {
            (int x, int d, int k) = command;
            Rotate(x, d, k);  // 회전 수행
            
            // 인접한 수를 제거하거나 평균에 따라 조정
            if (!RemoveAdjacent())
            {
                AdjustByAverage();
            }
        }

        // 최종 결과 계산
        int result = board.Sum(row => row.Sum());

        Console.WriteLine(result);  // 결과 출력
    }
}