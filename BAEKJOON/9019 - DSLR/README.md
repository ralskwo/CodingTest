# DSLR 문제 풀이 및 설명

https://www.acmicpc.net/problem/9019

## 문제 이해

이 문제는 네 가지 명령어(D, S, L, R)를 이용하여 주어진 숫자 A를 목표 숫자 B로 변환하는 최소 명령어 시퀀스를 찾는 문제입니다. 각 명령어는 다음과 같은 변환을 수행합니다:
- D: 숫자를 두 배로 만들고, 10000으로 나눈 나머지로 변환.
- S: 숫자에서 1을 빼고, 음수가 되면 9999로 변환.
- L: 숫자의 자릿수를 왼쪽으로 한 칸 회전.
- R: 숫자의 자릿수를 오른쪽으로 한 칸 회전.

## 접근 방식

이 문제는 최단 경로를 찾는 문제로, BFS(너비 우선 탐색) 알고리즘을 사용하면 적합합니다. BFS는 시작점에서 목표점까지의 최단 경로를 찾을 때 유용합니다. 

## 풀이 과정

1. BFS 알고리즘을 사용하여 초기 숫자 A에서 시작하여 가능한 모든 변환을 탐색합니다.
2. 각 숫자에 대해 네 가지 명령어(D, S, L, R)를 적용하고, 새로운 숫자가 목표 숫자 B와 일치하는지 확인합니다.
3. 새로운 숫자가 이미 방문된 숫자가 아니라면 큐에 추가하고, 해당 숫자로 변환하기 위한 명령어 시퀀스를 기록합니다.
4. 목표 숫자 B에 도달하면 현재까지의 명령어 시퀀스를 반환합니다.

## 문제 제출 시 주의 사항

이 문제는 Python3로 제출하면 시간 초과 오류가 발생하므로, Python3 대신 PyPy3로 제출해야 합니다. Python3와 PyPy3의 차이점은 다음 포스트를 참고해 주세요.

## 코드
```python
from collections import deque

def command(n, cmd):
    """주어진 숫자 n에 대해 명령어 cmd를 적용한 결과를 반환"""
    if cmd == 'D':
        return (2 * n) % 10000  # D 명령어: 숫자를 두 배로 하고 10000으로 나눈 나머지
    elif cmd == 'S':
        return 9999 if n == 0 else n - 1  # S 명령어: 숫자에서 1을 빼고 음수가 되면 9999로 설정
    elif cmd == 'L':
        return (n % 1000) * 10 + n // 1000  # L 명령어: 자릿수를 왼쪽으로 한 칸 회전
    elif cmd == 'R':
        return (n % 10) * 1000 + n // 10  # R 명령어: 자릿수를 오른쪽으로 한 칸 회전

def bfs(start, end):
    """시작 숫자 start에서 목표 숫자 end까지의 최단 명령어 시퀀스를 찾는 BFS 함수"""
    queue = deque([(start, "")])  # 큐 초기화 (숫자, 명령어 시퀀스)
    visited = [False] * 10000  # 방문 여부를 저장할 리스트
    visited[start] = True  # 시작 숫자는 방문 처리
    
    while queue:
        current, path = queue.popleft()  # 큐에서 현재 숫자와 경로를 꺼냄
        
        if current == end:  # 목표 숫자에 도달하면 경로 반환
            return path
        
        for cmd in 'DSLR':  # 네 가지 명령어를 순차적으로 적용
            next_num = command(current, cmd)
            if not visited[next_num]:  # 새로운 숫자가 방문되지 않았으면
                visited[next_num] = True  # 방문 처리
                queue.append((next_num, path + cmd))  # 큐에 추가 (새로운 숫자, 경로 업데이트)

import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])  # 테스트 케이스 개수
index = 1

results = []
for _ in range(T):
    A = int(data[index])
    B = int(data[index + 1])
    results.append(bfs(A, B))  # 각 테스트 케이스에 대해 BFS 수행
    index += 2

for result in results:
    print(result)  # 결과 출력
