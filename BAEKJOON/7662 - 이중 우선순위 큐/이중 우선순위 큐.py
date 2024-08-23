import heapq
import sys

# 표준 입력을 읽기 위해 사용
input = sys.stdin.read

# 입력 데이터를 공백을 기준으로 나누어 리스트로 변환
data = input().split()

# 테스트 케이스의 수를 읽음
index = 0
T = int(data[index])
index += 1

# 결과를 저장할 리스트 초기화
results = []

# 각 테스트 케이스를 처리
for _ in range(T):
    # 각 테스트 케이스에서 명령어의 수를 읽음
    k = int(data[index])
    index += 1

    # 최대 힙과 최소 힙을 초기화
    max_heap = []
    min_heap = []

    # 삽입된 원소의 개수를 추적하기 위한 딕셔너리와 카운터 초기화
    entry_finder = {}
    count = 0

    # 각 명령어를 처리
    for _ in range(k):
        # 명령어와 값을 읽음
        command = data[index]
        value = int(data[index + 1])
        index += 2

        if command == 'I':  # 삽입 연산
            # 최소 힙과 최대 힙에 각각 삽입
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            # 삽입된 값을 기록
            entry_finder[value] = entry_finder.get(value, 0) + 1
            count += 1
        elif command == 'D':  # 삭제 연산
            if count == 0:
                continue
            if value == 1:  # 최대값 삭제
                # 유효하지 않은 최대 힙의 루트를 제거
                while max_heap and entry_finder[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    # 최대값을 제거하고 기록 업데이트
                    max_value = -heapq.heappop(max_heap)
                    entry_finder[max_value] -= 1
                    count -= 1
            elif value == -1:  # 최소값 삭제
                # 유효하지 않은 최소 힙의 루트를 제거
                while min_heap and entry_finder[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    # 최소값을 제거하고 기록 업데이트
                    min_value = heapq.heappop(min_heap)
                    entry_finder[min_value] -= 1
                    count -= 1

    # 유효하지 않은 최소 힙의 루트를 제거
    while min_heap and entry_finder[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    # 유효하지 않은 최대 힙의 루트를 제거
    while max_heap and entry_finder[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if count == 0:
        # 큐가 비어 있으면 "EMPTY"를 결과에 추가
        results.append("EMPTY")
    else:
        # 큐에 값이 있으면 최대값과 최소값을 결과에 추가
        results.append(f"{-max_heap[0]} {min_heap[0]}")

# 모든 결과를 출력
for result in results:
    print(result)
