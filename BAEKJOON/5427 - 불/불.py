from collections import deque  # BFS 구현을 위해 deque를 임포트합니다.
import sys  # sys를 사용하여 입력을 빠르게 처리합니다.

input = sys.stdin.read  # 전체 입력을 한 번에 받아서 처리합니다.

def escape_building(w, h, building):
    # 불과 상근이의 위치를 저장할 큐를 초기화합니다.
    fire_queue = deque()
    person_queue = deque()
    # 불과 상근이의 각 위치에서의 시간을 저장할 2차원 배열을 초기화합니다.
    fire_times = [[-1] * w for _ in range(h)]
    person_times = [[-1] * w for _ in range(h)]

    # 빌딩의 각 칸을 확인하여 불과 상근이의 위치를 찾아 초기 설정합니다.
    for y in range(h):
        for x in range(w):
            if building[y][x] == '*':  # 해당 위치가 불인 경우
                fire_queue.append((x, y))  # 불의 위치를 큐에 추가합니다.
                fire_times[y][x] = 0  # 불이 퍼지기 시작한 시간을 0으로 설정합니다.
            elif building[y][x] == '@':  # 해당 위치가 상근이의 시작 위치인 경우
                person_queue.append((x, y))  # 상근이의 위치를 큐에 추가합니다.
                person_times[y][x] = 0  # 상근이가 출발하는 시간을 0으로 설정합니다.

    # 이동 가능한 방향을 나타내는 벡터 (동, 서, 남, 북)입니다.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 불의 확산을 BFS로 계산합니다.
    while fire_queue:
        x, y = fire_queue.popleft()  # 현재 불이 있는 위치를 꺼냅니다.
        for dx, dy in directions:  # 네 방향으로 확산을 시도합니다.
            nx, ny = x + dx, y + dy  # 다음 위치를 계산합니다.
            # 다음 위치가 지도 범위 안에 있고, 아직 불이 도달하지 않은 위치인 경우
            if 0 <= nx < w and 0 <= ny < h and fire_times[ny][nx] == -1:
                if building[ny][nx] == '.':  # 빈 공간일 경우에만 불이 퍼질 수 있습니다.
                    fire_times[ny][nx] = fire_times[y][x] + 1  # 현재 위치의 시간보다 1초 늦게 불이 도달합니다.
                    fire_queue.append((nx, ny))  # 불의 새로운 위치를 큐에 추가합니다.

    # 상근이의 이동을 BFS로 계산합니다.
    while person_queue:
        x, y = person_queue.popleft()  # 상근이의 현재 위치를 꺼냅니다.
        for dx, dy in directions:  # 네 방향으로 이동을 시도합니다.
            nx, ny = x + dx, y + dy  # 다음 위치를 계산합니다.

            # 상근이가 지도 밖으로 나가는 경우 탈출에 성공한 것입니다.
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                return person_times[y][x] + 1  # 현재 시간에 1초를 더하여 탈출 시간을 반환합니다.

            # 다음 위치가 지도 범위 내에 있을 때
            if 0 <= nx < w and 0 <= ny < h:
                # 상근이가 방문하지 않은 빈 공간이고, 이동 가능한 경우
                if person_times[ny][nx] == -1 and building[ny][nx] == '.':
                    # 불이 도착하지 않았거나 상근이가 먼저 도착할 수 있는 경우
                    if fire_times[ny][nx] == -1 or fire_times[ny][nx] > person_times[y][x] + 1:
                        person_times[ny][nx] = person_times[y][x] + 1  # 상근이의 이동 시간을 기록합니다.
                        person_queue.append((nx, ny))  # 상근이의 새로운 위치를 큐에 추가합니다.

    # 상근이가 빌딩을 탈출하지 못한 경우 "IMPOSSIBLE"을 반환합니다.
    return "IMPOSSIBLE"

def main():
    # 전체 입력을 받아 공백을 기준으로 나누어 리스트로 저장합니다.
    input_data = input().split()
    idx = 0  # 입력 리스트의 현재 위치를 나타내는 인덱스를 초기화합니다.
    t = int(input_data[idx])  # 테스트 케이스의 개수를 가져옵니다.
    idx += 1  # 다음 입력을 처리하기 위해 인덱스를 증가시킵니다.
    results = []  # 각 테스트 케이스의 결과를 저장할 리스트입니다.

    # 각 테스트 케이스를 처리합니다.
    for _ in range(t):
        w = int(input_data[idx])  # 빌딩의 너비를 가져옵니다.
        h = int(input_data[idx + 1])  # 빌딩의 높이를 가져옵니다.
        idx += 2  # 다음 입력을 처리하기 위해 인덱스를 증가시킵니다.

        # 빌딩 지도를 가져와 리스트에 저장합니다.
        building = [input_data[idx + i] for i in range(h)]
        idx += h  # 다음 테스트 케이스를 처리하기 위해 인덱스를 증가시킵니다.

        # 현재 테스트 케이스의 결과를 계산하여 리스트에 추가합니다.
        result = escape_building(w, h, building)
        results.append(result)

    # 모든 테스트 케이스의 결과를 출력합니다.
    for result in results:
        print(result)

# 이 코드가 직접 실행될 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    main()