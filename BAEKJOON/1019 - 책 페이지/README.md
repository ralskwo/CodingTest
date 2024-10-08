# 책 페이지 문제 풀이 및 설명

<https://www.acmicpc.net/problem/1019>

<https://mayquartet.com/python-파이썬-백준-1019-책-페이지/>

## 문제 이해

이 문제는 1부터 `N`까지의 페이지에서 0부터 9까지의 숫자가 각각 몇 번 등장하는지를 구하는 문제입니다. 주어진 숫자 `N`이 최대 10억(1,000,000,000)까지 주어질 수 있으므로, 단순하게 `1`부터 `N`까지의 모든 숫자를 순회하며 각각의 숫자 빈도를 세는 방식으로는 시간 복잡도와 메모리 효율성을 맞출 수 없습니다. 따라서 문제를 효율적으로 풀기 위해서는 수학적 규칙과 각 자리수의 패턴을 이해하고, 이를 바탕으로 각 숫자의 등장 횟수를 계산할 필요가 있습니다.

이 문제를 해결하기 위해서는 다음과 같은 사항을 고려해야 합니다:

1. **숫자 `0`에 대한 특수 처리**: 0은 맨 앞에 등장하지 않으므로 이를 고려하여 보정해야 합니다. 예를 들어, 1000~1999까지의 범위에서 0은 백의 자리, 십의 자리, 일의 자리에서만 등장합니다.
2. **자릿수별로 각 숫자 빈도를 계산**: 모든 자릿수에 대해 각 숫자가 등장하는 빈도를 따로따로 계산해야 합니다. 예를 들어, 12345가 주어졌을 때, 일의 자리, 십의 자리, 백의 자리 등 각 자리수에서 숫자가 어떻게 반복적으로 등장하는지를 따져보아야 합니다.
3. **규칙적인 패턴을 통한 효율적 계산**: 숫자의 자리별로 등장하는 규칙을 이용하여 각 숫자의 빈도를 효율적으로 계산할 수 있어야 합니다. 예를 들어, 100~999 범위에서는 각 자리수마다 0부터 9까지의 숫자가 골고루 반복됩니다. 이를 규칙으로 정의하여 효율적으로 계산할 수 있습니다.

## 입출력 조건

- **입력**: 자연수 `N`이 주어집니다. `N`은 1 이상 1,000,000,000 이하의 값입니다. 이는 최대 10자리의 숫자까지 입력될 수 있음을 의미합니다.
- **출력**: 0부터 9까지의 각 숫자가 1부터 `N`까지의 페이지에서 몇 번 등장했는지를 공백으로 구분하여 출력합니다. 출력되는 순서는 `0`부터 `9`까지의 빈도를 나타내며, 예를 들어 `1 4 1 1 1 1 1 1 1 1`와 같은 형태가 됩니다.

## 접근 방식

이 문제를 해결하기 위해서는 각 숫자(0~9)가 1부터 `N`까지의 모든 숫자에서 몇 번 등장하는지를 효율적으로 계산할 수 있는 방법을 찾아야 합니다. 최대 10억이라는 큰 범위에서 모든 숫자를 탐색하는 방식은 매우 비효율적이므로, 각 자리수의 특성을 이용한 수학적 접근이 필요합니다.

1. **자리수별로 숫자 빈도 계산**: `N`의 각 자리수(일의 자리, 십의 자리, 백의 자리 등)에 대해 각 숫자가 어떻게 등장하는지를 분석합니다. 예를 들어, 54321이라는 숫자에서 천의 자리의 5는 10000번 이상 등장할 수 없습니다. 이를 이용해 각 자리의 숫자 빈도를 따로따로 계산합니다.

2. **각 자리수의 패턴을 통한 빈도 계산**: 자리수별로 숫자 등장 횟수를 따져보면 일정한 패턴이 존재합니다. 예를 들어, 1~999까지의 범위에서는 각 자리수마다 0부터 9까지의 숫자가 골고루 반복됩니다. 이를 규칙으로 정의하여 효율적으로 계산할 수 있습니다.

3. **숫자 0에 대한 특수 처리**: 0은 맨 앞자리에 등장하지 않으므로, 각 자리수별로 0의 등장 횟수를 보정해줘야 합니다. 예를 들어, 1000부터 1999까지의 범위에서 0이 맨 앞자리에 등장할 수 없으므로 이를 고려하여 0의 횟수를 조정합니다.

4. **반복적으로 등장하는 패턴을 이용하여 각 숫자의 빈도를 계산**: 각 자리수에 대해 반복적으로 등장하는 숫자의 패턴을 이용하여 0부터 9까지의 숫자 빈도를 효율적으로 계산합니다. 이를 통해 모든 숫자에 대해 한번에 계산할 수 있습니다.

## 풀이 과정

