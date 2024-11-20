def max_sticker_score(test_cases):
    # 결과를 저장할 리스트를 초기화
    results = []

    # 각 테스트 케이스에 대해 반복
    for stickers in test_cases:
        # 스티커 열의 개수를 계산
        n = len(stickers[0])

        # 열의 개수가 1인 경우 처리
        if n == 1:
            results.append(max(stickers[0][0], stickers[1][0]))
            continue

        # 두 열 전의 결과를 저장할 배열 초기화 (dp[i-2])
        dp_prev = [0, 0]
        # 한 열 전의 결과를 저장할 배열 초기화 (dp[i-1])
        dp_curr = [stickers[0][0], stickers[1][0]]

        # 두 번째 열부터 마지막 열까지 반복
        for i in range(1, n):
            # 현재 열에서 얻을 수 있는 최대 점수 계산
            new_dp = [
                max(dp_curr[1], dp_prev[1])
                + stickers[0][i],  # 위쪽 행의 현재 열 점수 계산
                max(dp_curr[0], dp_prev[0])
                + stickers[1][i],  # 아래쪽 행의 현재 열 점수 계산
            ]
            # 이전 두 열 값을 갱신
            dp_prev = dp_curr
            dp_curr = new_dp

        # 현재 열에서 최대 점수를 결과 리스트에 추가
        results.append(max(dp_curr))

    # 모든 테스트 케이스에 대해 계산된 결과 반환
    return results


# 테스트 케이스의 개수를 입력받음
t = int(input())
# 각 테스트 케이스를 저장할 리스트 초기화
test_cases = []

# 각 테스트 케이스를 입력받아 저장
for _ in range(t):
    # 열의 개수를 입력받음
    n = int(input())
    # 위쪽 행 스티커 점수를 입력받음
    row1 = list(map(int, input().split()))
    # 아래쪽 행 스티커 점수를 입력받음
    row2 = list(map(int, input().split()))
    # 위쪽 행과 아래쪽 행을 한 쌍으로 리스트에 추가
    test_cases.append([row1, row2])

# 각 테스트 케이스에 대해 최대 점수를 계산
results = max_sticker_score(test_cases)

# 계산된 결과를 한 줄씩 출력
for result in results:
    print(result)
