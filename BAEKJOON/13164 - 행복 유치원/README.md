def minimum_cost(N, K, heights): # 원생들의 키 차이를 저장할 리스트를 계산한다 # 인접한 두 원생의 키 차이를 계산하여 differences 리스트에 저장한다
differences = [heights[i + 1] - heights[i] for i in range(N - 1)]

    # 키 차이 리스트를 내림차순으로 정렬한다
    # 큰 차이를 먼저 제거하기 위해 정렬을 수행한다
    differences.sort(reverse=True)

    # K-1개의 큰 키 차이를 제거한 뒤 남은 차이들의 합을 반환한다
    # 남은 차이의 합이 티셔츠 비용의 최소값이 된다
    return sum(differences[K-1:])

# 입력 값을 받아서 N에는 원생 수, K에는 조의 개수를 저장한다

N, K = map(int, input().split())

# 원생들의 키를 입력받아 heights 리스트에 저장한다

heights = list(map(int, input().split()))

# 최소 티셔츠 비용을 계산하여 출력한다

print(minimum_cost(N, K, heights))
