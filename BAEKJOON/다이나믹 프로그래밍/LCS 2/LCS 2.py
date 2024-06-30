def lcs(X, Y):
    m = len(X)  # 첫 번째 문자열의 길이
    n = len(Y)  # 두 번째 문자열의 길이

    # DP 테이블 생성 (0으로 초기화된 (m+1)x(n+1) 배열)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1  # 문자가 같으면 대각선 위 + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])  # 문자가 다르면 위 또는 왼쪽 값 중 큰 값

    # LCS의 길이
    length_of_lcs = L[m][n]

    # LCS 문자열 구성 (역추적)
    index = L[m][n]
    lcs = [""] * index  # LCS 문자열을 저장할 리스트
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]  # 공통 문자를 LCS 리스트에 저장
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1  # 위쪽 값이 더 크면 위로 이동
        else:
            j -= 1  # 왼쪽 값이 더 크면 왼쪽으로 이동

    return length_of_lcs, "".join(lcs)  # LCS의 길이와 LCS 문자열을 반환

# 입력 받기
X = input().strip()
Y = input().strip()

# 함수 호출 및 결과 출력
length_of_lcs, lcs_str = lcs(X, Y)
print(length_of_lcs)  # LCS의 길이 출력
if length_of_lcs > 0:
    print(lcs_str)  # LCS 문자열 출력
