import sys
import heapq

class TrieNode:
    def __init__(self):
        # 자식 노드를 저장할 딕셔너리
        self.children = {}
        # 현재 노드가 단어의 끝인지 여부
        self.end = False
        # 이 노드부터 최대 깊이를 나타내는 값
        self.max_depth = 0

class Trie:
    def __init__(self):
        # 루트 노드를 초기화
        self.root = TrieNode()

    def insert(self, word):
        # 단어를 트라이에 삽입
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                # 자식 노드가 없으면 새로 생성
                node.children[char] = TrieNode()
            node = node.children[char]
            # 현재 노드의 최대 깊이 갱신
            node.max_depth = max(node.max_depth, len(word) - i - 1)
        # 단어의 끝임을 표시
        node.end = True

def solve(node, operations):
    if node.end:
        # 단어의 끝이면 'P' 추가
        operations.append('P')
    # 우선순위 큐를 사용해 자식 노드를 정렬
    pq = []
    for char, child in node.children.items():
        heapq.heappush(pq, (child.max_depth, char))
    while pq:
        # 최대 깊이와 문자를 꺼내서 처리
        _, char = heapq.heappop(pq)
        operations.append(char)
        solve(node.children[char], operations)
    # 자식 노드 처리가 끝나면 '-' 추가
    operations.append('-')

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    words = data[1:]
    
    # 트라이에 단어 삽입
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    operations = []
    # 트라이를 탐색하며 필요한 연산 계산
    solve(trie.root, operations)
    
    # 마지막 '-' 제거
    while operations and operations[-1] == '-':
        operations.pop()
    
    # 연산의 총 개수 출력
    print(len(operations))
    # 각 연산을 출력
    for op in operations:
        print(op)

if __name__ == "__main__":
    main()
