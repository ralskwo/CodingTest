def find_closest_to_zero_pair(N, properties):
    # 리스트를 정렬합니다.
    properties.sort()
    left, right = 0, N - 1  # 왼쪽 포인터와 오른쪽 포인터 초기화
    closest_pair = (properties[left], properties[right])
    closest_sum = abs(properties[left] + properties[right])
    
    # 투 포인터를 사용하여 합이 0에 가장 가까운 두 용액을 찾습니다.
    while left < right:
        current_sum = properties[left] + properties[right]
        
        # 현재 합이 더 0에 가까운 경우 업데이트합니다.
        if abs(current_sum) < closest_sum:
            closest_sum = abs(current_sum)
            closest_pair = (properties[left], properties[right])
        
        # 현재 합이 0보다 작으면 left 포인터를 오른쪽으로 이동
        if current_sum < 0:
            left += 1
        # 현재 합이 0보다 크면 right 포인터를 왼쪽으로 이동
        elif current_sum > 0:
            right -= 1
        # 현재 합이 0이면 가장 가까운 값을 찾은 것이므로 반복을 종료
        else:
            break
    
    return closest_pair

N = int(input().strip())
properties = list(map(int, input().strip().split()))

# 가장 가까운 두 용액의 특성값을 찾습니다.
result = find_closest_to_zero_pair(N, properties)

# 결과를 출력합니다.
print(result[0], result[1])
