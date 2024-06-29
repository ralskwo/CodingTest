# 입력 데이터 처리
import sys
input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄: 포켓몬의 개수 N과 문제의 개수 M
n, m = map(int, data[0].split())

# 포켓몬 이름과 번호를 저장할 딕셔너리
name_to_number = {}
number_to_name = {}

# 포켓몬 이름과 번호 입력
for i in range(1, n + 1):
    name = data[i]
    name_to_number[name] = i
    number_to_name[i] = name

# 문제 입력 및 처리
results = []
for i in range(n + 1, n + 1 + m):
    query = data[i]
    if query.isdigit():
        # 숫자인 경우: 번호에 해당하는 포켓몬 이름 출력
        results.append(number_to_name[int(query)])
    else:
        # 문자인 경우: 이름에 해당하는 포켓몬 번호 출력
        results.append(name_to_number[query])

# 결과 출력
for result in results:
    print(result)
