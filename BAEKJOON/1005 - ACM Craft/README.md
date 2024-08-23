# ACM Craft 문제 풀이

https://www.acmicpc.net/problem/1005

## 문제 이해

이 문제는 ACM Craft라는 게임에서 특정 건물을 짓는 데 필요한 최소 시간을 계산하는 문제입니다. 각 건물은 특정 순서에 따라 지어져야 하며, 건물 간의 의존 관계(선행 조건)가 주어집니다. 주어진 조건을 만족하며 목표 건물을 짓는 데 필요한 최소 시간을 계산하는 것이 목표입니다.

## 입력 형식
1. 첫 번째 줄에는 테스트 케이스의 수 \( T \)가 주어집니다.
2. 각 테스트 케이스는 다음과 같이 구성됩니다:
   - 첫 줄에는 건물의 수 \( N \)과 규칙의 수 \( K \)가 주어집니다.
   - 그 다음 줄에는 각 건물을 짓는 데 걸리는 시간 \( D_1, D_2, \ldots, D_N \)이 공백으로 구분되어 주어집니다.
   - 다음 \( K \)줄에는 두 정수 \( X \)와 \( Y \)가 주어지며, 이는 건물 \( X \)가 건물 \( Y \)보다 먼저 지어져야 함을 의미합니다.
   - 마지막 줄에는 목표 건물 \( W \)가 주어집니다.

## 출력 형식
- 각 테스트 케이스마다 목표 건물 \( W \)를 짓는 데 걸리는 최소 시간을 출력합니다.

## 접근 방식

이 문제를 해결하기 위해 위상 정렬(Topological Sort) 알고리즘을 사용합니다. 위상 정렬은 방향 그래프의 정점을 순서대로 나열하는 방법으로, 각 정점이 그 이전에 나오는 정점에 의존하는 경우에 유용합니다.

## 풀이 과정

1. **그래프와 진입 차수 구성**:
   - 각 건물의 건설 시간을 저장합니다.
   - 건물 간의 선행 관계를 그래프로 나타내고, 각 건물의 진입 차수(indegree)를 계산합니다.

2. **위상 정렬을 통해 최소 시간 계산**:
   - 진입 차수가 0인 건물들을 큐에 추가합니다.
   - 큐에서 건물을 하나씩 꺼내면서 해당 건물로부터 출발하는 간선을 제거하고, 연결된 건물의 진입 차수를 감소시킵니다.
   - 진입 차수가 0이 된 건물들을 큐에 추가하고, 해당 건물을 짓는 데 걸리는 최소 시간을 업데이트합니다.

3. **결과 출력**:
   - 각 테스트 케이스에 대해 목표 건물을 짓는 데 걸리는 최소 시간을 출력합니다.

## 코드
```python
from collections import deque, defaultdict
import sys
input = sys.stdin.read

def acm_craft():
    # 표준 입력에서 모든 데이터를 읽어옵니다.
    data = input().strip().split()
    idx = 0
    T = int(data[idx])  # 테스트 케이스의 수
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])  # 건물의 수
        K = int(data[idx + 1])  # 규칙의 수
        idx += 2
        build_times = list(map(int, data[idx:idx + N]))  # 각 건물을 짓는 데 걸리는 시간
        idx += N
        
        rules = []
        for _ in range(K):
            X = int(data[idx])
            Y = int(data[idx + 1])
            rules.append((X, Y))  # 건설 순서 규칙 (X -> Y)
            idx += 2
        
        target = int(data[idx])  # 목표 건물
        idx += 1

        indegree = [0] * (N + 1)  # 각 건물의 진입 차수
        graph = defaultdict(list)  # 그래프 초기화
        time = [0] * (N + 1)  # 각 건물을 짓는 데 걸리는 시간 초기화
        
        # 각 건물의 건설 시간을 설정합니다.
        for i in range(1, N + 1):
            time[i] = build_times[i - 1]
        
        # 그래프를 구성하고 진입 차수를 설정합니다.
        for X, Y in rules:
            graph[X].append(Y)
            indegree[Y] += 1
        
        # Kahn의 알고리즘을 사용한 위상 정렬
        queue = deque()
        dp = [0] * (N + 1)  # 각 건물을 짓는 데 걸리는 최소 시간을 저장할 배열
        
        # 진입 차수가 0인 건물들을 큐에 추가하고, 초기 시간을 설정합니다.
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i]
        
        # 위상 정렬을 수행하면서 각 건물을 짓는 데 걸리는 최소 시간을 계산합니다.
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                dp[neighbor] = max(dp[neighbor], dp[current] + time[neighbor])
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 목표 건물을 짓는 데 걸리는 최소 시간을 결과 리스트에 추가합니다.
        results.append(dp[target])
    
    # 각 테스트 케이스의 결과를 출력합니다.
    for result in results:
        print(result)

if __name__ == "__main__":
    acm_craft()
```