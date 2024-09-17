# 상어 중학교 문제 풀이 및 설명

https://www.acmicpc.net/problem/21609

https://mayquartet.com/python-%ed%8c%8c%ec%9d%b4%ec%8d%ac-%eb%b0%b1%ec%a4%80-21609-%ec%83%81%ec%96%b4-%ec%a4%91%ed%95%99%ea%b5%90-%eb%ac%b8%ec%a0%9c-%ed%92%80%ec%9d%b4-%eb%b0%8f-%ec%84%a4%eb%aa%85/

## 문제 이해

이 문제는 격자에서 여러 종류의 블록을 제거하며 점수를 획득하는 게임을 자동으로 플레이하는 것을 목표로 합니다. 격자는 \( N \times N \) 크기로, 각 칸에는 일반 블록, 무지개 블록, 또는 검은색 블록이 들어 있습니다. 일반 블록은 1부터 \( M \)까지의 자연수로 표현되고, 무지개 블록은 0으로, 검은색 블록은 -1로 표시됩니다.

게임은 다음과 같은 일련의 단계를 반복하며 진행됩니다:

1. 크기가 가장 큰 블록 그룹을 찾는다.
2. 해당 블록 그룹을 제거하고 점수를 획득한다.
3. 중력을 적용하여 블록을 아래로 떨어뜨린다.
4. 격자를 90도 반시계 방향으로 회전한다.
5. 다시 중력을 적용한다.

이러한 과정을 블록 그룹이 더 이상 존재하지 않을 때까지 반복하며, 최종적으로 획득한 점수를 구하는 것이 이 문제의 목표입니다. 여기서 블록 그룹은 적어도 2개의 블록이 연결되어 있어야 하며, 하나 이상의 일반 블록을 포함해야 합니다. 또한, 블록 그룹의 색상은 동일해야 하고, 무지개 블록은 어떤 색상과도 연결될 수 있습니다.

## 입출력 조건

**입력 조건**:

- 첫째 줄에 격자의 크기 \( N \)과 색상의 개수 \( M \)이 주어집니다.
- 둘째 줄부터 \( N \)개의 줄에 걸쳐 격자의 각 칸에 들어있는 블록의 정보가 주어집니다.
  - 각 칸의 정보는 -1 (검은색 블록), 0 (무지개 블록), 또는 1부터 \( M \) 사이의 자연수 (일반 블록)로 주어집니다.

**출력 조건**:

- 블록 그룹이 더 이상 존재하지 않을 때까지 반복된 게임 진행 후 획득한 총 점수를 한 줄에 출력합니다.

## 접근 방식

이 문제를 해결하기 위해서는 시뮬레이션과 그래프 탐색이 결합된 복합적인 알고리즘을 사용해야 합니다. 주어진 문제는 크게 네 가지 주요 단계로 구성되어 있으며, 각 단계마다 효율적인 처리가 요구됩니다. 다음은 문제를 해결하기 위한 접근 방식입니다:

1. **블록 그룹 찾기**: BFS(너비 우선 탐색)를 사용하여 격자에서 가장 큰 블록 그룹을 찾아야 합니다. 그룹의 크기가 같을 경우 무지개 블록의 수, 기준 블록의 위치를 고려하여 가장 큰 블록 그룹을 선택합니다.
2. **블록 제거 및 점수 계산**: 찾은 블록 그룹을 제거하고, 그 크기의 제곱을 점수에 더합니다.
3. **중력 작용**: 블록을 격자의 아래로 떨어뜨리는 중력 효과를 구현해야 합니다.
4. **격자 회전 및 중력 재적용**: 격자를 90도 반시계 방향으로 회전하고, 중력을 다시 적용하여 블록을 아래로 떨어뜨립니다.

이러한 단계들을 효율적으로 처리하기 위해 BFS를 사용하여 블록 그룹을 찾고, 배열 조작을 통해 중력과 회전을 구현해야 합니다. 주어진 격자의 크기가 최대 20이므로 BFS와 격자 회전을 여러 번 수행해도 시간 내에 처리할 수 있습니다.

## 풀이 과정

