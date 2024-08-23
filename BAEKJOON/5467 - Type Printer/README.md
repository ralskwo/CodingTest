# Type Printer 문제 풀이 및 설명 

https://www.acmicpc.net/problem/5467

## 문제 설명

이 문제에서는 이동식 활자 프린터를 사용하여 단어를 출력해야 합니다. 이동식 활자 프린터는 각 문자가 담긴 작은 금속 조각들을 배치하여 단어를 형성하는 구식 프린터입니다. 종이에 단어를 인쇄하려면 다음 작업을 수행할 수 있습니다:
1. 현재 프린터에 있는 단어의 끝에 문자를 추가하기.
2. 현재 프린터에 있는 단어의 끝에서 문자를 제거하기. 단, 현재 프린터에 최소한 하나의 문자가 있어야 제거할 수 있음.
3. 현재 프린터에 있는 단어를 인쇄하기.

초기에는 프린터가 비어 있습니다. 단어를 모두 인쇄한 후, 프린터에 문자가 남아 있어도 괜찮습니다. 단어들은 어떤 순서로든 인쇄할 수 있습니다.

각 작업은 시간 소모가 있으므로 전체 작업의 수를 최소화하고자 합니다.

주어진 단어들을 인쇄하는 데 필요한 최소 작업 수를 찾고, 그 작업 순서를 출력하는 프로그램을 작성해야 합니다.

## 문제 이해

이 문제는 이동식 활자 프린터를 사용하여 단어를 출력하는 과정에서 최소한의 작업으로 모든 단어를 출력하는 문제입니다. 각 단어는 인쇄될 때 추가, 제거 및 인쇄 작업을 거쳐야 합니다. 작업의 수를 최소화하려면 공통 접두사를 최대한 활용하여 불필요한 작업을 줄여야 합니다.

## 접근 방식

1. **트라이 자료구조 사용**: 단어들을 트라이에 삽입하여 공통 접두사를 효율적으로 관리할 수 있습니다.
2. **재귀적 탐색**: 트라이를 재귀적으로 탐색하면서 각 노드에서 필요한 작업을 수행합니다.
3. **우선순위 큐 사용**: 최대 깊이를 기준으로 자식 노드를 정렬하여 효율적으로 작업을 수행합니다.

## 풀이 과정

1. **트라이 노드 정의**: `TrieNode` 클래스는 자식 노드를 저장할 딕셔너리, 단어의 끝을 나타내는 `end` 플래그, 최대 깊이를 저장하는 `max_depth` 속성을 가집니다.
2. **트라이 클래스 정의**: `Trie` 클래스는 루트 노드를 초기화하고, 단어를 삽입하는 `insert` 메소드를 제공합니다. 단어를 삽입할 때 각 문자를 자식 노드로 추가하고, 각 노드의 최대 깊이를 갱신합니다.
3. **재귀적 탐색 함수 정의**: `solve` 함수는 현재 노드가 단어의 끝이면 'P'를 추가하고, 자식 노드를 최대 깊이를 기준으로 정렬하여 처리합니다. 각 문자를 추가한 후 재귀적으로 자식 노드를 탐색하며, 처리가 끝난 후 '-'를 추가합니다.
4. **메인 함수**: `main` 함수는 입력을 받아 트라이에 단어를 삽입하고, `solve` 함수를 호출하여 필요한 연산을 계산합니다. 결과를 출력하기 전에 마지막 '-'를 제거하고, 총 연산 수와 각 연산을 출력합니다.

이 과정을 통해 문제를 효율적으로 해결할 수 있습니다.

# 코드
```python
import sys
import heapq

class TrieNode:
    def __init__(self):
        # 자식 노드를 저장할 딕셔너리
        self.children = {}
        # 현재 노드가 단어의 끝인지 여부
        self.end = False
        # 이 노드부터 최대 깊이를 나타내는 값
        self.max_depth = 0

class Trie:
    def __init__(self):
        # 루트 노드를 초기화
        self.root = TrieNode()

    def insert(self, word):
        # 단어를 트라이에 삽입
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                # 자식 노드가 없으면 새로 생성
                node.children[char] = TrieNode()
            node = node.children[char]
            # 현재 노드의 최대 깊이 갱신
            node.max_depth = max(node.max_depth, len(word) - i - 1)
        # 단어의 끝임을 표시
        node.end = True

def solve(node, operations):
    if node.end:
        # 단어의 끝이면 'P' 추가
        operations.append('P')
    # 우선순위 큐를 사용해 자식 노드를 정렬
    pq = []
    for char, child in node.children.items():
        heapq.heappush(pq, (child.max_depth, char))
    while pq:
        # 최대 깊이와 문자를 꺼내서 처리
        _, char = heapq.heappop(pq)
        operations.append(char)
        solve(node.children[char], operations)
    # 자식 노드 처리가 끝나면 '-' 추가
    operations.append('-')

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    words = data[1:]
    
    # 트라이에 단어 삽입
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    operations = []
    # 트라이를 탐색하며 필요한 연산 계산
    solve(trie.root, operations)
    
    # 마지막 '-' 제거
    while operations and operations[-1] == '-':
        operations.pop()
    
    # 연산의 총 개수 출력
    print(len(operations))
    # 각 연산을 출력
    for op in operations:
        print(op)

if __name__ == "__main__":
    main()
