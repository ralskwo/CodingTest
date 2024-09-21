def find_year(E, S, M):
    year = 1  # year 변수를 1로 초기화 (1년부터 시작)
    while True:  # 조건을 만족하는 연도를 찾을 때까지 무한 반복
        if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
            # year에서 E, S, M을 뺀 값이 각각 15, 28, 19로 나누어 떨어지면 그 year가 답
            return year  # 조건을 만족하면 해당 year 반환
        year += 1  # 조건을 만족하지 않으면 year를 1 증가시키고 계속 탐색

E, S, M = map(int, input().split())  # 입력값을 E, S, M으로 각각 나누어 정수로 변환

print(find_year(E, S, M))  # 조건을 만족하는 year를 찾아 출력
