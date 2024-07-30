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
