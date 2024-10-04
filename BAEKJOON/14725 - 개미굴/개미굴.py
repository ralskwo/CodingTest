from collections import defaultdict  # collections 모듈에서 defaultdict 클래스 임포트

# TrieNode 클래스 정의 (트리의 각 노드를 표현)
class TrieNode:
    def __init__(self):
        # 자식 노드를 저장하기 위한 defaultdict 초기화
        self.children = defaultdict(TrieNode)
        # 해당 노드가 끝 노드인지 표시하는 플래그
        self.is_end = False

# 트리를 깊이 우선 탐색(DFS)으로 출력하는 함수
def print_trie(node, depth):
    # 자식 노드들을 사전 순서로 정렬하여 순회
    for key in sorted(node.children):
        # 현재 깊이만큼 "--"를 출력하고, 해당 노드의 key 출력
        print("--" * depth + key)
        # 자식 노드에 대해 재귀적으로 같은 방식으로 출력
        print_trie(node.children[key], depth + 1)

# 입력 개수 N을 첫 번째 줄에서 읽음
N = int(input().strip())

# 트리의 루트 노드 생성
root = TrieNode()

# N개의 입력을 읽어와 트리에 저장
for _ in range(N):
    # 입력 받은 값을 공백을 기준으로 분리하고, 첫 번째 값은 K이므로 제외한 나머지 먹이 정보만 추출
    data = list(input().strip().split())[1:]
    # 트리의 현재 위치를 루트 노드로 설정
    current_node = root
    # 먹이 정보를 하나씩 읽어가면서 트리에 추가
    for item in data:
        # 현재 위치의 자식 노드로 이동 또는 새로운 자식 노드 생성
        current_node = current_node.children[item]

# 트리의 루트 노드부터 깊이 0으로 시작하여 트리 출력
print_trie(root, 0)