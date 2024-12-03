from itertools import combinations
from collections import deque

# 5x5 격자를 입력 받는다. 각 줄은 문자열로 구성된다.
grid = [input().strip() for _ in range(5)]

# 상하좌우 이동을 위한 방향 벡터를 정의한다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 5x5 격자의 모든 좌표를 리스트로 생성한다.
positions = [(i, j) for i in range(5) for j in range(5)]


# 선택된 7개의 좌표가 모두 인접해 있는지를 확인하는 함수
def is_adjacent(selected):
    # BFS를 수행하기 위해 초기 큐에 첫 번째 좌표를 넣는다.
    queue = deque([selected[0]])
    # 방문한 좌표를 기록하기 위해 집합에 첫 번째 좌표를 추가한다.
    visited = set([selected[0]])
    # 현재 연결된 좌표의 수를 초기화한다.
    count = 1

    # BFS 탐색을 시작한다.
    while queue:
        # 큐에서 하나의 좌표를 꺼낸다.
        x, y = queue.popleft()
        # 상하좌우로 이동하면서 연결된 좌표를 확인한다.
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 선택된 좌표 중 방문하지 않은 좌표라면 방문 처리 후 큐에 추가한다.
            if (nx, ny) in selected and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                count += 1
    # 연결된 좌표의 수가 7개라면 True를 반환한다.
    return count == 7


# 선택된 좌표 중 'S' 학생의 수를 세는 함수
def count_s(selected):
    # 선택된 좌표에서 해당 좌표의 값이 'S'인 경우를 세어 반환한다.
    return sum(1 for x, y in selected if grid[x][y] == "S")


# 가능한 경우의 수를 저장할 변수를 초기화한다.
result = 0

# 25개의 좌표에서 7개의 좌표를 선택하는 모든 조합을 생성한다.
for comb in combinations(positions, 7):
    # 선택된 조합이 'S' 학생 4명 이상을 포함하고, 모두 인접해 있는 경우를 확인한다.
    if count_s(comb) >= 4 and is_adjacent(comb):
        # 조건을 만족하면 경우의 수를 증가시킨다.
        result += 1

# 모든 경우의 수를 출력한다.
print(result)
