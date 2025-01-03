# 통계학 문제 풀이 및 설명

<https://www.acmicpc.net/problem/2108>

<https://mayquartet.com/python-파이썬-백준-2108-통계학/>

## 문제 이해

이 문제는 주어진 수열에서 통계적으로 중요한 네 가지 값을 계산하는 문제입니다. 이때, 주어진 조건을 충족하면서 효율적으로 결과를 도출하는 것이 핵심입니다. 각 통계값은 수의 분포를 분석하는 데 중요한 역할을 합니다. 문제를 해결하기 위해서는 다음 네 가지 통계값을 정확하게 계산해야 합니다:

- `산술평균`: 모든 수의 합을 개수 `N`으로 나눈 값으로, 소수점 첫째 자리에서 반올림하여 출력합니다.
- `중앙값`: 주어진 수들을 오름차순으로 정렬한 후, 중간에 위치한 값을 의미합니다. 문제에서 `N`은 홀수라고 주어졌기 때문에 정확히 한 개의 중앙값이 존재합니다.
- `최빈값`: 수열에서 가장 빈도가 높은 수를 의미합니다. 만약 최빈값이 여러 개일 경우 두 번째로 작은 값을 출력해야 합니다.
- `범위`: 수열의 최댓값과 최솟값의 차이를 의미하며, 이는 데이터의 분포 폭을 나타냅니다.

이 문제에서 주어진 입력의 크기가 최대 500,000개까지 될 수 있으므로, 시간 복잡도를 고려한 알고리즘 설계가 필수적입니다. 입력값의 크기와 데이터의 분포를 고려하여 효율적인 데이터 처리 및 연산 방법을 선택해야 합니다.

## 입출력 조건

- **입력 조건**:
  - 첫 번째 줄에는 정수 `N`이 주어집니다. `N`은 수의 개수를 나타내며, `1 ≤ N ≤ 500,000`의 값을 가지며 항상 홀수입니다. 이는 중앙값 계산을 단순하게 해줍니다.
  - 두 번째 줄부터 `N`개의 줄에 걸쳐 각 수열의 원소가 한 줄에 하나씩 정수 형태로 주어집니다. 각 정수의 절댓값은 4,000을 넘지 않습니다.
- **출력 조건**:
  - 첫 번째 줄에는 산술평균을 소수점 첫째 자리에서 반올림하여 출력합니다.
  - 두 번째 줄에는 중앙값을 출력합니다.
  - 세 번째 줄에는 최빈값을 출력합니다. 만약 최빈값이 여러 개라면, 그중 두 번째로 작은 값을 출력해야 합니다.
  - 네 번째 줄에는 수열의 범위를 출력합니다.

## 접근 방식

이 문제를 풀기 위해서는 입력 데이터의 크기와 각 통계값의 특성에 따라 적절한 알고리즘과 데이터를 처리하는 방법을 선택해야 합니다. 다음과 같은 접근 방식으로 문제를 해결할 수 있습니다:

1. **정렬 사용**:

   - 중앙값을 구하기 위해서는 수열을 오름차순으로 정렬해야 하므로, `N`개의 수를 정렬하는 작업이 필요합니다. 정렬은 `O(N log N)`의 시간 복잡도를 가지며, 이는 `N`이 크더라도 충분히 처리할 수 있는 범위입니다.
   - 정렬된 수열을 이용하면 중앙값과 범위를 쉽게 계산할 수 있습니다. 중앙값은 정렬된 리스트에서 가운데 있는 원소를 가져오면 되고, 범위는 정렬된 리스트의 마지막 원소(최댓값)와 첫 번째 원소(최솟값)의 차이로 계산할 수 있습니다.

2. **산술평균 계산**:

   - 산술평균은 모든 수의 합을 `N`으로 나눈 값입니다. Python에서 `sum()` 함수를 사용하여 쉽게 계산할 수 있으며, `round()` 함수를 사용하여 소수점 첫째 자리에서 반올림된 값을 얻을 수 있습니다.
   - 계산된 평균값은 정수로 변환하여 출력해야 합니다.

3. **최빈값 계산**:

   - 최빈값을 계산하기 위해서는 각 숫자의 출현 빈도를 저장해야 합니다. 이를 위해 `defaultdict` 또는 `Counter`를 사용하여 빈도수를 기록할 수 있습니다.
   - 이후 빈도수를 기준으로 정렬하여 가장 많이 나타난 값을 찾고, 빈도가 같은 경우에는 두 번째로 작은 값을 출력해야 하므로 이 조건을 처리하는 로직이 필요합니다.

