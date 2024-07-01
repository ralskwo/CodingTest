# 이진 검색 트리 후위 순회 구하기

## 문제 이해

주어진 문제는 전위 순회 결과를 이용하여 이진 검색 트리(BST)를 재구성하고, 후위 순회를 출력하는 것입니다. 전위 순회의 첫 번째 원소는 트리의 루트가 되며, 이후 원소들은 루트를 기준으로 왼쪽 서브트리와 오른쪽 서브트리로 나뉩니다. 이를 이용하여 후위 순회를 구합니다.

## 접근 방식

1. **전위 순회 결과를 이용하여 트리 재구성**:
   - 전위 순회의 첫 번째 원소는 트리의 루트입니다.
   - 이후 원소들을 루트를 기준으로 왼쪽 서브트리와 오른쪽 서브트리로 분할합니다.

2. **트리 재구성**:
   - 재귀적으로 노드를 삽입하여 트리를 구성합니다.

3. **후위 순회 수행**:
   - 트리의 후위 순회를 수행하여 결과를 출력합니다.

## 코드 설명

```python
import sys
sys.setrecursionlimit(10**6)  # 재귀 한도를 늘림
input = sys.stdin.read

def find_postorder(preorder, start, end):
    if start > end:  # 범위가 잘못된 경우 종료
        return

    root = preorder[start]  # 현재 서브트리의 루트
    right_start = start + 1  # 오른쪽 서브트리의 시작 지점 찾기

    while right_start <= end and preorder[right_start] < root:
        right_start += 1

    # 왼쪽 서브트리에 대해 재귀 호출
    find_postorder(preorder, start + 1, right_start - 1)
    # 오른쪽 서브트리에 대해 재귀 호출
    find_postorder(preorder, right_start, end)
    # 후위 순회 결과에 현재 루트 추가
    postorder.append(root)

# 입력 처리
preorder = list(map(int, input().split()))  # 전위 순회 결과 입력
postorder = []  # 후위 순회 결과를 저장할 리스트

# 후위 순회 구하기
find_postorder(preorder, 0, len(preorder) - 1)

# 결과 출력
for value in postorder:
    print(value)
```