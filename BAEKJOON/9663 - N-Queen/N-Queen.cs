using System;

class Program
{
    // N-Queen 문제 해결 함수
    static int NQueen(int N)
    {
        // 백트래킹을 통해 퀸을 배치하는 함수
        // row: 현재 퀸을 놓을 행
        // cols: 퀸이 배치된 열을 비트마스크로 저장
        // diag1: 좌하향 대각선 비트마스크
        // diag2: 우하향 대각선 비트마스크
        Func<int, int, int, int, int> solve = null;
        solve = (row, cols, diag1, diag2) =>
        {
            if (row == N) return 1; // 모든 퀸을 배치했을 경우, 배치 성공
            int count = 0; // 가능한 배치 수를 저장
            int availablePositions = (~(cols | diag1 | diag2)) & ((1 << N) - 1); // 퀸을 놓을 수 있는 자리 계산

            // 가능한 위치가 있을 때까지 반복
            while (availablePositions > 0)
            {
                int pos = availablePositions & -availablePositions; // 가장 오른쪽의 1비트를 추출 (놓을 수 있는 자리)
                availablePositions -= pos; // 해당 자리에 퀸을 놓았으므로, 그 자리를 제거
                // 다음 행으로 넘어가며 재귀 호출
                count += solve(row + 1, cols | pos, (diag1 | pos) << 1, (diag2 | pos) >> 1);
            }
            return count; // 가능한 배치 수 반환
        };

        return solve(0, 0, 0, 0); // 초기 상태로 백트래킹 시작
    }

    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()); // 사용자로부터 N 입력받기
        Console.WriteLine(NQueen(N)); // 가능한 퀸 배치 경우의 수 출력
    }
}
