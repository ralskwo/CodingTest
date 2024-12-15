using System;

class Program {
    const int MAX = 500; // 대나무 숲의 최대 크기
    static int n; // 대나무 숲의 크기
    static int[,] forest = new int[MAX, MAX]; // 대나무 숲 정보를 저장하는 배열
    static int[,] dp = new int[MAX, MAX]; // 각 지점에서 판다가 이동할 수 있는 최대 칸 수를 저장
    static int[] dx = { -1, 1, 0, 0 }; // 상하좌우 방향 탐색을 위한 x 변화량
    static int[] dy = { 0, 0, -1, 1 }; // 상하좌우 방향 탐색을 위한 y 변화량

    static int DFS(int x, int y) {
        if (dp[x, y] != -1) // 이미 계산된 값이 있으면 그 값을 반환
            return dp[x, y];

        dp[x, y] = 1; // 초기값 설정 (현재 칸은 최소 1칸 이동 가능)

        for (int i = 0; i < 4; i++) { // 네 방향 탐색
            int nx = x + dx[i]; // 새로운 x 좌표
            int ny = y + dy[i]; // 새로운 y 좌표

            // 범위를 벗어나지 않고, 다음 칸의 대나무 양이 현재 칸보다 많은 경우
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && forest[nx, ny] > forest[x, y]) {
                dp[x, y] = Math.Max(dp[x, y], 1 + DFS(nx, ny)); // 최대 이동 칸 수 갱신
            }
        }

        return dp[x, y]; // 계산된 값 반환
    }

    static void Main(string[] args) {
        n = int.Parse(Console.ReadLine()); // 대나무 숲의 크기 입력
        for (int i = 0; i < n; i++) { // 대나무 숲 정보 입력
            string[] line = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; j++) {
                forest[i, j] = int.Parse(line[j]);
                dp[i, j] = -1; // DP 배열 초기화 (-1은 아직 탐색되지 않은 상태)
            }
        }

        int result = 0; // 최댓값 저장 변수
        for (int i = 0; i < n; i++) { // 모든 칸을 순회하며 DFS 호출
            for (int j = 0; j < n; j++) {
                result = Math.Max(result, DFS(i, j)); // 최댓값 갱신
            }
        }

        Console.WriteLine(result); // 결과 출력
    }
}
