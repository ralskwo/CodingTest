import sys
input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용

class SegmentTree:
    def __init__(self, data):
        # 세그먼트 트리 초기화
        # 입력 배열의 크기를 저장하고, 트리 배열의 크기를 4배로 설정하여 초기화
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)  # 초기 트리 구축

    def build(self, data, node, start, end):
        # 세그먼트 트리 빌드 함수
        # 리프 노드인 경우 배열의 값을 트리에 저장
        if start == end:
            self.tree[node] = data[start]
        else:
            # 내부 노드인 경우 자식 노드들을 재귀적으로 생성하고, 자식 노드의 합을 현재 노드에 저장
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(data, left_child, start, mid)  # 왼쪽 자식 노드 생성
            self.build(data, right_child, mid + 1, end)  # 오른쪽 자식 노드 생성
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # 자식 노드들의 합을 저장

    def update(self, idx, value, node, start, end):
        # 세그먼트 트리의 특정 인덱스를 주어진 값으로 갱신하는 함수
        if start == end:
            # 리프 노드에 도달한 경우 값 갱신
            self.tree[node] = value
        else:
            # 내부 노드인 경우 재귀적으로 자식 노드로 이동하여 갱신
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                # 갱신할 인덱스가 왼쪽 자식 노드의 구간에 있는 경우
                self.update(idx, value, left_child, start, mid)
            else:
                # 갱신할 인덱스가 오른쪽 자식 노드의 구간에 있는 경우
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # 갱신 후 부모 노드 값도 재계산

    def query(self, l, r, node, start, end):
        # 세그먼트 트리에서 특정 구간의 합을 계산하는 함수
        if r < start or end < l:
            # 구간이 겹치지 않는 경우 0을 반환
            return 0
        if l <= start and end <= r:
            # 구간이 완전히 포함되는 경우 해당 노드 값을 반환
            return self.tree[node]
        # 구간이 일부만 겹치는 경우 좌우 자식 노드를 재귀적으로 탐색
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query(l, r, left_child, start, mid)  # 왼쪽 자식 구간 합 계산
        right_sum = self.query(l, r, right_child, mid + 1, end)  # 오른쪽 자식 구간 합 계산
        return left_sum + right_sum  # 두 구간 합을 더하여 반환

    def update_value(self, idx, value):
        # 외부에서 호출할 수 있는 간단한 갱신 함수
        self.update(idx, value, 0, 0, self.n - 1)

    def range_query(self, l, r):
        # 외부에서 호출할 수 있는 간단한 구간 합 함수
        return self.query(l, r, 0, 0, self.n - 1)

n, q = map(int, input().split())  # 정수 배열의 길이 n과 쿼리의 개수 q를 입력받음
data = list(map(int, input().split()))  # 초기 배열을 입력받음

seg_tree = SegmentTree(data)  # 입력 배열을 기반으로 세그먼트 트리 생성
results = []  # 각 쿼리의 구간 합 결과를 저장할 리스트

for _ in range(q):
    # 각 쿼리를 처리
    x, y, a, b = map(int, input().split())
    x -= 1  # 1-인덱스에서 0-인덱스로 변환
    y -= 1
    a -= 1

    # x와 y의 크기에 관계없이 작은 값부터 큰 값으로 구간 설정
    l, r = min(x, y), max(x, y)
    results.append(seg_tree.range_query(l, r))  # 구간 합을 계산하여 결과 리스트에 추가

    # a번째 인덱스 값을 b로 갱신
    seg_tree.update_value(a, b)

print("\n".join(map(str, results)))  # 모든 구간 합 결과를 출력