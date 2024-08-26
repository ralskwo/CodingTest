class SegmentTree:
    def __init__(self, n):  # 세그먼트 트리 초기화 메서드
        self.n = n  # 트리에서 관리할 맛의 범위 크기 (예: 1부터 n까지)
        self.tree = [0] * (4 * n)  # 트리 배열 초기화 (4*n 크기)

    def update(self, idx, diff, node, node_left, node_right):  # 트리 업데이트 메서드
        if idx < node_left or node_right < idx:  # 업데이트하려는 인덱스가 현재 노드의 범위 밖이면 종료
            return
        self.tree[node] += diff  # 현재 노드에 diff를 더함 (사탕의 수 변화 반영)
        if node_left != node_right:  # 리프 노드가 아닌 경우
            mid = (node_left + node_right) // 2  # 현재 구간을 반으로 나눔
            # 좌측 자식 노드에 업데이트 전파
            self.update(idx, diff, node * 2, node_left, mid)
            # 우측 자식 노드에 업데이트 전파
            self.update(idx, diff, node * 2 + 1, mid + 1, node_right)

    def query(self, k, node, node_left, node_right):  # k번째 사탕 찾기 위한 쿼리 메서드
        if node_left == node_right:  # 리프 노드에 도달한 경우
            return node_left  # 해당 리프 노드의 인덱스를 반환 (사탕의 맛 번호)
        mid = (node_left + node_right) // 2  # 현재 구간을 반으로 나눔
        if k <= self.tree[node * 2]:  # k번째 사탕이 왼쪽 구간에 있는 경우
            return self.query(k, node * 2, node_left, mid)  # 왼쪽 자식 노드로 이동하여 계속 탐색
        else:  # k번째 사탕이 오른쪽 구간에 있는 경우
            # 오른쪽 자식 노드로 이동하며, 왼쪽 노드의 사탕 수를 k에서 뺌
            return self.query(k - self.tree[node * 2], node * 2 + 1, mid + 1, node_right)

    def add(self, idx, diff):  # 사탕의 수를 추가하거나 제거하는 메서드
        self.update(idx, diff, 1, 1, self.n)  # 인덱스 idx에 해당하는 사탕의 변화를 트리에 반영

    def find_kth(self, k):  # k번째 맛의 사탕을 찾는 메서드
        return self.query(k, 1, 1, self.n)  # k번째 사탕의 맛 번호를 반환

import sys
input = sys.stdin.read  # 입력을 빠르게 처리하기 위해 sys.stdin.read 사용
data = input().splitlines()  # 여러 줄 입력을 받아 줄 단위로 나눔

n = int(data[0])  # 첫 번째 줄: 수정이가 사탕상자에 손을 댄 횟수
commands = [list(map(int, line.split())) for line in data[1:]]  # 나머지 줄: 명령어 리스트로 변환

MAX_TASTE = 1000000  # 사탕의 맛 번호의 최대값 (1부터 1000000까지)
seg_tree = SegmentTree(MAX_TASTE)  # 사탕 맛 범위를 기반으로 세그먼트 트리 생성

result = []  # 출력 결과를 저장할 리스트

for command in commands:  # 각 명령어를 순차적으로 처리
    if command[0] == 1:  # A가 1인 경우 (사탕을 꺼내는 경우)
        k = command[1]  # B: 꺼낼 사탕의 순위
        taste = seg_tree.find_kth(k)  # k번째 사탕의 맛 번호 찾기
        result.append(taste)  # 결과 리스트에 추가
        seg_tree.add(taste, -1)  # 해당 맛의 사탕을 1개 제거
    elif command[0] == 2:  # A가 2인 경우 (사탕을 넣거나 제거하는 경우)
        taste = command[1]  # B: 넣을 사탕의 맛 번호
        count = command[2]  # C: 넣을 사탕의 개수 (음수면 제거)
        seg_tree.add(taste, count)  # 해당 맛의 사탕을 count만큼 추가 또는 제거

sys.stdout.write('\n'.join(map(str, result)) + '\n')  # 모든 출력 결과를 한 번에 출력
