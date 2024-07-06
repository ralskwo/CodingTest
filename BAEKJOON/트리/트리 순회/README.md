# 이진 트리 순회 문제 해결

https://www.acmicpc.net/problem/1991

## 문제 이해

이 문제는 주어진 이진 트리에 대해 세 가지 순회 방식(전위, 중위, 후위)을 구현하고, 그 결과를 출력하는 프로그램을 작성하는 것입니다. 

입력은 다음과 같은 형식으로 주어집니다:
- 첫 번째 줄에 노드의 개수 \( N \)이 주어집니다.
- 다음 \( N \)개의 줄에는 각 노드와 그 왼쪽, 오른쪽 자식 노드가 주어집니다. 자식 노드가 없는 경우 '.'으로 표현됩니다.

출력은 세 가지 순회 방식의 결과를 공백 없이 출력합니다.

## 접근 방식

1. **이진 트리 구성**:
   주어진 노드 정보를 바탕으로 이진 트리를 구성합니다. 노드 클래스를 정의하고, 각 노드를 생성하여 트리를 만듭니다.

2. **전위, 중위, 후위 순회 함수 구현**:
   각각의 순회 방식에 따라 트리를 순회하는 함수를 구현합니다. 각 함수는 재귀적으로 노드를 방문하여 결과 리스트에 추가합니다.

3. **결과 출력**:
   각 순회 함수의 결과를 문자열로 변환하여 출력합니다.

## 풀이 과정

1. **노드 클래스 정의**:
   노드 클래스는 노드의 값을 저장하고, 왼쪽과 오른쪽 자식을 참조합니다.

2. **이진 트리 구축**:
   `build_tree` 함수는 주어진 노드 정보를 바탕으로 트리를 구축합니다. 노드 정보를 순회하면서 각 노드를 생성하고, 해당 노드의 왼쪽과 오른쪽 자식을 설정합니다.

3. **순회 함수 구현**:
   - `preorder` 함수는 전위 순회를 구현합니다. 루트 노드를 먼저 처리하고, 왼쪽 자식과 오른쪽 자식을 순서대로 방문합니다.
   - `inorder` 함수는 중위 순회를 구현합니다. 왼쪽 자식을 먼저 방문하고, 루트 노드를 처리한 후, 오른쪽 자식을 방문합니다.
   - `postorder` 함수는 후위 순회를 구현합니다. 왼쪽 자식을 먼저 방문하고, 오른쪽 자식을 방문한 후, 루트 노드를 처리합니다.

4. **메인 함수**:
   표준 입력으로 데이터를 읽어들여 트리를 구축하고, 각 순회 방식의 결과를 출력합니다.

## 코드
```python
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

```