from itertools import combinations
from bisect import bisect_right

def get_subsets(weights):
    n = len(weights)  # 리스트의 길이(원소의 개수)를 변수 n에 저장
    subsets = []  # 부분 집합의 합을 저장할 빈 리스트 생성
    for i in range(n + 1):  # 부분 집합의 크기를 0부터 n까지 반복
        for comb in combinations(weights, i):  # 각 크기에 해당하는 모든 조합을 생성
            subsets.append(sum(comb))  # 조합의 합을 계산하여 subsets 리스트에 추가
    return subsets  # 계산된 부분 집합의 합 리스트를 반환

def count_valid_combinations(N, C, weights):
    left_weights = weights[:N//2]  # 리스트의 첫 번째 절반을 left_weights로 설정
    right_weights = weights[N//2:]  # 리스트의 나머지 절반을 right_weights로 설정

    left_subsets = get_subsets(left_weights)  # 왼쪽 절반의 부분 집합의 합 계산
    right_subsets = get_subsets(right_weights)  # 오른쪽 절반의 부분 집합의 합 계산

    right_subsets.sort()  # 이진 탐색을 위해 오른쪽 부분 집합의 합을 오름차순으로 정렬

    count = 0  # 가능한 조합의 수를 저장할 변수 초기화

    for left_sum in left_subsets:  # 왼쪽 부분 집합의 합을 하나씩 순회
        if left_sum <= C:  # 왼쪽 부분 집합의 합이 C 이하인 경우에만 처리
            count += bisect_right(right_subsets, C - left_sum)  
            # 오른쪽 부분 집합에서 left_sum과 합쳐서 C 이하가 되는 경우의 수를 이진 탐색으로 계산하여 count에 더함

    return count  # 최종 계산된 가능한 조합의 수 반환

N, C = map(int, input().split())  # 첫 번째 줄의 입력 값을 받아 N과 C에 저장
weights = list(map(int, input().split()))  # 두 번째 줄의 입력 값을 리스트로 받아 weights에 저장

print(count_valid_combinations(N, C, weights))  # 가능한 조합의 수를 계산하여 출력
