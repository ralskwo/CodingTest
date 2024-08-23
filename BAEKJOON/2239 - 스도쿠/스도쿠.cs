using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 입력 받기
        var board = new int[9, 9];
        for (int i = 0; i < 9; i++)
        {
            string input = Console.ReadLine();
            for (int j = 0; j < 9; j++)
            {
                board[i, j] = input[j] - '0';
            }
        }

        // 스도쿠 풀기
        SolveSudoku(board);

        // 결과 출력
        PrintBoard(board);
    }

    static bool IsValid(int[,] board, int row, int col, int num)
    {
        // 해당 행에 num이 있는지 확인
        for (int i = 0; i < 9; i++)
        {
            if (board[row, i] == num)
            {
                return false;
            }
        }

        // 해당 열에 num이 있는지 확인
        for (int i = 0; i < 9; i++)
        {
            if (board[i, col] == num)
            {
                return false;
            }
        }

        // 3x3 박스 내에 num이 있는지 확인
        int startRow = 3 * (row / 3);
        int startCol = 3 * (col / 3);
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (board[startRow + i, startCol + j] == num)
                {
                    return false;
                }
            }
        }

        // num을 놓을 수 있으면 true 반환
        return true;
    }

    static bool Backtrack(int[,] board, List<(int, int)> emptyCells, int index)
    {
        // 모든 빈 칸을 다 채웠다면 true 반환
        if (index == emptyCells.Count)
        {
            return true;
        }

        // 현재 빈 칸의 좌표 가져오기
        var (row, col) = emptyCells[index];

        // 1부터 9까지의 숫자 시도
        for (int num = 1; num <= 9; num++)
        {
            if (IsValid(board, row, col, num))
            {
                // 유효한 숫자라면 보드에 숫자 배치
                board[row, col] = num;

                // 다음 빈 칸으로 이동
                if (Backtrack(board, emptyCells, index + 1))
                {
                    return true;
                }

                // 현재 숫자가 유효하지 않다면 다시 0으로 되돌림
                board[row, col] = 0;
            }
        }

        // 가능한 숫자가 없다면 false 반환
        return false;
    }

    static bool SolveSudoku(int[,] board)
    {
        // 빈 칸들의 좌표를 리스트로 저장
        var emptyCells = new List<(int, int)>();
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (board[i, j] == 0)
                {
                    emptyCells.Add((i, j));
                }
            }
        }

        // 백트래킹 시작
        return Backtrack(board, emptyCells, 0);
    }

    static void PrintBoard(int[,] board)
    {
        // 보드 출력
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                Console.Write(board[i, j]);
            }
            Console.WriteLine();
        }
    }
}
