def find_a_and_b(D, K):
    # D일째까지의 계수를 저장할 리스트 초기화
    coeff = [[0, 0] for _ in range(D + 1)]

    # 첫째 날 떡 개수는 A, 둘째 날 떡 개수는 B로 표현
    coeff[1] = [1, 0]
    coeff[2] = [0, 1]

    # 셋째 날부터 D일까지의 계수를 계산
    for i in range(3, D + 1):
        # i번째 날 A와 B의 계수는 이전 두 날의 계수의 합
        coeff[i][0] = coeff[i - 2][0] + coeff[i - 1][0]
        coeff[i][1] = coeff[i - 2][1] + coeff[i - 1][1]

    # D일째 떡 개수 K를 만족하기 위해 필요한 계수
    a_coeff = coeff[D][0]
    b_coeff = coeff[D][1]

    # 가능한 A 값을 1부터 탐색하여 K를 만족하는 A와 B를 찾음
    for A in range(1, K // a_coeff + 1):
        # K에서 A에 대한 값을 뺀 나머지가 B에 의해 나눠떨어지면 유효한 B를 찾음
        if (K - A * a_coeff) % b_coeff == 0:
            B = (K - A * a_coeff) // b_coeff
            return A, B


# 입력값을 읽어와 D와 K에 저장
D, K = map(int, input().split())

# 주어진 D와 K에 대해 A와 B를 계산
A, B = find_a_and_b(D, K)

# 계산된 A와 B를 출력
print(A)
print(B)
