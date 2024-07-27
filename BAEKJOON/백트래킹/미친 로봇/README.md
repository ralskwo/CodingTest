# 미친 로봇 문제 풀이 및 설명

https://www.acmicpc.net/problem/1405

## 문제 이해

이 문제는 로봇이 평면 위에서 특정 확률로 동서남북으로 이동하며, 주어진 횟수만큼 이동했을 때 경로가 단순한지 확인하는 것입니다. 단순한 경로는 로봇이 이동 중에 동일한 위치를 재방문하지 않는 경로를 의미합니다. 따라서 문제를 해결하려면 로봇이 모든 가능한 경로를 탐색하면서 재방문 여부를 체크해야 합니다.

## 입력/출력 조건

- 입력:
  - 첫 줄에 이동 횟수 \( N \) (1 ≤ \( N \) ≤ 14)와 동쪽, 서쪽, 남쪽, 북쪽으로 이동할 확률(0 ≤ 확률 ≤ 100)이 주어집니다.
  - 각 확률은 100을 기준으로 백분율로 주어집니다.
- 출력:
  - 로봇이 단순한 경로로 이동할 확률을 소수점 10자리까지 출력합니다.

## 접근 방법

이 문제는 깊이 우선 탐색(DFS)와 백트래킹을 사용하여 해결할 수 있습니다. DFS를 사용하여 로봇의 모든 가능한 이동 경로를 탐색하고, 백트래킹을 통해 경로가 단순한지 확인합니다. 이를 통해 로봇이 단순한 경로로 이동할 확률을 계산합니다.

## 문제 해결 과정

### 1. 문제 이해 및 입력 처리

1.1. 문제를 이해하고 입력 조건을 분석합니다.

1.2. 입력을 받아 필요한 변수에 저장합니다. \( N \)은 이동 횟수, 동서남북 확률은 각각 `east`, `west`, `south`, `north` 변수에 저장합니다.

### 2. 확률 변환 및 방향 설정

2.1. 입력으로 받은 동서남북 확률을 100으로 나누어 소수로 변환합니다.

2.2. 로봇의 이동 방향을 `(dx, dy)` 형태로 설정합니다.

### 3. DFS 및 백트래킹 구현

3.1. 방문한 좌표를 추적하기 위한 세트를 초기화합니다.

3.2. DFS 함수를 정의합니다.
   - 현재 좌표 `(x, y)`와 남은 이동 횟수 `n`을 인자로 받습니다.
   - `n`이 0이 되면 단순 경로 하나를 찾은 것이므로 확률 1을 반환합니다.
   - 현재 좌표를 `visited` 세트에 추가합니다.
   - 각 방향으로 이동을 시도하며, 아직 방문하지 않은 좌표로만 이동합니다.
   - 이동 후 확률을 재귀적으로 계산하여 누적합니다.
   - 현재 좌표를 `visited` 세트에서 제거하여 백트래킹합니다.

### 4. 메인 함수 및 결과 출력

4.1. 메인 함수에서 입력을 읽어옵니다.

4.2. 입력 값을 기반으로 `simple_path_probability` 함수를 호출하여 결과를 계산합니다.

4.3. 결과를 소수점 10자리까지 출력합니다.

이를 통해 주어진 입력에 따라 로봇이 단순한 경로로 이동할 확률을 정확하게 구할 수 있습니다.

## 코드 구현
```python
def simple_path_probability(N, east, west, south, north):
    # 동, 서, 남, 북으로의 이동 확률을 각각 백분율에서 소수로 변환
    prob_east = east / 100
    prob_west = west / 100
    prob_south = south / 100
    prob_north = north / 100
    
    # 이동할 방향에 따른 좌표 변화 (동, 서, 남, 북)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    probs = [prob_east, prob_west, prob_south, prob_north]
    
    # 방문한 좌표를 추적하기 위한 세트
    visited = set()
    
    def dfs(x, y, n):
        # n번의 이동이 모두 완료된 경우, 단순 경로 하나를 찾은 것이므로 확률 1을 반환
        if n == 0:
            return 1.0
        # 현재 좌표를 방문한 좌표로 추가
        visited.add((x, y))
        prob = 0.0
        # 모든 방향에 대해 재귀적으로 이동 시도
        for (dx, dy), p in zip(directions, probs):
            nx, ny = x + dx, y + dy
            # 다음 좌표가 아직 방문하지 않은 경우에만 이동
            if (nx, ny) not in visited:
                prob += p * dfs(nx, ny, n - 1)
        # 현재 좌표를 방문한 좌표에서 제거 (백트래킹)
        visited.remove((x, y))
        return prob
    
    return dfs(0, 0, N)

# 입력 처리
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    east = int(data[1])
    west = int(data[2])
    south = int(data[3])
    north = int(data[4])
    
    # 결과 계산 및 출력
    result = simple_path_probability(N, east, west, south, north)
    print(f"{result:.10f}")
