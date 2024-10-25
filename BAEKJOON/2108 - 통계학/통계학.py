import sys
from collections import defaultdict

# sys.stdin.read를 통해 입력을 한 번에 받아온다.
input = sys.stdin.read
# 입력된 데이터를 공백 기준으로 분리하여 리스트로 저장한다.
data = input().split()

# 첫 번째 입력값은 수의 개수 N이다.
N = int(data[0])
# 두 번째부터 N+1번째까지의 값을 정수 리스트로 변환한다.
arr = list(map(int, data[1:N + 1]))
# 리스트를 오름차순으로 정렬한다.
arr.sort()

# 산술평균을 구하기 위해 리스트의 합을 N으로 나누고 반올림한다.
mean = round(sum(arr) / N)
# 중앙값은 정렬된 리스트의 가운데 위치한 값이다.
median = arr[N // 2]

# 각 숫자의 빈도를 저장할 defaultdict를 생성한다.
counter = defaultdict(int)
# 리스트의 각 숫자에 대해 빈도를 1씩 증가시킨다.
for num in arr:
    counter[num] += 1

# 빈도수가 높은 순서로 정렬하고, 빈도가 같을 경우 숫자가 작은 순으로 정렬한다.
most_commons = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# 최빈값이 여러 개 있을 경우 두 번째로 작은 값을 선택한다.
if len(most_commons) > 1 and most_commons[0][1] == most_commons[1][1]:
    mode = most_commons[1][0]
# 최빈값이 하나뿐인 경우 첫 번째 값을 선택한다.
else:
    mode = most_commons[0][0]

# 범위는 정렬된 리스트에서 최대값과 최소값의 차이이다.
range_value = arr[-1] - arr[0]

# 각각의 값을 순서대로 출력한다.
print(f"{mean}\n{median}\n{mode}\n{range_value}")