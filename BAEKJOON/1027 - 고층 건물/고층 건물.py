def count_visible_buildings(N, heights):
    # 두 빌딩이 서로 보이는지 여부를 판단하는 함수
    def is_visible(i, j):
        # 두 빌딩 i, j 사이의 기울기 계산
        slope = (heights[j] - heights[i]) / (j - i)
        # i와 j 사이에 있는 모든 빌딩을 확인
        for k in range(i + 1, j):
            # k번 빌딩이 i에서 j로 가는 선분 위나 위쪽에 있는 경우 가려짐
            if heights[k] >= heights[i] + slope * (k - i):
                return False
        # 가려지지 않으면 두 빌딩은 서로 보임
        return True

    # 최대 보이는 빌딩 수를 저장하는 변수
    max_count = 0

    # 각 빌딩을 기준으로 보이는 빌딩 수 계산
    for i in range(N):
        # 현재 빌딩에서 보이는 빌딩 수 초기화
        visible_count = 0

        # 현재 빌딩의 왼쪽에 있는 빌딩을 확인
        for j in range(i - 1, -1, -1):
            # i번 빌딩에서 j번 빌딩이 보이는 경우 카운트 증가
            if is_visible(j, i):
                visible_count += 1

        # 현재 빌딩의 오른쪽에 있는 빌딩을 확인
        for j in range(i + 1, N):
            # i번 빌딩에서 j번 빌딩이 보이는 경우 카운트 증가
            if is_visible(i, j):
                visible_count += 1

        # 최대 보이는 빌딩 수 갱신
        max_count = max(max_count, visible_count)

    # 모든 빌딩에 대해 계산한 결과 중 가장 큰 값을 반환
    return max_count


# 빌딩의 개수 입력
N = int(input())
# 빌딩의 높이 입력
heights = list(map(int, input().split()))
# 결과 출력
print(count_visible_buildings(N, heights))
