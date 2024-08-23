def largest_rectangle_area(hist):
    # 스택을 초기화합니다. 스택에는 히스토그램 막대의 인덱스가 저장됩니다.
    stack = []
    # 최대 면적을 저장할 변수를 초기화합니다.
    max_area = 0
    # 현재 히스토그램의 인덱스를 가리키는 변수를 초기화합니다.
    index = 0

    # 히스토그램의 모든 막대를 순회합니다.
    while index < len(hist):
        # 스택이 비어 있거나 현재 막대가 스택의 최상단 막대보다 높으면 인덱스를 스택에 추가합니다.
        if not stack or hist[stack[-1]] <= hist[index]:
            stack.append(index)
            index += 1
        else:
            # 현재 막대가 스택의 최상단 막대보다 낮으면 스택에서 인덱스를 꺼냅니다.
            top_of_stack = stack.pop()
            # 꺼낸 막대의 높이를 기준으로 넓이를 계산합니다.
            area = (hist[top_of_stack] * 
                   ((index - stack[-1] - 1) if stack else index))
            # 최대 면적을 갱신합니다.
            max_area = max(max_area, area)

    # 남아 있는 스택의 막대들에 대해 넓이를 계산합니다.
    while stack:
        top_of_stack = stack.pop()
        area = (hist[top_of_stack] * 
              ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    # 최대 면적을 반환합니다.
    return max_area

def process_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while index < len(data):
        # 각 테스트 케이스의 막대 수를 읽습니다.
        n = int(data[index])
        # 막대 수가 0이면 종료합니다.
        if n == 0:
            break
        # 히스토그램의 높이를 리스트로 저장합니다.
        hist = list(map(int, data[index+1:index+1+n]))
        # 가장 큰 직사각형의 넓이를 계산하여 출력합니다.
        print(largest_rectangle_area(hist))
        # 다음 테스트 케이스로 이동합니다.
        index += n + 1

# 입력을 처리하는 함수를 호출합니다.
process_input()
