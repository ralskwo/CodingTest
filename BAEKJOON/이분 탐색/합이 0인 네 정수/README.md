# 합이 0인 네 정수 문제 풀이 및 설명

https://www.acmicpc.net/problem/7453

## 문제 이해

주어진 문제는 다음과 같습니다:
- 네 개의 배열 \( A, B, C, D \)가 있습니다.
- 각 배열은 크기 \( n \)으로, 배열의 크기는 최대 4000입니다.
- 배열의 원소는 절댓값이 최대 \( 2^{28} \)인 정수입니다.
- \( A[a] + B[b] + C[c] + D[d] = 0 \)이 되는 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성해야 합니다.

## 접근 방식

이 문제를 해결하기 위해 네 개의 배열에서 가능한 모든 합을 계산하는 것은 시간 초과를 유발할 수 있습니다. 따라서, 최적화된 방법으로 문제를 해결해야 합니다. 두 배열씩 합을 계산하여 해시맵을 사용하는 방식이 효율적입니다.

1. \( A \)와 \( B \) 배열의 모든 가능한 합을 계산하여 해시맵에 저장합니다. 이때, 해시맵의 키는 합이고, 값은 해당 합이 발생한 빈도입니다.
2. \( C \)와 \( D \) 배열의 모든 가능한 합을 계산하면서, 그 합의 음수가 해시맵에 존재하는지 확인합니다. 존재한다면, 해당 빈도를 카운트에 추가합니다.
3. 이 접근 방식은 \( O(n^2) \) 시간 복잡도로 문제를 해결할 수 있습니다.

## 풀이 과정

1. `count_zero_sum_pairs` 함수 정의:
    - 네 개의 배열 \( A, B, C, D \)를 입력으로 받습니다.
    - `AB_sum`이라는 해시맵을 생성하여 \( A \)와 \( B \) 배열의 합을 저장합니다.
    - \( A \)와 \( B \) 배열의 모든 가능한 합을 계산하여 `AB_sum` 해시맵에 해당 합이 발생한 빈도를 저장합니다.
    - \( C \)와 \( D \) 배열의 모든 가능한 합을 계산하면서 그 합의 음수가 `AB_sum`에 존재하는지 확인합니다.
    - 존재한다면, 해당 빈도를 카운트에 추가합니다.
    - 최종적으로 합이 0이 되는 쌍의 개수를 반환합니다.

2. 입력 처리:
    - 표준 입력으로부터 데이터를 읽고 배열 \( A, B, C, D \)를 생성합니다.
    - 입력 데이터를 공백으로 분리하여 첫 번째 값은 배열의 크기 \( n \)으로 사용하고, 나머지 값들은 각 배열에 채웁니다.
    - `count_zero_sum_pairs` 함수를 호출하여 결과를 계산하고 출력합니다.

## 분석 및 최적화

이 접근 방식은 배열의 모든 가능한 합을 계산하는 대신 두 배열씩 합을 계산하여 해시맵을 사용하는 방법으로 시간 복잡도를 크게 줄일 수 있습니다. 이는 \( O(n^2) \) 시간 복잡도로 문제를 해결할 수 있게 하며, 주어진 문제의 제약 조건을 만족합니다.

## 코드
```python
import sys
from collections import defaultdict

def count_zero_sum_pairs(A, B, C, D):
    # 합이 발생하는 빈도를 저장할 해시맵 생성
    AB_sum = defaultdict(int)
    
    # A와 B 배열의 모든 가능한 합을 계산하여 해시맵에 저장
    for a in A:
        for b in B:
            AB_sum[a + b] += 1
    
    count = 0
    
    # C와 D 배열의 모든 가능한 합을 계산
    # 해당 합의 음수가 AB_sum에 있는지 확인하여 카운트 증가
    for c in C:
        for d in D:
            target = -(c + d)
            if target in AB_sum:
                count += AB_sum[target]
    
    return count

input = sys.stdin.read
data = input().split()

# 첫 번째 값은 배열의 크기 n
n = int(data[0])
A, B, C, D = [], [], [], []
index = 1

# 각 배열에 값 채우기
for _ in range(n):
    A.append(int(data[index]))
    B.append(int(data[index+1]))
    C.append(int(data[index+2]))
    D.append(int(data[index+3]))
    index += 4

# 결과 계산 및 출력
result = count_zero_sum_pairs(A, B, C, D)
print(result)
```