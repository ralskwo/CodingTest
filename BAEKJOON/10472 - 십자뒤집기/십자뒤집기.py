def flip(board, x, y):
    # 주어진 좌표 (x, y)를 클릭했을 때 보드를 반전시키는 함수
    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        # 현재 위치 (0, 0)과 상하좌우 위치를 표현하는 (dx, dy) 쌍을 순회
        nx, ny = x + dx, y + dy
        # 새로운 좌표 (nx, ny)가 보드의 범위 안에 있는지 확인
        if 0 <= nx < 3 and 0 <= ny < 3:
            # 해당 좌표의 색상을 반전 ('*'는 '.'로, '.'는 '*'로)
            board[nx][ny] = '*' if board[nx][ny] == '.' else '.'

def min_clicks_to_all_white(board):
    from itertools import product  # 모든 조합을 생성하기 위해 itertools 모듈에서 product를 가져옴
    
    min_clicks = float('inf')  # 최소 클릭 수를 큰 값으로 초기화 (무한대)
    
    # 3x3 보드의 각 칸에 대해 클릭할지 말지의 모든 조합을 생성
    for clicks in product([0, 1], repeat=9):
        temp_board = [row[:] for row in board]  # 현재 보드를 복사
        click_count = 0  # 현재 조합의 클릭 횟수를 초기화
        
        # 클릭 조합을 적용
        for idx, click in enumerate(clicks):
            # 클릭하는 경우
            if click:
                x, y = divmod(idx, 3)  # idx를 3으로 나눈 몫과 나머지를 좌표로 변환
                flip(temp_board, x, y)  # 해당 좌표를 클릭하여 보드를 반전시킴
                click_count += 1  # 클릭 횟수 증가
        
        # 모든 칸이 흰색인지 확인
        if all(temp_board[i][j] == '.' for i in range(3) for j in range(3)):
            # 현재 클릭 조합이 최소 클릭 수인지 확인하고 갱신
            min_clicks = min(min_clicks, click_count)
    
    return min_clicks  # 최소 클릭 수를 반환

# 입력 처리
import sys
input = sys.stdin.read  # 표준 입력을 읽어옴
data = input().split()  # 입력 데이터를 공백을 기준으로 분할

P = int(data[0])  # 첫 번째 줄은 테스트 케이스 수 P

results = []  # 결과를 저장할 리스트
index = 1  # 데이터의 현재 위치 인덱스 (첫 번째 테스트 케이스 시작 위치)
for _ in range(P):
    # 보드를 입력 데이터에서 추출
    board = [list(data[index]), list(data[index + 1]), list(data[index + 2])]
    index += 3  # 다음 테스트 케이스로 인덱스를 이동
    results.append(min_clicks_to_all_white(board))  # 최소 클릭 수를 계산하여 결과에 추가

# 결과 출력
for result in results:
    print(result)  # 각 테스트 케이스의 결과를 출력
