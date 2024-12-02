def min_remove_wires(n, connections):
    # 전깃줄을 A 전봇대의 위치를 기준으로 정렬
    connections.sort()

    # LIS를 저장하기 위한 dp 배열 초기화
    dp = []
    for _, b in connections:
        # 현재 B 전봇대 위치를 LIS 배열에서 이분 탐색
        idx = binary_search(dp, b)
        # LIS 배열의 끝에 추가할 경우
        if idx == len(dp):
            dp.append(b)
        # LIS 배열의 기존 위치를 갱신할 경우
        else:
            dp[idx] = b

    # 전체 전깃줄에서 LIS의 길이를 빼서 제거해야 하는 전깃줄의 최소 개수 반환
    return n - len(dp)


def binary_search(dp, target):
    # 이분 탐색을 위한 시작과 끝 인덱스 초기화
    low, high = 0, len(dp)
    while low < high:
        # 중간 인덱스 계산
        mid = (low + high) // 2
        # 중간 값이 목표 값보다 작은 경우 오른쪽으로 탐색
        if dp[mid] < target:
            low = mid + 1
        # 중간 값이 목표 값 이상인 경우 왼쪽으로 탐색
        else:
            high = mid
    # 목표 값이 들어갈 위치 반환
    return low


# 전깃줄의 개수를 입력받음
n = int(input())

# 전깃줄의 연결 정보를 입력받아 리스트로 저장
connections = [tuple(map(int, input().split())) for _ in range(n)]

# 제거해야 하는 전깃줄의 최소 개수를 계산하고 출력
print(min_remove_wires(n, connections))
