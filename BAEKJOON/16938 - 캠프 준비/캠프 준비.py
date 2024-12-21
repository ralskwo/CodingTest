from itertools import (
    combinations,
)  # itertools의 combinations를 사용해 가능한 모든 조합 생성


def count_valid_combinations(N, L, R, X, A):
    count = 0  # 조건을 만족하는 조합의 개수를 저장할 변수 초기화

    for i in range(2, N + 1):  # 최소 두 문제 이상 선택해야 하므로 2부터 N까지 반복
        for comb in combinations(
            A, i
        ):  # 난이도 리스트 A에서 i개의 문제를 선택하는 모든 조합 생성
            total = sum(comb)  # 현재 선택된 조합의 난이도 합 계산
            if (
                L <= total <= R and max(comb) - min(comb) >= X
            ):  # 난이도 합이 L 이상 R 이하이고, 난이도 차이가 X 이상인지 확인
                count += 1  # 조건을 만족하면 카운트 증가

    return count  # 최종적으로 조건을 만족하는 조합의 개수를 반환


N, L, R, X = map(
    int, input().split()
)  # 문제 개수 N, 난이도 합의 최소 L, 최대 R, 최소 난이도 차이 X 입력
A = list(map(int, input().split()))  # 각 문제의 난이도를 리스트 A로 입력받음

print(count_valid_combinations(N, L, R, X, A))  # 조건을 만족하는 조합의 개수를 출력
