# 커피숍2 문제 풀이 및 설명

<https://www.acmicpc.net/problem/1275>

<https://mayquartet.com/python-파이썬-백준-1275-커피숍2/>

## 문제 이해

이 문제는 주어진 정수 배열에서 특정 구간의 합을 빠르게 구하고, 특정 인덱스의 값을 다른 값으로 변경하는 작업을 반복하는 게임에 대한 것입니다. 각각의 요청(쿼리)에 따라 두 가지 작업이 번갈아 가며 수행됩니다:

1. 특정 구간의 합을 계산하는 요청
2. 특정 위치의 값을 변경하는 요청

주어진 배열의 크기와 요청 횟수가 최대 100,000에 이를 수 있으므로, 배열을 매번 순회하며 구간 합을 구하거나 값을 변경하는 방식은 비효율적입니다. 따라서, 구간 합과 값 변경 작업을 효율적으로 처리할 수 있는 자료구조를 사용하는 것이 필요합니다.

일반적으로 이러한 유형의 문제는 **세그먼트 트리** 또는 **펜윅 트리(= 바이너리 인덱스 트리)**를 사용해 풀이할 수 있습니다. 여기서는 세그먼트 트리를 사용하여 각 요청에 대해 효율적으로 처리하는 방식을 채택합니다.

## 입출력 조건

- **입력**:

  1. 첫 번째 줄에는 배열의 크기 `N`과 요청(쿼리)의 수 `Q`가 공백을 두고 주어집니다. 여기서 `N`과 `Q`는 각각 1 이상 100,000 이하의 정수입니다.
  2. 두 번째 줄에는 정수 `N`개가 공백으로 구분되어 주어지며, 각 정수는 배열의 초기 값을 나타냅니다. 이 정수는 `-2^31` 이상 `2^31 - 1` 이하의 값을 가질 수 있습니다.
  3. 세 번째 줄부터 `Q+2`번째 줄까지는 각 요청이 주어집니다. 각 요청은 네 개의 정수 `x`, `y`, `a`, `b`로 구성됩니다:
     - `x`부터 `y`까지의 구간 합을 구하라는 의미이며,
     - `a`번째 위치의 값을 `b`로 변경하라는 뜻입니다.
     - `x`와 `y`는 구간의 시작과 끝을 의미하며, 이 두 값은 문제의 설명에 따라 큰 수와 작은 수의 순서가 주어질 수 있으므로, 두 값 중 작은 값을 구간의 시작으로, 큰 값을 구간의 끝으로 정합니다.

- **출력**:
  - 각 쿼리의 구간 합 계산 결과를 한 줄씩 출력합니다.

## 접근 방식

이 문제는 효율적으로 구간 합을 구하고 특정 인덱스의 값을 갱신할 수 있는 자료구조를 필요로 합니다. 배열의 길이와 쿼리의 수가 최대 100,000이므로 `O(N)`에 해당하는 단순 구간 합 계산을 매번 수행한다면 시간 초과가 발생합니다. 따라서, 구간 합과 값 변경을 빠르게 처리할 수 있는 **세그먼트 트리**를 이용해 해결할 수 있습니다.

세그먼트 트리는 다음과 같은 방식으로 사용됩니다:

1. **구간 합 계산**: 특정 구간 합을 구하는 데 `O(log N)`의 시간 복잡도로 빠르게 접근할 수 있습니다. 주어진 `x`와 `y`의 순서를 정렬하여 작은 값부터 큰 값까지의 구간 합을 구합니다.

2. **값 변경**: 특정 인덱스의 값을 다른 값으로 변경할 때에도 세그먼트 트리를 이용하여 `O(log N)`의 시간 복잡도로 갱신이 가능합니다.

이렇게 세그먼트 트리를 통해 구간 합과 값 갱신을 처리하면 매번 전체 배열을 탐색하지 않고도 효율적으로 요청을 처리할 수 있습니다.

<https://mayquartet.com/algorithm-세그먼트-트리segment-tree-알고리즘-이해하기/>

## 풀이 과정

1. **세그먼트 트리 초기화**:

   - 입력으로 받은 배열을 기반으로 세그먼트 트리를 초기화합니다. 트리는 배열의 모든 구간 합을 효율적으로 저장하도록 구성되며, 각 노드는 특정 구간의 합을 저장하게 됩니다.
   - 이 초기화 과정은 재귀적으로 수행되며 `O(N)`의 시간 복잡도를 가집니다.

2. **구간 합 쿼리 처리**:

   - 쿼리 요청에서 구간 합을 요청받으면, 세그먼트 트리를 통해 해당 구간의 합을 빠르게 계산합니다.
   - 문제에서 `x`와 `y`가 순서대로 주어지지 않을 수 있기 때문에, `x`와 `y`의 값 중 작은 값을 시작으로, 큰 값을 끝으로 정렬하여 구간을 설정합니다.
   - 구간 합 계산은 `O(log N)`의 시간 복잡도를 가지며, 세그먼트 트리의 노드에서 필요한 구간의 합만을 더하여 반환합니다.

3. **값 변경 쿼리 처리**:

   - 특정 위치의 값을 새로운 값으로 변경하는 요청을 받으면, 세그먼트 트리에서 해당 위치의 값을 갱신합니다.
   - 값 변경 작업 또한 `O(log N)`에 수행되며, 변경된 값을 기준으로 트리의 상위 노드들도 갱신됩니다.

4. **출력**:
   - 모든 구간 합 요청의 결과를 `results` 리스트에 저장하고, 모든 쿼리가 처리된 후 리스트의 값을 한 줄씩 출력합니다.

## 코드 구현

```python
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
```
