# 달리기 문제 풀이 및 설명

<https://www.acmicpc.net/problem/2517>

<https://mayquartet.com/python-파이썬-백준-2517-달리기/>

## 문제 이해

이 문제는 KOI 장거리 달리기 대회에서 각 선수가 얻을 수 있는 최선의 등수를 계산하는 문제입니다. 문제의 핵심은 각 선수가 자신보다 앞에 있는 선수들 중 실력이 더 좋은 사람은 앞지르지 못하지만, 실력이 낮은 선수는 앞지를 수 있다는 점입니다. 따라서 각 선수는 현재 위치에서 자신이 추월할 수 있는 사람들을 고려하여 최선의 등수를 결정해야 합니다.

각 선수의 실력은 정수로 주어지며, 더 큰 값이 더 좋은 실력을 의미합니다. 예를 들어, 앞서 달리고 있는 선수들 중 실력이 더 높은 사람은 추월할 수 없고, 실력이 낮은 사람만 추월할 수 있으므로, 선수의 위치와 실력을 기반으로 최선의 등수를 계산해야 합니다.

## 입출력 조건

### 입력 조건

- 첫째 줄에는 선수의 수 `N`이 주어집니다. (`3 ≤ N ≤ 500,000`)
- 이후 `N`개의 줄에는 각 선수의 평소 실력을 나타내는 정수가 한 줄에 하나씩 주어집니다. 각 정수는 `1` 이상 `1,000,000,000` 이하이며, 모든 참가자의 실력은 서로 다릅니다.

### 출력 조건

- 각 선수의 최선의 등수를 나타내는 정수 `N`개를 입력에 주어진 선수 순서와 동일한 순서로 한 줄에 하나씩 출력합니다.

## 접근 방식

1. **좌표 압축**: 실력 값의 범위가 `1`부터 `1,000,000,000`까지 매우 크기 때문에, 이 값을 그대로 사용하여 세그먼트 트리나 펜윅 트리를 사용할 경우 트리의 크기가 지나치게 커집니다. 따라서, 각 선수의 실력을 압축하여 작은 범위로 매핑해주는 좌표 압축을 적용합니다. 이는 입력된 값의 순서를 유지하면서 값을 작은 범위의 순위로 변환해 트리의 크기를 줄이는 방법입니다.
2. **펜윅 트리(Fenwick Tree)**: 펜윅 트리는 구간 합을 빠르게 계산하고 업데이트할 수 있는 자료구조입니다. 이 문제에서는 특정 범위 내에 있는 값의 개수를 빠르게 구하기 위해 펜윅 트리를 사용합니다. 각 선수의 위치에서 실력이 자신보다 낮은 선수의 수를 구하여 최선의 등수를 계산합니다.
3. **압축된 값을 이용한 쿼리와 업데이트**: 좌표 압축을 통해 변환된 실력 값을 이용하여, 펜윅 트리에서 특정 범위에 존재하는 선수 수를 구합니다. 현재 선수의 실력을 트리에 추가하며, 이를 통해 이후 선수들의 최선의 등수 계산에 반영되도록 합니다.

## 풀이 과정

1. **입력 처리 및 좌표 압축**:

   - 먼저 `N`과 `N`개의 실력 값을 입력받고, 실력 값에 대해 좌표 압축을 적용합니다. 좌표 압축을 통해 실력 값을 1부터 시작하는 순위로 변환하여 트리의 크기를 줄입니다.

2. **펜윅 트리 초기화**:

   - 압축된 실력 값의 최대값을 이용해 펜윅 트리의 크기를 결정하고, 이를 초기화합니다. 펜윅 트리는 `1`부터 `max_value`까지의 인덱스를 사용해 빠르게 구간 합과 업데이트를 수행할 수 있도록 설정합니다.

