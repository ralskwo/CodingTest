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
