def max_substring_length(n, s):
    # 왼쪽 포인터를 초기화 (윈도우의 시작점)
    left = 0
    
    # 각 문자의 개수를 저장할 딕셔너리 초기화
    char_count = {}
    
    # 최대 길이를 저장할 변수 초기화
    max_len = 0

    # 오른쪽 포인터를 이동하며 문자열을 순회
    for right in range(len(s)):
        # 오른쪽 포인터가 가리키는 문자를 딕셔너리에 추가하거나, 기존 값에 1을 더함
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # 고유 문자 개수가 n을 초과하는 경우
        while len(char_count) > n:
            # 왼쪽 포인터가 가리키는 문자의 개수를 1 감소
            char_count[s[left]] -= 1
            
            # 해당 문자의 개수가 0이 되면 딕셔너리에서 삭제하여 고유 문자 개수를 줄임
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            
            # 왼쪽 포인터를 오른쪽으로 한 칸 이동하여 윈도우를 축소
            left += 1

        # 현재 윈도우의 길이를 계산하고 최대 길이를 갱신
        max_len = max(max_len, right - left + 1)

    # 최대 길이를 반환
    return max_len

if __name__ == "__main__":
    # 첫 줄에서 인식할 수 있는 최대 알파벳 종류 수를 입력받음
    n = int(input().strip())
    
    # 두 번째 줄에서 문자열을 입력받음
    s = input().strip()
    
    # 최대 길이를 계산하는 함수를 호출하여 결과를 변수에 저장
    result = max_substring_length(n, s)
    
    # 결과를 출력
    print(result)