# 가장 큰 정사각형 문제 풀이

## 문제 이해

- **문제 설명**: 주어진 이진 행렬에서 1로 이루어진 가장 큰 정사각형을 찾아 그 넓이를 구하는 문제입니다.
- **입력**: 첫 줄에 두 개의 정수 `n`과 `m`이 주어지며, 이는 각각 행렬의 행 수와 열 수를 나타냅니다. 그 다음 `n`개의 줄에 `m` 길이의 이진 문자열이 주어집니다.
- **출력**: 1로 이루어진 가장 큰 정사각형의 넓이를 출력합니다.
- **제약 조건**: 행렬의 각 요소는 '0' 또는 '1'입니다.

## 접근 방식

문제를 해결하기 위한 접근 방식을 설명합니다.

- **아이디어**: 동적 프로그래밍(DP)을 사용하여 문제를 해결합니다. 각 위치에서 가장 큰 정사각형의 변의 길이를 저장하는 `dp` 테이블을 생성합니다.
- **알고리즘 선택**: 2차원 DP 배열을 사용하여, 각 위치에서 가능한 정사각형의 크기를 계산합니다. 
- **단계별 접근**:
  1. 문자열 리스트를 2차원 리스트로 변환합니다.
  2. DP 배열을 초기화하고, 각 위치에서 정사각형의 크기를 계산합니다.
  3. 최대 변의 길이를 저장하고, 이를 이용해 넓이를 계산합니다.

## 코드 설명
```python
def maximalSquare(n, m, matrix_str):
    if not matrix_str:
        return 0

    # 문자열 리스트를 2차원 리스트로 변환
    matrix = [list(row) for row in matrix_str]
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1  # 첫 행 또는 첫 열인 경우
                else:
                    # 이전 행, 이전 열, 대각선 값을 참고하여 최소값에 1을 더함
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 최대 변의 길이 갱신
                max_side = max(max_side, dp[i][j])

    # 최대 변의 길이의 제곱이 가장 큰 정사각형의 넓이
    return max_side * max_side

# 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 n과 m을 입력 받음
matrix_str = [input().strip() for _ in range(n)]  # 다음 n개의 줄에서 문자열 리스트를 입력 받음

# 결과 출력
print(maximalSquare(n, m, matrix_str))  # 함수 호출 및 결과 출력
```