def min_total_distance(N, K, sensors):
    # 집중국의 수가 센서의 개수 이상이면 모든 센서를 개별적으로 커버할 수 있으므로 거리 합은 0
    if K >= N:
        return 0

    # 센서 좌표를 오름차순으로 정렬하여 계산을 간단하게 만듦
    sensors.sort()

    # 인접한 센서들 간의 거리 차이를 저장할 리스트 생성
    distances = []
    for i in range(1, N):
        # 각 센서 간의 거리를 계산하여 distances 리스트에 추가
        distances.append(sensors[i] - sensors[i - 1])

    # 거리를 내림차순으로 정렬하여 가장 큰 간격부터 처리 가능하게 함
    distances.sort(reverse=True)

    # 집중국이 K개라면, 가장 큰 K-1개의 간격을 제거
    for _ in range(K - 1):
        distances.pop(0)

    # 남은 간격의 합을 반환하여 최종 최소 거리 합을 계산
    return sum(distances)


# 첫 번째 입력: 센서의 개수
N = int(input().strip())

# 두 번째 입력: 집중국의 개수
K = int(input().strip())

# 세 번째 입력: 센서의 좌표들
sensors = list(map(int, input().strip().split()))

# 최종 계산 결과를 출력
print(min_total_distance(N, K, sensors))
