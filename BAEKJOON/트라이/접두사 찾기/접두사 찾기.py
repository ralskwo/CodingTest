# Trie의 각 노드를 정의하는 클래스
class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드를 저장하는 딕셔너리
        self.is_end_of_word = False  # 단어의 끝을 표시하는 플래그

# Trie 자료구조를 정의하는 클래스
class Trie:
    def __init__(self):
        self.root = TrieNode()  # 루트 노드를 초기화

    # 단어를 트라이에 삽입하는 메소드
    def insert(self, word):
        node = self.root  # 시작은 항상 루트 노드부터
        for char in word:  # 단어의 각 문자를 순회하며
            if char not in node.children:  # 현재 노드의 자식 중에 문자가 없으면
                node.children[char] = TrieNode()  # 새로운 노드를 추가
            node = node.children[char]  # 현재 노드를 자식 노드로 갱신
        node.is_end_of_word = True  # 단어의 끝임을 표시

    # 주어진 접두사로 시작하는 단어가 있는지 확인하는 메소드
    def starts_with(self, prefix):
        node = self.root  # 시작은 항상 루트 노드부터
        for char in prefix:  # 접두사의 각 문자를 순회하며
            if char not in node.children:  # 현재 노드의 자식 중에 문자가 없으면
                return False  # 접두사가 없음을 반환
            node = node.children[char]  # 현재 노드를 자식 노드로 갱신
        return True  # 접두사가 있음을 반환

# 접두사의 개수를 계산하는 함수
def count_prefixes(N, M, N_strings, M_strings):
    trie = Trie()  # 트라이를 초기화
    for word in N_strings:  # 주어진 N개의 문자열을 순회하며
        trie.insert(word)  # 각 문자열을 트라이에 삽입
    
    prefix_count = 0  # 접두사의 개수를 세기 위한 카운터 초기화
    for prefix in M_strings:  # 주어진 M개의 접두사를 순회하며
        if trie.starts_with(prefix):  # 접두사가 트라이에 존재하면
            prefix_count += 1  # 카운터를 증가
    
    return prefix_count  # 최종 접두사의 개수를 반환

# 표준 입력으로부터 데이터를 읽어옵니다.
import sys
input = sys.stdin.read  # 표준 입력 전체를 읽어오는 함수
data = input().split()  # 읽어온 데이터를 공백 기준으로 나누어 리스트로 저장

# 첫 번째 줄에 주어진 N과 M을 읽어옵니다.
N = int(data[0])  # 첫 번째 값은 N
M = int(data[1])  # 두 번째 값은 M

# N개의 문자열을 리스트로 저장합니다.
N_strings = data[2:2 + N]  # 그 다음 N개의 값은 N개의 문자열

# M개의 문자열을 리스트로 저장합니다.
M_strings = data[2 + N:2 + N + M]  # 그 다음 M개의 값은 M개의 문자열

# 접두사 개수를 계산하는 함수를 호출합니다.
result = count_prefixes(N, M, N_strings, M_strings)  # 접두사의 개수를 계산하여 결과 저장

# 결과를 출력합니다.
print(result)  # 최종 결과를 출력
