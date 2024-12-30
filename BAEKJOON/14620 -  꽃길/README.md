# 꽃길 문제 풀이 및 설명

<https://www.acmicpc.net/problem/14620>

<https://mayquartet.com/python-백준-14620-꽃길/>

## 문제 이해

이 문제는 N x N 크기의 격자 형태로 이루어진 화단에 세 개의 꽃을 심는 상황을 다룬다. 각 칸에는 꽃을 심는 데 드는 비용이 주어지며, 꽃은 특정한 형태로 피어나게 된다. 꽃을 심을 때 중심 좌표를 기준으로 상하좌우 4개의 칸에 꽃잎이 퍼지며, 이 5칸이 하나의 꽃을 구성한다.  
진아는 세 개의 꽃이 모두 피어야 하고, 서로 겹치거나 화단을 벗어나지 않도록 꽃을 심어야 한다. 또한, 화단을 대여하는 비용이 꽃을 심는 위치에 따라 달라지므로, 세 개의 꽃을 심는 데 드는 최소 비용을 구하는 것이 문제의 핵심이다.

따라서, 이 문제를 해결하기 위해서는 꽃을 심을 수 있는 모든 경우를 탐색하고, 세 개의 꽃이 정상적으로 피어날 수 있도록 배치하는 조합을 찾는 방식으로 접근해야 한다. 문제의 목표는 세 개의 꽃이 겹치지 않도록 하면서 화단 대여 비용의 합이 최소가 되는 경우를 찾는 것이다.

## 입출력 조건

**입력 조건**

- 첫 번째 줄에 화단의 크기 N이 주어진다. N은 6 이상 10 이하의 정수이다.
- 두 번째 줄부터 N개의 줄에 걸쳐 N x N 크기의 격자의 각 지점당 비용이 주어진다. 각 비용은 0 이상 200 이하의 정수이다.

**출력 조건**

- 세 개의 꽃을 심는 데 드는 최소 비용을 출력한다.

**제약 조건**

- 꽃은 정확히 세 개를 심어야 하며, 세 개의 꽃이 모두 정상적으로 피어야 한다.
- 꽃의 중심은 (1, 1)부터 (N-2, N-2) 범위 내에서 선택할 수 있다.
- 꽃잎이 화단을 벗어나거나 다른 꽃의 꽃잎과 겹치면 꽃이 죽게 되므로, 이런 경우는 고려하지 않는다.
- 화단에서 꽃이 차지하는 면적은 중심 1칸과 상하좌우 4칸을 포함해 총 5칸이다.

## 접근 방식

이 문제를 해결하기 위해서는 **브루트포스(완전탐색)**와 **백트래킹** 방식을 사용해야 한다.  
브루트포스는 가능한 모든 경우를 하나씩 탐색하는 방식으로, 화단의 크기가 최대 10x10으로 제한되어 있기 때문에 충분히 모든 경우를 직접 탐색할 수 있다.  
백트래킹은 조건에 맞지 않는 경우 탐색을 중단하고 되돌아가는 방식이다. 이를 통해 효율적으로 탐색을 수행할 수 있다.

꽃을 심는 방식은 다음과 같다.

- 꽃의 중심이 되는 칸을 선택하고, 그 위치에서 상하좌우 방향으로 꽃잎이 퍼진다.
- 꽃을 심기 위해서는 중심과 상하좌우 4칸이 모두 비어 있어야 하며, 이미 다른 꽃이 심어진 곳과 겹치지 않아야 한다.
- 꽃이 겹치거나 화단을 벗어나는 경우는 탐색에서 제외된다.

세 개의 꽃을 심기 위해

- 먼저 꽃을 심을 수 있는 모든 위치를 (1, 1)부터 (N-2, N-2)까지의 좌표로 설정한다.
- 세 개의 꽃을 심을 수 있는 좌표의 모든 조합을 구한다.
- 각 조합에 대해 꽃을 심을 수 있는지 확인하고, 비용을 계산해 최소 비용을 갱신한다.

이 과정에서 화단의 범위를 벗어나거나 꽃이 겹치는 경우 해당 조합은 무시된다.  
이를 통해 최소 비용을 찾는 방식으로 문제를 해결한다.

<https://mayquartet.com/algorithm-알고리즘-backtracking-백트래킹-알고리즘-이해하기/>

## 풀이 과정

1. **입력 받기 및 초기 설정**

   - N과 화단의 각 지점 비용을 2차원 리스트 형태로 입력받는다.
   - 꽃을 심을 수 있는 중심 좌표의 후보는 (1, 1)부터 (N-2, N-2)까지이다.
   - 가능한 모든 중심 좌표를 리스트에 저장한다.

2. **꽃이 차지하는 칸의 비용 계산**

   - 특정 좌표에 꽃을 심었을 때 드는 비용을 계산하는 함수를 구현한다.
   - 꽃의 중심 비용에 상하좌우 4칸의 비용을 더해 총 5칸의 비용을 합산한다.

3. **꽃 심기 유효성 검사**

   - 꽃의 중심이 화단을 벗어나거나, 이미 다른 꽃이 심어진 칸과 겹치는 경우를 확인하는 함수를 구현한다.
   - 꽃의 중심 및 상하좌우 4칸이 모두 겹치지 않는 경우에만 꽃을 심을 수 있도록 한다.

4. **꽃 심기 및 방문 처리**

   - 꽃을 심으면 방문 여부를 기록하는 2차원 리스트를 사용해 꽃이 차지하는 5칸을 방문 처리한다.
   - 꽃을 심는 과정에서 방문 처리된 칸이 다시 사용되지 않도록 한다.

5. **모든 조합 탐색**

   - 가능한 모든 꽃의 중심 좌표 중 세 개를 선택하는 조합을 생성한다.
   - 각 조합에 대해 꽃을 심을 수 있는지 확인하고, 꽃을 심을 수 있는 경우 비용을 계산한다.
   - 비용이 기존 최소 비용보다 작으면 최소 비용을 갱신한다.

6. **결과 출력**
   - 모든 조합을 탐색한 후 최종적으로 최소 비용을 출력한다.

## 코드 구현

```python
import sys
input = sys.stdin.read
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def calculate_cost(board, x, y, N):
    cost = board[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        cost += board[nx][ny]
    return cost

def is_valid(x, y, N):
    if x <= 0 or x >= N-1 or y <= 0 or y >= N-1:
        return False
    return True

def check_overlap(visited, x, y):
    if visited[x][y]:
        return False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny]:
            return False
    return True

def place_flower(visited, x, y, place):
    visited[x][y] = place
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        visited[nx][ny] = place

def solve(N, board):
    candidates = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]
    min_cost = float('inf')

    for comb in combinations(candidates, 3):
        visited = [[False] * N for _ in range(N)]
        total_cost = 0
        valid = True

        for x, y in comb:
            if not is_valid(x, y, N) or not check_overlap(visited, x, y):
                valid = False
                break
            total_cost += calculate_cost(board, x, y, N)
            place_flower(visited, x, y, True)

        if valid:
            min_cost = min(min_cost, total_cost)

    return min_cost

def main():
    data = input().splitlines()
    N = int(data[0])
    board = [list(map(int, line.split())) for line in data[1:]]
    print(solve(N, board))

main()
```
