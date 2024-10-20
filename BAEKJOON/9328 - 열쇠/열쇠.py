from collections import deque

# BFS를 사용하여 상근이가 얻을 수 있는 최대 문서 수를 계산하는 함수
def optimized_bfs(h, w, building, initial_keys):
    # BFS에서 사용할 상하좌우 이동 방향 설정
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 빌딩 맵을 확장하여 가장자리에 빈 공간을 추가하여 상근이가 건물 외부에서 시작할 수 있도록 설정
    extended_building = [['.'] * (w + 2)] + [['.'] + list(row) + ['.'] for row in building] + [['.'] * (w + 2)]
    
    # 초기 열쇠 목록을 대문자로 변환하여 집합에 저장 (열쇠가 "0"인 경우 제외)
    keys = set(k.upper() for k in initial_keys if k != '0')
    
    # BFS 탐색을 위한 큐 초기화 및 방문 여부 기록 배열 초기화
    queue = deque([(0, 0)])  # 상근이는 (0, 0) 위치에서 시작
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True  # 시작 위치를 방문 처리
    
    # 열쇠가 없어서 접근할 수 없는 문을 저장할 딕셔너리
    inaccessible_doors = {}
    # 상근이가 획득한 문서의 개수를 기록할 변수
    documents_collected = 0
    
    # BFS 탐색 시작
    while queue:
        # 큐에서 현재 위치를 꺼냄
        x, y = queue.popleft()

        # 상하좌우 네 방향에 대해 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 새로운 위치가 지도 범위 내에 있고 방문하지 않은 경우
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visited[nx][ny]:
                cell = extended_building[nx][ny]  # 해당 위치의 셀 값을 가져옴

                # 벽('*')인 경우, 이동할 수 없으므로 무시하고 넘어감
                if cell == '*':
                    continue

                # 현재 위치를 방문 처리
                visited[nx][ny] = True

                # 문서('$')를 발견한 경우, 문서 개수를 증가시킴
                if cell == '$':
                    documents_collected += 1
                # 소문자(열쇠)를 발견한 경우
                elif cell.islower():
                    key = cell.upper()  # 소문자를 대문자로 변환하여 열쇠로 사용
                    # 새로운 열쇠를 얻은 경우
                    if key not in keys:
                        keys.add(key)  # 열쇠를 추가
                        # 해당 열쇠로 열 수 있는 문들이 대기 중인 경우, 대기열에서 꺼내 큐에 추가
                        if key in inaccessible_doors:
                            queue.extend(inaccessible_doors[key])
                            del inaccessible_doors[key]  # 대기열을 제거
                # 대문자(문)를 발견한 경우
                elif cell.isupper():
                    # 해당 문에 필요한 열쇠가 없는 경우
                    if cell not in keys:
                        # 열쇠가 없으므로 대기열에 해당 문의 좌표를 저장하고 탐색을 멈춤
                        inaccessible_doors.setdefault(cell, []).append((nx, ny))
                        continue

                # 빈 공간 또는 열쇠가 있는 경우 큐에 추가하여 탐색을 계속 진행
                queue.append((nx, ny))

    # 획득한 문서의 총 개수를 반환
    return documents_collected

# 각 테스트 케이스를 처리하는 함수
def solve():
    # 빌딩의 높이와 너비 입력 받기
    h, w = map(int, input().split())
    # 빌딩의 평면도를 입력받아 리스트로 저장
    building = [input().strip() for _ in range(h)]
    # 상근이가 처음에 가지고 있는 열쇠 정보를 입력받음
    initial_keys = input().strip()
    # BFS 결과로 얻을 수 있는 최대 문서 개수를 반환
    return optimized_bfs(h, w, building, initial_keys)

# 테스트 케이스의 수를 입력받음
T = int(input())
# 각 테스트 케이스에 대해 결과를 출력
for _ in range(T):
    print(solve())