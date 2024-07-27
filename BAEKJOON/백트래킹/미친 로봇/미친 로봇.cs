using System; // 기본 시스템 라이브러리를 포함
using System.Collections.Generic; // 컬렉션 라이브러리를 포함

class Program
{
    // 이동할 방향에 따른 좌표 변화 (동, 서, 남, 북)
    static readonly (int, int)[] directions = { (0, 1), (0, -1), (1, 0), (-1, 0) };
    static readonly double[] probs = new double[4]; // 동, 서, 남, 북 이동 확률을 저장할 배열

    static void Main()
    {
        // 입력 처리
        string[] inputs = Console.ReadLine().Split(); // 입력을 공백 기준으로 분리하여 배열에 저장
        int N = int.Parse(inputs[0]); // 첫 번째 입력을 정수로 변환하여 이동 횟수 N에 저장
        double east = double.Parse(inputs[1]); // 두 번째 입력을 실수로 변환하여 east에 저장
        double west = double.Parse(inputs[2]); // 세 번째 입력을 실수로 변환하여 west에 저장
        double south = double.Parse(inputs[3]); // 네 번째 입력을 실수로 변환하여 south에 저장
        double north = double.Parse(inputs[4]); // 다섯 번째 입력을 실수로 변환하여 north에 저장

        // 확률을 소수로 변환
        probs[0] = east / 100.0; // 동쪽으로 이동할 확률을 100으로 나누어 소수로 변환
        probs[1] = west / 100.0; // 서쪽으로 이동할 확률을 100으로 나누어 소수로 변환
        probs[2] = south / 100.0; // 남쪽으로 이동할 확률을 100으로 나누어 소수로 변환
        probs[3] = north / 100.0; // 북쪽으로 이동할 확률을 100으로 나누어 소수로 변환

        // 결과 계산 및 출력
        double result = SimplePathProbability(N); // 단순 경로로 이동할 확률을 계산하여 result에 저장
        Console.WriteLine($"{result:F10}"); // 결과를 소수점 10자리까지 출력
    }

    // 단순 경로로 이동할 확률을 계산하는 함수
    static double SimplePathProbability(int N)
    {
        var visited = new HashSet<(int, int)>(); // 방문한 좌표를 저장할 HashSet 초기화
        return Dfs(0, 0, N, visited); // DFS를 호출하여 단순 경로로 이동할 확률을 계산하여 반환
    }

    // 깊이 우선 탐색(DFS) 함수
    static double Dfs(int x, int y, int n, HashSet<(int, int)> visited)
    {
        if (n == 0)
        {
            // n번의 이동이 모두 완료된 경우, 단순 경로 하나를 찾은 것이므로 확률 1을 반환
            return 1.0;
        }
        // 현재 좌표를 방문한 좌표로 추가
        visited.Add((x, y));
        double prob = 0.0; // 단순 경로로 이동할 확률을 저장할 변수
        // 모든 방향에 대해 재귀적으로 이동 시도
        for (int i = 0; i < 4; i++)
        {
            int nx = x + directions[i].Item1; // 새로운 x 좌표
            int ny = y + directions[i].Item2; // 새로운 y 좌표
            if (!visited.Contains((nx, ny)))
            {
                // 다음 좌표가 아직 방문하지 않은 경우에만 이동
                prob += probs[i] * Dfs(nx, ny, n - 1, visited);
            }
        }
        // 현재 좌표를 방문한 좌표에서 제거 (백트래킹)
        visited.Remove((x, y));
        return prob; // 계산된 확률 반환
    }
}
