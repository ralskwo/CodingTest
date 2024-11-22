# DNA 문제 풀이 및 설명

<https://www.acmicpc.net/problem/1969>

<https://mayquartet.com/python-백준-1969-dna/>

## 문제 이해

이 문제는 DNA 배열에서 Hamming Distance의 합이 최소가 되는 새로운 DNA 배열을 생성하는 작업입니다. DNA는 A, T, G, C로 이루어진 문자열로 표현되며, Hamming Distance는 같은 길이의 두 문자열에서 서로 다른 문자 개수를 의미합니다. 주어진 DNA 목록에서 각 열(column)마다 가장 많이 나타나는 문자를 선택해 새로운 DNA 배열을 만들고, 그 배열과 모든 입력 DNA 간의 Hamming Distance 합을 계산해야 합니다. 즉, 이 문제는 **입력된 DNA와의 차이를 최소화하는 최적의 DNA 배열을 찾는 것**을 목표로 합니다.

## 입출력 조건

- **입력**:
  - 첫 번째 줄에는 DNA의 개수 `N`과 각 DNA 문자열의 길이 `M`이 주어집니다.
    - `N`은 1 이상 1000 이하의 자연수
    - `M`은 1 이상 50 이하의 자연수
  - 두 번째 줄부터는 각 DNA 배열이 한 줄에 하나씩 주어집니다. 각 문자열은 길이 `M`이며 A, T, G, C로만 구성됩니다.
- **출력**:
  - 첫 번째 줄에는 최소 Hamming Distance를 갖는 DNA 배열을 출력합니다.
  - 두 번째 줄에는 그 DNA 배열과 입력 DNA들 사이의 Hamming Distance 총합을 출력합니다.
  - 동일한 최소 Hamming Distance를 갖는 DNA 배열이 여러 개인 경우, 사전순으로 가장 앞서는 배열을 출력합니다.

## 접근 방식

이 문제를 해결하기 위해 아래의 방식으로 접근해야 합니다.

1. **열(column) 단위로 가장 빈번한 문자 선택**  
   각 열에서 A, T, G, C의 빈도를 계산한 후, 가장 빈번히 나타나는 문자를 선택합니다. 빈도가 동일한 경우에는 알파벳 순서대로 가장 앞선 문자를 선택해야 합니다.

2. **최소 거리 DNA 생성**  
   각 열에서 가장 빈번한 문자를 선택하여 최적의 DNA 배열을 생성합니다.

3. **Hamming Distance 계산**  
   생성한 DNA 배열과 입력 DNA들 간의 Hamming Distance를 계산합니다. 이를 위해 각 문자열과 최적의 DNA 배열을 비교하여 서로 다른 문자의 개수를 세어 합산합니다.

4. **시간 복잡도 고려**
   - 각 열에 대해 빈도를 계산하는 데 `O(N)`의 시간이 소요되며, 총 `M`개의 열을 처리해야 하므로 시간 복잡도는 `O(N × M)`입니다. 이는 제한 조건 내에서 효율적으로 동작합니다.

## 풀이 과정

1. DNA의 개수 `N`과 길이 `M`을 입력받습니다. 이후 `N`개의 DNA 문자열을 리스트로 저장합니다.
2. 각 열에 대해 다음을 수행합니다.
   - 모든 DNA 문자열에서 해당 열의 문자를 추출합니다.
   - 추출한 문자들의 빈도를 계산하여 가장 빈번한 문자를 선택합니다. 빈도가 동일할 경우 사전순으로 가장 앞선 문자를 선택합니다.
   - 선택한 문자를 최적의 DNA 배열에 추가합니다.
3. 최적의 DNA 배열이 생성되면, 입력 DNA 리스트와의 Hamming Distance를 계산합니다.
   - 각 DNA와 최적의 DNA를 비교하여 서로 다른 문자의 개수를 구하고 이를 합산합니다.
4. 최적의 DNA 배열과 Hamming Distance 총합을 출력합니다.

## 코드 구현

```python
def find_min_hamming_dna(N, M, dna_list):
    # 문자열 빈도 계산을 위해 Counter 모듈을 가져온다
    from collections import Counter

    # 최소 거리 DNA를 저장할 변수
    min_distance_dna = ""
    # Hamming Distance 총합을 저장할 변수
    total_hamming_distance = 0

    # 각 열(column)마다 반복
    for col in range(M):
        # 현재 열에서 모든 DNA 문자열의 해당 위치 문자들을 추출
        column_nucleotides = [dna[col] for dna in dna_list]

        # 현재 열에서 문자의 빈도를 계산
        freq = Counter(column_nucleotides)

        # 빈도가 가장 높은 문자를 선택하며, 빈도가 같다면 사전순으로 가장 앞선 문자를 선택
        most_common = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[0][0]

        # 최소 거리 DNA에 가장 빈번한 문자를 추가
        min_distance_dna += most_common

        # 현재 열에서 Hamming Distance에 해당하는 문자 수를 계산
        # 전체 문자의 개수에서 가장 빈번한 문자의 개수를 뺀 값을 더함
        total_hamming_distance += sum(freq.values()) - freq[most_common]

    # 최소 거리 DNA와 총 Hamming Distance를 반환
    return min_distance_dna, total_hamming_distance

# DNA의 개수와 문자열의 길이를 입력받음
N, M = map(int, input().split())

# 각 DNA 문자열을 입력받아 리스트에 저장
dna_list = [input().strip() for _ in range(N)]

# 최소 거리 DNA와 Hamming Distance 총합을 계산
result_dna, hamming_distance = find_min_hamming_dna(N, M, dna_list)

# 최소 거리 DNA를 출력
print(result_dna)

# Hamming Distance의 총합을 출력
print(hamming_distance)
```
