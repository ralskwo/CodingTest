# collections 모듈에서 deque를 가져옵니다. deque는 양방향 큐를 지원하는 모듈입니다.
from collections import deque

# 프린터 큐 문제를 해결하는 함수입니다.
def printer_queue(test_cases):
    results = []  # 각 테스트 케이스의 결과를 저장할 리스트
    
    for case in test_cases:
        N, M, priorities = case  # 문서의 수 N, 궁금한 문서의 위치 M, 문서의 중요도 리스트 priorities
        # 각 문서의 위치와 중요도를 튜플로 저장하여 deque에 넣습니다.
        queue = deque([(i, priority) for i, priority in enumerate(priorities)])
        print_order = 0  # 현재 인쇄된 문서의 순서를 기록할 변수
        
        while queue:
            current = queue.popleft()  # 큐의 가장 앞에 있는 문서를 꺼냅니다.
            
            # 현재 문서의 중요도보다 높은 중요도를 가진 문서가 큐에 하나라도 있으면 True
            if any(current[1] < q[1] for q in queue):
                queue.append(current)  # 중요도가 높은 문서가 있으면 현재 문서를 다시 큐의 뒤로 보냅니다.
            else:
                print_order += 1  # 중요도가 높은 문서가 없으면 현재 문서를 인쇄합니다.
                if current[0] == M:  # 현재 문서가 궁금한 문서라면
                    results.append(print_order)  # 현재 인쇄 순서를 결과 리스트에 추가
                    break  # 반복을 종료합니다.
    
    return results  # 모든 테스트 케이스에 대한 결과를 반환합니다.

# 표준 입력을 사용하기 위해 sys 모듈을 가져옵니다.
import sys
input = sys.stdin.read
data = input().strip().split('\n')  # 입력 데이터를 한 번에 읽어와서 줄 단위로 나눕니다.

T = int(data[0])  # 첫 번째 줄은 테스트 케이스의 수입니다.
test_cases = []

index = 1
# 각 테스트 케이스를 순회하면서 데이터를 읽어옵니다.
for _ in range(T):
    N, M = map(int, data[index].split())  # 문서의 수 N과 궁금한 문서의 위치 M
    priorities = list(map(int, data[index + 1].split()))  # 각 문서의 중요도를 리스트로 저장
    test_cases.append((N, M, priorities))  # 각 테스트 케이스 데이터를 튜플로 저장
    index += 2  # 다음 테스트 케이스로 이동

# 결과를 계산합니다.
results = printer_queue(test_cases)

# 결과를 출력합니다.
for result in results:
    print(result)