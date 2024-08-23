import sys
input = sys.stdin.read
data = input().splitlines()

# 첫 줄의 숫자를 가져옵니다.
# n은 출입 로그의 개수를 나타냅니다.
n = int(data[0])

# 출입 로그를 처리합니다.
# 로그를 저장할 리스트를 생성합니다.
logs = data[1:n+1]

# 현재 회사에 있는 사람들을 저장할 집합을 생성합니다.
present_people = set()

# 각 로그를 순회하면서 처리합니다.
for log in logs:
    # 로그는 "이름 action" 형식으로 주어지므로, 이를 분리합니다.
    name, action = log.split()
    # 'enter' 동작일 경우, 이름을 집합에 추가합니다.
    if action == 'enter':
        present_people.add(name)
    # 'leave' 동작일 경우, 이름을 집합에서 제거합니다.
    elif action == 'leave':
        present_people.discard(name)

# 현재 회사에 있는 사람들의 이름을 사전 순으로 정렬하여 출력합니다.
# 사전 역순으로 정렬하기 위해 sorted 함수에 reverse=True를 설정합니다.
result = sorted(present_people, reverse=True)

# 결과를 한 줄에 한 명씩 출력합니다.
print('\n'.join(result))
