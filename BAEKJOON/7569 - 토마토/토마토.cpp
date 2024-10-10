#include <iostream>   // 표준 입출력 사용
#include <queue>      // BFS 탐색을 위한 큐 사용
#include <tuple>      // 여러 값의 그룹화를 위한 튜플 사용
using namespace std;

int M, N, H;            // 상자의 가로, 세로, 높이 크기
int box[100][100][100]; // 최대 크기의 3차원 배열 선언
int directions[6][3] = { {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1} }; // 6방향 탐색

// BFS 탐색을 위한 큐 선언 (층, 행, 열, 경과 일수)
queue<tuple<int, int, int, int>> q;

int main() {
    cin >> M >> N >> H;  // 상자의 가로, 세로, 높이 크기 입력
    int total_tomatoes = 0; // 전체 토마토 개수
    int ripe_tomatoes = 0;  // 익은 토마토 개수
    int result = 0;         // 최종 최소 일수

    // 3차원 배열 입력 받기 및 초기 큐 설정
    for (int h = 0; h < H; h++) {
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                cin >> box[h][n][m]; // 현재 칸의 상태 입력 받기
                if (box[h][n][m] == 1) { // 익은 토마토인 경우
                    q.push(make_tuple(h, n, m, 0)); // 큐에 현재 위치와 일수 0을 추가
                    ripe_tomatoes++; // 익은 토마토 개수 증가
                }
                if (box[h][n][m] != -1) total_tomatoes++; // 빈 칸이 아닌 경우 전체 토마토 개수 증가
            }
        }
    }

    // 처음부터 모든 토마토가 익어있는 경우
    if (ripe_tomatoes == total_tomatoes) {
        cout << 0 << endl; // 0 출력 후 프로그램 종료
        return 0;
    }

    // BFS 탐색 시작
    while (!q.empty()) {
        int z, x, y, days;
        tie(z, x, y, days) = q.front(); // 큐의 맨 앞 요소를 꺼내기
        q.pop(); // 큐에서 꺼낸 요소 제거

        // 6방향으로 탐색
        for (int i = 0; i < 6; i++) {
            int nz = z + directions[i][0];
            int nx = x + directions[i][1];
            int ny = y + directions[i][2];

            // 새로운 위치가 범위 내에 있고, 익지 않은 토마토가 있는 경우
            if (nz >= 0 && nz < H && nx >= 0 && nx < N && ny >= 0 && ny < M && box[nz][nx][ny] == 0) {
                box[nz][nx][ny] = 1; // 익은 토마토로 변경
                q.push(make_tuple(nz, nx, ny, days + 1)); // 큐에 추가하고 일수 증가
                result = days + 1; // 현재까지의 최소 일수를 결과에 저장
            }
        }
    }

    // 익지 않은 토마토가 남아 있는지 확인
    for (int h = 0; h < H; h++) {
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                if (box[h][n][m] == 0) { // 익지 않은 토마토가 남아있다면
                    cout << -1 << endl; // -1 출력 후 종료
                    return 0;
                }
            }
        }
    }

    // 모든 토마토가 익은 경우 최소 일수 출력
    cout << result << endl;
    return 0;
}
