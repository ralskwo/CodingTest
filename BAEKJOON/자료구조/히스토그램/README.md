# 히스토그램에서 가장 큰 직사각형의 넓이 구하기

https://www.acmicpc.net/problem/1725

## 문제 이해
이 문제는 히스토그램 막대들의 높이를 주어 가장 큰 직사각형의 넓이를 찾는 것입니다. 히스토그램의 각 막대는 동일한 너비를 가지며, 막대 높이는 주어진 리스트에 저장되어 있습니다.

## 접근 방식
이 문제를 효율적으로 해결하기 위해 스택을 사용합니다. 스택은 현재 처리 중인 막대들의 인덱스를 저장하며, 스택을 통해 막대들을 관리하면서 가장 큰 직사각형의 넓이를 계산합니다.

## 풀이 과정
1. 히스토그램의 각 막대를 순회하면서, 스택에 현재 막대의 인덱스를 저장합니다.
2. 스택의 상단에 있는 막대보다 현재 막대의 높이가 작으면, 스택에서 인덱스를 꺼내어 해당 막대를 기준으로 직사각형의 넓이를 계산합니다.
3. 모든 막대를 처리한 후, 스택에 남아 있는 막대들도 동일한 방식으로 넓이를 계산합니다.
4. 이 과정을 통해 가장 큰 직사각형의 넓이를 찾습니다.

## 코드
```python
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
