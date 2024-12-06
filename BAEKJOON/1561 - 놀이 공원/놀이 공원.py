def find_last_ride(N, M, ride_times):
    # 이분 탐색의 시작 범위를 설정. 놀이기구에 탑승하는 최소 시간은 0, 최대 시간은 2000000000 * 30
    left, right = 0, 2000000000 * 30

    # 이분 탐색을 통해 마지막 아이가 탑승 가능한 최소 시간을 찾음
    while left < right:
        # 중간 시간 계산
        mid = (left + right) // 2

        # 현재 중간 시간(mid)까지 탑승할 수 있는 총 아이의 수를 계산
        total = sum(mid // time + 1 for time in ride_times)

        # 만약 총 탑승 가능한 아이 수가 N보다 크거나 같다면 더 작은 시간으로 범위를 줄임
        if total >= N:
            right = mid
        # 그렇지 않다면 더 큰 시간으로 범위를 늘림
        else:
            left = mid + 1

    # 최종적으로 찾은 최소 시간
    T = left

    # T-1 시간까지 탑승한 총 아이 수를 계산
    total_before = sum((T - 1) // time + 1 for time in ride_times)

    # T 시간에 탑승할 수 있는 아이 중 몇 번째 아이가 마지막인지 계산
    remaining = N - total_before

    # 각 놀이기구를 순회하며 T 시간에 탑승 가능한 놀이기구를 확인
    for i, time in enumerate(ride_times):
        # 놀이기구가 T 시간에 비어 있는지 확인
        if T % time == 0:
            # 한 아이가 해당 놀이기구에 탑승하면 남은 아이 수를 줄임
            remaining -= 1
            # 남은 아이 수가 0이 되면 해당 놀이기구 번호를 반환
            if remaining == 0:
                return i + 1


# 첫 번째 줄에서 N과 M을 입력받음
N, M = map(int, input().split())

# 두 번째 줄에서 각 놀이기구의 운행 시간을 입력받음
ride_times = list(map(int, input().split()))

# 마지막 아이가 탑승하는 놀이기구 번호를 출력
print(find_last_ride(N, M, ride_times))
