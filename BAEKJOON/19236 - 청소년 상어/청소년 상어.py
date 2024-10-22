import copy  # 공간의 상태를 복사하기 위해 copy 모듈을 사용

# 8방향에 대한 이동 좌표 (↑, ↖, ←, ↙, ↓, ↘, →, ↗ 순서)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # x 좌표 변화량
dy = [0, -1, -1, -1, 0, 1, 1, 1]  # y 좌표 변화량

# 물고기를 이동시키는 함수
def move_fish(space, shark_x, shark_y):
    # 물고기 번호 1부터 16까지 순서대로 이동
    for i in range(1, 17):
        fish_x, fish_y = -1, -1  # 물고기의 현재 위치를 저장할 변수
        # 공간을 탐색하여 현재 물고기의 위치를 찾음
        for x in range(4):
            for y in range(4):
                if space[x][y][0] == i:
                    fish_x, fish_y = x, y
                    break
            if fish_x != -1:
                break
        
        # 물고기가 이미 먹혀서 공간에 없을 경우 건너뜀
        if fish_x == -1:
            continue
        
        fish_dir = space[fish_x][fish_y][1]  # 물고기의 현재 방향
        
        # 8방향을 시계 방향으로 회전하며 이동할 수 있는 위치를 찾음
        for _ in range(8):
            nx, ny = fish_x + dx[fish_dir], fish_y + dy[fish_dir]  # 이동할 위치 계산
            # 이동할 위치가 공간 안에 있고, 상어의 위치가 아닐 때 이동
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (shark_x, shark_y):
                # 이동할 수 있는 방향으로 물고기의 방향을 업데이트
                space[fish_x][fish_y][1] = fish_dir
                # 물고기가 이동할 위치에 있는 물고기와 위치를 바꿈
                space[fish_x][fish_y], space[nx][ny] = space[nx][ny], space[fish_x][fish_y]
                break
            # 이동할 수 없는 경우 45도 반시계 회전
            fish_dir = (fish_dir + 1) % 8

# 깊이 우선 탐색(DFS) 함수
def dfs(space, shark_x, shark_y, total):
    global answer  # 최댓값을 저장할 전역 변수
    space = copy.deepcopy(space)  # 공간의 상태를 복사하여 재귀 호출 간 상태 유지

    # 상어가 현재 위치의 물고기를 먹고 해당 물고기의 번호와 방향을 얻음
    number = space[shark_x][shark_y][0]
    direction = space[shark_x][shark_y][1]
    space[shark_x][shark_y][0] = -1  # 물고기를 먹은 자리를 빈칸으로 표시

    total += number  # 현재까지 먹은 물고기 번호의 합에 현재 물고기 번호를 추가
    answer = max(answer, total)  # 최댓값 갱신
    
    # 물고기 이동 처리
    move_fish(space, shark_x, shark_y)
    
    # 상어가 현재 방향으로 이동할 수 있는 모든 경우를 탐색
    for i in range(1, 4):  # 1, 2, 3 칸까지 이동 가능
        nx, ny = shark_x + dx[direction] * i, shark_y + dy[direction] * i  # 다음 위치 계산
        # 이동할 위치가 공간 내에 있고, 물고기가 있는 위치일 때만 이동
        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0] > 0:
            # 재귀적으로 상어를 이동시켜 새로운 상태에서 탐색 진행
            dfs(space, nx, ny, total)

# 4x4 공간을 초기화하고 입력을 받아 저장
space = [[] for _ in range(4)]  # 각 칸에 물고기의 번호와 방향 저장
for i in range(4):
    row = list(map(int, input().split()))  # 한 줄씩 입력받아 물고기 번호와 방향으로 분리
    for j in range(4):
        space[i].append([row[j*2], row[j*2+1]-1])  # 물고기 번호와 방향을 저장 (방향은 0부터 시작하도록 조정)

answer = 0  # 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 저장할 변수
dfs(space, 0, 0, 0)  # DFS 탐색 시작 (상어는 (0, 0)에서 시작)
print(answer)  # 최댓값 출력