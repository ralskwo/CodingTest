# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

# 첫째 줄: 숫자 카드의 개수 N
n = int(data[0])

# 둘째 줄: 숫자 카드에 적혀있는 정수들
cards = list(map(int, data[1:n+1]))

# 셋째 줄: 구해야 할 정수의 개수 M
m = int(data[n+1])

# 넷째 줄: 상근이가 몇 개 가지고 있는지 구해야 할 M개의 정수
queries = list(map(int, data[n+2:]))

# 숫자 카드의 개수를 세기 위한 딕셔너리
card_count = {}

# 숫자 카드의 개수를 센다
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

# 각 쿼리에 대해 결과를 출력한다
results = []
for query in queries:
    if query in card_count:
        results.append(card_count[query])
    else:
        results.append(0)

# 결과 출력
print(' '.join(map(str, results)))
