def minimum_time_to_finish(n, m, times):
    # 초기 최소 시간과 최대 시간을 설정
    left = 1
    right = max(times) * m
    answer = right

    # 이분 탐색을 통해 최소 시간을 찾음
    while left <= right:
        mid = (left + right) // 2
        total = 0

        # 현재 중간 시간(mid) 내에 모든 친구들이 심사를 받을 수 있는지 계산
        for time in times:
            total += mid // time

        # 총 심사받은 친구 수가 m 이상이면 시간 줄이기 시도
        if total >= m:
            answer = mid
            right = mid - 1
        # 총 심사받은 친구 수가 m보다 적으면 시간 늘리기 시도
        else:
            left = mid + 1

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    times = list(map(int, data[2:2 + n]))
    
    result = minimum_time_to_finish(n, m, times)
    print(result)
