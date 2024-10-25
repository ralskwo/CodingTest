import sys

# 펜윅 트리(Fenwick Tree)를 정의하는 클래스
class FenwickTree:
    def __init__(self, size):
        # 트리의 크기를 저장하고, 그 크기만큼의 배열을 초기화한다.
        self.size = size
        self.tree = [0] * (size + 1)

    # 특정 인덱스에 값을 추가하는 함수
    def update(self, index, value):
        # 인덱스가 트리의 크기를 넘지 않을 때까지 값을 추가
        while index <= self.size:
            self.tree[index] += value
            # 인덱스를 업데이트하여 다음 노드로 이동
            index += index & -index

    # 특정 인덱스까지의 누적 합을 계산하는 함수
    def query(self, index):
        result = 0
        # 인덱스가 0보다 클 때까지 값을 누적
        while index > 0:
            result += self.tree[index]
            # 인덱스를 업데이트하여 이전 노드로 이동
            index -= index & -index
        return result

# 좌표 압축을 수행하는 함수
def coordinate_compress(values):
    # 입력값들을 중복 제거 및 내림차순 정렬
    sorted_unique = sorted(set(values), reverse=True)
    # 정렬된 값을 기반으로 각 값에 순위를 매겨 매핑
    rank = {value: idx + 1 for idx, value in enumerate(sorted_unique)}
    # 입력값들을 순위로 변환하여 반환
    return [rank[value] for value in values]

# 문제를 해결하는 메인 함수
def solve():
    # 첫 줄에서 선수의 수를 입력받음
    N = int(sys.stdin.readline())
    # 각 선수의 실력을 리스트에 저장
    abilities = [int(sys.stdin.readline()) for _ in range(N)]
    
    # 좌표 압축 수행
    compressed_abilities = coordinate_compress(abilities)
    # 펜윅 트리의 크기는 압축된 최대값으로 설정
    max_value = max(compressed_abilities)
    fenwick_tree = FenwickTree(max_value)
    
    results = []
    # 각 선수의 압축된 실력을 순회하며 등수를 계산
    for ability in compressed_abilities:
        # 현재 선수보다 실력이 낮은 선수의 수를 쿼리
        higher_count = fenwick_tree.query(ability - 1)
        # 현재 선수의 최선의 등수를 결과 리스트에 추가
        results.append(higher_count + 1)
        # 현재 선수의 실력을 펜윅 트리에 업데이트하여 이후 계산에 반영
        fenwick_tree.update(ability, 1)
    
    # 결과를 한 줄씩 출력
    sys.stdout.write("\n".join(map(str, results)) + '\n')

# 문제 해결 함수 실행
solve()