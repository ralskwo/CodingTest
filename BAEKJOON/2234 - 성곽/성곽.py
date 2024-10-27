import sys
from collections import deque

# 방향 벡터 설정 (서쪽, 북쪽, 동쪽, 남쪽 순서)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 각 방향에 대한 벽 비트마스크 값 (서쪽: 1, 북쪽: 2, 동쪽: 4, 남쪽: 8)
DIRECTION_WALL = [1, 2, 4, 8]

# BFS를 통해 방을 탐색하고 방의 크기를 반환하는 함수
def bfs(start_x, start_y, room_id):
    # 시작 위치를 큐에 추가하고, 해당 위치를 현재 방 ID로 방문 표시
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = room_id
    room_size = 1  # 현재 방의 크기 (칸 수)

    # 큐가 빌 때까지 반복하여 BFS 탐색 수행
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄

        # 4방향(서, 북, 동, 남)을 순회하며 이동할 수 있는지 확인
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]  # 이동할 좌표 계산

            # 성곽 크기 내에 있고, 아직 방문하지 않은 위치인지 확인
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                # 현재 위치에서 해당 방향에 벽이 없을 때만 이동
                if not (castle[x][y] & DIRECTION_WALL[direction]):
                    visited[nx][ny] = room_id  # 이동할 위치를 현재 방 ID로 표시
                    queue.append((nx, ny))  # 큐에 이동할 위치 추가
                    room_size += 1  # 방 크기 증가

    return room_size  # 최종 방 크기 반환

# 성곽의 크기 입력 받기 (N은 너비, M은 높이)
N, M = map(int, input().split())

# 성곽의 벽 정보 입력 받기
castle = [list(map(int, input().split())) for _ in range(M)]

# 방문 여부와 방 ID를 저장할 리스트 초기화
visited = [[0] * N for _ in range(M)]

# 각 방의 크기를 저장할 리스트와 방의 개수를 저장할 변수 초기화
room_sizes = []
room_count = 0

# 성곽의 각 칸을 순회하며 방 탐색 수행
for i in range(M):
    for j in range(N):
        # 아직 방문하지 않은 칸이면 새로운 방으로 간주하고 탐색
        if visited[i][j] == 0:
            room_count += 1  # 방의 개수 증가
            room_size = bfs(i, j, room_count)  # BFS로 방 크기 계산
            room_sizes.append(room_size)  # 방 크기 리스트에 추가

# 가장 큰 방의 크기 계산
max_room_size = max(room_sizes)

# 벽을 하나 제거하여 얻을 수 있는 최대 방 크기 계산 변수 초기화
max_combined_room_size = 0

# 성곽의 각 칸을 순회하며 벽 제거 시도를 통해 방 크기 계산
for i in range(M):
    for j in range(N):
        current_room_id = visited[i][j]  # 현재 칸의 방 ID 저장

        # 4방향을 확인하여 인접 방과의 연결 시도
        for direction in range(4):
            ni, nj = i + dx[direction], j + dy[direction]  # 이동할 좌표 계산
            if 0 <= ni < M and 0 <= nj < N:
                neighbor_room_id = visited[ni][nj]  # 인접 방의 ID 저장

                # 인접 방이 다른 방일 경우에만 벽을 제거하고 방을 합친 크기 계산
                if current_room_id != neighbor_room_id:
                    combined_size = room_sizes[current_room_id - 1] + room_sizes[neighbor_room_id - 1]
                    max_combined_room_size = max(max_combined_room_size, combined_size)  # 최대 크기 갱신

# 최종 결과 출력: 방의 개수, 가장 큰 방의 크기, 벽을 제거하여 얻을 수 있는 최대 방 크기
print(room_count)
print(max_room_size)
print(max_combined_room_size)