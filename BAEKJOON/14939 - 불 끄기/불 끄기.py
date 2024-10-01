def toggle(grid, x, y):
    # 상하좌우 및 현재 위치를 포함한 5개의 위치를 나타내는 이동 방향 배열 설정
    dx = [0, 0, -1, 1, 0]
    dy = [0, -1, 0, 0, 1]
    
    # 5개의 위치에 대해 순회하며 전구 상태를 반전시킴
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]  # 현재 위치에서의 이동된 좌표를 계산
        if 0 <= nx < 10 and 0 <= ny < 10:  # 좌표가 전구 배열의 범위 내에 있는지 확인
            # 전구 상태를 반전시킴 ('O'면 '#'으로, '#'이면 'O'로 변경)
            grid[nx][ny] = '#' if grid[nx][ny] == 'O' else 'O'

def all_off(grid):
    # 전구 배열의 모든 전구가 꺼져 있는지 확인하기 위해 10x10 배열을 순회
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'O':  # 켜진 전구가 하나라도 있으면 False 반환
                return False
    return True  # 모든 전구가 꺼져 있으면 True 반환

def solve(grid):
    import copy  # 배열의 깊은 복사를 위해 copy 모듈을 사용
    min_switches = float('inf')  # 최소 스위치 누르기 횟수를 무한대로 초기화
    
    # 첫 번째 줄의 모든 스위치 조합(2^10 = 1024가지)을 비트마스크로 표현하여 순회
    for case in range(1 << 10):
        switches = 0  # 현재 경우에 따른 스위치 누르기 횟수 초기화
        test_grid = copy.deepcopy(grid)  # 현재 상태를 복사하여 test_grid에 저장

        # 첫 번째 줄의 각 전구에 대해 스위치를 누를지 여부를 결정 (비트마스크를 통해 결정)
        for j in range(10):
            if case & (1 << j):  # case의 j번째 비트가 1인 경우 해당 전구를 누름
                toggle(test_grid, 0, j)  # 전구 상태 변경
                switches += 1  # 스위치 누른 횟수 증가

        # 첫 번째 줄을 기준으로 두 번째 줄부터 차례대로 전구 상태를 조정
        for i in range(1, 10):
            for j in range(10):
                if test_grid[i - 1][j] == 'O':  # 위쪽 전구가 켜져 있으면 현재 위치의 전구를 누름
                    toggle(test_grid, i, j)  # 전구 상태 변경
                    switches += 1  # 스위치 누른 횟수 증가

        # 모든 전구가 꺼진 상태인지 확인
        if all_off(test_grid):
            min_switches = min(min_switches, switches)  # 최소 스위치 누른 횟수 갱신

    # 최소 스위치 누른 횟수가 초기값 그대로면 불가능한 경우이므로 -1 반환
    return -1 if min_switches == float('inf') else min_switches

# 입력 받기: 10줄에 걸쳐 전구 배열의 상태를 입력으로 받음
grid = [list(input().strip()) for _ in range(10)]

# 문제 해결 및 결과 출력
print(solve(grid))
