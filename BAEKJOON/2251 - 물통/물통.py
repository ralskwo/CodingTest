from collections import deque  # deque를 사용하여 BFS 큐를 생성합니다.

def pour(x, y, max_y):  # 두 물통 사이에서 물을 옮기는 함수입니다.
    if x + y > max_y:  # 옮길 물의 양이 max_y를 초과하는 경우
        return x + y - max_y, max_y  # 옮기고 남은 양과 가득 찬 상태를 반환합니다.
    else:
        return 0, x + y  # 아니면 x의 모든 물을 y에 옮긴 결과를 반환합니다.

def possible_amounts(A, B, C):  # 가능한 물의 양을 계산하는 메인 함수입니다.
    visited = set()  # 방문한 상태를 저장하기 위한 집합입니다.
    result = set()  # 결과로 반환할 물의 양을 저장하는 집합입니다.
    queue = deque([(0, 0, C)])  # 시작 상태 (0, 0, C)를 큐에 추가합니다.

    while queue:  # 큐가 빌 때까지 BFS를 반복합니다.
        a, b, c = queue.popleft()  # 현재 상태를 큐에서 꺼냅니다.
        
        if a == 0:  # 첫 번째 물통이 비어 있을 때
            result.add(c)  # 세 번째 물통의 물의 양을 결과에 추가합니다.
        
        if (a, b, c) in visited:  # 이미 방문한 상태라면
            continue  # 스킵하고 다음 상태로 넘어갑니다.
        visited.add((a, b, c))  # 현재 상태를 방문 처리합니다.
        
        na, nb = pour(a, b, B)  # A → B로 물을 옮기기
        queue.append((na, nb, c))  # 새 상태를 큐에 추가합니다.
        
        na, nc = pour(a, c, C)  # A → C로 물을 옮기기
        queue.append((na, b, nc))  # 새 상태를 큐에 추가합니다.
        
        nb, na = pour(b, a, A)  # B → A로 물을 옮기기
        queue.append((na, nb, c))  # 새 상태를 큐에 추가합니다.
        
        nb, nc = pour(b, c, C)  # B → C로 물을 옮기기
        queue.append((a, nb, nc))  # 새 상태를 큐에 추가합니다.
        
        nc, na = pour(c, a, A)  # C → A로 물을 옮기기
        queue.append((na, b, nc))  # 새 상태를 큐에 추가합니다.
        
        nc, nb = pour(c, b, B)  # C → B로 물을 옮기기
        queue.append((a, nb, nc))  # 새 상태를 큐에 추가합니다.
    
    return sorted(result)  # 결과를 오름차순으로 정렬하여 반환합니다.

A, B, C = map(int, input().split())  # 입력을 받아 A, B, C에 저장합니다.
result = possible_amounts(A, B, C)  # possible_amounts 함수를 호출하여 결과를 계산합니다.
print(" ".join(map(str, result)))  # 결과를 공백으로 구분하여 출력합니다.