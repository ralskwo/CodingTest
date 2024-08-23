def distance(x1, y1, x2, y2):
    # 두 지점 사이의 맨해튼 거리를 계산하는 함수
    return abs(x1 - x2) + abs(y1 - y2)

def solve(n, w, events):
    # DP 테이블 초기화: 경찰차 1과 2가 각각 i, j 번째 사건을 처리한 후의 최소 거리를 저장
    dp = [[float('inf')] * (w + 1) for _ in range(w + 1)]
    dp[0][0] = 0
    # 경로 추적을 위한 테이블 초기화
    trace = [[(-1, -1)] * (w + 1) for _ in range(w + 1)]
    
    # 모든 사건에 대해 반복
    for i in range(w + 1):
        for j in range(w + 1):
            # 다음 처리할 사건 번호
            next_event = max(i, j) + 1
            if next_event > w:
                continue
            
            event_pos = events[next_event]
            # 경찰차 1의 현재 위치
            if i == 0:
                car1_pos = (1, 1)
            else:
                car1_pos = events[i]
            # 경찰차 2의 현재 위치
            if j == 0:
                car2_pos = (n, n)
            else:
                car2_pos = events[j]

            # 경찰차 1이 다음 사건을 처리하는 경우의 거리 계산
            new_dist_car1 = dp[i][j] + distance(car1_pos[0], car1_pos[1], event_pos[0], event_pos[1])
            # 경찰차 2가 다음 사건을 처리하는 경우의 거리 계산
            new_dist_car2 = dp[i][j] + distance(car2_pos[0], car2_pos[1], event_pos[0], event_pos[1])
            
            # dp 배열 업데이트 및 경로 추적
            if new_dist_car1 < dp[next_event][j]:
                dp[next_event][j] = new_dist_car1
                trace[next_event][j] = (i, j)
            if new_dist_car2 < dp[i][next_event]:
                dp[i][next_event] = new_dist_car2
                trace[i][next_event] = (i, j)
    
    # 최소 거리를 찾고, 마지막 사건을 처리한 후의 위치 추적
    result = float('inf')
    last_i, last_j = -1, -1
    for i in range(w + 1):
        if dp[w][i] < result:
            result = dp[w][i]
            last_i, last_j = w, i
        if dp[i][w] < result:
            result = dp[i][w]
            last_i, last_j = i, w
    
    # 경로 추적: 어떤 경찰차가 사건을 처리했는지 기록
    path = []
    x, y = last_i, last_j
    while trace[x][y] != (-1, -1):
        px, py = trace[x][y]
        if px == x:
            path.append(2)
        else:
            path.append(1)
        x, y = px, py
    
    path.reverse()
    return result, path

# 입력 처리
import sys
input = sys.stdin.read
data = input().strip().split()
index = 0

# 도시의 크기
n = int(data[index])
index += 1
# 사건의 수
w = int(data[index])
index += 1

# 사건의 위치
events = [(0, 0)] * (w + 1)
for i in range(1, w + 1):
    x = int(data[index])
    index += 1
    y = int(data[index])
    index += 1
    events[i] = (x, y)

# 문제 해결 및 결과 출력
result, path = solve(n, w, events)
print(result)
for p in path:
    print(p)
