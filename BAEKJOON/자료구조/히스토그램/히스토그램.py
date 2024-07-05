def largest_rectangle_area(histogram):
    # 스택을 초기화합니다.
    stack = []
    # 최대 넓이를 저장할 변수를 초기화합니다.
    max_area = 0
    # 현재 인덱스를 초기화합니다.
    index = 0

    # 히스토그램의 모든 막대를 순회합니다.
    while index < len(histogram):
        # 스택이 비어 있거나 현재 막대의 높이가 스택 상단의 막대 높이보다 크거나 같으면
        if not stack or histogram[stack[-1]] <= histogram[index]:
            # 현재 인덱스를 스택에 추가합니다.
            stack.append(index)
            # 다음 인덱스로 이동합니다.
            index += 1
        else:
            # 스택의 상단 인덱스를 꺼냅니다.
            top_of_stack = stack.pop()
            # 넓이를 계산합니다.
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            # 최대 넓이를 갱신합니다.
            max_area = max(max_area, area)

    # 남아 있는 스택을 처리합니다.
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    histogram = list(map(int, data[1:N+1]))
    print(largest_rectangle_area(histogram))
