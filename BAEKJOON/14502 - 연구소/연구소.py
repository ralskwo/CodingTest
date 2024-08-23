from itertools import combinations  # 조합을 구하기 위해 itertools의 combinations 함수 임포트
from collections import deque  # BFS 구현을 위해 deque를 임포트
import copy  # 연구소 상태를 깊은 복사하기 위해 copy 모듈 임포트

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 x축 방향 벡터
dy = [0, 0, -1, 1]  # 상하좌우 이동을 위한 y축 방향 벡터

def spread_virus(lab, viruses):  # 바이러스 확산 함수
    queue = deque(viruses)  # 바이러스 위치를 큐에 삽입
    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        for i in range(4):  # 상하좌우 4방향에 대해
            nx, ny = x + dx[i], y + dy[i]  # 새로운 위치 계산
            if 0 <= nx < len(lab) and 0 <= ny < len(lab[0]) and lab[nx][ny] == 0:  # 연구소 범위 내에 있고 빈 칸이면
                lab[nx][ny] = 2  # 바이러스를 확산
                queue.append((nx, ny))  # 새 위치를 큐에 추가

def get_safe_area(lab):  # 안전 영역의 크기를 계산하는 함수
    return sum(row.count(0) for row in lab)  # 연구소에서 빈 칸(0)의 개수를 모두 더함

def find_max_safe_area(n, m, lab):  # 최대 안전 영역을 찾는 함수
    empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]  # 빈 칸의 좌표 리스트
    viruses = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]  # 바이러스의 좌표 리스트
    
    max_safe_area = 0  # 최대 안전 영역 크기를 저장할 변수
    
    for walls in combinations(empty_spaces, 3):  # 3개의 빈 칸을 선택해 벽을 세우는 모든 조합에 대해 반복
        temp_lab = copy.deepcopy(lab)  # 연구소 상태를 깊은 복사
        for x, y in walls:  # 선택된 3개의 좌표에 대해
            temp_lab[x][y] = 1  # 벽을 세움
        spread_virus(temp_lab, viruses)  # 바이러스를 확산시킴
        safe_area = get_safe_area(temp_lab)  # 확산 후의 안전 영역 크기를 계산
        max_safe_area = max(max_safe_area, safe_area)  # 최대 안전 영역 크기를 갱신
    
    return max_safe_area  # 최대 안전 영역 크기 반환

n, m = map(int, input().split())  # 연구소의 크기 입력 받기
lab = [list(map(int, input().split())) for _ in range(n)]  # 연구소 상태 입력 받기

print(find_max_safe_area(n, m, lab))  # 최대 안전 영역 크기를 계산하고 출력
