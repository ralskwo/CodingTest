# 친구 네트워크 문제 해결

https://www.acmicpc.net/problem/4195

## 문제 이해

민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구입니다. 소셜 네트워크 사이트에서 친구 관계가 주어질 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성해야 합니다. 여기서 친구 네트워크란 친구 관계만으로 이동할 수 있는 사람들의 집합을 의미합니다.

## 접근 방식

이 문제는 서로소 집합(Disjoint Set) 자료구조를 이용하여 해결할 수 있습니다. 서로소 집합 자료구조는 유니온 파인드(Union-Find) 알고리즘을 사용하여 구현할 수 있습니다. 유니온 파인드 알고리즘은 다음과 같은 두 가지 주요 연산을 효율적으로 수행합니다:

1. **Find**: 주어진 요소가 속한 집합을 찾습니다.
2. **Union**: 두 집합을 하나의 집합으로 합칩니다.

이 알고리즘을 사용하여 친구 관계를 트랙킹하고, 두 사람이 속한 네트워크의 크기를 효율적으로 계산할 수 있습니다.

## 풀이 과정

1. **입력 처리**:
   - 입력은 여러 줄로 주어집니다. 첫 줄에는 테스트 케이스의 수가 주어지고, 각 테스트 케이스의 첫 줄에는 친구 관계의 수 \( F \)가 주어집니다.
   - 각 친구 관계는 두 사람의 이름으로 이루어진 문자열 쌍으로 주어집니다.

2. **유니온 파인드 클래스 정의**:
   - `UnionFind` 클래스는 친구 네트워크를 관리하는 역할을 합니다.
   - `add` 메서드는 네트워크에 새로운 사람을 추가합니다.
   - `find` 메서드는 주어진 사람이 속한 네트워크의 루트 노드를 찾습니다. 경로 압축 기법을 사용하여 효율성을 높입니다.
   - `union` 메서드는 두 사람을 같은 네트워크로 합칩니다. 랭크 기법을 사용하여 더 작은 집합을 더 큰 집합에 합칩니다.

3. **메인 함수 구현**:
   - 입력을 받아 줄 단위로 나눕니다.
   - 각 테스트 케이스마다 새로운 `UnionFind` 인스턴스를 생성합니다.
   - 친구 관계를 읽어들이고, 이를 유니온 파인드 구조에 반영합니다.
   - 친구 관계가 추가될 때마다 두 사람이 속한 네트워크의 크기를 결과 리스트에 추가합니다.
   - 모든 테스트 케이스를 처리한 후 결과를 출력합니다.

## 코드
```python
class UnionFind:
    def __init__(self):
        self.parent = {}  # 각 노드의 부모를 저장하는 딕셔너리
        self.size = {}    # 각 루트 노드가 포함하는 집합의 크기를 저장하는 딕셔너리

    def find(self, person):
        # 경로 압축 기법을 사용하여 루트 노드를 찾고, 부모를 루트로 설정
        if self.parent[person] != person:
            self.parent[person] = self.find(self.parent[person])
        return self.parent[person]

    def union(self, person1, person2):
        root1 = self.find(person1)
        root2 = self.find(person2)

        if root1 != root2:
            # 더 큰 집합에 작은 집합을 합친다 (랭크 기법)
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def add(self, person):
        # 새로운 사람을 네트워크에 추가
        if person not in self.parent:
            self.parent[person] = person
            self.size[person] = 1

import sys
input = sys.stdin.read  # 표준 입력에서 한 번에 모든 입력을 읽어오는 함수

def main():
    data = input().strip().split('\n')  # 입력을 줄 단위로 나눠 리스트로 저장
    test_cases = int(data[0])  # 첫 번째 줄은 테스트 케이스의 개수
    index = 1  # 현재 읽고 있는 줄의 인덱스

    results = []  # 결과를 저장할 리스트

    for _ in range(test_cases):
        F = int(data[index])  # 각 테스트 케이스의 첫 번째 줄은 친구 관계의 수
        index += 1  # 다음 줄로 이동
        uf = UnionFind()  # 새로운 UnionFind 인스턴스 생성
        
        for _ in range(F):
            person1, person2 = data[index].split()  # 친구 관계를 읽어옴
            uf.add(person1)  # 첫 번째 사람을 네트워크에 추가
            uf.add(person2)  # 두 번째 사람을 네트워크에 추가
            uf.union(person1, person2)  # 두 사람을 같은 네트워크로 합침
            results.append(str(uf.size[uf.find(person1)]))  # 두 사람이 속한 네트워크의 크기를 결과에 추가
            index += 1  # 다음 줄로 이동

    print("\n".join(results))  # 결과를 줄 단위로 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행
```