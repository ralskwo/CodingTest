def fibonacci_counts(N):
    # N번째 피보나치 수를 계산할 때 0과 1이 각각 몇 번 출력되는지 구하는 함수
    
    # dp_zero는 N번째 피보나치 수를 계산할 때 0이 출력되는 횟수를 저장하는 리스트
    # dp_one은 N번째 피보나치 수를 계산할 때 1이 출력되는 횟수를 저장하는 리스트
    # 리스트의 크기를 N+1로 설정해 N까지의 값을 모두 저장할 수 있게 함
    dp_zero = [0] * (N + 1)
    dp_one = [0] * (N + 1)
    
    # 피보나치 수열에서 N이 0일 때, 0이 한 번 출력되고, 1은 출력되지 않음
    # 따라서 dp_zero[0]은 1, dp_one[0]은 0으로 초기화
    dp_zero[0] = 1
    dp_one[0] = 0
    
    # 피보나치 수열에서 N이 1일 때, 1이 한 번 출력되고, 0은 출력되지 않음
    # 따라서 dp_zero[1]은 0, dp_one[1]은 1로 초기화
    if N > 0:
        dp_zero[1] = 0
        dp_one[1] = 1
    
    # 피보나치 수열의 특성에 따라 dp_zero[i]는 dp_zero[i-1]과 dp_zero[i-2]의 합이 됨
    # 마찬가지로 dp_one[i]도 dp_one[i-1]과 dp_one[i-2]의 합이 됨
    # 이를 통해 피보나치 수를 계산하는 과정에서 0과 1이 출력되는 횟수를 누적하여 계산
    for i in range(2, N + 1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]
    
    # 주어진 N에 대해 0과 1이 각각 몇 번 출력되었는지를 반환
    return dp_zero[N], dp_one[N]

# 테스트 케이스의 수 T를 입력받음
T = int(input())

# 결과를 저장할 리스트 초기화
results = []

# 각 테스트 케이스에서 피보나치 수 N을 입력받음
for _ in range(T):
    N = int(input())
    
    # 입력받은 N에 대해 0과 1의 출력 횟수를 계산
    zero_count, one_count = fibonacci_counts(N)
    
    # 계산된 결과를 "0의 출력 횟수 1의 출력 횟수" 형식으로 results 리스트에 저장
    results.append(f"{zero_count} {one_count}")

# 모든 테스트 케이스에 대해 저장된 결과를 한 줄씩 출력
for result in results:
    print(result)