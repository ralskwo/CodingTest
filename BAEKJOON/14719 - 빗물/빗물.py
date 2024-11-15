def calculate_trapped_rainwater(H, W, heights):
    # 왼쪽 최대 높이를 저장할 리스트를 0으로 초기화하여 생성
    left_max = [0] * W
    # 오른쪽 최대 높이를 저장할 리스트를 0으로 초기화하여 생성
    right_max = [0] * W
    
    # 첫 번째 위치의 왼쪽 최대 높이는 그 위치의 높이로 설정
    left_max[0] = heights[0]
    # 두 번째 위치부터 끝까지 각 위치의 왼쪽 최대 높이를 계산
    for i in range(1, W):
        # 현재 위치의 왼쪽 최대 높이는 이전 위치의 최대 높이와 현재 높이 중 큰 값
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # 마지막 위치의 오른쪽 최대 높이는 그 위치의 높이로 설정
    right_max[W - 1] = heights[W - 1]
    # 마지막에서 두 번째 위치부터 첫 번째 위치까지 각 위치의 오른쪽 최대 높이를 계산
    for i in range(W - 2, -1, -1):
        # 현재 위치의 오른쪽 최대 높이는 다음 위치의 최대 높이와 현재 높이 중 큰 값
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # 총 고이는 빗물의 양을 저장할 변수를 0으로 초기화
    total_water = 0
    # 각 위치에서 고일 수 있는 물의 양을 계산
    for i in range(W):
        # 현재 위치에서 고일 수 있는 빗물의 양은 왼쪽과 오른쪽 최대 높이 중 작은 값에서 현재 높이를 뺀 값
        water = min(left_max[i], right_max[i]) - heights[i]
        # 만약 물의 양이 양수일 경우에만 총 빗물 양에 추가
        if water > 0:
            total_water += water
    
    # 최종적으로 고일 수 있는 빗물의 총량을 반환
    return total_water

# 첫 줄의 입력값을 받아 세로 길이(H)와 가로 길이(W)로 저장
H, W = map(int, input().split())
# 두 번째 줄의 입력값을 받아 각 위치의 높이를 리스트로 저장
heights = list(map(int, input().split()))
# 고인 빗물의 총량을 계산하고 결과를 출력
print(calculate_trapped_rainwater(H, W, heights))
