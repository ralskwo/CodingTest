import heapq
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.read 사용
input = sys.stdin.read
data = input().splitlines()

# 첫 줄에서 강의 개수 N 입력 받기
N = int(data[0])

# 강의 정보를 저장할 리스트 선언
lectures = []

# 두 번째 줄부터 각 강의의 번호, 시작 시간, 종료 시간을 읽어서 리스트에 저장
for i in range(1, N + 1):
    _, start, end = map(int, data[i].split())
    lectures.append((start, end))

# 강의 시작 시간을 기준으로 정렬
# 시작 시간이 동일할 경우 종료 시간이 빠른 순서로 정렬됨
lectures.sort()

# 최소 종료 시간을 저장할 우선순위 큐 생성
min_heap = []

# 강의 정보를 순회하며 강의실 배정
for start, end in lectures:
    # 현재 강의의 시작 시간이 기존 강의실 중 가장 빨리 끝나는 강의의 종료 시간 이후라면
    if min_heap and min_heap[0] <= start:
        # 강의실을 재사용하므로 우선순위 큐에서 해당 종료 시간을 제거
        heapq.heappop(min_heap)
    # 현재 강의의 종료 시간을 우선순위 큐에 추가
    heapq.heappush(min_heap, end)

# 최종적으로 우선순위 큐에 남아있는 요소의 개수가 필요한 최소 강의실 개수
print(len(min_heap))
