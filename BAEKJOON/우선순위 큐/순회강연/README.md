# 순회강연 문제 풀이 및 설명

https://www.acmicpc.net/problem/2109

## 문제 이해

한 저명한 학자에게 \( n \)개의 대학에서 강연 요청이 들어왔습니다. 각 대학은 특정 날짜 \( d \)일 이내에 강연을 해주면 강연료 \( p \)를 지불하겠다고 했습니다. 학자는 하루에 하나의 대학에서만 강연할 수 있습니다. 우리의 목표는 학자가 가장 많은 강연료를 받을 수 있도록 강연 일정을 최적화하는 것입니다. 주어진 문제의 입력 범위와 조건은 다음과 같습니다:

- 대학의 수 \( n \)은 0 이상 10,000 이하입니다.
- 각 대학이 요구하는 강연 날짜 \( d \)는 1 이상 10,000 이하입니다.
- 강연료 \( p \)는 1 이상 10,000 이하입니다.
- 학자는 하루에 하나의 대학에서만 강연할 수 있습니다.

## 접근 방식

1. **강연 요청 정렬**:
   - 강연 요청을 강연료 \( p \)를 기준으로 내림차순 정렬합니다. 이렇게 하면 가장 높은 강연료부터 배정할 수 있습니다.

2. **우선순위 큐 사용**:
   - 각 대학의 강연 요청을 처리할 때, 가능한 날짜 중 가장 가까운 날에 강연을 배정합니다.
   - 가능한 날짜를 효율적으로 관리하기 위해 집합(Set)을 사용합니다. 집합은 요소의 추가 및 삭제가 빠르며, 특정 요소의 존재 여부를 빠르게 확인할 수 있습니다.

3. **반복문을 통한 배정**:
   - 정렬된 강연 요청을 하나씩 처리하며, 해당 요청이 가능한 날짜 중 가장 가까운 날에 배정될 수 있는지 확인합니다.
   - 가능한 날이 있으면 그 날을 집합에서 제거하고, 해당 강연료를 총합에 더합니다.

## 풀이 과정

1. **입력 데이터 처리**:
   - 입력 데이터를 한 줄씩 읽어들이고, 첫 줄에서 강연 요청의 수 \( n \)을 입력받습니다.
   - 이후 각 줄에서 강연료 \( p \)와 강연 가능 일수 \( d \)를 입력받아 `lectures` 리스트에 저장합니다.

2. **강연 요청 정렬**:
   - `lectures` 리스트를 강연료 \( p \)를 기준으로 내림차순 정렬합니다.

3. **강연 배정**:
   - 가능한 모든 날을 관리하기 위해 1일부터 10000일까지의 날을 포함하는 집합(Set)을 생성합니다.
   - 각 강연 요청에 대해 가능한 가장 가까운 날을 찾아 배정합니다. 이때 배정된 날은 집합에서 제거합니다.

4. **결과 출력**:
   - 배정된 강연의 총 강연료를 계산하여 출력합니다.

## 코드 설명
```python
import heapq  # 힙큐 모듈을 불러옵니다. 이 모듈을 사용하여 우선순위 큐를 구현합니다.
import sys  # 시스템 모듈을 불러옵니다.

def solve():
    input = sys.stdin.readline  # 표준 입력을 한 줄씩 읽는 함수를 설정합니다.
    
    n = int(input().strip())  # 첫 줄에서 정수 n을 입력 받아 공백을 제거하고 정수로 변환합니다.
    
    lectures = []  # 강연 정보를 저장할 리스트를 초기화합니다.
    for _ in range(n):
        p, d = map(int, input().strip().split())  # 각 줄에서 강연료 p와 강연 가능 일수 d를 입력받아 정수로 변환합니다.
        lectures.append((p, d))  # 강연료와 강연 가능 일수를 튜플로 저장합니다.
    
    # 강연료를 기준으로 내림차순 정렬합니다.
    lectures.sort(reverse=True, key=lambda x: x[0])
    
    # 강연 가능한 날들을 집합으로 관리합니다. 가능한 최대 일수인 10000일까지 초기화합니다.
    days = set(range(1, 10001))
    
    total_value = 0  # 챙길 수 있는 강연료의 합의 최대값을 저장할 변수를 초기화합니다.
    for p, d in lectures:
        # 가능한 날 중 가장 가까운 날에 강연을 배정합니다.
        for day in range(d, 0, -1):
            if day in days:  # 현재 날이 강연 가능한 날들에 포함되어 있는지 확인합니다.
                days.remove(day)  # 배정된 날은 집합에서 제거합니다.
                total_value += p  # 총 강연료에 현재 강연료를 더합니다.
                break  # 강연을 배정했으므로 더 이상 반복하지 않습니다.
    
    print(total_value)  # 최종적으로 챙길 수 있는 강연료의 합의 최대값을 출력합니다.

if __name__ == "__main__":
    solve()  