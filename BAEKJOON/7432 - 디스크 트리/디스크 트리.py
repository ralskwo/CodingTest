class TrieNode:
    def __init__(self):
        # 각 TrieNode는 자식 노드를 저장할 딕셔너리와
        # 경로의 끝을 나타내는 플래그를 가진다.
        self.children = {}
        self.is_end_of_path = False

class Trie:
    def __init__(self):
        # Trie는 루트 노드를 가진다.
        self.root = TrieNode()

    def insert(self, path):
        # 주어진 경로를 트라이에 삽입하는 함수
        node = self.root
        # 경로를 '\' 기준으로 나눈다.
        parts = path.split("\\")
        for part in parts:
            # 자식 노드 중 현재 part가 없다면 새로운 노드를 추가
            if part not in node.children:
                node.children[part] = TrieNode()
            # 현재 노드를 자식 노드로 이동
            node = node.children[part]
        # 경로의 끝 부분 표시
        node.is_end_of_path = True

    def display(self, node=None, depth=0):
        # 트라이 구조를 출력하는 함수
        if node is None:
            # 초기 호출 시 루트 노드부터 시작
            node = self.root
        # 자식 노드들을 이름순으로 정렬하여 순회
        for key in sorted(node.children.keys()):
            # 현재 깊이만큼 공백을 추가하고 디렉토리 이름 출력
            print(" " * depth + key)
            # 재귀적으로 자식 노드들을 출력
            self.display(node.children[key], depth + 1)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    # 표준 입력으로부터 전체 데이터를 읽어온다.
    data = input().strip().split('\n')
    
    # 첫 번째 줄은 디렉토리 경로의 개수 N
    n = int(data[0])
    # 나머지 줄들은 디렉토리 경로
    paths = data[1:]
    
    # Trie 객체 생성
    trie = Trie()
    
    # 각 경로를 트라이에 삽입
    for path in paths:
        trie.insert(path)
    
    # 트라이 구조를 출력
    trie.display()
