# 주어진 문자열 `s`가 균형잡힌 문자열인지 확인하는 함수 정의
def is_balanced_string(s):
    # 스택을 초기화하여 여는 괄호를 저장
    stack = []
    # 닫는 괄호와 여는 괄호를 매핑하는 딕셔너리 정의
    pairs = {')': '(', ']': '['}
    
    # 문자열 `s`의 각 문자에 대해 반복
    for char in s:
        # 문자가 여는 괄호인 경우
        if char in '([':
            # 스택에 여는 괄호를 추가
            stack.append(char)
        # 문자가 닫는 괄호인 경우
        elif char in ')]':
            # 스택이 비어있거나 스택의 상단이 대응하는 여는 괄호가 아닌 경우
            if not stack or stack[-1] != pairs[char]:
                # 균형이 맞지 않으므로 "no" 반환
                return "no"
            # 스택의 상단을 제거하여 짝을 맞춤
            stack.pop()
    
    # 모든 문자를 처리한 후 스택이 비어있지 않은 경우
    if stack:
        # 여는 괄호가 남아 있으므로 "no" 반환
        return "no"
    # 스택이 비어있는 경우 균형잡힌 문자열이므로 "yes" 반환
    return "yes"

# 표준 입력에서 데이터를 읽어옴
import sys
input = sys.stdin.read

# 입력 데이터를 줄 단위로 분할
data = input().split('\n')

# 각 줄에 대해 반복
for line in data:
    # 줄이 점 하나(".")인 경우
    if line == '.':
        # 입력 종료를 의미하므로 반복문 탈출
        break
    # 현재 줄이 균형잡힌 문자열인지 확인하고 결과 출력
    print(is_balanced_string(line))
