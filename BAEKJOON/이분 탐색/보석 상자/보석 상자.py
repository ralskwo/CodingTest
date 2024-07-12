def can_distribute(j, jewel_counts, n):
    # 주어진 질투심 j로 보석을 n명에게 나눌 수 있는지 확인하는 함수
    total_students = 0  # 필요한 학생 수를 초기화
    for count in jewel_counts:
        # 각 색상마다 보석을 주어진 질투심 기준으로 나누는 학생 수 계산
        total_students += -(-count // j)  # math.ceil(count / j)와 동일
        if total_students > n:
            # 필요한 학생 수가 n보다 크면 나눌 수 없음
            return False
    return True

def find_min_jealousy(n, m, jewel_counts):
    # 질투심의 최소값을 찾는 함수 (이진 탐색)
    left, right = 1, max(jewel_counts)  # 초기 범위 설정
    while left < right:
        mid = (left + right) // 2  # 중간값 계산
        if can_distribute(mid, jewel_counts, n):
            right = mid  # 나눌 수 있으면 범위를 줄임
        else:
            left = mid + 1  # 나눌 수 없으면 범위를 늘림
    return left

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
jewel_counts = list(map(int, data[2:]))

# 질투심의 최소값 찾기
result = find_min_jealousy(n, m, jewel_counts)
print(result)
