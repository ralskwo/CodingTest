from collections import deque  # collections 모듈에서 deque를 가져옵니다. deque는 양방향 큐를 쉽게 다룰 수 있게 해줍니다.

def min_operations(n, m, positions):
    dq = deque(range(1, n + 1))  # 1부터 n까지의 숫자로 초기화된 큐를 생성합니다.
    operations = 0  # 연산 횟수를 저장할 변수를 초기화합니다.
    
    for position in positions:  # 뽑아내고자 하는 위치들을 순서대로 처리합니다.
        idx = dq.index(position)  # 현재 큐에서 목표 위치의 인덱스를 찾습니다.
        
        if idx < len(dq) - idx:  # 왼쪽으로 이동하는 것이 빠른지 확인합니다.
            operations += idx  # 왼쪽으로 이동한 횟수를 연산 횟수에 더합니다.
            dq.rotate(-idx)  # 큐를 왼쪽으로 idx만큼 회전시킵니다.
        else:  # 오른쪽으로 이동하는 것이 더 빠른 경우
            operations += len(dq) - idx  # 오른쪽으로 이동한 횟수를 연산 횟수에 더합니다.
            dq.rotate(len(dq) - idx)  # 큐를 오른쪽으로 (len(dq) - idx)만큼 회전시킵니다.
        
        dq.popleft()  # 첫 번째 원소(목표 위치의 원소)를 큐에서 제거합니다.
        
    return operations  # 총 연산 횟수를 반환합니다.

n, m = map(int, input().split())  # 첫 번째 줄에서 큐의 크기 n과 뽑아낼 위치의 수 m을 입력받습니다.
positions = list(map(int, input().split()))  # 두 번째 줄에서 뽑아낼 위치들을 리스트로 입력받습니다.

print(min_operations(n, m, positions))  # 연산 결과를 출력합니다.
