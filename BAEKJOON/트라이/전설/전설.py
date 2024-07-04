import sys
input = sys.stdin.readline

def is_valid_team_name(team_name):
    current_node = color_trie
    for i in range(len(team_name)):
        # 현재 위치가 색상 끝이고, 남은 부분이 닉네임 집합에 있는지 확인
        if current_node.get(0) and team_name[i:] in nickname_set:
            return True
        # 현재 문자가 트라이에 없는 경우
        if not current_node.get(team_name[i]):
            return False
        # 현재 노드를 다음 자식 노드로 변경
        current_node = current_node[team_name[i]]
    return False

# 색상과 닉네임의 개수를 입력받음
C, N = map(int, input().split())

# 색상을 저장할 트라이 자료구조
color_trie = {}
for _ in range(C):
    current_node = color_trie
    for char in input().strip():
        if not current_node.get(char):
            current_node[char] = {}
        current_node = current_node[char]
    current_node[0] = 1  # 단어의 끝을 표시

# 닉네임을 저장할 집합 자료구조
nickname_set = {input().strip() for _ in range(N)}

# 팀 이름 개수 입력받고 각 팀 이름에 대해 검증
for _ in range(int(input().strip())):
    print("Yes" if is_valid_team_name(input().strip()) else "No")
