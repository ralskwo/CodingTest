import copy  # 사무실 상태를 복사하기 위한 copy 모듈을 임포트

# CCTV가 감시할 수 있는 방향을 나타내는 리스트 (우, 하, 좌, 상 순서)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 각 CCTV 번호에 따라 감시할 수 있는 방향 설정
# 예를 들어 1번 CCTV는 한 방향만, 5번 CCTV는 네 방향 모두 감시 가능
cctv_directions = [
    [],  # 0번 인덱스는 사용하지 않음
    [[0], [1], [2], [3]],  # 1번 CCTV는 4가지 방향 (우, 하, 좌, 상)
    [[0, 2], [1, 3]],  # 2번 CCTV는 반대 방향 (우-좌, 하-상)
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV는 직각 방향 (우-하, 하-좌 등)
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV는 세 방향
    [[0, 1, 2, 3]]  # 5번 CCTV는 네 방향 모두 감시
]

# CCTV가 주어진 방향을 따라 감시할 수 있는 영역을 표시하는 함수
def watch(x, y, directions, office):
    n = len(office)  # 사무실의 세로 크기
    m = len(office[0])  # 사무실의 가로 크기
    for d in directions:  # 감시할 방향들을 반복
        nx, ny = x, y  # CCTV의 시작 위치
        while True:  # 주어진 방향으로 감시를 계속 진행
            nx += dx[d]  # 다음 x 위치 (현재 위치에서 방향에 따른 이동)
            ny += dy[d]  # 다음 y 위치 (현재 위치에서 방향에 따른 이동)
            if not (0 <= nx < n and 0 <= ny < m):  # 범위를 벗어나면 중단
                break
            if office[nx][ny] == 6:  # 벽(6)을 만나면 중단
                break
            if office[nx][ny] == 0:  # 빈 칸(0)을 만나면 감시 처리
                office[nx][ny] = '#'  # 감시된 구역은 '#'으로 표시

# 현재 사무실 상태에서 사각지대(감시되지 않은 영역)의 크기를 계산하는 함수
def calculate_blind_spot(office):
    count = 0  # 사각지대 카운트를 0으로 초기화
    for row in office:  # 사무실의 각 행에 대해 반복
        count += row.count(0)  # 각 행에서 감시되지 않은 빈 칸(0)의 개수를 셈
    return count  # 사각지대의 총 개수를 반환

# 백트래킹을 통해 모든 CCTV 방향을 조합하여 탐색하는 함수
def dfs(depth, office):
    global min_blind_spot  # 전역 변수로 최소 사각지대를 저장
    if depth == len(cctvs):  # 모든 CCTV에 대한 방향을 설정 완료한 경우
        min_blind_spot = min(min_blind_spot, calculate_blind_spot(office))  # 최소 사각지대 갱신
        return
    
    x, y, cctv_type = cctvs[depth]  # 현재 탐색 중인 CCTV의 좌표와 타입
    for directions in cctv_directions[cctv_type]:  # CCTV가 가질 수 있는 모든 방향에 대해 반복
        new_office = copy.deepcopy(office)  # 현재 사무실 상태를 복사 (원본 손상 방지)
        watch(x, y, directions, new_office)  # CCTV가 해당 방향으로 감시
        dfs(depth + 1, new_office)  # 다음 CCTV에 대해 재귀적으로 탐색

# 입력 처리
n, m = map(int, input().split())  # 사무실의 크기(N, M) 입력
office = []  # 사무실 상태를 저장할 리스트
cctvs = []  # CCTV의 좌표와 타입을 저장할 리스트

# 사무실의 상태를 입력받으면서 CCTV의 위치와 타입을 기록
for i in range(n):
    row = list(map(int, input().split()))  # 각 행을 입력받음
    office.append(row)  # 사무실 상태를 리스트에 추가
    for j in range(m):
        if 1 <= row[j] <= 5:  # CCTV가 있으면
            cctvs.append((i, j, row[j]))  # CCTV의 위치와 타입을 리스트에 저장

min_blind_spot = float('inf')  # 최소 사각지대를 매우 큰 값으로 초기화

dfs(0, office)  # 백트래킹 시작

print(min_blind_spot)  # 최소 사각지대 출력
