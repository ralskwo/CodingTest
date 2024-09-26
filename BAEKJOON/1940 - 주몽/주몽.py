def count_armors(N, M, materials):
    # 재료 배열 정렬
    materials.sort()
    
    # 투 포인터 초기화
    left = 0
    right = N - 1
    count = 0
    
    # 투 포인터 방식으로 갑옷을 만들 수 있는 경우의 수를 셈
    while left < right:
        sum_value = materials[left] + materials[right]
        
        if sum_value == M:
            count += 1
            left += 1
            right -= 1
        elif sum_value < M:
            left += 1
        else:
            right -= 1
    
    return count

# 입력 받기
N = int(input())  # 재료의 개수
M = int(input())  # 갑옷을 만들기 위해 필요한 수
materials = list(map(int, input().split()))  # 재료의 고유 번호 리스트

# 결과 출력
print(count_armors(N, M, materials))
