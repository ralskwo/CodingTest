from collections import Counter

# Counter 모듈을 사용하여 문자열의 각 문자 빈도를 계산할 수 있도록 가져옴

g, s_len = map(int, input().split())
# 단어 W의 길이(g)와 문자열 S의 길이(s_len)를 입력받음

W = input().strip()
# 단어 W를 입력받고 양쪽 공백을 제거

S = input().strip()
# 문자열 S를 입력받고 양쪽 공백을 제거

w_count = Counter(W)
# 단어 W의 각 문자 빈도를 계산하여 w_count에 저장

window_count = Counter(S[:g])
# 문자열 S의 처음 g개의 문자에 대한 빈도를 계산하여 window_count에 저장

count = 0
# 조건을 만족하는 경우의 수를 저장할 변수 count 초기화

if w_count == window_count:
    count += 1
# 초기 윈도우(처음 g개의 문자)의 빈도와 W의 빈도가 같으면 count를 1 증가

for i in range(g, s_len):
    start_char = S[i - g]
    # 슬라이딩 윈도우의 시작 문자를 가져옴

    end_char = S[i]
    # 슬라이딩 윈도우의 끝 문자를 가져옴

    window_count[end_char] += 1
    # 새로 추가된 문자(end_char)의 빈도를 1 증가

    window_count[start_char] -= 1
    # 윈도우에서 제외된 문자(start_char)의 빈도를 1 감소

    if window_count[start_char] == 0:
        del window_count[start_char]
    # 제외된 문자의 빈도가 0이 되면 딕셔너리에서 삭제

    if window_count == w_count:
        count += 1
    # 현재 윈도우의 문자 빈도가 W의 문자 빈도와 같으면 count를 1 증가

print(count)
# 최종적으로 조건을 만족하는 경우의 수를 출력
