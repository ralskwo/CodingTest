# 철로 문제 풀이 및 설명 

https://www.acmicpc.net/problem/13334

## 문제 이해

이 문제는 n명의 사람들이 각각 집과 사무실을 가지고 있을 때, 임의의 선분이 주어지면 그 선분에 포함되는 사람의 최대 수를 구하는 것입니다. 각 사람의 집과 사무실 위치는 서로 다르며, 이 두 점을 잇는 선분을 통해 해당 사람의 위치를 판단합니다. 예를 들어, 선분이 주어졌을 때 해당 선분이 몇 명의 사람을 포함하는지 계산하는 것이 목표입니다.

## 입출력 조건

- **입력 조건**:
  1. 첫 번째 줄에 사람의 수 \( n \)이 주어집니다. (1 ≤ \( n \) ≤ 100,000)
  2. 다음 \( n \)개의 줄에는 각 사람의 집 위치 \( h_i \)와 사무실 위치 \( o_i \)가 주어집니다. (-100,000,000 ≤ \( h_i, o_i \) ≤ 100,000,000)
  3. 마지막 줄에는 선분의 길이 \( d \)가 주어집니다. (1 ≤ \( d \) ≤ 200,000,000)
  
- **출력 조건**:
  - 주어진 선분 \( d \)의 길이 안에 포함되는 사람의 최대 수를 출력합니다.

## 접근 방식

이 문제를 해결하기 위해서는 다음과 같은 알고리즘적 접근이 필요합니다:

1. **정렬**: 집과 사무실 위치를 기반으로 시작점과 끝점을 계산하여 리스트를 생성하고, 이 리스트를 끝점을 기준으로 정렬합니다.
2. **우선순위 큐**: 우선순위 큐를 사용하여 슬라이딩 윈도우 기법을 구현합니다. 이를 통해 주어진 선분 길이 \( d \) 안에 포함되는 사람 수를 효율적으로 계산할 수 있습니다.
3. **슬라이딩 윈도우**: 끝점을 기준으로 정렬된 리스트에서, 현재 끝점에서 \( d \)만큼 떨어진 범위 내에 시작점이 있는지를 확인하며 최대 사람 수를 계산합니다.

## 풀이 과정

1. **입력 받기**: 먼저 입력된 사람 수 \( n \), 각 사람의 집 위치 \( h_i \)와 사무실 위치 \( o_i \), 선분의 길이 \( d \)를 입력받습니다.
2. **시작점과 끝점 계산**: 각 사람의 집 위치와 사무실 위치를 비교하여, 시작점은 두 위치 중 작은 값, 끝점은 큰 값으로 설정합니다. 이를 통해 모든 사람의 위치를 선분으로 표현할 수 있습니다.
3. **정렬**: 생성된 선분 리스트를 끝점을 기준으로 정렬합니다. 이는 슬라이딩 윈도우 기법을 적용하기 위해 필요한 사전 작업입니다.
4. **우선순위 큐 초기화**: 시작점을 저장할 우선순위 큐를 초기화합니다.
5. **슬라이딩 윈도우 적용**:
   - 끝점을 기준으로 정렬된 리스트를 순회하며 현재 사람의 시작점을 우선순위 큐에 삽입합니다.
   - 우선순위 큐의 첫 번째 요소가 현재 끝점에서 \( d \)를 뺀 값보다 작으면 큐에서 제거합니다. 이는 현재 끝점에서 \( d \) 범위 내에 포함되지 않는 시작점들을 제거하는 과정입니다.
   - 우선순위 큐의 크기가 현재 선분 내에 포함된 사람의 수가 되며, 이를 통해 최대 사람 수를 갱신합니다.
6. **최대 사람 수 출력**: 위 과정을 통해 계산된 최대 사람 수를 출력합니다.

## 코드 구현
```python
import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 임포트

def max_people_in_segment(n, positions, d):
    # 각 사람의 집과 사무실 위치를 받아서 시작점과 끝점을 계산
    segments = [(min(h, o), max(h, o)) for h, o in positions]
    
    # 끝점을 기준으로 정렬
    segments.sort(key=lambda x: x[1])
    
    max_count = 0  # 최대 사람 수를 저장할 변수 초기화
    pq = []  # 우선순위 큐 초기화
    
    for start, end in segments:
        # 현재 사람의 시작점을 우선순위 큐에 삽입
        heapq.heappush(pq, start)
        
        # 우선순위 큐의 첫 번째 요소가 현재 끝점에서 d를 뺀 값보다 작으면 큐에서 제거
        while pq and pq[0] < end - d:
            heapq.heappop(pq)
        
        # 현재 우선순위 큐의 크기를 최대 사람 수와 비교하여 갱신
        max_count = max(max_count, len(pq))
    
    return max_count  # 최대 사람 수 반환

# 입력 처리
n = int(input())  # 첫 번째 줄에서 사람 수를 입력 받음
positions = [tuple(map(int, input().split())) for _ in range(n)]  # 각 사람의 집과 사무실 위치를 입력 받음
d = int(input())  # 마지막 줄에서 선분의 길이를 입력 받음

# 결과 출력
print(max_people_in_segment(n, positions, d))  # 최대 사람 수를 계산하여 출력
