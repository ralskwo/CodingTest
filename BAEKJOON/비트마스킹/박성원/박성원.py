from math import gcd

def solve():
    N = int(input().strip())  # 집합의 수의 개수를 입력받습니다.
    numbers = [input().strip() for _ in range(N)]  # 집합에 포함된 수들을 입력받아 리스트에 저장합니다.
    K = int(input().strip())  # 정수 K를 입력받습니다.

    mod_numbers = []  # 각 숫자를 K로 나눈 나머지를 저장할 리스트입니다.
    for num in numbers:
        mod_numbers.append(int(num) % K)  # 각 숫자를 K로 나눈 나머지를 리스트에 추가합니다.
    
    power_of_10 = [1] * 51  # 10의 거듭제곱을 K로 나눈 나머지를 저장할 리스트입니다.
    for i in range(1, 51):
        power_of_10[i] = (power_of_10[i-1] * 10) % K  # 10^i % K를 계산하여 리스트에 저장합니다.

    dp = [[0] * K for _ in range(1 << N)]  # DP 테이블을 초기화합니다. 크기는 (2^N) x K입니다.
    dp[0][0] = 1  # 초기 상태: 아무 숫자도 사용하지 않았을 때 나머지가 0인 경우의 수는 1입니다.

    for mask in range(1 << N):  # 모든 비트마스크(숫자의 사용 여부를 나타내는 상태)를 순회합니다.
        for rem in range(K):  # 모든 나머지 값에 대해 순회합니다.
            if dp[mask][rem] == 0:  # 현재 상태에서 가능한 경우의 수가 0이라면, 스킵합니다.
                continue
            for i in range(N):  # 집합의 각 숫자에 대해 반복합니다.
                if not (mask & (1 << i)):  # i번째 숫자가 사용되지 않았다면,
                    new_mask = mask | (1 << i)  # i번째 숫자를 사용한 새로운 비트마스크를 만듭니다.
                    new_rem = (rem * power_of_10[len(numbers[i])] + mod_numbers[i]) % K  # 새로운 나머지를 계산합니다.
                    dp[new_mask][new_rem] += dp[mask][rem]  # 새로운 상태에서의 경우의 수를 갱신합니다.

    p = dp[(1 << N) - 1][0]  # 모든 숫자를 사용했을 때 나머지가 0인 경우의 수를 p로 설정합니다.
    q = 1  # 전체 경우의 수를 계산하기 위해 초기값 1로 설정합니다.
    for i in range(2, N + 1):
        q *= i  # 전체 순열의 개수 (N!)을 계산합니다.

    if p == 0:  # 만약 나머지가 0인 경우의 수가 없다면,
        print("0/1")  # 0/1을 출력합니다.
    else:
        divisor = gcd(p, q)  # 기약분수를 만들기 위해 p와 q의 최대공약수를 계산합니다.
        print(f"{p // divisor}/{q // divisor}")  # 기약분수 형태로 출력합니다.

solve()  # 함수 실행