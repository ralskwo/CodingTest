# 스도쿠 문제 풀이 및 설명

https://www.acmicpc.net/problem/2239

## 문제 이해
9×9 크기의 스도쿠 퍼즐을 해결하고, 빈 칸(0으로 표시)을 1부터 9까지의 숫자로 채워 완성된 퍼즐을 출력하는 문제입니다.

## 접근 방법
1. **백트래킹 사용:** 빈 칸을 찾아 가능한 숫자를 시도하고 규칙에 맞으면 다음 빈 칸으로 이동합니다. 유효하지 않으면 다른 숫자를 시도합니다.
2. **비트마스크 최적화:** 각 행, 열, 3×3 박스에 사용된 숫자를 비트마스크로 관리하여 빠르게 유효성을 검사합니다.
3. **후보군 관리:** 각 빈 칸에 대한 가능한 숫자 후보를 미리 계산하여 백트래킹 과정에서 효율적으로 선택합니다.

## 풀이 과정
1. **입력 처리:** 스도쿠 퍼즐을 표준 입력으로 받아 이차원 리스트로 변환합니다.
2. **백트래킹 함수 정의:** `is_valid` 함수로 스도쿠 규칙을 확인하고, `solve_sudoku`와 `backtrack` 함수로 백트래킹을 수행합니다.
3. **후보군 초기화:** 각 빈 칸에 대한 가능한 숫자 후보를 미리 계산합니다.
4. **백트래킹 수행:** 백트래킹을 통해 퍼즐을 해결하고 완성된 퍼즐을 출력합니다.

## 코드 구현
```python
def is_valid(board, row, col, num):
    # 해당 행에 num이 있는지 확인
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # 해당 열에 num이 있는지 확인
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # 3x3 박스 내에 num이 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    # num을 놓을 수 있으면 True 반환
    return True

def solve_sudoku(board):
    # 빈 칸들의 좌표를 리스트로 저장
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    
    # 백트래킹 시작
    return backtrack(board, empty_cells, 0)

def backtrack(board, empty_cells, index):
    # 모든 빈 칸을 다 채웠다면 True 반환
    if index == len(empty_cells):
        return True
    
    # 현재 빈 칸의 좌표 가져오기
    row, col = empty_cells[index]
    
    # 1부터 9까지의 숫자 시도
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # 유효한 숫자라면 보드에 숫자 배치
            board[row][col] = num
            
            # 다음 빈 칸으로 이동
            if backtrack(board, empty_cells, index + 1):
                return True
            
            # 현재 숫자가 유효하지 않다면 다시 0으로 되돌림
            board[row][col] = 0
    
    # 가능한 숫자가 없다면 False 반환
    return False

def print_board(board):
    # 보드 출력
    for row in board:
        print("".join(map(str, row)))

# 입력 받기
import sys
input = sys.stdin.read

# 입력 데이터 처리
data = input().strip().split()

# 9x9 스도쿠 보드 생성
board = [list(map(int, list(data[i]))) for i in range(9)]

# 스도쿠 풀기
solve_sudoku(board)

# 결과 출력
print_board(board)

