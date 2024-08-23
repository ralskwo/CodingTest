def calculate_bracket_value(bracket_string):
    stack = []
    value = 0
    temp = 1

    for i in range(len(bracket_string)):
        if bracket_string[i] == '(':
            # 여는 괄호 '('를 만나면 스택에 푸시하고 temp를 2로 곱함
            stack.append('(')
            temp *= 2
        elif bracket_string[i] == '[':
            # 여는 괄호 '['를 만나면 스택에 푸시하고 temp를 3으로 곱함
            stack.append('[')
            temp *= 3
        elif bracket_string[i] == ')':
            # 닫는 괄호 ')'를 만나면
            if not stack or stack[-1] != '(':
                # 스택이 비어있거나 스택의 최상단이 '['이면 올바르지 않은 괄호열
                return 0
            if bracket_string[i-1] == '(':
                # 바로 직전이 '('이면 현재 temp를 value에 더함
                value += temp
            # 스택에서 '('를 팝하고 temp를 2로 나눔
            stack.pop()
            temp //= 2
        elif bracket_string[i] == ']':
            # 닫는 괄호 ']'를 만나면
            if not stack or stack[-1] != '[':
                # 스택이 비어있거나 스택의 최상단이 '('이면 올바르지 않은 괄호열
                return 0
            if bracket_string[i-1] == '[':
                # 바로 직전이 '['이면 현재 temp를 value에 더함
                value += temp
            # 스택에서 '['를 팝하고 temp를 3으로 나눔
            stack.pop()
            temp //= 3

    if stack:
        # 문자열을 모두 순회한 후 스택이 비어있지 않으면 올바르지 않은 괄호열
        return 0
    return value

# 입력 처리
import sys
input = sys.stdin.read().strip()
print(calculate_bracket_value(input))