1. **입력 파싱 및 초기화**:
   - 격자의 크기 \( N \)과 색상 수 \( M \)을 입력받고, 격자 정보를 2차원 리스트에 저장합니다.
2. **가장 큰 블록 그룹 찾기**:
   - 격자의 각 칸을 순회하며 일반 블록을 발견할 때마다 BFS를 실행합니다.
   - BFS를 통해 현재 블록을 시작으로 연결된 블록 그룹을 탐색합니다. 이때 그룹의 크기, 무지개 블록의 수, 그룹의 기준 블록을 기록합니다.
   - 블록 그룹은 적어도 2개의 블록을 포함해야 하며, 하나 이상의 일반 블록을 포함해야 합니다. 그룹을 찾을 때 방문했던 무지개 블록은 다른 그룹에서도 사용할 수 있도록 다시 방문 가능 상태로 되돌려야 합니다.
   - 여러 블록 그룹 중에서 조건에 따라 가장 큰 그룹을 선택합니다:
     1. 그룹의 크기가 가장 큰 것
     2. 무지개 블록의 수가 가장 많은 것
     3. 기준 블록의 행 번호가 가장 큰 것
     4. 기준 블록의 열 번호가 가장 큰 것
3. **블록 그룹 제거 및 점수 계산**:

   - 가장 큰 블록 그룹을 찾으면, 해당 그룹의 모든 블록을 격자에서 제거하고 빈 공간으로 표시합니다.
   - 제거된 블록의 수를 \( B \)라고 할 때, \( B^2 \)를 점수에 누적합니다.

4. **중력 작용**:

   - 격자에 중력을 적용하여 모든 블록이 아래로 떨어지도록 합니다.
   - 각 열을 아래에서 위로 순회하면서, 블록을 가능한 아래쪽으로 이동시킵니다. 이때 검은색 블록은 다른 블록의 낙하를 막는 장애물로 작용합니다.

5. **격자 회전**:

   - 격자를 90도 반시계 방향으로 회전합니다. 새로운 격자를 생성하여 회전된 위치에 기존 격자의 값을 복사합니다.

6. **중력 재적용**:

   - 회전된 격자에 다시 중력을 적용하여 블록을 아래로 떨어뜨립니다.

7. **반복 및 종료**:

   - 블록 그룹이 더 이상 존재하지 않을 때까지 위의 과정을 반복합니다.
   - 최종적으로 획득한 총 점수를 출력합니다.

8. **최적화 고려 사항**:
   - 격자의 크기가 20 이하이므로 BFS를 사용하여 모든 블록 그룹을 찾아도 시간 내에 충분히 처리할 수 있습니다.
   - 블록 그룹 탐색과 정렬을 효율적으로 처리하여 가장 큰 블록 그룹을 정확하게 선택합니다.

## 코드 구현

