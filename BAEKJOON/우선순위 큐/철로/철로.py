import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 임포트

def max_people_in_segment(n, positions, d):
    # 각 사람의 집과 사무실 위치를 받아서 시작점과 끝점을 계산
    segments = [(min(h, o), max(h, o)) for h, o in positions]
    
    # 끝점을 기준으로 정렬
    segments.sort(key=lambda x: x[1])
    
    max_count = 0  # 최대 사람 수를 저장할 변수 초기화
    pq = []  # 우선순위 큐 초기화
    
    for start, end in segments:
        # 현재 사람의 시작점을 우선순위 큐에 삽입
        heapq.heappush(pq, start)
        
        # 우선순위 큐의 첫 번째 요소가 현재 끝점에서 d를 뺀 값보다 작으면 큐에서 제거
        while pq and pq[0] < end - d:
            heapq.heappop(pq)
        
        # 현재 우선순위 큐의 크기를 최대 사람 수와 비교하여 갱신
        max_count = max(max_count, len(pq))
    
    return max_count  # 최대 사람 수 반환

# 입력 처리
n = int(input())  # 첫 번째 줄에서 사람 수를 입력 받음
positions = [tuple(map(int, input().split())) for _ in range(n)]  # 각 사람의 집과 사무실 위치를 입력 받음
d = int(input())  # 마지막 줄에서 선분의 길이를 입력 받음

# 결과 출력
print(max_people_in_segment(n, positions, d))  # 최대 사람 수를 계산하여 출력
