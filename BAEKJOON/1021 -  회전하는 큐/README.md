# 회전하는 큐 문제 풀이 및 설명

https://www.acmicpc.net/problem/1021

https://mayquartet.com/python-%ed%8c%8c%ec%9d%b4%ec%8d%ac-%eb%b0%b1%ec%a4%80-1021-%ed%9a%8c%ec%a0%84%ed%95%98%eb%8a%94-%ed%81%90-%eb%ac%b8%ec%a0%9c-%ed%92%80%ec%9d%b4-%eb%b0%8f-%ec%84%a4%eb%aa%85/

## 문제 이해

이 문제는 양방향 순환 큐에서 특정 위치에 있는 원소를 뽑아내는 과정을 다룹니다. 주어진 큐는 앞뒤로 자유롭게 회전할 수 있으며, 우리는 주어진 순서대로 큐에서 원소를 뽑아내야 합니다. 이때, 큐의 회전을 최소화하는 것이 목표입니다. 문제에서 요구하는 것은 원소를 순서대로 뽑아내는데 필요한 회전 연산의 최소 횟수를 계산하는 것입니다.

즉, 주어진 원소들을 뽑아내기 위해 큐를 왼쪽 또는 오른쪽으로 회전시킬 수 있는데, 이 회전의 횟수를 최소화하여 목표 원소를 맨 앞으로 가져오고, 그 후 뽑아내는 방식으로 문제를 해결해야 합니다.

## 입출력 조건

- **입력 조건**
  - 첫 번째 줄에는 큐의 크기 `N`과 뽑아내야 할 원소의 개수 `M`이 주어집니다. 여기서 `N`은 50 이하의 자연수, `M`은 `N`보다 작거나 같은 자연수입니다.
  - 두 번째 줄에는 뽑아내야 할 원소의 위치가 순서대로 주어집니다. 위치는 1부터 시작하며, `N` 이하의 자연수입니다.
- **출력 조건**
  - 뽑아내기 위해 필요한 2번과 3번 연산(회전)의 최소 횟수를 한 줄에 출력합니다.

## 접근 방식

이 문제를 풀기 위해서는 `deque` 자료구조를 활용하는 것이 효과적입니다. `deque`는 양방향 큐로, 양쪽 끝에서 삽입과 삭제가 모두 가능하기 때문에 큐를 왼쪽이나 오른쪽으로 회전시키는 연산을 효율적으로 처리할 수 있습니다.

문제를 해결하기 위해 다음과 같은 단계를 거칩니다:

1. **위치 계산**: 각 목표 원소에 대해 현재 큐에서의 위치를 계산합니다.
2. **회전 방향 결정**: 해당 원소를 맨 앞으로 이동시키기 위해 큐를 왼쪽으로 회전하는 것이 빠를지, 오른쪽으로 회전하는 것이 빠를지를 계산합니다. 이때 더 적은 연산이 필요한 방향으로 큐를 회전시킵니다.
3. **연산 횟수 누적**: 선택한 회전 방향에 따른 연산 횟수를 누적합니다.
4. **원소 제거**: 원소를 큐에서 제거한 후, 남은 원소들에 대해 동일한 과정을 반복합니다.

이 방식으로 모든 원소를 순서대로 뽑아내면서 연산 횟수를 최소화할 수 있습니다.

## 풀이 과정

1. **초기화**: 먼저, 1부터 `N`까지의 숫자로 이루어진 큐를 생성합니다. 이 큐는 `deque` 자료구조로 초기화됩니다. 또한, 총 연산 횟수를 기록할 변수를 0으로 초기화합니다.

2. **목표 원소 처리**: 뽑아내야 할 각 원소에 대해 순차적으로 접근합니다. 현재 큐에서 목표 원소의 위치를 찾습니다. 이때 목표 원소가 현재 큐의 첫 번째 원소가 될 때까지 큐를 회전시켜야 합니다.

3. **회전 방향 선택**: 목표 원소의 위치에 따라 큐를 왼쪽으로 회전하는 것이 빠른지, 오른쪽으로 회전하는 것이 빠른지를 판단합니다. 만약 왼쪽으로 회전하는 것이 더 빠르다면, 왼쪽으로 회전한 횟수를 연산 횟수에 더하고, 큐를 왼쪽으로 회전시킵니다. 반대로 오른쪽으로 회전하는 것이 더 빠르다면, 오른쪽으로 회전한 횟수를 연산 횟수에 더하고, 큐를 오른쪽으로 회전시킵니다.

4. **원소 제거**: 회전을 통해 목표 원소가 큐의 첫 번째 위치로 오면, 해당 원소를 큐에서 제거합니다.

5. **반복**: 모든 목표 원소를 처리할 때까지 위 과정을 반복하며, 모든 목표 원소를 제거한 후 최종적으로 계산된 연산 횟수를 출력합니다.

## 코드 구현

```python
from collections import deque  # collections 모듈에서 deque를 가져옵니다. deque는 양방향 큐를 쉽게 다룰 수 있게 해줍니다.

def min_operations(n, m, positions):
    dq = deque(range(1, n + 1))  # 1부터 n까지의 숫자로 초기화된 큐를 생성합니다.
    operations = 0  # 연산 횟수를 저장할 변수를 초기화합니다.

    for position in positions:  # 뽑아내고자 하는 위치들을 순서대로 처리합니다.
        idx = dq.index(position)  # 현재 큐에서 목표 위치의 인덱스를 찾습니다.

        if idx < len(dq) - idx:  # 왼쪽으로 이동하는 것이 빠른지 확인합니다.
            operations += idx  # 왼쪽으로 이동한 횟수를 연산 횟수에 더합니다.
            dq.rotate(-idx)  # 큐를 왼쪽으로 idx만큼 회전시킵니다.
        else:  # 오른쪽으로 이동하는 것이 더 빠른 경우
            operations += len(dq) - idx  # 오른쪽으로 이동한 횟수를 연산 횟수에 더합니다.
            dq.rotate(len(dq) - idx)  # 큐를 오른쪽으로 (len(dq) - idx)만큼 회전시킵니다.

        dq.popleft()  # 첫 번째 원소(목표 위치의 원소)를 큐에서 제거합니다.

    return operations  # 총 연산 횟수를 반환합니다.

n, m = map(int, input().split())  # 첫 번째 줄에서 큐의 크기 n과 뽑아낼 위치의 수 m을 입력받습니다.
positions = list(map(int, input().split()))  # 두 번째 줄에서 뽑아낼 위치들을 리스트로 입력받습니다.

print(min_operations(n, m, positions))  # 연산 결과를 출력합니다.
```
