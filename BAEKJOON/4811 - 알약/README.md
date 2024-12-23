# 알약 문제 풀이 및 설명

<https://www.acmicpc.net/problem/4811>

<https://mayquartet.com/python-백준-4811-알약/>

## 문제 이해

이 문제는 약을 복용하는 방식과 그에 따른 문자열을 생성하는 규칙을 바탕으로, 가능한 서로 다른 문자열의 개수를 구하는 문제입니다. 할아버지는 매일 약을 한 조각씩 복용하는데, 이때 병에 있는 약을 반으로 쪼개서 복용하는 경우도 포함됩니다. 이를 통해 각 날마다 할아버지가 꺼낸 약의 상태에 따라 `W`와 `H` 문자가 기록됩니다. 즉, `W`는 약 하나를 꺼내 반으로 쪼갠 후 절반을 복용하고 나머지 절반을 병에 다시 넣는 경우를 의미하고, `H`는 병에 있는 반 조각을 꺼내서 복용하는 경우를 의미합니다.

병에 약이 `N`개 있다면, 할아버지는 총 `2N`일 동안 약을 복용하게 되고, 이 기간 동안 생성되는 문자열의 길이도 `2N`이 됩니다. 문제의 핵심은 병에 있는 약의 개수 `N`이 주어졌을 때, 할아버지가 매일 약을 꺼내고 복용하는 규칙을 통해 생성할 수 있는 서로 다른 문자열의 개수를 구하는 것입니다.

## 입출력 조건

- **입력 조건**:
  - 여러 테스트 케이스가 주어지며, 각 줄에 약의 개수 `N`이 주어집니다. (`1 ≤ N ≤ 30`)
  - 입력의 마지막 줄에는 `0`이 주어지며, 이 줄은 테스트 종료를 의미하므로 처리하지 않습니다.
- **출력 조건**:
  - 각 테스트 케이스마다 가능한 서로 다른 문자열의 개수를 한 줄에 하나씩 출력합니다.

## 접근 방식

이 문제는 가능한 경우의 수를 구하는 문제로, 기본적으로 **재귀와 동적 프로그래밍(DP)**을 사용하여 해결할 수 있습니다. 병에 있는 전체 조각의 개수와 반 조각의 개수의 조합에 따라 발생할 수 있는 가능한 문자열의 상태를 추적해야 하므로, 각 상태에서 가능한 경우의 수를 계산하고 이를 저장하여 중복 계산을 방지하는 방식이 필요합니다. 이 문제는 주어진 조각을 꺼내고 반으로 나누는 형태의 규칙 때문에 **카탈란 수(Catalan Number)**의 성질을 지니고 있습니다. 카탈란 수는 재귀적으로 파생되는 경우의 수를 동적 프로그래밍으로 최적화하여 구할 수 있는 문제와 유사하기 때문에 이와 유사한 접근 방식으로 해결할 수 있습니다.

## 풀이 과정

1. **동적 프로그래밍 테이블 정의**:

   - 상태 `(whole, half)`에서 가능한 경우의 수를 저장하는 `dp` 딕셔너리를 정의합니다. 여기서 `whole`은 병에 있는 전체 조각의 개수, `half`는 병에 있는 반 조각의 개수를 나타냅니다.
   - 초기 상태는 `(N, 0)`이며, `whole`이 0이고 `half`가 0일 때는 약을 모두 복용한 상태이므로 경우의 수 `1`을 반환합니다.

2. **재귀 함수 구현**:

   - `count_ways(whole, half)` 함수는 병에 있는 전체 조각(`whole`)과 반 조각(`half`)의 개수에 따른 경우의 수를 계산합니다.
   - 이 함수는 두 가지 상황을 고려하여 재귀적으로 호출됩니다:
     - `whole > 0`인 경우, 전체 조각에서 하나를 꺼내 반으로 쪼개서 하나는 복용하고 나머지 반을 병에 넣습니다. 이 경우 `count_ways(whole - 1, half + 1)`로 재귀 호출하여 가능한 문자열의 개수를 구합니다.
     - `half > 0`인 경우, 병에 있는 반 조각을 복용하는 상황으로, 이때 `count_ways(whole, half - 1)`로 재귀 호출하여 가능한 문자열의 개수를 구합니다.

3. **메모이제이션을 통한 최적화**:

   - 재귀 호출 과정에서 동일한 상태가 여러 번 발생할 수 있습니다. 이를 방지하기 위해 `dp[(whole, half)]`에 현재 상태에서의 결과를 저장합니다.
   - `dp`에 저장된 상태는 이후 동일한 상태에서 바로 값을 가져오도록 하여 연산을 최적화합니다.

4. **입력 및 결과 처리**:
   - 사용자로부터 여러 테스트 케이스를 입력받아, 입력이 `0`일 때까지 반복합니다. 각 테스트 케이스마다 `count_ways(N, 0)`을 호출하여 결과를 `results` 리스트에 저장합니다.
   - 마지막으로 `results` 리스트의 각 결과를 순서대로 출력합니다.

## 코드 구현

```python
dp = {}  # 동적 프로그래밍을 위한 딕셔너리 초기화. 이미 계산한 경우의 수를 저장하여 중복 계산을 방지

def count_ways(whole, half):
    if whole == 0 and half == 0:  # 전체 조각과 반 조각이 모두 0이면, 가능한 문자열 한 가지가 완성된 것이므로 1을 반환
        return 1
    if (whole, half) in dp:  # 현재 (whole, half) 상태가 이미 dp에 저장되어 있다면, 저장된 값을 바로 반환하여 계산을 최적화
        return dp[(whole, half)]

    ways = 0  # 가능한 경우의 수를 저장할 변수 초기화
    if whole > 0:  # 전체 조각이 남아 있다면, 새로운 조각을 꺼내 반으로 쪼개서 하나는 먹고 다른 하나는 병에 넣는 경우를 고려
        ways += count_ways(whole - 1, half + 1)  # 전체 조각에서 하나를 줄이고 반 조각을 하나 추가하여 재귀 호출
    if half > 0:  # 반 조각이 남아 있다면, 반 조각을 하나 꺼내 먹는 경우를 고려
        ways += count_ways(whole, half - 1)  # 반 조각을 하나 줄인 상태로 재귀 호출

    dp[(whole, half)] = ways  # 현재 상태에서 가능한 경우의 수를 dp 테이블에 저장
    return ways  # 현재 (whole, half) 상태에서 가능한 문자열의 총 경우의 수를 반환

results = []  # 각 테스트 케이스의 결과를 저장할 리스트 초기화
while True:
    N = int(input())  # 약의 개수 N을 입력 받음
    if N == 0:  # 입력이 0이면 종료 조건으로 판단하여 반복문 탈출
        break
    results.append(count_ways(N, 0))  # 가능한 문자열의 개수를 계산하여 results 리스트에 추가

for result in results:  # 저장된 결과를 순서대로 출력
    print(result)
```
