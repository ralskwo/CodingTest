# 파이프 옮기기 1 문제 풀이 및 설명

<https://www.acmicpc.net/problem/17070>

<https://mayquartet.com/python-백준-17070-파이프-옮기기-1/>

## 문제 이해

이 문제는 크기 `N×N`의 격자판에서 파이프를 특정 위치로 이동시키는 경우의 수를 구하는 문제입니다. 파이프는 2개의 연속된 칸을 차지하며, 초기에는 가로 방향으로 `(1, 1)`과 `(1, 2)`에 놓여 있습니다. 목표는 파이프의 끝을 `(N, N)`에 도달시키는 것입니다. 파이프는 이동 중 벽(값이 1)과 겹칠 수 없으며, 이동 가능 방향은 가로(`→`), 세로(`↓`), 대각선(`↘`) 세 가지입니다.

각 방향에서 이동 가능한 조건은 아래와 같습니다:

- **가로(`→`)**: 현재 위치의 오른쪽 칸이 빈 칸이어야 합니다.
- **세로(`↓`)**: 현재 위치의 아래쪽 칸이 빈 칸이어야 합니다.
- **대각선(`↘`)**: 현재 위치의 오른쪽, 아래쪽, 대각선 아래 칸이 모두 빈 칸이어야 합니다.

파이프를 목표 지점으로 이동시키는 방법의 개수를 계산해야 하며, 이 개수는 항상 1,000,000보다 작습니다.

---

## 입출력 조건

### 입력

1. 첫 줄에 격자의 크기 `N`이 주어지며, 3 ≤ `N` ≤ 16입니다.
2. 다음 `N`개의 줄에는 격자의 상태가 주어집니다. 각 칸은 다음과 같은 값으로 구성됩니다:
   - `0`: 빈 칸
   - `1`: 벽
3. 항상 `(1, 1)`과 `(1, 2)`는 빈 칸으로 주어지며, 파이프가 처음 위치할 수 있습니다.

### 출력

1. 파이프의 끝을 `(N, N)`에 도달시키는 가능한 방법의 개수를 출력합니다.
2. 이동할 수 없는 경우에는 `0`을 출력합니다.

---

## 접근 방식

이 문제는 파이프의 상태(위치와 방향)와 이동 조건에 따라 문제를 나누어 해결하는 **다이나믹 프로그래밍(DP)** 방식으로 접근할 수 있습니다. 다음과 같은 논리로 접근합니다:

1. **DP 테이블 정의**:

   - `dp[r][c][d]`: 파이프의 끝점이 `(r, c)`이고 방향이 `d`일 때의 가능한 이동 방법의 수
     - `d = 0`: 가로 방향
     - `d = 1`: 세로 방향
     - `d = 2`: 대각선 방향

2. **초기 상태 설정**:

   - 파이프의 시작 위치는 `(1, 1)`과 `(1, 2)`이며, 가로 방향입니다.
   - 따라서 `dp[1][2][0] = 1`로 초기화합니다.

3. **상태 전이**:

   - 각 방향에서 이동 가능한 경우를 확인하여 DP 테이블을 갱신합니다.
     - **가로 이동**: 현재 방향이 가로(`0`) 또는 대각선(`2`)일 때, 오른쪽 칸으로 이동 가능합니다.
     - **세로 이동**: 현재 방향이 세로(`1`) 또는 대각선(`2`)일 때, 아래쪽 칸으로 이동 가능합니다.
     - **대각선 이동**: 모든 방향에서 이동 가능하며, 이동하려는 칸과 주변 2개의 칸(오른쪽, 아래쪽)이 빈 칸이어야 합니다.

4. **최종 결과 계산**:
   - 목표 위치 `(N, N)`에 도달하는 모든 경우의 수를 계산합니다.
   - `dp[N][N][0] + dp[N][N][1] + dp[N][N][2]` 값을 반환합니다.

---

## 풀이 과정

1. `N`과 격자의 상태를 입력받아 DP 테이블을 초기화합니다. DP 테이블은 `N×N×3` 크기로 생성되며, 각각 가로, 세로, 대각선 방향의 경우를 저장합니다.

