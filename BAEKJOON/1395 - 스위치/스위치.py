import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline을 사용합니다.

class SegmentTree:
    def __init__(self, n):
        # n은 스위치의 개수입니다.
        self.n = n
        # 구간의 켜진 스위치 개수를 저장하는 트리 배열입니다.
        self.tree = [0] * (4 * n)
        # 지연 갱신을 위한 lazy 배열입니다.
        self.lazy = [0] * (4 * n)
        
    def _update_lazy(self, node, start, end):
        # lazy 배열을 이용해 현재 노드의 반영이 필요한 경우 처리합니다.
        if self.lazy[node] != 0:  # lazy 값이 0이 아니라면 반전 필요
            # 현재 구간의 스위치 상태를 반전시킵니다.
            self.tree[node] = (end - start + 1) - self.tree[node]
            
            # 리프 노드가 아닐 경우 자식 노드에 lazy 값을 전파합니다.
            if start != end:
                # 자식 노드의 lazy 값을 반전합니다.
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
                
            # 현재 노드의 lazy 값을 초기화합니다.
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, l, r):
        # 현재 구간의 lazy 값을 먼저 반영합니다.
        self._update_lazy(node, start, end)
        
        # 현재 구간이 업데이트할 범위를 벗어나면 반환합니다.
        if start > r or end < l:
            return
        
        # 현재 구간이 완전히 업데이트할 범위에 포함될 경우
        if start >= l and end <= r:
            # 구간의 스위치 상태를 반전시킵니다.
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                # 자식 노드에 lazy 값을 반영합니다.
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
            return
        
        # 구간을 반으로 나누어 왼쪽, 오른쪽 자식 노드에 대해 재귀적으로 처리합니다.
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, l, r)
        self.update_range(node * 2 + 1, mid + 1, end, l, r)
        
        # 현재 노드의 값을 자식 노드의 값으로 갱신합니다.
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def query_range(self, node, start, end, l, r):
        # 현재 구간의 lazy 값을 먼저 반영합니다.
        self._update_lazy(node, start, end)
        
        # 현재 구간이 탐색할 범위를 벗어나면 0을 반환합니다.
        if start > r or end < l:
            return 0
        
        # 현재 구간이 완전히 탐색할 범위에 포함될 경우
        if start >= l and end <= r:
            # 현재 구간의 켜진 스위치 개수를 반환합니다.
            return self.tree[node]
        
        # 구간을 반으로 나누어 왼쪽, 오른쪽 자식 노드에 대해 재귀적으로 처리합니다.
        mid = (start + end) // 2
        left_query = self.query_range(node * 2, start, mid, l, r)
        right_query = self.query_range(node * 2 + 1, mid + 1, end, l, r)
        
        # 왼쪽과 오른쪽 결과를 합하여 반환합니다.
        return left_query + right_query

# 스위치 개수 n과 쿼리 개수 m을 입력 받습니다.
n, m = map(int, input().split())
# 세그먼트 트리 객체를 생성합니다.
segment_tree = SegmentTree(n)

# 결과를 저장할 리스트입니다.
results = []
for _ in range(m):
    # 각 쿼리에 대한 명령어와 범위를 입력 받습니다.
    o, si, ti = map(int, input().split())
    if o == 0:
        # o가 0일 경우 Si에서 Ti까지의 구간을 반전합니다.
        segment_tree.update_range(1, 0, n - 1, si - 1, ti - 1)
    elif o == 1:
        # o가 1일 경우 Si에서 Ti까지의 켜진 스위치 개수를 구하고 결과 리스트에 추가합니다.
        result = segment_tree.query_range(1, 0, n - 1, si - 1, ti - 1)
        results.append(result)

# 쿼리 결과를 출력합니다.
print("\n".join(map(str, results)))
