# 전설 문제 풀이

https://www.acmicpc.net/problem/19585

## 문제 이해
이 문제는 주어진 색상 목록과 닉네임 목록을 이용하여 주어진 팀 이름이 색상과 닉네임의 조합으로 이루어졌는지를 확인하는 문제입니다.

## 접근 방식
1. **트라이 자료구조**: 색상과 닉네임을 효율적으로 저장하고 검색할 수 있는 트라이(Trie)를 사용합니다.
2. **입력 처리**: 표준 입력을 통해 색상, 닉네임, 그리고 팀 이름을 입력받습니다.
3. **검증**: 각 팀 이름을 앞부분과 뒷부분으로 나누어 앞부분이 색상 트라이에 존재하고 뒷부분이 닉네임 집합에 존재하는지 확인합니다.

## 풀이 과정
1. **입력 처리**: `sys.stdin.readline`을 사용하여 입력을 빠르게 처리합니다.
   - 첫 줄에서 색상과 닉네임의 개수(`C`, `N`)를 입력받습니다.
   - 그 다음 `C`개의 색상 문자열과 `N`개의 닉네임 문자열을 입력받아 각각 트라이와 집합에 저장합니다.
   - 마지막으로 팀 이름의 개수와 각 팀 이름을 입력받습니다.

2. **트라이 구축**: 색상을 트라이 자료구조에 삽입합니다.
   - 각 색상 문자열을 트라이에 삽입할 때, 문자열의 끝을 표시하기 위해 특별한 키 `0`을 사용합니다.

3. **닉네임 집합**: 닉네임을 빠르게 검색하기 위해 집합 자료구조에 저장합니다.

4. **검증 함수**: `is_valid_team_name` 함수는 주어진 팀 이름을 앞부분과 뒷부분으로 나누어 앞부분이 색상 트라이에 존재하고 뒷부분이 닉네임 집합에 존재하는지 확인합니다.
   - 팀 이름의 각 문자에 대해 현재 노드가 색상의 끝인지 확인하고, 남은 부분이 닉네임 집합에 있는지 확인합니다.
   - 조건을 만족하면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

5. **결과 출력**: 각 팀 이름에 대해 검증한 결과를 "Yes" 또는 "No"로 출력합니다.

## 코드 설명
다음은 문제를 해결하기 위한 파이썬 코드입니다:

```python
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
