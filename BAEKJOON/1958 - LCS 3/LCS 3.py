def longest_common_subsequence(str1, str2, str3):
    # 각 문자열의 길이를 구한다.
    len1, len2, len3 = len(str1), len(str2), len(str3)

    # 3차원 DP 테이블을 생성하고, 초기값은 모두 0으로 설정한다.
    # dp[i][j][k]는 str1의 i번째 문자까지, str2의 j번째 문자까지, str3의 k번째 문자까지의 LCS 길이를 의미한다.
    dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for __ in range(len1 + 1)]

    # 세 문자열의 각 문자를 비교하여 DP 테이블을 채운다.
    for i in range(1, len1 + 1):  # 첫 번째 문자열의 길이만큼 반복
        for j in range(1, len2 + 1):  # 두 번째 문자열의 길이만큼 반복
            for k in range(1, len3 + 1):  # 세 번째 문자열의 길이만큼 반복
                # 현재 위치의 세 문자가 모두 같으면 이전 상태의 값에서 1을 더한다.
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                # 그렇지 않다면, 가능한 세 가지 경우 중 최대값을 선택한다.
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    # 최종 결과값은 dp[len1][len2][len3]에 저장되어 있다.
    return dp[len1][len2][len3]


# 첫 번째 문자열 입력을 받는다.
str1 = input().strip()
# 두 번째 문자열 입력을 받는다.
str2 = input().strip()
# 세 번째 문자열 입력을 받는다.
str3 = input().strip()

# 세 문자열의 LCS 길이를 계산하여 출력한다.
print(longest_common_subsequence(str1, str2, str3))
