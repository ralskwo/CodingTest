from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 가져옵니다.

def elevator(F, S, G, U, D):  # 함수 정의, F는 총 층 수, S는 현재 층, G는 목표 층, U는 위로 이동할 층 수, D는 아래로 이동할 층 수
    visited = [-1] * (F + 1)  # 방문 여부와 버튼 누름 횟수를 저장할 리스트를 초기화합니다. 초기값은 -1로 설정하여 방문하지 않음을 표시합니다.
    queue = deque([(S, 0)])  # 현재 층과 버튼 누름 횟수를 저장하는 큐를 초기화합니다. 시작 층 S와 누름 횟수 0을 추가합니다.
    visited[S] = 0  # 시작 층은 방문했으므로 0으로 설정합니다.
    
    while queue:  # 큐가 빌 때까지 반복합니다.
        current_floor, presses = queue.popleft()  # 큐에서 현재 층과 버튼 누름 횟수를 가져옵니다.
        
        if current_floor == G:  # 현재 층이 목표 층과 같으면
            return presses  # 버튼 누름 횟수를 반환합니다.
        
        # 위로 이동
        if current_floor + U <= F and visited[current_floor + U] == -1:  # 위로 이동한 층이 총 층 수를 넘지 않고 아직 방문하지 않았다면
            visited[current_floor + U] = presses + 1  # 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
            queue.append((current_floor + U, presses + 1))  # 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
        
        # 아래로 이동
        if current_floor - D > 0 and visited[current_floor - D] == -1:  # 아래로 이동한 층이 1층 이상이고 아직 방문하지 않았다면
            visited[current_floor - D] = presses + 1  # 해당 층을 방문했음을 기록하고 버튼 누름 횟수를 1 증가시킵니다.
            queue.append((current_floor - D, presses + 1))  # 이동한 층과 버튼 누름 횟수를 큐에 추가합니다.
    
    return "use the stairs"  # 큐가 비고도 목표 층에 도달하지 못하면 "use the stairs"를 반환합니다.

# 입력을 읽습니다.
F, S, G, U, D = map(int, input().split())  # 입력된 값을 정수로 변환하여 F, S, G, U, D에 각각 저장합니다.

# 함수 호출 및 결과 출력
result = elevator(F, S, G, U, D)  # elevator 함수를 호출하고 결과를 result에 저장합니다.
print(result)  # 결과를 출력합니다.
