class Node:
    def __init__(self, value):
        self.value = value  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

def build_tree(node_info):
    # 주어진 노드 정보를 바탕으로 이진 트리를 구축하는 함수
    nodes = {}
    for value, left, right in node_info:
        if value not in nodes:
            nodes[value] = Node(value)  # 노드 생성
        if left != '.':
            nodes[left] = Node(left)
            nodes[value].left = nodes[left]  # 왼쪽 자식 노드 설정
        if right != '.':
            nodes[right] = Node(right)
            nodes[value].right = nodes[right]  # 오른쪽 자식 노드 설정
    return nodes[node_info[0][0]]  # 루트 노드 반환

def preorder(node, result):
    # 전위 순회: 루트 -> 왼쪽 -> 오른쪽
    if node:
        result.append(node.value)  # 루트 노드 처리
        preorder(node.left, result)  # 왼쪽 자식 노드 순회
        preorder(node.right, result)  # 오른쪽 자식 노드 순회

def inorder(node, result):
    # 중위 순회: 왼쪽 -> 루트 -> 오른쪽
    if node:
        inorder(node.left, result)  # 왼쪽 자식 노드 순회
        result.append(node.value)  # 루트 노드 처리
        inorder(node.right, result)  # 오른쪽 자식 노드 순회

def postorder(node, result):
    # 후위 순회: 왼쪽 -> 오른쪽 -> 루트
    if node:
        postorder(node.left, result)  # 왼쪽 자식 노드 순회
        postorder(node.right, result)  # 오른쪽 자식 노드 순회
        result.append(node.value)  # 루트 노드 처리

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # 노드의 개수
    # 노드 정보 (노드 값, 왼쪽 자식, 오른쪽 자식) 리스트 생성
    node_info = [(data[i], data[i+1], data[i+2]) for i in range(1, len(data), 3)]
    
    root = build_tree(node_info)  # 이진 트리 구축
    
    result = []
    preorder(root, result)
    print(''.join(result))  # 전위 순회 결과 출력
    
    result = []
    inorder(root, result)
    print(''.join(result))  # 중위 순회 결과 출력
    
    result = []
    postorder(root, result)
    print(''.join(result))  # 후위 순회 결과 출력

if __name__ == "__main__":
    main()
