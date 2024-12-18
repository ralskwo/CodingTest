def min_difficulty(t_cases):
    # 결과를 저장할 리스트 생성
    results = []
    for case in t_cases:
        # 각 테스트 케이스의 통나무 개수와 높이 배열을 가져옴
        N, heights = case
        # 통나무 높이를 오름차순으로 정렬
        heights.sort()

        # 통나무를 재배치할 배열 초기화
        arranged = [0] * N
        # 배열의 양 끝을 가리키는 포인터 초기화
        left, right = 0, N - 1

        # 정렬된 높이를 번갈아 배열에 배치
        for i, height in enumerate(heights):
            if i % 2 == 0:
                arranged[left] = height  # 왼쪽에 작은 값 배치
                left += 1
            else:
                arranged[right] = height  # 오른쪽에 큰 값 배치
                right -= 1

        # 난이도의 최댓값 계산
        max_diff = 0
        for i in range(N):
            # 현재 통나무와 다음 통나무 간의 높이 차 계산
            max_diff = max(max_diff, abs(arranged[i] - arranged[(i + 1) % N]))

        # 계산된 난이도를 결과 리스트에 추가
        results.append(max_diff)
    return results


# 테스트 케이스 개수 입력 받음
T = int(input())
# 각 테스트 케이스를 저장할 리스트
t_cases = []
for _ in range(T):
    # 통나무 개수와 높이를 입력 받음
    N = int(input())
    heights = list(map(int, input().split()))
    t_cases.append((N, heights))

# 각 테스트 케이스의 최소 난이도를 계산
results = min_difficulty(t_cases)
for result in results:
    # 결과를 한 줄씩 출력
    print(result)
