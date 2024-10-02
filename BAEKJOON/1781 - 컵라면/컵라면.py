import heapq  # 힙 자료구조를 사용하기 위해 heapq 모듈을 임포트

n = int(input())  # 문제의 개수 N 입력받기
problems = []  # 각 문제의 (데드라인, 컵라면 수) 정보를 저장할 리스트 초기화

for _ in range(n):  # N개의 문제에 대해 반복하면서 데드라인과 컵라면 수를 입력받기
    deadline, ramen = map(int, input().split())  # 데드라인과 컵라면 수를 입력받아 변수에 저장
    problems.append((deadline, ramen))  # (데드라인, 컵라면 수) 형태로 리스트에 추가

problems.sort()  # 문제들을 데드라인 기준으로 오름차순 정렬 (같은 데드라인이면 자동으로 컵라면 수 기준 정렬됨)

ramen_heap = []  # 현재까지 풀기로 선택한 문제의 컵라면 수를 관리하기 위한 최소 힙 생성

for deadline, ramen in problems:  # 정렬된 문제 리스트를 하나씩 확인
    heapq.heappush(ramen_heap, ramen)  # 힙에 현재 문제의 컵라면 수를 추가
    
    # 힙의 길이가 현재 문제의 데드라인을 초과하면, 즉 데드라인 내에 풀 수 있는 문제 수를 초과하면
    if len(ramen_heap) > deadline:
        heapq.heappop(ramen_heap)  # 힙에서 가장 컵라면 수가 적은 문제를 제거하여 데드라인에 맞추기

# 최종적으로 힙에 남아 있는 문제들은 동호가 풀 수 있는 문제들이므로, 힙의 요소들을 합산하여 출력
print(sum(ramen_heap))  # 동호가 받을 수 있는 최대 컵라면 수 출력
