# 최대 정사각형 넓이 구하기

## 문제 설명
주어진 n x m 크기의 2차원 배열에서 1로 이루어진 가장 큰 정사각형의 넓이를 구하는 문제입니다.

예를 들어, 다음과 같은 배열에서는 가운데의 2x2 배열이 가장 큰 정사각형입니다.

0 1 0 0
1 1 1 0
1 1 1 0
0 0 1 0

## 입력
- 첫째 줄에 n (1 ≤ n, m ≤ 1,000)이 주어진다.
- 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

## 출력
- 첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

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