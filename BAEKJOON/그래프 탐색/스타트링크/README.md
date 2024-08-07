# 스타트링크 문제 풀이 및 설명

https://www.acmicpc.net/problem/5014

## 문제 이해

이 문제는 엘리베이터를 타고 특정 층에서 목표 층으로 이동하기 위해 필요한 최소 버튼 누름 횟수를 계산하는 문제입니다. 엘리베이터에는 두 개의 버튼만 있으며, 하나는 위로 올라가는 버튼(U)이고, 다른 하나는 아래로 내려가는 버튼(D)입니다. 현재 층(S)에서 목표 층(G)으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 계산해야 합니다. 만약 목표 층에 도달할 수 없다면 "use the stairs"를 출력해야 합니다.

문제를 해결하기 위해 다음과 같은 관점을 가지고 접근해야 합니다:
1. **층 이동의 제약 조건**: 엘리베이터는 총 F층이 있고, 엘리베이터가 있는 층에서만 작동합니다. 따라서 이동할 수 있는 범위 내에서만 탐색이 가능합니다.
2. **최소 이동 횟수 계산**: 최소 횟수를 계산하기 위해 최단 경로 탐색 알고리즘을 사용해야 합니다.
3. **특정 상태에서의 이동 가능 여부**: 특정 층에 도달할 수 있는지 여부를 확인해야 하며, 불가능할 경우 대체 메시지를 출력해야 합니다.

## 접근 방식

이 문제를 해결하기 위해 최단 경로 탐색 알고리즘인 BFS(너비 우선 탐색)를 사용할 것입니다. BFS는 주로 그래프에서 최단 경로를 찾는 데 사용되며, 여기서 각 층을 노드로 생각하고 이동을 간선으로 간주하여 문제를 그래프로 모델링할 수 있습니다.

## 풀이 과정

1. **입력값 처리**: F(총 층 수), S(현재 층), G(목표 층), U(위로 이동할 층 수), D(아래로 이동할 층 수)를 입력받습니다.
2. **방문 체크 리스트 초기화**: 각 층을 방문했는지 여부와 해당 층에 도달하기 위한 버튼 누름 횟수를 저장할 리스트를 초기화합니다.
3. **BFS 초기 설정**: 큐(queue)를 초기화하고 현재 층과 버튼 누름 횟수를 큐에 추가합니다. 시작 층의 방문을 기록합니다.
4. **BFS 탐색**:
   - 큐에서 현재 층과 버튼 누름 횟수를 꺼냅니다.
   - 현재 층이 목표 층과 같다면 현재 버튼 누름 횟수를 반환합니다.
   - 위로 이동할 수 있다면 이동한 층을 큐에 추가하고 방문을 기록합니다.
   - 아래로 이동할 수 있다면 이동한 층을 큐에 추가하고 방문을 기록합니다.
5. **목표 층 도달 여부 확인**: BFS 탐색이 끝난 후에도 목표 층에 도달하지 못했다면 "use the stairs"를 출력합니다.

## 코드 구현
```python
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
