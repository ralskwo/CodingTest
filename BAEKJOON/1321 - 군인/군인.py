import sys
input = sys.stdin.readline

# 세그먼트 트리(SegmentTree) 클래스 정의
class SegmentTree:
    def __init__(self, n):  # 세그먼트 트리의 초기화 메서드
        self.size = 1  # 초기 사이즈를 1로 설정
        # 주어진 n보다 크거나 같은 가장 가까운 2의 제곱수 찾기
        while self.size < n:  
            self.size *= 2  # 사이즈를 2배씩 늘림
        # 트리 배열을 0으로 초기화. 트리의 크기는 2 * self.size
        self.tree = [0] * (2 * self.size)
    
    # 초기 배열을 세그먼트 트리에 빌드하는 함수
    def build(self, arr):
        # 입력 배열을 세그먼트 트리의 리프 노드에 삽입
        for i in range(len(arr)):
            self.tree[self.size + i] = arr[i]
        # 리프 노드 이후의 모든 부모 노드들을 자식 노드들의 합으로 초기화
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    # 특정 인덱스의 값을 변경하는 함수
    def update(self, index, value):
        # 인덱스를 트리의 리프 노드 위치로 이동
        index += self.size
        # 리프 노드의 값을 value만큼 더함
        self.tree[index] += value
        # 부모 노드로 거슬러 올라가면서 값을 갱신
        while index > 1:
            index //= 2  # 부모 노드로 이동
            # 부모 노드는 두 자식 노드의 합으로 설정
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]
    
    # 특정 군번이 속한 부대를 찾는 함수
    def query(self, soldier):
        # soldier가 전체 군인의 수를 초과할 경우 -1을 반환
        if soldier > self.tree[1]:
            return -1
        index = 1  # 루트 노드에서 탐색 시작
        # 리프 노드에 도달할 때까지 반복
        while index < self.size:
            # 왼쪽 자식 노드의 값이 soldier보다 크거나 같으면 왼쪽으로 이동
            if soldier <= self.tree[2*index]:
                index = 2*index
            # 그렇지 않으면 오른쪽으로 이동하고, soldier 값을 왼쪽 자식의 값만큼 감소
            else:
                soldier -= self.tree[2*index]
                index = 2*index + 1
        # index는 리프 노드의 위치이므로, 이를 부대 번호로 변환하여 반환
        return index - self.size + 1

# 입력: 부대의 개수 n
n = int(input())

# 입력: 각 부대의 군사 수
soldiers = list(map(int, input().split()))

# 세그먼트 트리 생성 및 초기화
seg_tree = SegmentTree(n)
seg_tree.build(soldiers)

# 입력: 명령의 개수 m
m = int(input())

# m개의 명령을 처리
for _ in range(m):
    # 각 명령을 입력받음
    query = list(map(int, input().split()))
    
    # "1 i a" 형태의 명령: i번 부대에 a명 증감
    if query[0] == 1:
        seg_tree.update(query[1]-1, query[2])  # 부대 번호를 0-based index로 변환하여 업데이트
    
    # "2 i" 형태의 명령: i번 군번이 속한 부대 찾기
    else:
        print(seg_tree.query(query[1]))  # i번 군번이 속한 부대를 출력