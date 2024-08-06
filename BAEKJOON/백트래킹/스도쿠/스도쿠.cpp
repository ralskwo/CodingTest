#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool is_valid(vector<vector<int>>& board, int row, int col, int num) {
    // 해당 행에 num이 있는지 확인
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) {
            return false;
        }
    }
    
    // 해당 열에 num이 있는지 확인
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == num) {
            return false;
        }
    }
    
    // 3x3 박스 내에 num이 있는지 확인
    int start_row = 3 * (row / 3);
    int start_col = 3 * (col / 3);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[start_row + i][start_col + j] == num) {
                return false;
            }
        }
    }
    
    // num을 놓을 수 있으면 true 반환
    return true;
}

bool backtrack(vector<vector<int>>& board, vector<pair<int, int>>& empty_cells, int index) {
    // 모든 빈 칸을 다 채웠다면 true 반환
    if (index == empty_cells.size()) {
        return true;
    }
    
    // 현재 빈 칸의 좌표 가져오기
    int row = empty_cells[index].first;
    int col = empty_cells[index].second;
    
    // 1부터 9까지의 숫자 시도
    for (int num = 1; num <= 9; num++) {
        if (is_valid(board, row, col, num)) {
            // 유효한 숫자라면 보드에 숫자 배치
            board[row][col] = num;
            
            // 다음 빈 칸으로 이동
            if (backtrack(board, empty_cells, index + 1)) {
                return true;
            }
            
            // 현재 숫자가 유효하지 않다면 다시 0으로 되돌림
            board[row][col] = 0;
        }
    }
    
    // 가능한 숫자가 없다면 false 반환
    return false;
}

bool solve_sudoku(vector<vector<int>>& board) {
    // 빈 칸들의 좌표를 리스트로 저장
    vector<pair<int, int>> empty_cells;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == 0) {
                empty_cells.push_back(make_pair(i, j));
            }
        }
    }
    
    // 백트래킹 시작
    return backtrack(board, empty_cells, 0);
}

void print_board(const vector<vector<int>>& board) {
    // 보드 출력
    for (const auto& row : board) {
        for (int num : row) {
            cout << num;
        }
        cout << endl;
    }
}

int main() {
    // 입력 받기
    string input;
    vector<vector<int>> board(9, vector<int>(9));
    
    for (int i = 0; i < 9; i++) {
        cin >> input;
        for (int j = 0; j < 9; j++) {
            board[i][j] = input[j] - '0';
        }
    }
    
    // 스도쿠 풀기
    solve_sudoku(board);
    
    // 결과 출력
    print_board(board);
    
    return 0;
}
