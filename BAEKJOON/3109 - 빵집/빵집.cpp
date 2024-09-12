#include <iostream>
#include <vector>

using namespace std;

int R, C;  // 격자의 행과 열 크기
vector<string> grid;  // 빵집 근처의 격자 상태 저장
vector<vector<bool>> visited;  // 각 칸의 방문 여부 저장
int dx[3] = {-1, 0, 1};  // 이동할 수 있는 세 방향: 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선
int dy[3] = {1, 1, 1};   // 세 방향 모두 오른쪽으로 이동

// 깊이 우선 탐색(DFS) 함수
bool dfs(int x, int y) {
    if (y == C - 1)  // 마지막 열에 도착했으면 파이프 설치 성공
        return true;
    
    // 세 방향으로 이동
    for (int i = 0; i < 3; ++i) {
        int nx = x + dx[i];  // 새로운 x 좌표 계산
        int ny = y + dy[i];  // 새로운 y 좌표 계산
        
        // 새로운 좌표가 격자 범위 내에 있고, 빈 칸이며, 아직 방문하지 않았을 때
        if (nx >= 0 && nx < R && ny < C && grid[nx][ny] == '.' && !visited[nx][ny]) {
            visited[nx][ny] = true;  // 해당 칸을 방문한 것으로 표시
            if (dfs(nx, ny))  // 재귀적으로 다음 칸으로 이동
                return true;  // 경로가 성공적으로 연결되면 true 반환
        }
    }
    
    return false;  // 세 방향 모두 경로를 찾지 못하면 false 반환
}

int main() {
    cin >> R >> C;  // 격자의 크기를 입력받음
    grid.resize(R);  // 격자의 각 행을 저장할 벡터 크기 설정
    visited.resize(R, vector<bool>(C, false));  // 방문 여부 벡터 초기화

    // 격자의 상태 입력
    for (int i = 0; i < R; ++i) {
        cin >> grid[i];
    }

    int pipeline_count = 0;  // 설치된 파이프라인의 개수

    // 첫 번째 열의 각 행에서 파이프 설치 시도
    for (int i = 0; i < R; ++i) {
        if (grid[i][0] == '.') {  // 첫 번째 열의 빈 칸에서만 시도
            if (dfs(i, 0))  // 해당 행에서 파이프 경로를 찾으면
                pipeline_count++;  // 파이프 설치 개수 증가
        }
    }

    cout << pipeline_count << endl;  // 최종적으로 설치된 파이프의 개수 출력

    return 0;
}
