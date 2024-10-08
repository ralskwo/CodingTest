# 집배원 한상덕 문제 풀이 및 설명

https://www.acmicpc.net/problem/2842

## 문제 이해

이 문제는 상덕이가 매일 아침 마을의 모든 집에 우편을 배달하는 과정에서 최소한의 피로도로 배달을 완료할 수 있도록 하는 경로를 찾는 것입니다. 마을은 `N×N` 크기의 행렬로 표현되며, 행렬의 각 칸은 우체국(P), 집(K), 목초지(.) 중 하나로 나타납니다. 또한, 각 칸의 고도 정보가 주어집니다. 상덕이는 우체국에서 출발하여 모든 집에 우편을 배달한 후 다시 우체국으로 돌아와야 하며, 이때 경로 상에서 가장 높은 고도와 가장 낮은 고도의 차이를 피로도라고 합니다. 이 문제의 목표는 모든 집에 배달을 완료할 수 있는 경로 중에서 가장 작은 피로도를 찾는 것입니다.

이 문제를 풀기 위해서는 경로 상에서 고도의 차이를 최소화하는 방법을 찾는 것이 중요합니다. 상덕이는 인접한 칸으로 이동할 수 있으며, 이동할 때마다 고도가 다른 칸으로 이동하게 됩니다. 따라서 가능한 경로 중에서 고도 차이가 최소화되는 경로를 찾아야 합니다.

## 입출력 조건

### 입력

1. 첫 번째 줄에는 마을의 크기 `N`이 주어집니다. (`2 ≤ N ≤ 50`)
2. 두 번째 줄부터 `N`개의 줄에는 마을의 상태가 주어지며, 각 줄에는 `N`개의 문자가 포함됩니다. 각 문자는 우체국(P), 집(K), 목초지(.) 중 하나를 나타냅니다.
3. 이어지는 `N`개의 줄에는 각 지역의 고도가 주어지며, 각 줄에는 `N`개의 자연수가 포함됩니다. 이 자연수는 해당 지역의 고도를 나타내며, 고도는 `1,000,000`보다 작거나 같은 자연수입니다.

### 출력

1. 첫 번째 줄에 가장 작은 피로도를 출력합니다. 이 값은 모든 집에 배달을 완료할 수 있는 경로 중에서 경로 상의 최고 고도와 최저 고도의 차이를 의미합니다.

## 접근 방식

이 문제를 해결하기 위해서는 경로 탐색과 이진 탐색을 결합한 접근 방식을 사용할 수 있습니다. 구체적으로 다음과 같은 방법으로 접근합니다:

1. **이진 탐색과 BFS(또는 DFS) 결합**: 이 문제의 핵심은 고도의 차이가 최소화되는 경로를 찾는 것입니다. 고도의 차이를 최소화하기 위해 이진 탐색을 사용하여 고도의 범위를 좁혀 나가고, BFS(또는 DFS)를 사용하여 현재 설정된 고도 범위 내에서 모든 집에 도달할 수 있는지를 확인합니다.
2. **이진 탐색의 범위 설정**: 먼저 마을 내의 모든 고도 값을 수집하고, 이를 오름차순으로 정렬합니다. 이 고도 값들에 대해 이진 탐색을 수행하여 가능한 고도의 범위를 설정합니다. 이진 탐색의 중간 값을 설정하고, 그 값이 가능한지를 BFS(또는 DFS)를 통해 탐색합니다.

3. **BFS(또는 DFS)로 경로 탐색**: 현재 설정된 고도 범위 내에서 우체국에서 출발하여 모든 집에 도달할 수 있는지를 BFS(또는 DFS)를 통해 확인합니다. 만약 가능한 경우, 이 범위에서의 피로도 차이를 계산하고, 이를 최소화하는 방향으로 이진 탐색을 계속 진행합니다.

## 풀이 과정

1. **입력 데이터 처리**: 먼저 마을의 크기 `N`을 입력받고, 마을 상태와 고도 정보를 2차원 리스트로 저장합니다. 이 과정에서 우체국의 위치와 집의 개수를 파악하고, 마을 내 모든 고도 값을 집합에 추가하여 고도의 중복을 제거합니다.

2. **고도 값 정렬**: 고도 값을 오름차순으로 정렬하여 이진 탐색을 위한 준비를 합니다. 이진 탐색은 이 고도 값들에 대해 최소와 최대 범위를 조정하여 수행됩니다.

3. **이진 탐색을 통한 최소 피로도 탐색**: 고도 값 리스트를 이용해 최소 피로도를 탐색합니다. `left`와 `right` 포인터를 사용하여 고도의 범위를 조정하고, 중간 고도 값을 설정하여 현재 범위 내에서 모든 집에 배달이 가능한지를 BFS(또는 DFS)를 통해 확인합니다.

4. **BFS(또는 DFS)로 경로 탐색**: 주어진 고도 범위 내에서 모든 집에 도달할 수 있는지를 확인합니다. BFS(또는 DFS)를 사용하여 우체국에서 시작해 인접한 칸으로 이동하며, 조건에 맞는 칸들을 탐색합니다. 이 과정에서 목표는 모든 집을 방문하는 것입니다.

5. **피로도 계산 및 출력**: 탐색이 완료되면 현재 범위에서의 피로도 차이를 계산하고, 이를 최소화하는 방향으로 이진 탐색을 진행합니다. 최종적으로 가장 작은 피로도를 출력합니다.

## 코드 구현

```python
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
```
