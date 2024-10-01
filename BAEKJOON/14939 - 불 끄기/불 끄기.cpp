#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// 10x10 크기의 전구 배열과 전구 상태 변경을 위한 좌표 변화를 정의합니다.
int dx[5] = {0, 0, -1, 1, 0};
int dy[5] = {0, -1, 0, 0, 1};

// 특정 위치의 전구와 상하좌우의 전구 상태를 반전시키는 함수
void toggle(vector<vector<char>>& grid, int x, int y) {
    for (int i = 0; i < 5; ++i) {  // 5개의 방향을 순회 (현재 위치와 상하좌우)
        int nx = x + dx[i];  // 현재 x 좌표에 이동 값을 더하여 새로운 x 좌표 계산
        int ny = y + dy[i];  // 현재 y 좌표에 이동 값을 더하여 새로운 y 좌표 계산
        if (nx >= 0 && nx < 10 && ny >= 0 && ny < 10) {  // 범위 체크
            // 현재 전구의 상태를 반전 ('#' -> 'O', 'O' -> '#')
            grid[nx][ny] = (grid[nx][ny] == 'O') ? '#' : 'O';
        }
    }
}

// 모든 전구가 꺼져 있는지 확인하는 함수
bool all_off(vector<vector<char>>& grid) {
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            if (grid[i][j] == 'O') {  // 켜져 있는 전구가 하나라도 있으면 false 반환
                return false;
            }
        }
    }
    return true;  // 모든 전구가 꺼져 있으면 true 반환
}

// 문제를 해결하는 함수
int solve(vector<vector<char>>& grid) {
    int min_switches = INT_MAX;  // 최소 스위치 횟수를 무한대로 초기화

    // 첫 번째 줄의 모든 경우의 수를 순회 (2^10 = 1024가지)
    for (int case_num = 0; case_num < (1 << 10); ++case_num) {
        vector<vector<char>> test_grid = grid;  // 현재 상태를 복사하여 사용
        int switches = 0;  // 현재 스위치 누른 횟수 초기화

        // 첫 번째 줄의 각 전구에 대해 스위치를 누를지 결정
        for (int j = 0; j < 10; ++j) {
            if (case_num & (1 << j)) {  // case_num의 j번째 비트가 1이면 스위치를 누름
                toggle(test_grid, 0, j);
                ++switches;
            }
        }

        // 두 번째 줄부터 전구 상태를 조정
        for (int i = 1; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                if (test_grid[i - 1][j] == 'O') {  // 위쪽 전구가 켜져 있으면 스위치를 누름
                    toggle(test_grid, i, j);
                    ++switches;
                }
            }
        }

        // 모든 전구가 꺼진 경우 최소 스위치 횟수를 갱신
        if (all_off(test_grid)) {
            min_switches = min(min_switches, switches);
        }
    }

    // 모든 전구를 끌 수 없으면 -1, 아니면 최소 스위치 횟수를 반환
    return (min_switches == INT_MAX) ? -1 : min_switches;
}

int main() {
    vector<vector<char>> grid(10, vector<char>(10));  // 10x10 크기의 전구 배열

    // 전구 배열의 초기 상태 입력 받기
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            cin >> grid[i][j];
        }
    }

    // 문제 해결 및 결과 출력
    cout << solve(grid) << endl;

    return 0;
}
