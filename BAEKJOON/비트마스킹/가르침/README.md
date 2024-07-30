# 가르침 문제 풀이 및 설명

https://www.acmicpc.net/problem/1062

## 문제 이해

문제는 학생들에게 주어진 단어 중 최대 몇 개를 읽을 수 있는지 찾는 것입니다. 단어들은 "anta"로 시작하고 "tica"로 끝나며, K개의 글자를 배울 수 있습니다. 학생들이 읽을 수 있는 단어의 최대 개수를 구하는 것이 목표입니다.

## 입출력 조건

**Input:**
1. 첫 번째 줄에 두 정수 N과 K가 주어집니다:
   - N: 단어의 수.
   - K: 배울 수 있는 글자의 수.
2. 다음 N개의 줄에는 각각 단어가 한 줄에 하나씩 주어집니다.

**Output:**
- 학생들이 읽을 수 있는 단어의 최대 개수를 나타내는 정수 하나를 출력합니다.

## 접근 방법

이 문제를 해결하기 위해서는 조합(combinatorial) 접근법과 집합(set) 연산을 결합하여 사용합니다:
1. 기본 글자인 "antic"를 기본 집합으로 사용합니다.
2. 추가로 배울 수 있는 K-5개의 글자를 선택합니다.
3. 이러한 추가 글자 조합을 생성합니다.
4. 각 조합에 대해 몇 개의 단어를 읽을 수 있는지 계산하여 최대 값을 찾습니다.

## 풀이 과정

1. **입력 및 초기 설정:**
   - N과 K 값을 입력받습니다.
   - 단어 리스트를 읽고, 각 단어에서 접두사 "anta"와 접미사 "tica"를 제거합니다.
   - 만약 K가 5보다 작다면, "antic"를 가르칠 수 없으므로 결과는 0입니다.
   - 만약 K가 26이면, 모든 알파벳을 배울 수 있으므로 모든 단어를 읽을 수 있습니다.

2. **기본 글자와 추가 글자 설정:**
   - 기본 글자인 'a', 'n', 't', 'i', 'c'를 `basic_letters` 집합에 저장합니다.
   - 모든 알파벳을 `all_letters` 집합에 저장한 후 `basic_letters`를 제외한 글자들을 `letters_to_learn`에 저장합니다.

3. **단어 처리:**
   - 각 단어를 "antic"를 제외한 글자들로만 구성된 집합으로 변환합니다.
   - 이러한 집합들을 `processed_words` 리스트에 저장합니다.

4. **조합 생성 및 읽을 수 있는 단어 수 계산:**
   - itertools의 combinations를 사용하여 K-5 크기의 `letters_to_learn`의 모든 조합을 생성합니다.
   - 각 조합에 대해, 해당 글자를 배운 것으로 표시한 후 읽을 수 있는 단어 수를 계산합니다.
   - 읽을 수 있는 단어 수의 최대 값을 `max_readable` 변수에 저장합니다.

5. **결과 출력:**
   - 읽을 수 있는 단어의 최대 개수를 출력합니다.

## 코드 구현

```python
from itertools import combinations

# 특정 글자를 배웠을 때 읽을 수 있는 단어의 수를 계산하는 함수
def count_readable_words(words, learned):
    count = 0  # 읽을 수 있는 단어의 수를 세기 위한 변수 초기화
    for word in words:
        readable = True  # 현재 단어를 읽을 수 있는지 여부를 표시하는 변수
        for char in word:
            if not learned[ord(char) - ord('a')]:  # 해당 문자를 배우지 않았다면
                readable = False  # 읽을 수 없다고 표시
                break  # 더 이상 확인할 필요 없음
        if readable:  # 모든 문자를 배웠다면
            count += 1  # 읽을 수 있는 단어 수 증가
    return count  # 읽을 수 있는 단어의 총 수 반환

# 주어진 단어의 수 N과 가르칠 수 있는 글자의 수 K로 최대 읽을 수 있는 단어의 수를 계산하는 함수
def solve(N, K, words):
    if K < 5:  # K가 5보다 작으면 "antic" 기본 글자를 배울 수 없으므로
        return 0  # 읽을 수 있는 단어는 0개
    elif K == 26:  # K가 26이면 모든 알파벳을 배울 수 있으므로
        return N  # 모든 단어를 읽을 수 있음
    
    basic_letters = {'a', 'n', 't', 'i', 'c'}  # 기본적으로 알아야 하는 글자 집합
    all_letters = set(chr(i) for i in range(ord('a'), ord('z') + 1))  # 모든 알파벳 집합
    letters_to_learn = all_letters - basic_letters  # 추가로 배워야 하는 글자 집합
    
    words = [set(word) - basic_letters for word in words]  # 단어에서 기본 글자를 제외한 글자들로 구성된 집합 리스트
    
    max_readable = 0  # 최대 읽을 수 있는 단어 수를 저장할 변수
    for comb in combinations(letters_to_learn, K - 5):  # 배울 수 있는 글자의 모든 조합을 탐색
        learned = [False] * 26  # 알파벳을 배웠는지 여부를 저장하는 리스트 초기화
        for letter in basic_letters:  # 기본 글자는 배운 것으로 설정
            learned[ord(letter) - ord('a')] = True
        for letter in comb:  # 현재 조합의 글자들도 배운 것으로 설정
            learned[ord(letter) - ord('a')] = True
        max_readable = max(max_readable, count_readable_words(words, learned))  # 최대 읽을 수 있는 단어 수 갱신
    
    return max_readable  # 최대 읽을 수 있는 단어 수 반환

# 입력 받기
N, K = map(int, input().split())  # 첫 번째 줄에서 단어의 개수 N과 가르칠 글자의 수 K를 입력 받음
words = [input().strip() for _ in range(N)]  # N개의 단어를 입력 받아 리스트에 저장

# 결과 출력
print(solve(N, K, words))  # 계산된 최대 읽을 수 있는 단어 수를 출력
