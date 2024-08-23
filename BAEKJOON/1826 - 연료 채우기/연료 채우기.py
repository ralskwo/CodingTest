import heapq  # 우선순위 큐를 사용하기 위한 힙큐 모듈을 임포트
import sys  # 표준 입력을 사용하기 위한 시스템 모듈 임포트

input = sys.stdin.read  # 표준 입력을 한 번에 읽어오는 함수로 정의

def minimum_refuel_stops(N, stations, L, P):
    # 주유소 리스트에 도착지 정보를 추가 (도착지는 연료를 제공하지 않음)
    stations.append((L, 0))
    # 주유소를 위치 순으로 정렬
    stations.sort()

    # 최대 힙으로 사용할 리스트와 기타 변수 초기화
    max_heap = []
    refuels = 0  # 주유 횟수
    current_fuel = P  # 현재 연료량
    prev_location = 0  # 이전 위치 (시작점은 0)

    for location, fuel in stations:
        # 현재 위치까지 도달하기 위해 필요한 연료를 소모
        current_fuel -= (location - prev_location)
        # 연료가 부족할 경우, 최대 힙에서 연료를 보충
        while max_heap and current_fuel < 0:
            current_fuel += -heapq.heappop(max_heap)  # 최대 힙에서 연료를 추출하여 보충
            refuels += 1  # 주유 횟수 증가
        # 여전히 연료가 부족하면 도착할 수 없음을 의미
        if current_fuel < 0:
            return -1
        # 현재 주유소에서 얻을 수 있는 연료를 최대 힙에 추가 (음수로 추가하여 최대 힙처럼 사용)
        heapq.heappush(max_heap, -fuel)
        # 이전 위치를 현재 위치로 업데이트
        prev_location = location
    
    return refuels  # 최소 주유 횟수를 반환

# 입력 처리
data = input().split()  # 표준 입력을 공백 기준으로 나누어 리스트로 저장
N = int(data[0])  # 첫 번째 값은 주유소의 개수
stations = []
for i in range(N):
    a, b = int(data[2 * i + 1]), int(data[2 * i + 2])  # 각 주유소의 위치와 연료량
    stations.append((a, b))

L = int(data[-2])  # 마지막에서 두 번째 값은 도착지의 위치
P = int(data[-1])  # 마지막 값은 시작 시 트럭의 연료량

# 결과 출력
result = minimum_refuel_stops(N, stations, L, P)
print(result)
