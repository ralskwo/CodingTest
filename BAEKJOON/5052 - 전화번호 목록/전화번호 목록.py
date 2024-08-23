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
    data = input().strip().split('\n')  # 입력을 줄 단위로 나누어 리스트로 저장
    test_cases = int(data[0])  # 첫 번째 줄은 테스트 케이스의 수
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
