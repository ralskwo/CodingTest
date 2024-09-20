class FenwickTree:
    def __init__(self, size):
        # 주어진 크기(size)를 받아서 펜윅 트리 초기화
        self.size = size
        # 크기 + 1 만큼의 배열을 0으로 초기화 (1-based index를 사용하기 때문에 크기를 하나 더 늘림)
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        # index 위치에서 value 값을 트리에 더하고, 영향을 받는 상위 인덱스들도 갱신
        while index <= self.size:
            # 해당 인덱스에 value 값을 더함
            self.tree[index] += value
            # index를 상위 노드로 이동 (index += index & -index)
            index += index & -index
    
    def query(self, index):
        # 1부터 index까지의 합을 구하는 함수
        sum = 0
        # index가 0보다 큰 동안 구간 합을 계산
        while index > 0:
            # 현재 index의 값을 sum에 더함
            sum += self.tree[index]
            # index를 하위 노드로 이동 (index -= index & -index)
            index -= index & -index
        # 1부터 주어진 index까지의 합을 반환
        return sum

def count_inversions(N, A, B):
    # A열의 각 식별번호를 인덱스로 변환하여 B열에서의 위치를 찾기 위한 매핑을 생성
    position_map = {number: i + 1 for i, number in enumerate(A)}
    # B열의 각 번호를 A열의 순서에 맞게 재배열
    mapped_B = [position_map[number] for number in B]

    # 펜윅 트리를 초기화
    fenwick_tree = FenwickTree(N)
    # 역순 쌍의 개수를 저장할 변수
    inversion_count = 0

    # B열을 재배열한 리스트를 오른쪽에서 왼쪽으로 순회
    for i in range(N - 1, -1, -1):
        # 현재 인덱스보다 작은 값이 앞에 몇 개 있는지 펜윅 트리로 계산하여 역순 쌍 개수에 더함
        inversion_count += fenwick_tree.query(mapped_B[i] - 1)
        # 현재 값을 펜윅 트리에 업데이트
        fenwick_tree.update(mapped_B[i], 1)
    
    # 역순 쌍의 총 개수를 반환
    return inversion_count

# 입력을 처리하여 N, A열, B열 값을 받음
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 교차하는 케이블 쌍의 개수를 계산하여 출력
print(count_inversions(N, A, B))
