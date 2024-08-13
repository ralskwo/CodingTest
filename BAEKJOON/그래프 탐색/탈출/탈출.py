from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 임포트

def bfs_escape(R, C, forest):  # 고슴도치 탈출을 계산하는 함수 정의
    water_queue = deque()  # 물의 위치를 저장할 큐를 생성
    hedgehog_queue = deque()  # 고슴도치의 위치를 저장할 큐를 생성
    water_time = [[-1] * C for _ in range(R)]  # 물의 퍼짐 시간을 저장할 2차원 배열을 초기화 (-1로 초기화)
    hedgehog_time = [[-1] * C for _ in range(R)]  # 고슴도치의 이동 시간을 저장할 2차원 배열을 초기화 (-1로 초기화)
    
    for i in range(R):  # 맵의 각 행을 순회
        for j in range(C):  # 각 행의 열을 순회
            if forest[i][j] == '*':  # 현재 위치에 물이 있으면
                water_queue.append((i, j))  # 해당 위치를 물 큐에 추가
                water_time[i][j] = 0  # 물의 시작 시간을 0으로 설정
            elif forest[i][j] == 'S':  # 현재 위치에 고슴도치가 있으면
                hedgehog_queue.append((i, j))  # 해당 위치를 고슴도치 큐에 추가
                hedgehog_time[i][j] = 0  # 고슴도치의 시작 시간을 0으로 설정
    
    while water_queue:  # 물 큐가 빌 때까지 반복
        x, y = water_queue.popleft()  # 물의 위치를 큐에서 꺼냄
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 방향으로 이동
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] == '.' and water_time[nx][ny] == -1:
                # 새로운 위치가 맵 내부이고, 빈 칸이며, 아직 물이 도달하지 않은 곳이라면
                water_time[nx][ny] = water_time[x][y] + 1  # 새로운 위치의 물 퍼짐 시간을 현재 위치의 시간보다 1 증가시킴
                water_queue.append((nx, ny))  # 새로운 위치를 물 큐에 추가
    
    while hedgehog_queue:  # 고슴도치 큐가 빌 때까지 반복
        x, y = hedgehog_queue.popleft()  # 고슴도치의 위치를 큐에서 꺼냄
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 방향으로 이동
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            if 0 <= nx < R and 0 <= ny < C:  # 새로운 위치가 맵 내부인지 확인
                if forest[nx][ny] == 'D':  # 새로운 위치가 비버의 굴이라면
                    return hedgehog_time[x][y] + 1  # 현재 위치의 시간보다 1 증가된 시간을 반환 (탈출 성공)
                if forest[nx][ny] == '.' and hedgehog_time[nx][ny] == -1:  # 빈 칸이고, 아직 방문하지 않은 곳이라면
                    if water_time[nx][ny] == -1 or water_time[nx][ny] > hedgehog_time[x][y] + 1:
                        # 해당 위치에 물이 도달하지 않았거나, 물이 도달하는 시간보다 고슴도치가 먼저 도달할 수 있는 경우
                        hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1  # 새로운 위치의 고슴도치 이동 시간을 현재 위치의 시간보다 1 증가시킴
                        hedgehog_queue.append((nx, ny))  # 새로운 위치를 고슴도치 큐에 추가
    
    return "KAKTUS"  # 비버의 굴에 도달할 수 없을 경우 "KAKTUS" 반환

R, C = map(int, input().split())  # 맵의 크기 R(행)과 C(열)을 입력받음
forest = [input().strip() for _ in range(R)]  # 맵의 상태를 입력받아 리스트로 저장

print(bfs_escape(R, C, forest))  # 고슴도치 탈출 결과를 출력
