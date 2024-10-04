#include <iostream>
#include <vector>
using namespace std;

// 상하좌우 이동을 위한 방향 벡터
int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int M, N;  // 지도 크기 M: 세로, N: 가로
vector<vector<int>> heights;  // 지도의 높이를 저장하는 2차원 벡터
vector<vector<int>> dp;  // DP 테이블: 각 지점에서 목적지까지 도달할 수 있는 경로의 수를 저장

// 깊이 우선 탐색(DFS) 함수
int dfs(int x, int y) {
    if (x == N - 1 && y == M - 1)  // 목적지에 도달했으면 경로의 수 1 반환
        return 1;

    if (dp[y][x] != -1)  // 이미 방문한 지점의 경로 수가 계산되었으면 해당 값을 반환
        return dp[y][x];

    dp[y][x] = 0;  // 현재 위치에서 가능한 경로 수를 0으로 초기화

    // 상하좌우 네 방향에 대해 탐색
    for (int i = 0; i < 4; i++) {
        int nx = x + directions[i][0];  // 다음 x 좌표
        int ny = y + directions[i][1];  // 다음 y 좌표

        // 다음 위치가 지도 범위 내에 있고, 현재 위치보다 높이가 낮은 지점인 경우
        if (nx >= 0 && nx < N && ny >= 0 && ny < M && heights[ny][nx] < heights[y][x]) {
            dp[y][x] += dfs(nx, ny);  // 다음 지점으로 이동하여 경로의 수 누적
        }
    }

    return dp[y][x];  // 계산된 현재 위치의 경로 수 반환
}

int main() {
    cin >> M >> N;  // 지도 크기 M과 N 입력받기

    heights = vector<vector<int>>(M, vector<int>(N));  // 지도의 높이를 저장할 2차원 벡터 초기화
    dp = vector<vector<int>>(M, vector<int>(N, -1));  // DP 테이블을 -1로 초기화

    // 지도 각 지점의 높이 입력받기
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> heights[i][j];
        }
    }

    // (0, 0) 지점에서 DFS 탐색 시작하여 가능한 경로의 수 계산
    cout << dfs(0, 0) << endl;

    return 0;
}