3. **최선의 등수 계산**:

   - 압축된 실력 값을 순회하며, 각 선수의 최선의 등수를 계산합니다. 현재 선수보다 높은 실력을 가진 사람의 수를 트리에서 쿼리하여 얻습니다. 이 값은 현재 선수가 추월할 수 있는 최대한의 수를 의미하며, 이를 통해 선수의 최선의 등수를 계산합니다. 쿼리는 `ability - 1`까지의 범위를 조회하여 자신보다 높은 실력을 가진 선수를 계산합니다.
   - 현재 선수의 실력을 펜윅 트리에 업데이트하여 이후 선수들이 해당 선수를 고려할 수 있도록 합니다. 이는 현재 선수의 위치를 기록하는 과정입니다.

4. **결과 출력**:
   - 모든 선수에 대해 최선의 등수를 계산한 뒤, 이를 리스트에 저장하고 `sys.stdout`을 사용해 한 줄씩 출력합니다. 이는 입력의 순서를 유지하며 빠르게 결과를 출력하기 위함입니다.

이와 같은 접근 방식을 통해 각 선수의 위치와 실력을 고려한 최선의 등수를 빠르게 계산할 수 있습니다. 좌표 압축을 통해 메모리 사용을 줄이고, 펜윅 트리를 통해 구간 합을 효율적으로 계산함으로써 시간 복잡도를 줄이는 것이 문제 해결의 핵심입니다.

## 코드 구현

```python
import sys

# 펜윅 트리(Fenwick Tree)를 정의하는 클래스
class FenwickTree:
    def __init__(self, size):
        # 트리의 크기를 저장하고, 그 크기만큼의 배열을 초기화한다.
        self.size = size
        self.tree = [0] * (size + 1)

    # 특정 인덱스에 값을 추가하는 함수
    def update(self, index, value):
        # 인덱스가 트리의 크기를 넘지 않을 때까지 값을 추가
        while index <= self.size:
            self.tree[index] += value
            # 인덱스를 업데이트하여 다음 노드로 이동
            index += index & -index

    # 특정 인덱스까지의 누적 합을 계산하는 함수
    def query(self, index):
        result = 0
        # 인덱스가 0보다 클 때까지 값을 누적
        while index > 0:
            result += self.tree[index]
            # 인덱스를 업데이트하여 이전 노드로 이동
            index -= index & -index
        return result

# 좌표 압축을 수행하는 함수
def coordinate_compress(values):
    # 입력값들을 중복 제거 및 내림차순 정렬
    sorted_unique = sorted(set(values), reverse=True)
    # 정렬된 값을 기반으로 각 값에 순위를 매겨 매핑
    rank = {value: idx + 1 for idx, value in enumerate(sorted_unique)}
    # 입력값들을 순위로 변환하여 반환
    return [rank[value] for value in values]

# 문제를 해결하는 메인 함수
def solve():
    # 첫 줄에서 선수의 수를 입력받음
    N = int(sys.stdin.readline())
    # 각 선수의 실력을 리스트에 저장
    abilities = [int(sys.stdin.readline()) for _ in range(N)]

    # 좌표 압축 수행
    compressed_abilities = coordinate_compress(abilities)
    # 펜윅 트리의 크기는 압축된 최대값으로 설정
    max_value = max(compressed_abilities)
    fenwick_tree = FenwickTree(max_value)

    results = []
    # 각 선수의 압축된 실력을 순회하며 등수를 계산
    for ability in compressed_abilities:
        # 현재 선수보다 실력이 낮은 선수의 수를 쿼리
        higher_count = fenwick_tree.query(ability - 1)
        # 현재 선수의 최선의 등수를 결과 리스트에 추가
        results.append(higher_count + 1)
        # 현재 선수의 실력을 펜윅 트리에 업데이트하여 이후 계산에 반영
        fenwick_tree.update(ability, 1)

    # 결과를 한 줄씩 출력
    sys.stdout.write("\n".join(map(str, results)) + '\n')

# 문제 해결 함수 실행
solve()
```
