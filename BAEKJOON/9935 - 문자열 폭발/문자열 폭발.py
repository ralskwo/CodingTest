def explode_string(s, bomb):
    # 함수 explode_string은 주어진 문자열 s와 폭발 문자열 bomb를 받아서
    # 폭발 과정을 수행한 후의 최종 문자열을 반환하는 함수입니다.
    
    stack = []
    # stack은 문자를 하나씩 쌓아두는 리스트입니다.
    # 문자열을 순차적으로 처리하면서 폭발 문자열을 발견하면 제거합니다.

    bomb_len = len(bomb)
    # bomb_len은 폭발 문자열의 길이를 저장하는 변수입니다.
    # 나중에 스택의 끝부분을 확인할 때 사용됩니다.

    for char in s:
        # 주어진 문자열 s를 한 글자씩 순회합니다.
        
        stack.append(char)
        # 현재 문자를 스택에 추가합니다.
        
        if ''.join(stack[-bomb_len:]) == bomb:
            # 스택의 끝에서 bomb_len 길이만큼 잘라서 폭발 문자열과 비교합니다.
            # 만약 일치하면, 폭발 문자열이 스택의 끝에 위치해 있는 것입니다.
            
            del stack[-bomb_len:]
            # 스택의 끝부분에 위치한 폭발 문자열을 제거합니다.
            # del stack[-bomb_len:]는 스택의 끝에서 bomb_len 만큼의 요소를 삭제합니다.

    result = ''.join(stack)
    # 스택에 남아 있는 문자들을 합쳐서 최종 결과 문자열을 만듭니다.

    if result == '':
        # 최종 결과 문자열이 빈 문자열이라면
        return "FRULA"
        # "FRULA"를 반환합니다.
    else:
        return result
        # 빈 문자열이 아니라면 최종 결과 문자열을 반환합니다.

# 입력
s = input().strip()
# 첫 번째 줄에서 문자열 s를 입력받습니다. strip()은 앞뒤의 공백을 제거합니다.

bomb = input().strip()
# 두 번째 줄에서 폭발 문자열 bomb를 입력받습니다. strip()은 앞뒤의 공백을 제거합니다.

# 출력
print(explode_string(s, bomb))
# explode_string 함수를 호출하여 최종 결과를 계산한 후, 그 결과를 출력합니다.
