from collections import deque

class ConvexHullTrick:
    def __init__(self):  # 클래스 초기화
        self.hull = deque()  # 최적의 직선을 저장하기 위한 deque 초기화
    
    def add_line(self, m, c):  # 새로운 직선을 추가하는 함수
        while len(self.hull) >= 2:  # 현재 deque에 두 개 이상의 직선이 있을 때
            if self.is_redundant(m, c):  # 새로운 직선이 기존 직선을 대체할 수 있는지 확인
                self.hull.pop()  # 기존 직선 제거
            else:
                break  # 대체할 수 없으면 루프 종료
        self.hull.append((m, c))  # 새로운 직선을 deque에 추가
    
    def is_redundant(self, m, c):  # 새로운 직선이 불필요한지 확인하는 함수
        last1 = self.hull[-1]  # 마지막 직선
        last2 = self.hull[-2]  # 마지막에서 두 번째 직선
        # 직선 교차점 비교를 통해 새로운 직선이 최적의 영역에 있는지 확인
        return (c - last1[1]) * (last2[0] - last1[0]) <= (last1[1] - last2[1]) * (last1[0] - m)
    
    def get_max(self, x):  # 주어진 x 값에서 최적의 직선 값을 계산하는 함수
        while len(self.hull) >= 2 and self.evaluate(self.hull[0], x) <= self.evaluate(self.hull[1], x):  # deque의 첫 두 직선 중 더 나은 것을 찾음
            self.hull.popleft()  # 최적이 아닌 첫 번째 직선을 제거
        return self.evaluate(self.hull[0], x)  # 최적의 직선 값을 반환
    
    def evaluate(self, line, x):  # 직선의 y 값을 계산하는 함수
        return line[0] * x + line[1]

def max_adjusted_combat_power(n, a, b, c, x):  # 최대 조정 전투력을 계산하는 함수
    dp_prev = 0  # 이전 dp 값을 저장할 변수 초기화
    prefix_sum = 0  # 누적 합을 저장할 변수 초기화
    
    cht = ConvexHullTrick()  # Convex Hull Trick 객체 생성
    cht.add_line(0, 0)  # 첫 번째 직선 추가 (m=0, c=0)
    
    for j in range(1, n + 1):  # 1번 군인부터 n번 군인까지 반복
        prefix_sum += x[j - 1]  # 현재 군인의 전투력을 누적 합에 더함
        S = prefix_sum  # 현재 구간의 합 S
        dp_curr = a * S * S + b * S + c + cht.get_max(S)  # 현재 구간에서의 최대 조정 전투력 계산
        cht.add_line(-2 * a * S, dp_curr + a * S * S - b * S)  # 새로운 직선을 Convex Hull Trick에 추가
        dp_prev = dp_curr  # 현재 dp 값을 이전 dp 값으로 업데이트
    
    return dp_prev  # 마지막 dp 값을 반환 (최대 조정 전투력)

import sys
input = sys.stdin.read  # 입력을 받기 위한 함수
data = input().split()  # 입력 데이터를 공백 기준으로 분리

n = int(data[0])  # 군인의 수 n
a = int(data[1])  # 계수 a
b = int(data[2])  # 계수 b
c = int(data[3])  # 계수 c
x = list(map(int, data[4:]))  # 각 군인의 전투력을 리스트로 변환

print(max_adjusted_combat_power(n, a, b, c, x))  # 최대 조정 전투력을 계산하고 출력