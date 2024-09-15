#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 종이의 크기를 저장할 변수
int N, M;
// 종이에 쓰인 수를 저장할 2차원 벡터
vector<vector<int>> paper;
// 방문 여부를 체크할 2차원 벡터
vector<vector<bool>> visited;
// 테트로미노의 최대 합을 저장할 변수
int max_sum = 0;

// 이동 방향을 나타내는 배열 (상, 하, 좌, 우)
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// DFS를 이용하여 가능한 테트로미노 모양을 탐색하는 함수
void dfs(int x, int y, int depth, int total) {
    // 깊이가 4가 되면 테트로미노가 완성된 것이므로 최대 합을 갱신
    if (depth == 4) {
        max_sum = max(max_sum, total);
        return;
    }

    // 4방향으로 이동하며 테트로미노의 다음 칸을 탐색
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        // 종이의 경계 안에 있고 아직 방문하지 않은 칸이라면
        if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny]) {
            // 해당 칸을 방문 표시하고 DFS로 재귀 호출
            visited[nx][ny] = true;
            dfs(nx, ny, depth + 1, total + paper[nx][ny]);
            // 탐색이 끝나면 방문 표시를 해제하여 다음 탐색에 영향을 주지 않도록 함
            visited[nx][ny] = false;
        }
    }
}

// 'ㅗ' 모양 테트로미노를 처리하는 함수
void check_special_shape(int x, int y) {
    // 'ㅗ' 모양을 중심으로 상하좌우 4방향 중 3방향을 선택하여 모양을 만듦
    for (int i = 0; i < 4; i++) {
        int total = paper[x][y];
        // 3개의 방향을 선택하여 'ㅗ' 모양을 만듦
        for (int j = 0; j < 3; j++) {
            int k = (i + j) % 4;
            int nx = x + dx[k];
            int ny = y + dy[k];
            // 선택한 방향이 종이의 경계를 벗어나면 현재 모양은 무시
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                total = -1;
                break;
            }
            total += paper[nx][ny];
        }
        // 'ㅗ' 모양이 완성되면 최대 합을 갱신
        max_sum = max(max_sum, total);
    }
}

int main() {
    // 종이의 크기 입력
    cin >> N >> M;
    // 종이에 쓰여 있는 수를 저장할 공간 할당
    paper.assign(N, vector<int>(M));
    visited.assign(N, vector<bool>(M, false));

    // 종이에 쓰여 있는 수 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> paper[i][j];
        }
    }

    // 각 칸을 테트로미노의 시작점으로 설정하여 가능한 모든 테트로미노 모양을 탐색
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            // 현재 칸을 방문 표시하고 DFS를 시작
            visited[i][j] = true;
            dfs(i, j, 1, paper[i][j]);
            // DFS 탐색이 끝나면 방문 표시를 해제
            visited[i][j] = false;

            // 'ㅗ' 모양은 DFS로 처리할 수 없으므로 따로 처리
            check_special_shape(i, j);
        }
    }

    // 최종적으로 찾은 테트로미노의 최대 합을 출력
    cout << max_sum << endl;

    return 0;
}
