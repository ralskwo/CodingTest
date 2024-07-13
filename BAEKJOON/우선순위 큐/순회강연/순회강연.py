import heapq  # 힙큐 모듈을 불러옵니다. 이 모듈을 사용하여 우선순위 큐를 구현합니다.
import sys  # 시스템 모듈을 불러옵니다.

def solve():
    input = sys.stdin.readline  # 표준 입력을 한 줄씩 읽는 함수를 설정합니다.
    
    n = int(input().strip())  # 첫 줄에서 정수 n을 입력 받아 공백을 제거하고 정수로 변환합니다.
    
    lectures = []  # 강연 정보를 저장할 리스트를 초기화합니다.
    for _ in range(n):
        p, d = map(int, input().strip().split())  # 각 줄에서 강연료 p와 강연 가능 일수 d를 입력받아 정수로 변환합니다.
        lectures.append((p, d))  # 강연료와 강연 가능 일수를 튜플로 저장합니다.
    
    # 강연료를 기준으로 내림차순 정렬합니다.
    lectures.sort(reverse=True, key=lambda x: x[0])
    
    # 강연 가능한 날들을 집합으로 관리합니다. 가능한 최대 일수인 10000일까지 초기화합니다.
    days = set(range(1, 10001))
    
    total_value = 0  # 챙길 수 있는 강연료의 합의 최대값을 저장할 변수를 초기화합니다.
    for p, d in lectures:
        # 가능한 날 중 가장 가까운 날에 강연을 배정합니다.
        for day in range(d, 0, -1):
            if day in days:  # 현재 날이 강연 가능한 날들에 포함되어 있는지 확인합니다.
                days.remove(day)  # 배정된 날은 집합에서 제거합니다.
                total_value += p  # 총 강연료에 현재 강연료를 더합니다.
                break  # 강연을 배정했으므로 더 이상 반복하지 않습니다.
    
    print(total_value)  # 최종적으로 챙길 수 있는 강연료의 합의 최대값을 출력합니다.

if __name__ == "__main__":
    solve()