1. **입력값 초기화**:

   - 자연수 `N`을 문자열로 변환하여 자리수를 확인합니다. 이를 통해 각 자리별로 숫자 등장 횟수를 계산할 수 있도록 준비합니다.
   - 각 숫자(0~9)의 등장 횟수를 저장할 리스트 `counts`를 `[0] * 10`으로 초기화합니다.

2. **각 자리수의 숫자 등장 횟수 계산**:

   - `for` 반복문을 통해 문자열로 변환된 `N`의 각 자리수를 순회합니다.
   - 현재 자리의 자릿값을 `place_value = 10 ** (length - i - 1)`로 정의하여, 현재 자리의 자릿값을 기준으로 각 숫자가 몇 번 등장하는지를 확인합니다.

3. **현재 자리수보다 앞의 완전한 세트에서 숫자 등장 횟수 계산**:

   - `for` 반복문을 통해 `0`부터 `9`까지의 각 숫자가 현재 자리보다 앞의 모든 완전한 세트에서 몇 번 등장하는지를 계산합니다.
   - 예를 들어, `5432`라는 숫자에서 천의 자리를 기준으로 할 때, 0~4999 범위에서는 0부터 9까지의 숫자가 각각 `500 * 1000 = 500,000`번 등장하게 됩니다.

4. **현재 자리의 숫자보다 작은 숫자들의 등장 횟수 계산**:

   - 현재 자리의 숫자보다 작은 숫자들(0부터 `curr - 1`까지)이 현재 자릿수에서 얼마나 자주 등장하는지 계산합니다.
   - 현재 자릿값만큼의 빈도를 각 숫자에 더합니다. 예를 들어, `5432`에서 천의 자리의 숫자가 5일 경우, 0~4의 숫자들은 천의 자리에서 각각 1000번씩 더 등장하게 됩니다.

5. **현재 자릿수의 숫자 등장 횟수 계산**:

   - 현재 자릿수의 숫자가 등장하는 횟수를 계산하여 `counts` 리스트에 더해줍니다. 예를 들어, `5432`에서 천의 자리의 숫자 `5`는 `432 + 1 = 433`번 등장합니다.

6. **0의 등장 횟수 보정**:

   - 0은 맨 앞자리에 올 수 없기 때문에, 0의 등장 횟수에서 자릿값만큼의 횟수를 빼줍니다. 예를 들어, 1000부터 1999까지의 범위에서 맨 앞자리의 0을 제외한 0의 등장 횟수를 보정합니다.

7. **최종 출력**:
   - 모든 자리수에 대한 숫자 빈도 계산이 완료되면, 0부터 9까지의 숫자 등장 횟수를 `counts` 리스트로 반환합니다.
   - 출력 시에는 리스트를 공백으로 구분하여 출력합니다. 예를 들어, 결과가 `[1, 4, 1, 1, 1, 1, 1, 1, 1, 1]`이라면 `1 4 1 1 1 1 1 1 1 1` 형태로 출력됩니다.

## 코드 구현

```python
def count_digits(n):
    # n이 0 이하일 경우 0부터 9까지의 숫자 등장 횟수는 모두 0이므로 [0] * 10 리스트를 반환
    if n <= 0:
        return [0] * 10

    # n을 문자열로 변환하여 자리수를 계산
    str_n = str(n)
    length = len(str_n)

    # 각 숫자(0~9)의 등장 횟수를 저장할 리스트를 초기화
    counts = [0] * 10

    # n의 각 자리수에 대해 등장 빈도를 계산
    for i in range(length):
        # 현재 자리의 숫자를 정수형으로 변환하여 저장
        curr = int(str_n[i])

        # 현재 자리의 자릿값을 계산 (예: 천의 자리면 1000)
        place_value = 10 ** (length - i - 1)

        # 현재 자릿수보다 앞의 모든 완전한 세트의 숫자 등장 횟수를 계산
        for digit in range(10):
            counts[digit] += (n // (place_value * 10)) * place_value

        # 현재 자리의 숫자보다 작은 숫자들이 해당 자릿수에서 몇 번 등장하는지 계산
        for digit in range(curr):
            counts[digit] += place_value

        # 현재 자릿수의 숫자가 현재 자릿값만큼 등장하는 횟수를 더해줌
        counts[curr] += (n % place_value) + 1

        # 0은 맨 앞자리에 올 수 없기 때문에, 0의 등장 횟수를 보정
        counts[0] -= place_value

    # 0부터 9까지의 숫자가 1부터 n까지 몇 번 등장했는지 리스트로 반환
    return counts

# 사용자로부터 숫자 n을 입력받음
N = int(input())

# 입력받은 n에 대해 0부터 9까지의 숫자 등장 횟수를 계산하여 result에 저장
result = count_digits(N)

# 결과를 공백으로 구분하여 출력
print(*result)
```
