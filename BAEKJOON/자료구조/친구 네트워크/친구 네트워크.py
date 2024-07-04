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
