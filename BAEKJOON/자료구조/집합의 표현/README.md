# 집합의 표현 문제 풀이 과정

https://www.acmicpc.net/problem/1717

## 문제 이해 및 접근 방법

### 문제 이해
1. 처음에 \( n + 1 \)개의 집합 \(\{0\}, \{1\}, \{2\}, \ldots, \{n\}\)이 있습니다.
2. 두 종류의 연산이 주어집니다:
   - 합집합 연산 \(0 \ a \ b\): \(\{a\}\)와 \(\{b\}\)가 같은 집합에 포함되도록 합집합 연산을 수행합니다.
   - 찾기 연산 \(1 \ a \ b\): \(\{a\}\)와 \(\{b\}\)가 같은 집합에 포함되어 있는지 확인합니다.

### 접근 방법
1. **Union-Find 자료구조 초기화**:
   - 각 원소는 처음에 자기 자신을 대표로 가지도록 초기화합니다.

2. **Union 연산**:
   - 두 원소가 같은 집합에 속하도록 합집합 연산을 수행합니다.

3. **Find 연산**:
   - 주어진 원소가 속한 집합의 대표 원소를 찾습니다.

4. **연산 수행**:
   - 주어진 쿼리에 따라 합집합 연산(0 a b)과 찾기 연산(1 a b)을 수행하여 결과를 출력합니다.

## 코드 구현

```python
import sys
input = sys.stdin.read

def find(parent, x):
    # Find 함수: 원소 x가 속한 집합의 대표 원소를 찾는 함수
    # 경로 압축(Path Compression)을 사용하여 트리의 높이를 줄입니다.
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    # Union 함수: 원소 x와 y가 속한 두 집합을 합치는 함수
    # 두 집합의 루트를 찾은 후, 랭크(Rank)를 비교하여 트리의 높이가 낮은 쪽을 높은 쪽에 붙입니다.
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# 입력 처리
data = input().strip().split()
n = int(data[0])  # n은 집합의 개수
m = int(data[1])  # m은 연산의 개수

# 부모와 랭크 배열 초기화
# parent 리스트는 각 원소의 부모를 나타냅니다. 초기에는 자기 자신이 부모입니다.
# rank 리스트는 각 집합의 트리 높이를 나타냅니다.
parent = list(range(n + 1))
rank = [0] * (n + 1)

index = 2
result = []

# m개의 연산 처리
for _ in range(m):
    operation = int(data[index])  # 연산의 종류 (0: 합집합, 1: 찾기)
    a = int(data[index + 1])  # 첫 번째 원소
    b = int(data[index + 2])  # 두 번째 원소
    index += 3

    if operation == 0:
        # 합집합 연산: a와 b가 속한 집합을 합칩니다.
        union(parent, rank, a, b)
    elif operation == 1:
        # 찾기 연산: a와 b가 같은 집합에 속하는지 확인합니다.
        if find(parent, a) == find(parent, b):
            result.append("YES")
        else:
            result.append("NO")

# 결과 출력
sys.stdout.write("\n".join(result) + "\n")

