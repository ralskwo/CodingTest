using System;

class RobotCleaner
{
    static void Main()
    {
        // 방의 크기 N과 M을 입력받음
        string[] nm = Console.ReadLine().Split();
        int N = int.Parse(nm[0]);
        int M = int.Parse(nm[1]);

        // 로봇 청소기의 초기 위치 (r, c)와 방향 d를 입력받음
        string[] rcd = Console.ReadLine().Split();
        int r = int.Parse(rcd[0]);
        int c = int.Parse(rcd[1]);
        int d = int.Parse(rcd[2]);

        // 방의 상태를 저장할 2차원 배열
        int[,] room = new int[N, M];

        // 방의 상태를 입력받음
        for (int i = 0; i < N; i++)
        {
            string[] line = Console.ReadLine().Split();
            for (int j = 0; j < M; j++)
            {
                room[i, j] = int.Parse(line[j]);
            }
        }

        // 로봇이 이동할 때 사용할 방향 벡터 정의: 북, 동, 남, 서
        int[,] directions = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

        // 청소한 칸의 수를 저장할 변수 초기화
        int cleanedCount = 0;

        // 로봇 청소기의 동작을 무한 루프를 통해 시뮬레이션
        while (true)
        {
            // 현재 칸이 청소되지 않은 경우, 청소함
            if (room[r, c] == 0)
            {
                room[r, c] = 2; // 청소한 칸은 2로 표시
                cleanedCount++; // 청소한 칸의 수를 증가시킴
            }

            // 주변 4칸 중 청소할 수 있는 칸이 있는지 확인하기 위한 플래그
            bool hasCleanableAdjacent = false;

            // 4방향을 모두 확인
            for (int i = 0; i < 4; i++)
            {
                // 현재 방향에서 반시계 방향으로 90도 회전
                d = (d + 3) % 4;

                // 회전 후 이동할 위치 계산
                int nr = r + directions[d, 0];
                int nc = c + directions[d, 1];

                // 이동할 위치가 청소되지 않은 빈 칸인 경우
                if (room[nr, nc] == 0)
                {
                    // 그 방향으로 한 칸 전진
                    r = nr;
                    c = nc;

                    // 청소할 수 있는 칸이 있음을 표시
                    hasCleanableAdjacent = true;

                    // 한 칸 전진했으므로 다음 동작을 위해 반복문 종료
                    break;
                }
            }

            // 4방향 모두 확인했는데 청소할 수 있는 인접 칸이 없는 경우
            if (!hasCleanableAdjacent)
            {
                // 바라보는 방향을 유지한 채로 후진할 위치 계산
                int backD = (d + 2) % 4;
                int backR = r + directions[backD, 0];
                int backC = c + directions[backD, 1];

                // 후진할 위치가 벽이 아닌 경우
                if (room[backR, backC] != 1)
                {
                    // 후진함
                    r = backR;
                    c = backC;
                }
                else
                {
                    // 후진할 수 없는 경우 작동 멈춤
                    break;
                }
            }
        }

        // 로봇 청소기가 청소한 칸의 수를 출력
        Console.WriteLine(cleanedCount);
    }
}
