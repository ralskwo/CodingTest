import sys
import math

def is_inside_circle(x, y, cx, cy, r):
    # 주어진 점 (x, y)가 행성계의 중심 (cx, cy)과 반지름 r을 기준으로
    # 행성계 내부에 위치하는지 확인하는 함수
    # (x - cx)^2 + (y - cy)^2 < r^2이면 내부에 있다고 판단
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

def minimum_planet_entry_exit_count(x1, y1, x2, y2, planets):
    # 출발점 (x1, y1)에서 도착점 (x2, y2)까지 이동할 때,
    # 행성계의 경계를 넘는 최소 진입/이탈 횟수를 계산하는 함수
    count = 0  # 진입/이탈 횟수를 저장할 변수
    for cx, cy, r in planets:  # 모든 행성계에 대해 반복
        # 출발점이 현재 행성계 내부에 있는지 확인
        start_inside = is_inside_circle(x1, y1, cx, cy, r)
        # 도착점이 현재 행성계 내부에 있는지 확인
        end_inside = is_inside_circle(x2, y2, cx, cy, r)
        
        # 출발점과 도착점 중 하나만 내부에 있을 경우, 진입 또는 이탈이 발생하므로 카운트 증가
        if start_inside != end_inside:
            count += 1
    return count  # 최종 진입/이탈 횟수를 반환

# 테스트 케이스 개수 입력
T = int(input().strip())
results = []  # 각 테스트 케이스의 결과를 저장할 리스트

for _ in range(T):  # 각 테스트 케이스에 대해 반복
    # 출발점과 도착점의 좌표 입력
    x1, y1, x2, y2 = map(int, input().strip().split())
    # 행성계의 개수 입력
    n = int(input().strip())
    
    planets = []  # 각 행성계 정보를 저장할 리스트
    for _ in range(n):  # 각 행성계에 대해 반복
        # 행성계의 중심 좌표와 반지름 입력
        cx, cy, r = map(int, input().strip().split())
        planets.append((cx, cy, r))  # 행성계 정보를 리스트에 추가
    
    # 최소 진입/이탈 횟수를 계산하여 결과 리스트에 추가
    result = minimum_planet_entry_exit_count(x1, y1, x2, y2, planets)
    results.append(result)

# 각 테스트 케이스의 결과를 출력
for result in results:
    print(result)