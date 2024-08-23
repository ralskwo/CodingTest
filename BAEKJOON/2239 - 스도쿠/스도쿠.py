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
