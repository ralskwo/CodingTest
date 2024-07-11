# 악당 로봇 문제 풀이 및 설명

https://www.acmicpc.net/problem/5905

## 문제 이해

슈퍼히어로 방송원은 악당 지구를 침략한 악당 로봇들을 해치우는 데 성공했습니다. 로봇은 N개의 취약점을 가지고 있으며, 취약점은 'A', 'B', 'C'로 이루어진 15개의 문자열 중 하나입니다. 각 취약점은 하나의 로봇을 의미하며, 이를 통해 방송원이 로봇을 공격할 수 있습니다. 방송원은 로봇의 취약점을 맞히기만 해도 공격에 성공합니다.

방송원이 여러 개의 취약점을 한꺼번에 공격할 수도 있고, 동일한 취약점을 여러 번 사용할 수도 있습니다. 주어진 시간 내에 방송원이 최대 몇 번의 공격을 할 수 있는지를 구하는 문제입니다.

## 접근 방식

이 문제는 문자열 매칭 알고리즘 중 하나인 **Aho-Corasick 알고리즘**을 사용하여 해결할 수 있습니다. Aho-Corasick 알고리즘은 다수의 패턴을 효율적으로 찾을 수 있는 알고리즘으로, 주어진 텍스트에서 여러 패턴을 동시에 찾는 데 적합합니다. 이 알고리즘을 사용하여 주어진 모든 취약점을 트라이 자료구조에 저장하고, 각 상태에 대한 실패 링크를 구축한 후, 동적 계획법(DP)을 이용하여 최적의 해를 구합니다.

## 풀이 과정

1. **Aho-Corasick 트라이 구축**
   - 각 취약점을 트라이에 삽입합니다.
   - 트라이의 각 상태는 다음 상태로의 전이 테이블을 가집니다. 여기서 'A', 'B', 'C'는 각각 인덱스 0, 1, 2로 매핑됩니다.
   - 실패 링크를 구축하여, 매칭 실패 시 이동할 상태를 설정합니다.

2. **동적 계획법(DP) 배열 초기화**
   - DP 배열을 초기화합니다. `dp[k][state]`는 길이 k의 문자열이 주어졌을 때, 트라이의 특정 상태에 있을 때의 최대 매칭 수를 의미합니다.
   - 초기 상태인 루트 상태에서 시작하여, 문자열의 길이가 0일 때의 초기 값을 설정합니다.

3. **DP를 통한 최적의 해 계산**
   - 문자열의 길이 K까지 반복하면서, 각 상태에 대해 가능한 모든 전이를 처리합니다.
   - 각 문자를 처리할 때마다 트라이의 상태를 전이하고, 실패 링크를 따라가며 최적의 매칭 수를 계산합니다.
   - DP 배열을 갱신하여, 최적의 매칭 수를 기록합니다.

4. **최대 매칭 수 계산**
   - DP 배열을 모두 채운 후, 마지막 문자열의 길이 K에서 가능한 모든 상태의 최대 값을 구합니다.

## 코드
```python
from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.num_states = 1
        self.transition = defaultdict(lambda: [0] * 3)
        self.fail = [0] * (20 * 15 + 2)
        self.output = [0] * (20 * 15 + 2)

    def insert(self, word):
        current_state = 1
        for char in word:
            index = ord(char) - ord('A')
            if self.transition[current_state][index] == 0:
                self.num_states += 1
                self.transition[current_state][index] = self.num_states
            current_state = self.transition[current_state][index]
        self.output[current_state] += 1

    def build_failure(self):
        queue = deque([1])
        self.fail[1] = 1

        while queue:
            current_state = queue.popleft()
            for i in range(3):
                next_state = self.transition[current_state][i]
                if next_state == 0:
                    continue

                if current_state == 1:
                    self.fail[next_state] = 1
                    queue.append(next_state)
                    continue

                failure_state = self.fail[current_state]
                while failure_state != 1 and self.transition[failure_state][i] == 0:
                    failure_state = self.fail[failure_state]

                if self.transition[failure_state][i] != 0:
                    failure_state = self.transition[failure_state][i]

                self.fail[next_state] = failure_state
                self.output[next_state] += self.output[failure_state]
                queue.append(next_state)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    K = int(data[1])
    patterns = data[2:2 + N]
    ac = AhoCorasick()

    for pattern in patterns:
        ac.insert(pattern)

    ac.build_failure()

    dp = [[-1] * (20 * 15 + 2) for _ in range(K + 2)]
    dp[0][1] = 0

    for k in range(K + 1):
        for state in range(1, ac.num_states + 1):
            if dp[k][state] == -1:
                continue

            for i in range(3):
                current_state = state

                while current_state != 1 and ac.transition[current_state][i] == 0:
                    current_state = ac.fail[current_state]
                if ac.transition[current_state][i] != 0:
                    current_state = ac.transition[current_state][i]

                dp[k + 1][current_state] = max(dp[k + 1][current_state], dp[k][state] + ac.output[current_state])

    answer = 0
    for state in range(1, ac.num_states + 1):
        answer = max(answer, dp[K][state])

    print(answer)

if __name__ == "__main__":
    main()
