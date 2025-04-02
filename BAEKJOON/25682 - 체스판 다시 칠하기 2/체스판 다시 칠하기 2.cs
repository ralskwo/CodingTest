using System;                             // 기본 입출력과 데이터 처리를 위한 네임스페이스를 포함합니다
using System.IO;                          // 파일 입출력을 위한 네임스페이스를 포함합니다

public class Program
{
    public static void Main()             // 프로그램의 진입점인 Main 메서드를 정의합니다
    {
        // 콘솔 입력을 빠르게 처리하기 위해 StreamReader를 사용합니다
        var sr = new StreamReader(Console.OpenStandardInput());
        var inputLine = sr.ReadLine();     // 첫 번째 줄을 입력받아 문자열로 저장합니다
        string[] tokens = inputLine.Split(); // 공백을 기준으로 입력값을 분리합니다
        int N = int.Parse(tokens[0]);      // 보드의 행 수 N을 정수로 파싱합니다
        int M = int.Parse(tokens[1]);      // 보드의 열 수 M을 정수로 파싱합니다
        int K = int.Parse(tokens[2]);      // 체스판 크기 K를 정수로 파싱합니다

        // 보드의 상태를 저장할 문자열 배열을 N 크기로 선언합니다
        string[] board = new string[N];
        for (int i = 0; i < N; i++)        // N개의 행에 대해 반복합니다
        {
            board[i] = sr.ReadLine();      // 각 행의 문자열을 입력받아 board 배열에 저장합니다
        }

        // 두 가지 체스판 패턴에 대한 2차원 누적합 배열을 (N+1)x(M+1) 크기로 초기화합니다
        int[,] p1 = new int[N + 1, M + 1]; // 패턴1 (맨 왼쪽 칸이 'W'인 경우)의 누적합 배열
        int[,] p2 = new int[N + 1, M + 1]; // 패턴2 (맨 왼쪽 칸이 'B'인 경우)의 누적합 배열

        // 보드의 각 칸에 대해 누적합 배열을 계산합니다
        for (int i = 0; i < N; i++)       // 보드의 각 행을 순회합니다
        {
            for (int j = 0; j < M; j++)   // 보드의 각 열을 순회합니다
            {
                char expected1, expected2; // 두 패턴에 대해 예상되는 색상을 저장할 변수를 선언합니다
                if ((i + j) % 2 == 0)       // (행 인덱스 + 열 인덱스)가 짝수이면
                {
                    expected1 = 'W';       // 패턴1에서는 'W'가 예상됩니다
                    expected2 = 'B';       // 패턴2에서는 'B'가 예상됩니다
                }
                else                        // (행 인덱스 + 열 인덱스)가 홀수이면
                {
                    expected1 = 'B';       // 패턴1에서는 'B'가 예상됩니다
                    expected2 = 'W';       // 패턴2에서는 'W'가 예상됩니다
                }
                // 현재 칸의 실제 색과 예상 색을 비교하여 불일치하면 1, 일치하면 0을 할당합니다
                int v1 = (board[i][j] != expected1) ? 1 : 0;
                int v2 = (board[i][j] != expected2) ? 1 : 0;

                // 2차원 누적합 공식을 사용하여 현재 칸까지의 누적합을 계산합니다
                p1[i + 1, j + 1] = v1 + p1[i, j + 1] + p1[i + 1, j] - p1[i, j];
                p2[i + 1, j + 1] = v2 + p2[i, j + 1] + p2[i + 1, j] - p2[i, j];
            }
        }

        int ans = int.MaxValue;         // 최소 재칠 횟수를 저장할 변수 ans를 매우 큰 값으로 초기화합니다

        // 가능한 모든 K×K 부분 보드의 시작 위치에 대해 검사합니다
        for (int i = 0; i <= N - K; i++) // 시작 행 인덱스 i를 0부터 N-K까지 순회합니다
        {
            for (int j = 0; j <= M - K; j++) // 시작 열 인덱스 j를 0부터 M-K까지 순회합니다
            {
                // 누적합 배열을 이용하여 (i, j)에서 시작하는 K×K 영역의 불일치 개수를 계산합니다
                int mismatches1 = p1[i + K, j + K] - p1[i, j + K] - p1[i + K, j] + p1[i, j];
                int mismatches2 = p2[i + K, j + K] - p2[i, j + K] - p2[i + K, j] + p2[i, j];
                // 두 패턴 중 더 적은 재칠 횟수를 현재 ans와 비교하여 갱신합니다
                ans = Math.Min(ans, Math.Min(mismatches1, mismatches2));
            }
        }

        // 최종 계산된 최소 재칠 횟수를 출력합니다
        Console.WriteLine(ans);
    }
}
