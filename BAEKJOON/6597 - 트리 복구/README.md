# 트리 복구 문제 풀이 및 설명 

https://www.acmicpc.net/problem/6597

## 문제 이해

이 문제는 주어진 프리오더(전위 순회)와 인오더(중위 순회) 순회 결과를 사용하여 이진 트리를 복원한 후, 해당 트리의 포스트오더(후위 순회) 순회 결과를 구하는 것입니다. 프리오더와 인오더 순회 결과를 통해 이진 트리를 복원하는 과정은, 프리오더의 첫 번째 요소가 트리의 루트 노드가 되며, 인오더에서 루트 노드를 기준으로 좌우 서브트리를 나눌 수 있다는 사실을 이용합니다. 이러한 구조를 이용해 트리를 재귀적으로 복원한 후, 포스트오더 순회를 통해 결과를 출력합니다.

## 입출력 조건

**입력:**
- 여러 개의 테스트 케이스가 주어집니다.
- 각 테스트 케이스는 두 줄로 구성됩니다.
  - 첫 번째 줄은 프리오더 순회 결과입니다.
  - 두 번째 줄은 인오더 순회 결과입니다.
- 문자열의 길이는 항상 같으며, 26자를 넘지 않습니다.

**출력:**
- 각 테스트 케이스에 대해, 포스트오더 순회 결과를 출력합니다.

## 접근 방식

이 문제를 해결하기 위해 다음과 같은 접근 방식을 사용합니다:
1. **트리 복원**: 프리오더와 인오더 순회 결과를 사용하여 트리를 복원합니다. 프리오더의 첫 번째 요소가 루트 노드가 되며, 인오더에서 루트 노드의 위치를 기준으로 좌우 서브트리를 나눌 수 있습니다.
2. **후위 순회**: 복원된 트리를 후위 순회하여 결과를 구합니다. 후위 순회는 좌우 서브트리를 먼저 방문한 후 루트 노드를 방문합니다.
3. **재귀적 접근**: 트리 복원과 후위 순회 모두 재귀적으로 접근합니다. 즉, 좌우 서브트리에 대해 같은 작업을 반복하여 트리를 완성하고 순회합니다.

## 풀이 과정

1. **트리 복원 함수 구현 (`build_tree`)**:
   - 입력된 프리오더와 인오더 리스트를 사용하여 트리를 복원합니다.
   - 프리오더의 첫 번째 요소를 루트 노드로 설정합니다.
   - 인오더 리스트에서 루트 노드의 위치를 찾고, 이를 기준으로 좌우 서브트리로 나눕니다.
   - 나뉜 좌우 서브트리에 대해 같은 작업을 재귀적으로 수행합니다.
   - 최종적으로 루트 노드와 좌우 서브트리를 포함하는 트리 구조를 반환합니다.

2. **후위 순회 함수 구현 (`postorder_traversal`)**:
   - 트리의 노드를 후위 순회하는 함수입니다.
   - 트리의 루트, 왼쪽 서브트리, 오른쪽 서브트를 방문합니다.
   - 후위 순회는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드의 순서로 방문합니다.
   - 재귀적으로 좌우 서브트리를 먼저 방문한 후 루트 노드를 추가하여 문자열로 반환합니다.

3. **메인 함수 (`main`)**:
   - 입력 데이터를 읽어와서 각 테스트 케이스를 처리합니다.
   - 프리오더와 인오더 순회 결과를 사용하여 후위 순회 결과를 구합니다.
   - 결과를 저장하고 최종적으로 출력합니다.

## 코드 구현
```python
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