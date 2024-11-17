# 첫 번째 줄에서 입력값 N과 K를 읽어온다.
# N은 전체 날짜의 수, K는 연속된 날짜의 수이다.
N, K = map(int, input().split())

# 두 번째 줄에서 온도를 나타내는 N개의 정수를 리스트로 읽어온다.
temperatures = list(map(int, input().split()))

# 처음 K일 동안의 온도의 합을 계산하여 current_sum 변수에 저장한다.
current_sum = sum(temperatures[:K])

# 초기 상태에서 current_sum 값을 최대 합으로 설정한다.
max_sum = current_sum

# K일 이후부터 N일까지 슬라이딩 윈도우 방식으로 최대 합을 계산한다.
for i in range(K, N):
    # 윈도우를 한 칸 오른쪽으로 이동시키며 새로운 합을 계산한다.
    # 이전 합에서 윈도우의 첫 번째 값을 빼고 새로운 값을 더한다.
    current_sum = current_sum - temperatures[i - K] + temperatures[i]

    # 계산된 합이 현재까지의 최대 합보다 크면 max_sum을 갱신한다.
    max_sum = max(max_sum, current_sum)

# 최종적으로 연속된 K일 동안의 최대 합을 출력한다.
print(max_sum)
