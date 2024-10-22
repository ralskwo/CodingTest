#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 8방향 정의 (↑, ↖, ←, ↙, ↓, ↘, →, ↗)
int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, -1, -1, -1, 0, 1, 1, 1};

// 물고기 구조체 정의
struct Fish {
    int num, dir;
    bool alive;
};

int answer = 0; // 최종 결과를 저장할 전역 변수

// 물고기 이동 함수
void moveFish(vector<vector<Fish>>& space, int shark_x, int shark_y) {
    for (int i = 1; i <= 16; i++) { // 1번부터 16번 물고기까지 순서대로 이동
        int fish_x = -1, fish_y = -1;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                if (space[x][y].num == i && space[x][y].alive) {
                    fish_x = x;
                    fish_y = y;
                    break;
                }
            }
            if (fish_x != -1) break;
        }
        
        if (fish_x == -1) continue; // 해당 번호의 물고기가 없으면 다음 물고기로
        
        int dir = space[fish_x][fish_y].dir;
        for (int d = 0; d < 8; d++) { // 최대 8번 방향을 바꿔가며 이동 가능한 칸 찾기
            int nx = fish_x + dx[dir];
            int ny = fish_y + dy[dir];
            if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4 && !(nx == shark_x && ny == shark_y)) {
                // 물고기 위치 교환
                swap(space[fish_x][fish_y], space[nx][ny]);
                space[nx][ny].dir = dir;
                break;
            }
            dir = (dir + 1) % 8; // 45도 반시계 회전
        }
    }
}

// DFS 함수
void dfs(vector<vector<Fish>> space, int shark_x, int shark_y, int total) {
    // 현재 위치의 물고기를 먹음
    total += space[shark_x][shark_y].num;
    int shark_dir = space[shark_x][shark_y].dir;
    space[shark_x][shark_y].alive = false;
    
    answer = max(answer, total); // 최대값 갱신
    
    // 물고기 이동
    moveFish(space, shark_x, shark_y);
    
    // 상어 이동
    for (int i = 1; i < 4; i++) {
        int nx = shark_x + dx[shark_dir] * i;
        int ny = shark_y + dy[shark_dir] * i;
        if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4 && space[nx][ny].alive) {
            dfs(space, nx, ny, total);
        }
    }
}

int main() {
    vector<vector<Fish>> space(4, vector<Fish>(4));
    
    // 입력 받기
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int num, dir;
            cin >> num >> dir;
            space[i][j] = {num, dir - 1, true};
        }
    }
    
    dfs(space, 0, 0, 0); // DFS 시작
    
    cout << answer << endl; // 결과 출력
    
    return 0;
}