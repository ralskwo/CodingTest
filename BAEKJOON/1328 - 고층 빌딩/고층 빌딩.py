MOD = 1000000007  # 결과 값을 나눌 모듈러 값 설정


def count_building_arrangements(N, L, R):
    # DP 테이블 초기화: dp[n][l][r]는 빌딩 n개일 때 왼쪽에서 l개, 오른쪽에서 r개 보이는 경우의 수
    dp = [[[0] * (R + 1) for _ in range(L + 1)] for _ in range(N + 1)]

    # 초기 조건: 빌딩이 하나일 때 왼쪽과 오른쪽에서 각각 하나씩 보이는 경우는 1가지
    dp[1][1][1] = 1

    # 동적 계획법을 이용해 dp 테이블 채우기
    for n in range(2, N + 1):  # 빌딩 개수를 2부터 N까지 순회
        for l in range(1, L + 1):  # 왼쪽에서 보이는 빌딩 개수를 1부터 L까지 순회
            for r in range(1, R + 1):  # 오른쪽에서 보이는 빌딩 개수를 1부터 R까지 순회
                # 새로운 빌딩이 가장 왼쪽에 추가되어 왼쪽에서 보이는 빌딩 개수가 늘어나는 경우
                left_visible = dp[n - 1][l - 1][r]
                # 새로운 빌딩이 가장 오른쪽에 추가되어 오른쪽에서 보이는 빌딩 개수가 늘어나는 경우
                right_visible = dp[n - 1][l][r - 1]
                # 새로운 빌딩이 중간에 위치하여 보이는 빌딩 개수가 변화하지 않는 경우
                middle_visible = (n - 2) * dp[n - 1][l][r]
                # 위 세 가지 경우를 더하여 현재 상태의 경우의 수 계산
                dp[n][l][r] = (left_visible + right_visible + middle_visible) % MOD

    # 계산된 경우의 수 반환
    return dp[N][L][R]


# 입력값 읽기
N, L, R = map(int, input().split())

# 결과 출력
print(count_building_arrangements(N, L, R))
