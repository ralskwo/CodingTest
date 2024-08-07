# 히스토그램에서 가장 큰 직사각형 문제 풀이 및 설명

https://www.acmicpc.net/problem/6549

## 문제 이해

이 문제는 히스토그램에서 가장 큰 직사각형을 찾는 것입니다. 히스토그램은 여러 개의 직사각형이 연속적으로 나열된 형태로, 각 직사각형은 같은 너비를 가지고 있지만 높이는 다를 수 있습니다. 주어진 히스토그램에서 가장 큰 면적을 가진 직사각형을 찾아야 합니다. 예를 들어, 히스토그램이 `[2, 1, 4, 5, 1, 3, 3]`이라면, 가장 큰 직사각형의 면적은 8입니다.

## 입출력 조건

**입력**:
- 입력은 여러 개의 테스트 케이스로 이루어져 있습니다.
- 각 테스트 케이스는 한 줄로 주어지며, 첫 번째 수는 직사각형의 수 `n`을 나타내고, 다음 `n`개의 정수는 각 직사각형의 높이 `h_1, h_2, ..., h_n`를 나타냅니다. (1 ≤ `n` ≤ 100,000)
- 각 높이 `h_i`는 0 이상 1,000,000,000 이하의 정수입니다.
- 입력의 마지막 줄에는 0이 하나 주어집니다.

**출력**:
- 각 테스트 케이스에 대해, 히스토그램에서 가장 큰 직사각형의 면적을 출력합니다.

## 접근 방식

이 문제를 효율적으로 해결하기 위해 스택을 사용하는 방법을 활용할 수 있습니다. 스택을 사용하여 각 히스토그램 막대를 순회하면서 최대 면적을 계산하는 방식입니다. 이 방법은 시간 복잡도가 O(n)으로, 모든 막대를 한 번씩만 처리하기 때문에 매우 효율적입니다.

## 풀이 과정

1. **스택 초기화**:
   스택은 현재까지의 히스토그램 막대의 인덱스를 저장하는 데 사용됩니다. 최대 면적을 저장할 변수 `max_area`와 현재 인덱스를 가리키는 `index` 변수를 초기화합니다.

2. **히스토그램 순회**:
   히스토그램의 각 막대를 순회합니다.
   - 스택이 비어 있거나 현재 막대의 높이가 스택의 최상단 막대 높이보다 크거나 같으면 현재 인덱스를 스택에 추가합니다.
   - 그렇지 않으면 스택에서 최상단 인덱스를 꺼내고, 이 인덱스에 해당하는 막대 높이를 기준으로 면적을 계산합니다. 계산된 면적과 현재 최대 면적을 비교하여 최대 면적을 갱신합니다.

3. **남아 있는 스택 처리**:
   히스토그램 순회가 끝난 후에도 스택에 남아 있는 인덱스들에 대해 면적을 계산하고 최대 면적을 갱신합니다.

4. **입력 처리 및 결과 출력**:
   여러 개의 테스트 케이스를 입력으로 받아 각 케이스에 대해 가장 큰 직사각형의 면적을 계산하여 출력합니다. 입력은 마지막에 0이 주어질 때까지 계속됩니다.

이 과정을 통해 히스토그램에서 가장 큰 직사각형의 면적을 효율적으로 찾을 수 있습니다.

## 코드 구현
```python
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
