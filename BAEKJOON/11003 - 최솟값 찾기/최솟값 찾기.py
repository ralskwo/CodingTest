from collections import deque

# N과 L을 입력받는다. N은 수열의 길이, L은 슬라이딩 윈도우의 크기
N, L = map(int, input().split())

# N개의 수열 A를 입력받는다.
A = list(map(int, input().split()))

# 덱(deque) 자료 구조를 초기화한다. 이 덱은 윈도우의 인덱스를 저장하는 데 사용된다.
dq = deque()

# 결과값을 저장할 리스트를 초기화한다.
result = []

# 수열의 각 원소에 대해 반복문을 실행한다.
for i in range(N):
    # 덱의 첫 번째 요소가 현재 윈도우의 범위를 벗어나면 제거한다.
    if dq and dq[0] < i - L + 1:
        dq.popleft()

    # 새로운 값이 들어올 때, 덱의 마지막 값이 현재 값보다 크면 덱에서 제거한다.
    # 이렇게 하면 덱은 항상 최솟값을 유지하게 된다.
    while dq and A[dq[-1]] > A[i]:
        dq.pop()

    # 현재 인덱스를 덱에 추가한다.
    dq.append(i)

    # 덱의 첫 번째 값은 현재 윈도우에서의 최솟값을 가리키므로, 이를 결과 리스트에 추가한다.
    result.append(A[dq[0]])

# 결과 리스트의 값을 공백으로 구분하여 출력한다.
print(" ".join(map(str, result)))