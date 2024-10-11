import sys
from collections import defaultdict

# 첫 번째 줄의 입력을 받아 회전 초밥의 접시 수(N), 초밥의 종류 수(d), 연속해서 먹는 접시 수(k), 쿠폰 번호(c)를 변수에 저장
N, d, k, c = map(int, sys.stdin.readline().split())

# 회전 초밥 벨트에 놓인 각 초밥의 종류를 입력받아 리스트로 저장
sushi = [int(sys.stdin.readline()) for _ in range(N)]

# 현재 윈도우(슬라이딩 윈도우 내에 존재하는 초밥)의 초밥 종류와 그 개수를 저장할 딕셔너리를 생성
eaten = defaultdict(int)

# 초기 슬라이딩 윈도우 설정: 처음부터 연속된 k개의 초밥을 윈도우에 추가
for i in range(k):
    eaten[sushi[i]] += 1  # 해당 초밥 종류의 개수를 1 증가

# 쿠폰 초밥을 윈도우에 추가하여 쿠폰 초밥이 포함된 상태에서 시작
eaten[c] += 1

# 초기 상태에서 윈도우에 포함된 서로 다른 초밥의 종류 수를 최대 종류 수로 설정
max_variety = len(eaten)

# 슬라이딩 윈도우를 사용하여 전체 초밥 벨트를 한 바퀴(모든 접시 위치) 순회
for i in range(N):
    # 슬라이딩 윈도우의 가장 첫 번째 초밥을 윈도우에서 제거
    eaten[sushi[i]] -= 1  # 해당 초밥의 개수를 1 감소
    if eaten[sushi[i]] == 0:  # 만약 해당 초밥의 개수가 0이 되면 딕셔너리에서 제거 (종류 수가 감소)
        del eaten[sushi[i]]
    
    # 슬라이딩 윈도우의 끝에 새로운 초밥을 추가 (회전 초밥 특성을 고려해 인덱스가 초과되면 다시 처음으로 돌아감)
    eaten[sushi[(i + k) % N]] += 1  # 새로 추가되는 초밥의 개수를 1 증가

    # 현재 윈도우에 포함된 초밥의 종류 수가 더 크면 최대 종류 수를 갱신
    max_variety = max(max_variety, len(eaten))

# 최종적으로 계산된 서로 다른 초밥의 최대 종류 수를 출력
print(max_variety)