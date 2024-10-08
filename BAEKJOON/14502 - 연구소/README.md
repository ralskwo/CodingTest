# 연구소 문제 풀이 및 설명

https://www.acmicpc.net/problem/14502

## 문제 이해

이 문제는 연구소 내부에서 바이러스의 확산을 막기 위해 벽을 설치하고, 최대한 많은 안전 영역을 확보하는 문제입니다. 주어진 연구소는 N×M 크기의 직사각형 격자로 표현되며, 격자 안에는 빈 칸(0), 벽(1), 그리고 바이러스(2)가 존재합니다. 바이러스는 상하좌우로 인접한 빈 칸으로 퍼져나갈 수 있습니다. 이 문제에서 우리가 할 일은 3개의 벽을 새로 설치하여 바이러스의 확산을 최대한 억제하고, 바이러스가 닿지 않는 안전 영역의 크기를 최대로 만드는 것입니다.

## 입출력 조건

- **입력**:

  - 첫째 줄에 연구소의 세로 크기 `N`과 가로 크기 `M`이 공백으로 구분되어 주어집니다. (`3 ≤ N, M ≤ 8`)
  - 둘째 줄부터 `N`개의 줄에 걸쳐 연구소의 상태가 주어집니다. 각 줄은 `M`개의 숫자로 이루어져 있으며, `0`은 빈 칸, `1`은 벽, `2`는 바이러스의 위치를 나타냅니다.
  - 바이러스의 개수는 2 이상 10 이하의 자연수이며, 빈 칸의 개수는 최소 3개 이상입니다.

- **출력**:
  - 첫째 줄에 3개의 벽을 세운 뒤 얻을 수 있는 안전 영역의 최대 크기를 출력합니다.

## 접근 방식

이 문제를 해결하기 위해 사용할 수 있는 알고리즘은 완전 탐색(Brute Force)과 BFS(너비 우선 탐색)입니다. 다음과 같은 접근 방식을 통해 문제를 해결할 수 있습니다:

1. **완전 탐색을 통한 벽 세우기**:

   - 먼저, 연구소의 빈 칸들 중에서 3개의 위치를 선택하여 벽을 세웁니다. 이때, 가능한 모든 경우의 수를 고려해야 합니다.
   - 빈 칸이 최대 64개(N, M이 각각 8일 때)라면, 그 중 3개를 선택하는 조합의 경우의 수는 `C(64, 3)`입니다. 이는 약 41,000가지 경우의 수가 됩니다. N과 M이 작기 때문에 모든 경우를 시도해보는 완전 탐색이 가능합니다.

2. **BFS를 사용한 바이러스 확산 시뮬레이션**:

   - 각 경우의 수에 대해 벽을 세운 후, 바이러스가 퍼지는 과정을 시뮬레이션합니다. 이때, BFS를 사용하여 바이러스를 상하좌우로 퍼뜨릴 수 있습니다.
   - 바이러스가 퍼진 후, 안전 영역의 크기를 계산합니다. 안전 영역은 바이러스가 닿지 않은 빈 칸의 개수로 정의됩니다.

3. **최대 안전 영역 계산**:
   - 모든 경우의 수에 대해 바이러스를 퍼뜨리고, 그 결과로 얻어지는 안전 영역의 크기를 계산합니다.
   - 그 중에서 가장 큰 안전 영역의 크기를 선택하여 출력합니다.

## 풀이 과정

1. **초기 설정**:

   - 연구소의 상태를 나타내는 2D 리스트를 입력받습니다. 그리고 빈 칸의 위치와 바이러스의 위치를 각각 리스트에 저장합니다.

2. **벽 세우기**:

   - `combinations` 함수를 이용하여 빈 칸 중 3개의 위치를 선택하는 모든 조합을 생성합니다.
   - 각 조합에 대해, 해당 위치에 벽을 세운 후의 연구소 상태를 깊은 복사로 생성합니다.

3. **바이러스 확산**:

   - BFS를 이용하여 바이러스를 확산시킵니다. 큐를 이용해 바이러스가 퍼질 수 있는 모든 빈 칸으로 확산시키며, 확산된 칸은 바이러스로 표시합니다.

4. **안전 영역 계산**:

   - 바이러스 확산이 완료된 후, 남아 있는 빈 칸의 수를 세어 안전 영역의 크기를 계산합니다.

5. **최대값 갱신**:

   - 각 조합에 대해 계산된 안전 영역 크기를 저장하고, 그 중 최대값을 갱신합니다.

6. **최종 결과 출력**:
   - 모든 경우를 다 계산한 후, 최종적으로 최대 안전 영역 크기를 출력합니다.

이 접근 방식은 연구소의 크기가 작기 때문에 가능한 방법입니다. 완전 탐색을 통해 모든 경우의 수를 시도하고, 그 중에서 최적의 해답을 도출해낼 수 있습니다.

## 코드 구현

```python
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
```
