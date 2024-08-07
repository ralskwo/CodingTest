# 문자열 폭발 문제 풀이 및 설명

https://www.acmicpc.net/problem/9935

## 문제 이해

이 문제는 주어진 문자열에서 특정 '폭발 문자열'이 발생할 때마다 그 부분을 제거하고, 남은 문자열을 다시 연결하여 새로운 문자열을 만드는 문제입니다. 이 과정을 반복하여 더 이상 폭발 문자열이 남지 않을 때 최종적으로 남아 있는 문자열을 출력해야 합니다. 만약 모든 문자열이 제거되어 빈 문자열이 된다면 `"FRULA"`를 출력합니다. 이 문제는 문자열 내에서 특정 패턴(폭발 문자열)을 찾아 반복적으로 제거하는 작업을 요구하므로, 효율적인 문자열 처리 방법이 필요합니다.

## 입출력 조건

- **입력 조건**:
  - 첫 번째 줄에는 문자열 `S`가 주어집니다. 이 문자열의 길이는 최소 1에서 최대 1,000,000까지입니다.
  - 두 번째 줄에는 폭발 문자열 `B`가 주어집니다. 이 문자열의 길이는 최소 1에서 최대 36까지입니다.
  
- **출력 조건**:
  - 모든 폭발 문자열을 제거한 후 남아 있는 문자열을 출력합니다.
  - 만약 남은 문자열이 없다면 `"FRULA"`를 출력합니다.

## 접근 방식

이 문제를 풀기 위해서는 스택을 이용한 접근 방식을 사용할 수 있습니다. 스택은 LIFO(Last In, First Out) 구조로, 최근에 추가된 요소를 먼저 처리할 수 있습니다. 문자열을 앞에서부터 한 글자씩 순회하면서, 각 글자를 스택에 추가합니다. 이때 스택의 끝 부분이 폭발 문자열과 일치하는지 확인합니다. 만약 일치한다면 스택에서 그 부분을 제거합니다. 이 과정은 주어진 문자열을 끝까지 처리할 때까지 반복됩니다.

이 접근 방식은 스택을 사용하기 때문에, 문자열을 한 번 순회하면서 폭발 문자열을 제거할 수 있습니다. 이는 시간 복잡도 O(n)으로 매우 효율적입니다. 이 방식은 문자열의 길이가 최대 1,000,000까지 주어지는 경우에도 성능적으로 문제없이 작동할 수 있습니다.

## 풀이 과정

1. **스택 초기화**: 
   - 비어 있는 스택을 하나 초기화합니다. 이 스택은 문자열을 순차적으로 처리하면서 폭발 문자열을 감지하고 제거하는 데 사용됩니다.

2. **문자열 순회**:
   - 주어진 문자열 `S`를 처음부터 끝까지 한 글자씩 순회합니다.
   - 각 글자를 스택에 추가합니다.

3. **폭발 문자열 확인**:
   - 스택에 새로 추가된 글자와 함께, 스택의 끝 부분이 폭발 문자열 `B`와 일치하는지 확인합니다.
   - 일치하는 경우, 스택에서 폭발 문자열의 길이만큼 문자를 제거합니다. 이때, 스택의 끝부분에서 폭발 문자열의 길이만큼을 잘라내어 문자열로 만든 후, 폭발 문자열과 비교합니다.

4. **최종 문자열 조합**:
   - 문자열 순회가 끝난 후, 스택에 남아 있는 문자들을 모두 합쳐서 최종 문자열을 만듭니다.
   - 이 최종 문자열이 빈 문자열인 경우 `"FRULA"`를 출력하고, 그렇지 않으면 그 결과 문자열을 출력합니다.

5. **시간 복잡도 분석**:
   - 이 접근 방식은 주어진 문자열을 한 번 순회하면서, 스택의 끝부분과 폭발 문자열을 비교하여 제거하는 방식입니다. 따라서 시간 복잡도는 O(n)으로 매우 효율적입니다. 이는 주어진 문자열의 길이가 최대 1,000,000일 경우에도 충분히 성능적으로 처리할 수 있음을 의미합니다.

## 코드 구현
```python
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
