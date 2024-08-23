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
