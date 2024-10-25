def is_valid_sudoku(sudoku):
    # 행 검사
    for row in sudoku:
        if len(set(row)) != 9:
            return 0
    
    # 열 검사
    for col in range(9):
        column = [sudoku[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return 0
    
    # 3x3 격자 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for x in range(3):
                for y in range(3):
                    block.append(sudoku[i+x][j+y])
            if len(set(block)) != 9:
                return 0

    # 모든 검사를 통과한 경우
    return 1

# 테스트 케이스 처리
T = int(input())
for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = is_valid_sudoku(sudoku)
    print(f"#{t} {result}")