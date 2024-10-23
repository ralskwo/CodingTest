def make_largest_number(N, K, number):
    # 결과를 저장할 스택을 초기화합니다.
    stack = []
    # 입력된 숫자의 각 자릿수를 순서대로 처리합니다.
    for num in number:
        # 스택이 비어있지 않고, 아직 제거할 수 있는 수가 남아 있으며,
        # 스택의 마지막 수가 현재 수보다 작으면 스택에서 제거합니다.
        while K > 0 and stack and stack[-1] < num:
            stack.pop()  # 스택의 마지막 수를 제거하여 더 큰 수를 만들 수 있도록 합니다.
            K -= 1  # 제거한 수의 개수를 1 줄입니다.
        # 현재 수를 스택에 추가합니다.
        stack.append(num)
    
    # 모든 수를 처리한 후에도 K가 남아 있으면, 뒤에서부터 K개의 수를 제거합니다.
    if K > 0:
        stack = stack[:-K]
    
    # 스택에 남아있는 숫자들을 이어붙여서 하나의 문자열로 반환합니다.
    return ''.join(stack)

# 첫째 줄에서 N과 K를 입력받고 정수로 변환합니다.
N, K = map(int, input().split())
# 둘째 줄에서 N자리 숫자를 입력받습니다.
number = input().strip()

# K개의 수를 제거했을 때 얻을 수 있는 가장 큰 수를 출력합니다.
print(make_largest_number(N, K, number))