# 괄호의 값 문제 풀이 과정

https://www.acmicpc.net/problem/2504

## 문제 이해 및 접근 방법

### 문제 이해
1. 4개의 기호 '(', ')', '[', ']'를 이용해서 만든 문자열 중에서 올바른 괄호열만 유효합니다. 유효한 괄호열의 값을 다음과 같이 정의합니다:
   - '()'는 값이 2입니다.
   - '[]'는 값이 3입니다.
   - (X)는 2 * 값(X)입니다.
   - [X]는 3 * 값(X)입니다.
   - X와 Y가 결합된 괄호열의 값은 값(X) + 값(Y)입니다.

2. 입력으로 주어진 문자열이 올바른 괄호열인지 판단하고, 올바른 괄호열이라면 그 값을 계산하는 프로그램을 작성합니다. 올바른 괄호열이 아닌 경우 값은 0으로 출력해야 합니다.

### 접근 방법
1. **스택 사용**:
   - 주어진 괄호열을 순회하면서 스택을 사용하여 여는 괄호를 저장하고, 닫는 괄호를 만났을 때 값을 계산합니다.

2. **여는 괄호 처리**:
   - 여는 괄호 '(', '  `[`'를 만나면 스택에 푸시하고 `temp` 값을 각각 2, 3으로 곱합니다.

3. **닫는 괄호 처리**:
   - 닫는 괄호 ')', '`]`'를 만나면 스택에서 값을 꺼내어 계산합니다.
   - 여는 괄호가 나오기 전까지 스택에서 값을 꺼내어 누적합을 구합니다.
   - 올바른 괄호열이 아닌 경우를 체크하여 처리합니다.

4. **올바른 괄호열 확인**:
   - 문자열을 모두 순회한 후 스택이 비어있지 않으면 올바르지 않은 괄호열이므로 0을 반환합니다.

### 코드 구현

```python
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
```