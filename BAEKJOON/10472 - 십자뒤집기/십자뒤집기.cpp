#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

// 주어진 좌표 (x, y)를 클릭했을 때 보드를 반전시키는 함수
void flip(vector<vector<char>>& board, int x, int y) {
    // 현재 위치 (0, 0)과 상하좌우 위치를 표현하는 (dx, dy) 쌍을 배열로 정의
    int dx[] = {0, 1, -1, 0, 0};
    int dy[] = {0, 0, 0, 1, -1};
    
    // 5개의 위치를 순회하며 보드를 반전
    for (int i = 0; i < 5; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
            board[nx][ny] = (board[nx][ny] == '*') ? '.' : '*';
        }
    }
}

// 모든 가능한 클릭 조합을 시도하여 최소 클릭 수를 찾는 함수
int min_clicks_to_all_white(vector<vector<char>> board) {
    int min_clicks = INT_MAX;

    // 3x3 보드의 각 칸에 대해 클릭할지 말지의 모든 조합을 생성 (0부터 511까지의 숫자를 이진수로 표현)
    for (int clicks = 0; clicks < (1 << 9); ++clicks) {
        vector<vector<char>> temp_board = board; // 현재 보드를 복사
        int click_count = 0;

        // 클릭 조합을 적용
        for (int idx = 0; idx < 9; ++idx) {
            if (clicks & (1 << idx)) { // 해당 칸을 클릭하는 경우
                int x = idx / 3;
                int y = idx % 3;
                flip(temp_board, x, y); // 해당 좌표를 클릭하여 보드를 반전시킴
                click_count++;
            }
        }

        // 모든 칸이 흰색인지 확인
        bool all_white = true;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (temp_board[i][j] == '*') {
                    all_white = false;
                    break;
                }
            }
            if (!all_white) break;
        }

        // 현재 클릭 조합이 최소 클릭 수인지 확인하고 갱신
        if (all_white) {
            min_clicks = min(min_clicks, click_count);
        }
    }

    return min_clicks; // 최소 클릭 수를 반환
}

int main() {
    int P;
    cin >> P; // 테스트 케이스 수 입력
    vector<int> results; // 결과를 저장할 벡터

    for (int p = 0; p < P; ++p) {
        vector<vector<char>> board(3, vector<char>(3));
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                cin >> board[i][j]; // 보드 입력
            }
        }
        results.push_back(min_clicks_to_all_white(board)); // 최소 클릭 수를 계산하여 결과에 추가
    }

    // 결과 출력
    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}
