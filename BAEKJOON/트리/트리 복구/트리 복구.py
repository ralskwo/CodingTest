def build_tree(preorder, inorder):
    # 재귀적으로 트리를 구축하는 함수입니다.
    if not preorder or not inorder:
        # 만약 프리오더나 인오더 리스트가 비어있다면 None을 반환합니다.
        return None

    root = preorder[0]
    # 프리오더의 첫 번째 요소는 루트 노드입니다.
    root_index = inorder.index(root)
    # 인오더 리스트에서 루트 노드의 인덱스를 찾습니다.

    left_inorder = inorder[:root_index]
    # 루트 노드의 왼쪽 부분은 왼쪽 서브트리의 인오더 순회 결과입니다.
    right_inorder = inorder[root_index + 1:]
    # 루트 노드의 오른쪽 부분은 오른쪽 서브트리의 인오더 순회 결과입니다.

    left_preorder = preorder[1:1 + len(left_inorder)]
    # 왼쪽 서브트리의 프리오더 순회 결과입니다.
    right_preorder = preorder[1 + len(left_inorder):]
    # 오른쪽 서브트리의 프리오더 순회 결과입니다.

    left_subtree = build_tree(left_preorder, left_inorder)
    # 재귀적으로 왼쪽 서브트리를 구축합니다.
    right_subtree = build_tree(right_preorder, right_inorder)
    # 재귀적으로 오른쪽 서브트리를 구축합니다.

    return (root, left_subtree, right_subtree)
    # 루트와 왼쪽 및 오른쪽 서브트리를 반환합니다.

def postorder_traversal(tree):
    # 트리를 후위 순회하는 함수입니다.
    if tree is None:
        # 만약 트리가 None이면 빈 문자열을 반환합니다.
        return ""

    root, left_subtree, right_subtree = tree
    # 트리의 루트, 왼쪽 서브트리, 오른쪽 서브트리를 가져옵니다.
    return postorder_traversal(left_subtree) + postorder_traversal(right_subtree) + root
    # 왼쪽 서브트리, 오른쪽 서브트리 순으로 후위 순회하고 마지막에 루트를 추가합니다.

def solve(preorder, inorder):
    # 주어진 프리오더와 인오더를 사용하여 후위 순회 결과를 구하는 함수입니다.
    tree = build_tree(preorder, inorder)
    # 프리오더와 인오더를 통해 트리를 구축합니다.
    return postorder_traversal(tree)
    # 구축된 트리를 후위 순회하여 결과를 반환합니다.

# 입력 및 출력 처리
import sys
input = sys.stdin.read

def main():
    data = input().strip().split()
    # 모든 입력 데이터를 읽고 공백을 기준으로 분할합니다.
    results = []
    for i in range(0, len(data), 2):
        # 두 줄씩 처리합니다.
        preorder = data[i]
        # 첫 번째 줄은 프리오더 순회 결과입니다.
        inorder = data[i + 1]
        # 두 번째 줄은 인오더 순회 결과입니다.
        results.append(solve(preorder, inorder))
        # 프리오더와 인오더 순회 결과를 사용하여 후위 순회 결과를 구합니다.
    
    for result in results:
        # 모든 결과를 출력합니다.
        print(result)

if __name__ == "__main__":
    # 메인 함수를 실행합니다.
    main()