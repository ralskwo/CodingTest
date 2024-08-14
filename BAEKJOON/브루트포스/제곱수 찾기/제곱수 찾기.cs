using System;

class Program
{
    // 숫자가 완전 제곱수인지 확인하는 함수입니다.
    static bool IsPerfectSquare(long num)
    {
        if (num < 0) return false; // 음수는 완전 제곱수가 될 수 없으므로 false를 반환합니다.
        long root = (long)Math.Sqrt(num); // num의 제곱근을 계산하고 정수로 변환합니다.
        return root * root == num; // 제곱근의 제곱이 num과 같으면 완전 제곱수이므로 true를 반환합니다.
    }

    static void Main(string[] args)
    {
        // N과 M을 입력받고 정수로 변환합니다.
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);

        // 표의 각 행을 입력받아 배열로 저장합니다.
        string[] table = new string[N];
        for (int i = 0; i < N; i++)
        {
            table[i] = Console.ReadLine();
        }

        long maxSquare = -1; // 최대 완전 제곱수를 저장할 변수를 초기화합니다.

        // 모든 행에 대해 반복합니다.
        for (int i = 0; i < N; i++)
        {
            // 모든 열에 대해 반복합니다.
            for (int j = 0; j < M; j++)
            {
                // 행 방향으로 가능한 모든 이동 거리를 설정합니다.
                for (int di = -N; di < N; di++)
                {
                    // 열 방향으로 가능한 모든 이동 거리를 설정합니다.
                    for (int dj = -M; dj < M; dj++)
                    {
                        if (di == 0 && dj == 0) continue; // 이동 거리가 0,0이면 숫자를 만들 수 없으므로 건너뜁니다.

                        int x = i, y = j; // 시작 위치를 현재 위치로 설정합니다.
                        string numStr = ""; // 숫자를 이어 붙일 문자열 변수를 초기화합니다.

                        // 위치가 유효한 범위 내에 있는 동안 반복합니다.
                        while (x >= 0 && x < N && y >= 0 && y < M)
                        {
                            numStr += table[x][y]; // 현재 위치의 숫자를 numStr에 추가합니다.
                            long num = long.Parse(numStr); // numStr을 정수로 변환합니다.
                            if (IsPerfectSquare(num)) // num이 완전 제곱수인지 확인합니다.
                            {
                                maxSquare = Math.Max(maxSquare, num); // 현재까지의 최대 완전 제곱수와 비교해 더 큰 값을 저장합니다.
                            }
                            x += di; // 행 방향으로 이동합니다.
                            y += dj; // 열 방향으로 이동합니다.
                        }
                    }
                }
            }
        }

        Console.WriteLine(maxSquare); // 찾은 최대 완전 제곱수를 출력합니다. 만약 완전 제곱수를 찾지 못했다면 -1이 출력됩니다.
    }
}