```python
from collections import deque

def find_largest_block_group(N, grid):
    # 블록 그룹을 찾기 위한 방문 체크 배열 생성
    visited = [[False] * N for _ in range(N)]
    # 상하좌우 탐색을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 가장 큰 블록 그룹을 저장할 변수
    largest_group = []
    # 가장 큰 블록 그룹 내 무지개 블록 수를 저장할 변수
    max_rainbow_count = -1
    # 블록 그룹의 기준 블록 위치를 저장할 변수
    standard_block = (-1, -1)

    # BFS를 이용하여 블록 그룹을 찾는 함수
    def bfs(r, c, color):
        # BFS 탐색을 위한 큐 초기화
        queue = deque([(r, c)])
        # 현재 그룹에 속한 블록의 위치 리스트
        group = [(r, c)]
        # 무지개 블록의 위치 리스트
        rainbow_blocks = []
        # 방문 표시
        visited[r][c] = True
        # 무지개 블록 수 카운트
        rainbow_count = 0
        # BFS 탐색 시작
        while queue:
            x, y = queue.popleft()
            # 상하좌우 인접한 블록 탐색
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                # 격자 범위 내에 있고 방문하지 않은 블록만 탐색
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    # 같은 색상의 블록이나 무지개 블록이면 그룹에 추가
                    if grid[nx][ny] == color or grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        group.append((nx, ny))
                        # 무지개 블록인 경우 카운트 및 리스트에 추가
                        if grid[nx][ny] == 0:
                            rainbow_count += 1
                            rainbow_blocks.append((nx, ny))

        # 무지개 블록은 다른 그룹에서 다시 사용될 수 있으므로 방문 표시 초기화
        for x, y in rainbow_blocks:
            visited[x][y] = False

        # 그룹과 무지개 블록 수 반환
        return group, rainbow_count

    # 격자 전체를 탐색하여 블록 그룹 찾기
    for i in range(N):
        for j in range(N):
            # 일반 블록이고 방문하지 않은 경우에만 그룹 탐색 시작
            if grid[i][j] > 0 and not visited[i][j]:
                group, rainbow_count = bfs(i, j, grid[i][j])
                # 그룹 크기가 2 이상이어야 유효한 그룹
                if len(group) >= 2:
                    # 기준 블록은 일반 블록 중 가장 위쪽, 왼쪽에 있는 블록 선택
                    standard_block_candidate = min((x, y) for x, y in group if grid[x][y] > 0)
                    # 가장 큰 그룹을 찾기 위한 조건 비교
                    if (len(group), rainbow_count, standard_block_candidate) > (
                        len(largest_group), max_rainbow_count, standard_block):
                        # 새로운 가장 큰 그룹 갱신
                        largest_group = group
                        max_rainbow_count = rainbow_count
                        standard_block = standard_block_candidate

    # 가장 큰 그룹 반환
    return largest_group

def apply_gravity(N, grid):
    # 중력 작용: 각 열에 대해 아래로 블록을 내림
    for col in range(N):
        # 블록이 내려올 빈 공간의 행 인덱스
        empty_row = N - 1
        # 아래쪽에서 위쪽으로 탐색
        for row in range(N - 1, -1, -1):
            # 검은색 블록을 만난 경우 그 위로는 중력이 작용하지 않음
            if grid[row][col] == -1:
                empty_row = row - 1
            # 일반 블록이나 무지개 블록을 만나면 아래로 이동
            elif grid[row][col] >= 0:
                # 빈 공간이 있으면 블록을 내림
                if empty_row != row:
                    grid[empty_row][col] = grid[row][col]
                    grid[row][col] = -2  # 빈 공간을 표시하기 위해 -2 사용
                # 빈 공간 인덱스를 위로 한 칸 이동
                empty_row -= 1

def rotate_counter_clockwise(N, grid):
    # 격자를 90도 반시계 방향으로 회전하는 함수
    new_grid = [[-2] * N for _ in range(N)]  # 새로운 격자 생성
    for i in range(N):
        for j in range(N):
            # 회전한 위치에 값 할당
            new_grid[N - j - 1][i] = grid[i][j]
    return new_grid

def play_game(N, grid):
    # 게임 진행 및 점수 계산
    total_score = 0
    while True:
        # 1. 가장 큰 블록 그룹 찾기
        largest_group = find_largest_block_group(N, grid)
        # 더 이상 블록 그룹이 없으면 게임 종료
        if not largest_group:
            break

        # 2. 블록 그룹 제거 및 점수 계산
        for r, c in largest_group:
            grid[r][c] = -2  # 블록 제거를 위해 빈 공간으로 표시
        total_score += len(largest_group) ** 2  # 점수 = 블록 수의 제곱

        # 3. 중력 작용
        apply_gravity(N, grid)

        # 4. 격자를 90도 반시계 방향으로 회전
        grid = rotate_counter_clockwise(N, grid)

        # 5. 중력 재적용
        apply_gravity(N, grid)

    # 총 점수 반환
    return total_score

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 입력 파싱
    N, M = int(data[0]), int(data[1])
    grid = []
    index = 2
    for _ in range(N):
        row = list(map(int, data[index:index + N]))
        grid.append(row)
        index += N

    # 게임 진행 및 결과 출력
    result = play_game(N, grid)
    print(result)

if __name__ == "__main__":
    main()
```
