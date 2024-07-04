# 전화번호 목록 일관성 검사 문제

https://www.acmicpc.net/problem/5052

## 문제 이해

전화번호 목록이 주어졌다. 이제, 이 목록이 일관성이 있는지를 구하는 프로그램을 작성하시오.

전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어가 되어서는 안 된다.

예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자:
- 긴급전화: 911
- 상근: 97 625 999
- 선영: 91 12 54 26

이 경우에 선영이 긴급전화로 전화할 수 있는 방법이 없다. 전화번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다.

## 접근 방식

이 문제는 전화번호 목록이 일관성을 유지하는지 확인하는 문제입니다. 이는 한 전화번호가 다른 전화번호의 접두어가 되는지를 확인하는 문제로 볼 수 있습니다. 이를 효율적으로 해결하기 위해 트라이(Trie) 자료구조를 사용할 수 있습니다.

트라이 자료구조를 사용하여 각 전화번호를 삽입하면서 접두어 여부를 확인할 수 있습니다. 만약 삽입하는 도중에 현재 노드가 이미 종료 노드이거나, 삽입이 완료된 후에 하위 노드가 존재한다면 이는 일관성이 없는 목록이라는 것을 의미합니다.

## 풀이 과정

1. **입력 처리**:
   - 입력은 여러 줄로 주어집니다. 첫 줄에는 테스트 케이스의 수가 주어지고, 각 테스트 케이스의 첫 줄에는 전화번호의 수 \( n \)이 주어집니다.
   - 그 다음 \( n \)개의 줄에 전화번호가 주어집니다.

2. **트라이 자료구조 정의**:
   - `TrieNode` 클래스는 각 노드를 정의하며, 자식 노드를 저장하는 `children` 딕셔너리와 현재 노드가 전화번호의 끝인지 여부를 저장하는 `is_end_of_number` 속성을 가집니다.
   - `Trie` 클래스는 트라이의 루트 노드를 초기화하고, 전화번호를 삽입하는 `insert` 메서드를 포함합니다. `insert` 메서드는 전화번호의 각 자릿수를 순차적으로 탐색하며 새로운 노드를 추가합니다. 삽입 과정에서 현재 노드가 이미 전화번호의 끝이거나, 삽입이 완료된 후에 하위 노드가 존재하면 일관성이 없는 것으로 판단합니다.

3. **메인 함수 구현**:
   - 입력을 받아 줄 단위로 나눕니다.
   - 각 테스트 케이스마다 새로운 트라이를 초기화하고 전화번호를 삽입하면서 일관성을 검사합니다.
   - 각 테스트 케이스에 대해 결과를 저장하고 출력합니다.

## 파이썬 코드

다음은 위 접근 방식을 기반으로 작성한 파이썬 코드입니다:

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 현재 노드의 자식 노드를 저장하는 딕셔너리
        self.is_end_of_number = False  # 현재 노드가 전화번호의 끝인지 여부를 저장

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 트라이의 루트 노드를 초기화

    def insert(self, number):
        current = self.root
        for digit in number:
            if digit not in current.children:
                current.children[digit] = TrieNode()  # 새로운 노드를 추가
            current = current.children[digit]
            if current.is_end_of_number:
                # 현재 노드가 이미 번호의 끝이라면 일관성 없음
                return False
        current.is_end_of_number = True
        if current.children:
            # 번호가 추가된 후에 하위 노드가 있으면 일관성 없음
            return False
        return True

import sys
input = sys.stdin.read  # 표준 입력에서 모든 입력을 한 번에 읽어오는 함수

def main():
    data = input().strip().split('\n')  # 입력을 줄 단위로 나눠 리스트로 저장
    test_cases = int(data[0])  # 첫 번째 줄은 테스트 케이스의 개수
    index = 1  # 현재 읽고 있는 줄의 인덱스

    results = []  # 결과를 저장할 리스트

    for _ in range(test_cases):
        n = int(data[index])  # 각 테스트 케이스의 첫 번째 줄은 전화번호의 수
        index += 1  # 다음 줄로 이동
        trie = Trie()  # 새로운 Trie 인스턴스 생성
        consistent = True  # 일관성 여부를 저장할 변수, 초기값은 True
        
        for _ in range(n):
            number = data[index]
            index += 1  # 다음 줄로 이동
            if consistent:
                if not trie.insert(number):
                    # 일관성이 깨지는 경우, False로 설정
                    consistent = False
        
        if consistent:
            results.append("YES")  # 일관성이 유지된 경우
        else:
            results.append("NO")  # 일관성이 깨진 경우

    print("\n".join(results))  # 결과를 줄 단위로 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행
