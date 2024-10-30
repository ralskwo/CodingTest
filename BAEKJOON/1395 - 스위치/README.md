# 스위치 문제 풀이 및 설명

<https://www.acmicpc.net/problem/1395>

<https://mayquartet.com/python-백준-1395-스위치/>

## 문제 이해

이 문제는 기본적으로 `N`개의 스위치가 있을 때, 이 스위치들의 상태를 조작하거나 상태를 확인하는 작업을 빠르게 수행하는 방법을 묻고 있습니다. 처음에 모든 스위치는 꺼진 상태(`0`)이며, 주어진 두 가지 작업을 여러 번 반복합니다. 작업은 크게 두 가지로 나뉩니다. 첫 번째는 특정 구간의 스위치 상태를 반전시키는 작업이며, 두 번째는 특정 구간에서 켜져 있는 스위치 개수를 세는 작업입니다. 문제의 목적은 이러한 작업을 효율적으로 처리하여 각각의 결과를 출력하는 것입니다.

주어진 스위치의 개수 `N`과 작업의 개수 `M`이 최대 100,000에 달하므로, 각 작업을 빠르게 수행하지 않으면 시간 초과가 발생합니다. 따라서 각 작업을 효율적으로 수행할 수 있는 자료 구조와 알고리즘을 사용하는 것이 필수입니다.

## 입출력 조건

- **입력 조건**  
  첫 번째 줄에는 스위치의 개수 `N`과 작업의 개수 `M`이 주어집니다.  
  다음 `M`개의 줄에는 각각 세 개의 정수 `O`, `Si`, `Ti`가 주어집니다.

  - `O`가 `0`일 때는 `Si`번 스위치부터 `Ti`번 스위치까지의 상태를 반전시킵니다.
  - `O`가 `1`일 때는 `Si`번 스위치부터 `Ti`번 스위치까지 켜져 있는 스위치의 개수를 구하여야 합니다.  
    스위치의 번호는 1번부터 시작하며, 문제에서는 1-based indexing을 사용합니다.

- **출력 조건**  
  각 `O=1` 쿼리마다 결과값을 한 줄에 하나씩 출력합니다.

## 접근 방식

이 문제는 구간에 대한 상태 변환 및 집계 연산을 요구하므로, 효율적인 구간 관리가 가능한 자료 구조를 사용하는 것이 중요합니다. 각 구간에 대해 반전 연산을 수행하고 켜진 스위치의 개수를 세야 하므로, 다음과 같은 두 가지 자료 구조적 개념을 사용합니다.

1. **세그먼트 트리(Segment Tree)**  
   세그먼트 트리는 구간 쿼리 문제를 해결하기 위한 대표적인 자료 구조입니다. 각 구간의 합, 최솟값, 최댓값 등을 빠르게 계산할 수 있으며, 특정 구간의 값을 효율적으로 갱신할 수 있습니다. 이 문제에서는 세그먼트 트리를 사용하여 각 구간에서 켜져 있는 스위치의 개수를 관리합니다.

2. **지연 갱신(Lazy Propagation)**  
   구간을 갱신하는 반전 연산이 자주 발생할 경우, 매번 구간의 모든 요소를 직접 갱신하면 비효율적입니다. 따라서 `Lazy Propagation`을 사용하여 필요한 시점에만 갱신이 이루어지도록 합니다. 이렇게 하면 특정 구간의 값만 빠르게 갱신할 수 있고, 다음 쿼리 때만 필요한 부분을 갱신하므로 성능이 크게 향상됩니다.

이 문제에서 `Lazy Propagation`을 사용해 반전 연산을 지연시킴으로써, 구간별 반전과 켜진 스위치 개수 계산 쿼리를 각각 `O(log N)`의 시간 복잡도로 처리할 수 있습니다.

<https://mayquartet.com/algorithm-세그먼트-트리segment-tree-알고리즘-이해하기/>

## 풀이 과정

1. **세그먼트 트리 초기화**  
   `N`개의 스위치를 관리할 수 있는 세그먼트 트리를 생성합니다. 각 노드에는 해당 구간 내 켜진 스위치의 개수가 저장됩니다. 초기 상태에서 모든 스위치가 꺼져 있으므로, 트리의 모든 노드는 `0`으로 초기화합니다.

2. **Lazy Propagation 설정**  
   구간을 반전할 때 자주 사용하는 `Lazy Propagation` 기법을 설정합니다. `lazy` 배열을 사용하여 구간 갱신 연산을 지연시키며, 특정 구간에 반전 요청이 들어오면 해당 구간의 `lazy` 값을 토글(`0`을 `1`로, `1`을 `0`으로)합니다. 이를 통해 필요할 때만 반전 연산이 적용되도록 합니다.

3. **반전 쿼리(`O=0`) 처리**  
   특정 구간 `[Si, Ti]`에 대해 스위치 상태를 반전시켜야 할 때, `lazy` 배열을 활용하여 해당 구간에 대해 반전 지시를 남겨둡니다. 이렇게 하면 해당 구간을 나중에 참조할 때 `lazy` 값을 통해 켜짐 또는 꺼짐 상태를 반전시킬 수 있습니다. 자식 노드에도 `lazy` 값을 전파하여 자식 구간에서도 반전이 일어날 수 있도록 합니다.

4. **켜진 스위치 개수 쿼리(`O=1`) 처리**  
   특정 구간 `[Si, Ti]`에서 켜져 있는 스위치의 개수를 구할 때는, 먼저 해당 구간의 `lazy` 값을 반영하여 최신 상태로 반영합니다. 이후, 구간 내 켜진 스위치 개수를 반환하도록 합니다. 이렇게 함으로써 빠르게 켜진 스위치 개수를 확인할 수 있습니다.

5. **결과 출력**  
   모든 쿼리를 처리하면서 `O=1` 쿼리에 대한 결과를 리스트에 저장하고, 마지막에 이 결과들을 출력합니다.

## 코드 구현

```python
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
```
