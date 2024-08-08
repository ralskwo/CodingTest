def can_withdraw_with_k(k, daily_usage, N, M):
    count = 1  # 인출 횟수 초기값은 1로 설정
    current_sum = 0  # 현재 인출 금액의 합 초기값은 0으로 설정
    
    for usage in daily_usage:  # 매일 사용할 금액을 순회하며
        if current_sum + usage > k:  # 현재 인출 금액에 오늘 사용할 금액을 더했을 때 k를 초과하면
            count += 1  # 인출 횟수를 증가시킨다
            current_sum = usage  # 현재 인출 금액을 오늘 사용할 금액으로 초기화
            if count > M:  # 인출 횟수가 M을 초과하면
                return False  # False를 반환하여 주어진 k로 인출이 불가능함을 알린다
        else:
            current_sum += usage  # k를 초과하지 않으면 현재 인출 금액에 오늘 사용할 금액을 더한다
            
    return True  # 모든 사용 금액을 k 이내에서 M번 이하로 인출할 수 있으면 True를 반환

def find_minimum_k(N, M, daily_usage):
    low = max(daily_usage)  # 최소 금액 K의 초기값은 매일 사용하는 금액 중 최대값으로 설정
    high = sum(daily_usage)  # 최대 금액 K의 초기값은 모든 날의 사용 금액의 합으로 설정
    
    while low < high:  # 이분 탐색을 통해 적절한 K를 찾는다
        mid = (low + high) // 2  # 중간값을 계산
        if can_withdraw_with_k(mid, daily_usage, N, M):  # 중간값으로 인출이 가능한지 확인
            high = mid  # 가능하면 상한값을 중간값으로 설정
        else:
            low = mid + 1  # 불가능하면 하한값을 중간값+1로 설정
            
    return low  # 최소 금액 K를 반환

# 입력
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])  # 첫 번째 줄의 첫 번째 숫자는 N
M = int(data[1])  # 첫 번째 줄의 두 번째 숫자는 M
daily_usage = list(map(int, data[2:]))  # 나머지 숫자들은 매일 사용할 금액

# 최소 금액 K 계산
minimum_k = find_minimum_k(N, M, daily_usage)

# 출력
print(minimum_k)  # 최소 금액 K를 출력