4. **효율적인 입력 처리**:
   - `N`의 최대값이 500,000이므로 입력을 빠르게 처리하는 것이 중요합니다. 반복적으로 `input()`을 호출하는 대신, `sys.stdin.read()`를 사용하여 한 번에 입력을 받아 처리하면 성능을 크게 향상시킬 수 있습니다.
   - 입력된 수를 빠르게 처리하여 리스트로 변환하고, 이를 정렬 및 빈도 계산에 활용합니다.

## 풀이 과정

1. **입력 받기**:

   - `sys.stdin.read()`를 사용하여 입력을 한 번에 받아옵니다. 이 방법은 대량의 입력을 빠르게 처리할 수 있도록 도와줍니다.
   - 입력된 데이터를 공백 기준으로 나눈 후, 첫 번째 값을 `N`으로 변환하여 수의 개수를 저장합니다. 이후의 값을 정수형 리스트로 변환하여 수열을 저장합니다.

2. **리스트 정렬**:

   - 수열을 오름차순으로 정렬합니다. 정렬된 리스트는 중앙값, 범위 계산, 최빈값 계산에 모두 유용하게 사용됩니다.
   - `N`이 크지만 정렬 시간복잡도가 `O(N log N)`이므로 충분히 처리 가능합니다.

3. **산술평균 계산**:

   - `sum()` 함수를 사용해 리스트의 모든 원소를 더하고, 이를 `N`으로 나누어 평균을 계산합니다.
   - `round()` 함수를 사용하여 소수점 첫째 자리에서 반올림된 값을 구합니다.

4. **중앙값 계산**:

   - 정렬된 리스트에서 `N // 2` 번째 원소를 가져와 중앙값을 계산합니다. 이는 `N`이 항상 홀수이기 때문에 한 개의 중앙값을 정확히 계산할 수 있습니다.

5. **최빈값 계산**:

   - `defaultdict`를 사용해 수열의 각 수에 대한 빈도를 계산합니다.
   - 계산된 빈도수를 기준으로 내림차순 정렬하여 빈도가 가장 높은 값을 찾습니다. 빈도가 같을 경우 두 번째로 작은 값을 출력해야 하므로, 정렬된 결과에서 조건에 맞는 값을 선택합니다.

6. **범위 계산**:

   - 정렬된 리스트의 마지막 원소와 첫 번째 원소의 차이를 계산하여 범위를 구합니다.
   - 이는 정렬된 상태에서 가장 큰 값과 가장 작은 값의 차이이므로 쉽게 계산할 수 있습니다.

7. **결과 출력**:
   - 계산된 평균, 중앙값, 최빈값, 범위를 순서대로 출력합니다.
   - 각 값을 문자열 형태로 변환하여 개행 문자(`\n`)를 이용해 한 줄씩 출력하도록 처리합니다.

## 코드 구현

```python
import sys
from collections import defaultdict

# sys.stdin.read를 통해 입력을 한 번에 받아온다.
input = sys.stdin.read
# 입력된 데이터를 공백 기준으로 분리하여 리스트로 저장한다.
data = input().split()

# 첫 번째 입력값은 수의 개수 N이다.
N = int(data[0])
# 두 번째부터 N+1번째까지의 값을 정수 리스트로 변환한다.
arr = list(map(int, data[1:N + 1]))
# 리스트를 오름차순으로 정렬한다.
arr.sort()

# 산술평균을 구하기 위해 리스트의 합을 N으로 나누고 반올림한다.
mean = round(sum(arr) / N)
# 중앙값은 정렬된 리스트의 가운데 위치한 값이다.
median = arr[N // 2]

# 각 숫자의 빈도를 저장할 defaultdict를 생성한다.
counter = defaultdict(int)
# 리스트의 각 숫자에 대해 빈도를 1씩 증가시킨다.
for num in arr:
    counter[num] += 1

# 빈도수가 높은 순서로 정렬하고, 빈도가 같을 경우 숫자가 작은 순으로 정렬한다.
most_commons = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# 최빈값이 여러 개 있을 경우 두 번째로 작은 값을 선택한다.
if len(most_commons) > 1 and most_commons[0][1] == most_commons[1][1]:
    mode = most_commons[1][0]
# 최빈값이 하나뿐인 경우 첫 번째 값을 선택한다.
else:
    mode = most_commons[0][0]

# 범위는 정렬된 리스트에서 최대값과 최소값의 차이이다.
range_value = arr[-1] - arr[0]

# 각각의 값을 순서대로 출력한다.
print(f"{mean}\n{median}\n{mode}\n{range_value}")
```