2. 초기 상태는 `(1, 2)`에서 가로 방향으로 시작하므로 `dp[0][1][0] = 1`로 설정합니다.

3. 격자의 모든 칸을 순회하며 아래의 조건에 따라 DP 테이블을 갱신합니다:

   - **가로 이동**:
     - `dp[r][c][0]`에 값을 추가하려면 이전 칸 `(r, c-1)`이 가로(`0`) 또는 대각선(`2`) 방향이어야 합니다.
     - `dp[r][c][0] += dp[r][c-1][0]` (가로 → 가로)
     - `dp[r][c][0] += dp[r][c-1][2]` (대각선 → 가로)
   - **세로 이동**:
     - `dp[r][c][1]`에 값을 추가하려면 이전 칸 `(r-1, c)`이 세로(`1`) 또는 대각선(`2`) 방향이어야 합니다.
     - `dp[r][c][1] += dp[r-1][c][1]` (세로 → 세로)
     - `dp[r][c][1] += dp[r-1][c][2]` (대각선 → 세로)
   - **대각선 이동**:
     - `dp[r][c][2]`에 값을 추가하려면 이전 칸 `(r-1, c-1)`이 가로(`0`), 세로(`1`), 대각선(`2`) 중 하나여야 하며, 현재 칸 `(r, c)`, 위쪽 칸 `(r-1, c)`, 왼쪽 칸 `(r, c-1)`이 모두 빈 칸이어야 합니다.
     - `dp[r][c][2] += dp[r-1][c-1][0]` (가로 → 대각선)
     - `dp[r][c][2] += dp[r-1][c-1][1]` (세로 → 대각선)
     - `dp[r][c][2] += dp[r-1][c-1][2]` (대각선 → 대각선)

4. 이동 불가능한 경우(벽 또는 경계를 벗어난 경우)는 건너뜁니다.

5. 최종적으로 목표 지점 `(N, N)`에서 모든 방향(가로, 세로, 대각선)의 경우를 합산하여 출력합니다.

6. 시간 복잡도는 \(O(N^2)\)이며, 공간 복잡도는 DP 테이블 저장을 위한 \(O(N^2×3)\)입니다. 이는 문제의 제약을 만족합니다.

## 코드 구현

```python
def move_pipe(N, house):
    # DP 테이블 초기화: 각 칸마다 3개의 방향(가로, 세로, 대각선)에 대한 경우를 저장
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

    # 초기 상태 설정: 파이프는 (1, 2)에서 가로 방향으로 시작 (인덱스는 0부터 시작)
    dp[0][1][0] = 1

    # 격자판의 모든 칸을 순회하며 DP 테이블 갱신
    for r in range(N):
        for c in range(N):
            # 현재 칸이 벽인 경우 이동 불가하므로 건너뜀
            if house[r][c] == 1:
                continue

            # 가로 방향에서 이동 가능한 경우
            if c > 0:  # 왼쪽 칸이 존재해야 함
                dp[r][c][0] += dp[r][c - 1][0]  # 가로 -> 가로
                dp[r][c][0] += dp[r][c - 1][2]  # 대각선 -> 가로

            # 세로 방향에서 이동 가능한 경우
            if r > 0:  # 위쪽 칸이 존재해야 함
                dp[r][c][1] += dp[r - 1][c][1]  # 세로 -> 세로
                dp[r][c][1] += dp[r - 1][c][2]  # 대각선 -> 세로

            # 대각선 방향에서 이동 가능한 경우
            if r > 0 and c > 0 and house[r - 1][c] == 0 and house[r][c - 1] == 0:
                # 대각선 이동은 현재 칸 외에도 상, 좌 칸이 모두 빈 칸이어야 함
                dp[r][c][2] += dp[r - 1][c - 1][0]  # 가로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][1]  # 세로 -> 대각선
                dp[r][c][2] += dp[r - 1][c - 1][2]  # 대각선 -> 대각선

    # 파이프의 끝이 (N, N)에 도달하는 모든 방향의 방법 수를 합산하여 반환
    return dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]


# 입력값으로 격자판의 크기 N과 집의 상태를 받음
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 계산된 결과를 출력
print(move_pipe(N, house))
```
