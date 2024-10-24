import sys

def max_planes_docked(G, P, gi_list):
    # parent 리스트를 초기화하여 각 게이트가 자기 자신을 부모로 가지게 함
    parent = list(range(G + 1))

    # find 함수는 주어진 게이트 번호 x의 루트를 찾음
    # 경로 압축을 통해 트리의 깊이를 줄여 효율성을 높임
    def find(x):
        # 현재 게이트의 부모가 자기 자신이 아니면 재귀적으로 루트를 찾음
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # union 함수는 x 게이트와 y 게이트를 연결함
    # 여기서, y는 x보다 1 작은 게이트를 의미하여 게이트 연결을 관리함
    def union(x, y):
        parent[find(x)] = find(y)

    # 도킹된 비행기의 수를 저장하는 변수
    docked_planes = 0

    # gi_list에 있는 각 비행기에 대해 도킹 가능한 게이트를 찾음
    for gi in gi_list:
        # 현재 비행기가 도킹 가능한 가장 높은 번호의 게이트를 찾음
        available_gate = find(gi)
        # 만약 가능한 게이트가 0이면, 더 이상 도킹할 수 없으므로 반복 종료
        if available_gate == 0:
            break
        # 도킹 후, 현재 게이트와 그보다 작은 게이트를 union하여 연결
        union(available_gate, available_gate - 1)
        # 도킹된 비행기 수를 1 증가시킴
        docked_planes += 1

    # 도킹할 수 있는 최대 비행기 수를 반환
    return docked_planes

def main():
    # 표준 입력을 받아오는 함수
    input = sys.stdin.readline
    # 게이트 수 G를 입력받음
    G = int(input().strip())
    # 비행기 수 P를 입력받음
    P = int(input().strip())
    # 각 비행기의 도킹 가능 게이트 정보를 리스트로 저장
    gi_list = [int(input().strip()) for _ in range(P)]
    
    # 최대 도킹 가능한 비행기 수를 계산하고 출력
    result = max_planes_docked(G, P, gi_list)
    print(result)

# 프로그램의 시작점으로, main 함수를 호출
if __name__ == "__main__":
    main()
