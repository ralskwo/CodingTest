MOD = 1_000_000_007  # 문제에서 요구하는 모듈러 값 (나머지 연산에 사용)

class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드를 저장하는 딕셔너리
        self.is_end_of_word = False  # 단어의 끝을 표시하는 플래그

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 트라이의 루트 노드를 초기화
    
    def insert(self, word):
        node = self.root  # 루트 노드부터 시작
        for char in word:  # 단어의 각 문자를 순회
            if char not in node.children:  # 현재 문자에 해당하는 자식 노드가 없으면
                node.children[char] = TrieNode()  # 새로운 자식 노드를 생성
            node = node.children[char]  # 현재 노드를 자식 노드로 이동
        node.is_end_of_word = True  # 단어의 끝을 표시
    
    def search(self, s, start):
        node = self.root  # 루트 노드부터 시작
        results = []  # 부분 문자열의 끝 인덱스를 저장할 리스트
        for i in range(start, len(s)):  # 시작 위치부터 문자열의 끝까지 순회
            char = s[i]  # 현재 문자
            if char not in node.children:  # 현재 문자에 해당하는 자식 노드가 없으면
                break  # 검색 종료
            node = node.children[char]  # 현재 노드를 자식 노드로 이동
            if node.is_end_of_word:  # 단어의 끝이면
                results.append(i + 1)  # 끝 인덱스를 결과 리스트에 추가
        return results  # 부분 문자열의 끝 인덱스 리스트 반환

def count_ways(N, S, t):
    trie = Trie()  # 트라이 초기화
    for word in S:  # 집합 S의 모든 단어를 트라이에 삽입
        trie.insert(word)
    
    len_t = len(t)  # 문자열 t의 길이
    dp = [0] * (len_t + 1)  # DP 배열 초기화 (길이 len_t + 1)
    dp[0] = 1  # 빈 문자열을 분할하는 방법은 1가지
    
    for i in range(len_t):  # 문자열 t의 각 위치를 순회
        if dp[i] > 0:  # 현재 위치 i에서 분할 가능한 경우
            for j in trie.search(t, i):  # 트라이에서 i부터 시작하는 부분 문자열 검색
                dp[j] = (dp[j] + dp[i]) % MOD  # DP 배열 갱신 (모듈러 연산 적용)
    
    return dp[len_t]  # 문자열 t 전체를 분할하는 방법의 수 반환

import sys
input = sys.stdin.read  # 표준 입력에서 모든 데이터를 읽음
data = input().split()  # 읽은 데이터를 공백을 기준으로 분할

N = int(data[0])  # 첫 번째 값은 N (문자열 집합 S의 크기)
S = data[1:N+1]  # 다음 N개의 값은 집합 S에 속하는 문자열
t = data[N+1]  # 마지막 값은 분할 대상 문자열 t

result = count_ways(N, S, t)  # count_ways 함수 호출하여 결과 계산
print(result)  # 결과 출력
