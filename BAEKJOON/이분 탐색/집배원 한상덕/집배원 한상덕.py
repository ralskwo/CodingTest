from collections import deque

def can_deliver(min_height, max_height):
    # 시작 지점의 고도가 지정된 범위 내에 있는지 확인
    if not (min_height <= altitude[p_start[0]][p_start[1]] <= max_height):
        return False
    
    # 방문한 지점을 기록하기 위한 2차원 리스트 생성
    visited = [[False] * N for _ in range(N)]
    # BFS를 위한 큐에 시작 지점 추가
    queue = deque([p_start])
    # 시작 지점을 방문 처리
    visited[p_start[0]][p_start[1]] = True
    delivered = 0  # 배달한 집의 수를 카운트하기 위한 변수
    
    # BFS 시작
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        if village[x][y] == 'K':  # 현재 위치가 집(K)이라면
            delivered += 1  # 배달한 집 수를 증가
            
        # 8방향으로 이동 (상하좌우 및 대각선)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = x + dx, y + dy  # 이동할 새로운 위치 계산
            # 새 위치가 마을 내에 있고 방문하지 않았으며 고도 범위 내에 있는지 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if min_height <= altitude[nx][ny] <= max_height:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny))  # 큐에 새 위치 추가
    
    # 모든 집에 배달이 완료되었는지 확인
    return delivered == total_houses

N = int(input())  # 마을의 크기 N 입력
village = [list(input().strip()) for _ in range(N)]  # 마을 지도를 입력받아 2차원 리스트로 저장
altitude = [list(map(int, input().strip().split())) for _ in range(N)]  # 각 지역의 고도 정보를 입력받아 2차원 리스트로 저장

p_start = None  # 우체국 위치를 저장할 변수
total_houses = 0  # 배달할 집의 총 수를 저장할 변수
heights = set()  # 마을의 고도들을 저장할 집합 (중복 제거를 위해 set 사용)

# 마을을 순회하며 우체국 위치와 집의 수를 파악하고, 고도 정보를 집합에 추가
for i in range(N):
    for j in range(N):
        if village[i][j] == 'P':  # 우체국 위치를 찾으면
            p_start = (i, j)  # 우체국 위치 저장
        elif village[i][j] == 'K':  # 집을 찾으면
            total_houses += 1  # 집의 수 증가
        heights.add(altitude[i][j])  # 고도 정보를 집합에 추가

heights = sorted(heights)  # 고도 정보를 오름차순으로 정렬

left, right = 0, 0  # 이진 탐색을 위한 좌우 포인터 초기화
min_fatigue = float('inf')  # 최소 피로도를 무한대로 초기화

# 이진 탐색으로 최소 피로도 계산
while right < len(heights):
    if left < len(heights) and can_deliver(heights[left], heights[right]):
        min_fatigue = min(min_fatigue, heights[right] - heights[left])  # 현재 피로도가 더 작으면 갱신
        left += 1  # 범위를 좁히기 위해 left 증가
    else:
        right += 1  # 범위를 넓히기 위해 right 증가

print(min_fatigue)  # 최소 피로도 출력
