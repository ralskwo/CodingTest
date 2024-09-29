def find(parent, x):
    # x의 부모 노드를 찾는 함수 (경로 압축 기법을 이용하여 최적화)
    if parent[x] != x:  # 현재 노드가 자기 자신이 아니라면
        parent[x] = find(parent, parent[x])  # 부모 노드를 재귀적으로 찾아서 최상위 부모로 업데이트
    return parent[x]  # 최상위 부모 노드 반환

def union(parent, a, b):
    # 두 노드 a와 b를 같은 그룹으로 합치는 함수
    rootA = find(parent, a)  # a의 최상위 부모 노드 찾기
    rootB = find(parent, b)  # b의 최상위 부모 노드 찾기
    if rootA != rootB:  # a와 b의 부모가 다르다면 (다른 그룹에 속해 있다면)
        parent[rootB] = rootA  # b의 부모를 a의 부모로 설정하여 그룹을 합침

N = int(input())  # 도시의 수 입력 받기
M = int(input())  # 여행 계획에 속한 도시의 수 입력 받기

parent = [i for i in range(N+1)]  # 부모 노드 배열 초기화 (1부터 N까지 각 도시의 부모를 자기 자신으로 설정)

for i in range(1, N+1):
    # 각 도시의 연결 정보를 입력 받아서 인접 행렬을 순회
    row = list(map(int, input().split()))  # i번째 도시의 j번째 연결 정보를 입력 받기
    for j in range(1, N+1):
        if row[j-1] == 1:  # i번째 도시와 j번째 도시가 연결되어 있다면
            union(parent, i, j)  # 두 도시를 같은 그룹으로 합침

plan = list(map(int, input().split()))  # 여행 계획에 포함된 도시들을 입력 받기

root = find(parent, plan[0])  # 여행 계획의 첫 번째 도시의 최상위 부모 노드를 찾기
possible = True  # 여행 계획이 가능한지 여부를 저장할 변수 (초기값은 True로 설정)
for city in plan:
    # 여행 계획에 포함된 각 도시가 같은 그룹에 속하는지 확인
    if find(parent, city) != root:  # 현재 도시의 부모 노드가 첫 번째 도시의 부모와 다르다면
        possible = False  # 여행 계획이 불가능하므로 possible을 False로 설정
        break  # 더 이상 확인할 필요 없으므로 반복문 종료

print("YES" if possible else "NO")  # 여행 계획이 가능하면 YES, 불가능하면 NO 출력