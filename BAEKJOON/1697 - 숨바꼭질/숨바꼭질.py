# BFS 알고리즘에 사용할 deque를 import합니다.
from collections import deque

def bfs(N, K):
    # BFS 함수는 수빈이의 위치 N과 동생의 위치 K를 인자로 받습니다.
    
    # 문제에서 주어진 위치의 최대값을 설정합니다.
    max_limit = 100000
    
    # 방문한 위치를 추적하기 위한 리스트를 생성합니다. 인덱스가 위치를 나타내고 값이 방문 여부를 나타냅니다.
    visited = [False] * (max_limit + 1)
    
    # deque를 초기화합니다. 시작 위치 N과 현재 시간을 튜플로 넣어줍니다.
    queue = deque([(N, 0)])
    
    # 큐가 비어있지 않은 동안 반복합니다.
    while queue:
        
        # 큐의 가장 앞에 있는 요소를 꺼내 현재 위치와 시간을 얻습니다.
        position, time = queue.popleft()
        
        # 현재 위치가 동생의 위치와 같으면
        if position == K:
            
            # 현재 시간을 반환합니다. (최단 시간)
            return time
        
        # 현재 위치에서 이동할 수 있는 세 가지 경우를 모두 확인합니다.
        for next_pos in (position - 1, position + 1, position * 2):
            
            # 다음 위치가 범위 내에 있고 방문하지 않은 위치라면
            if 0 <= next_pos <= max_limit and not visited[next_pos]:
                
                # 해당 위치를 방문한 것으로 표시합니다.
                visited[next_pos] = True
                
                # 다음 위치와 시간을 큐에 추가합니다.
                queue.append((next_pos, time + 1))

# 표준 입력으로부터 수빈이의 위치 N과 동생의 위치 K를 읽어옵니다.
N, K = map(int, input().split())

# BFS 함수의 결과를 출력합니다.
print(bfs(N, K))
