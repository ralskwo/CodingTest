from collections import defaultdict  # defaultdict를 사용해 그래프를 인접 리스트로 표현
import sys  # 재귀 한도를 설정하기 위해 sys 모듈을 사용

sys.setrecursionlimit(10**6)  # 재귀 한도를 100만으로 설정


def find_bridges(V, edges):
    graph = defaultdict(list)  # 그래프를 저장할 인접 리스트 생성
    for a, b in edges:  # 주어진 간선 정보를 그래프에 추가
        graph[a].append(b)
        graph[b].append(a)

    dfs_num = [-1] * (V + 1)  # 각 노드의 방문 순서를 저장하는 리스트
    low = [-1] * (V + 1)  # 각 노드의 최소 도달 순서를 저장하는 리스트
    bridges = []  # 단절선을 저장할 리스트
    timer = [0]  # DFS 탐색 순서를 저장할 타이머 변수

    def dfs(curr, parent):
        dfs_num[curr] = low[curr] = timer[
            0
        ]  # 현재 노드의 방문 순서와 low 값을 타이머로 초기화
        timer[0] += 1  # 타이머를 증가

        for neighbor in graph[curr]:  # 현재 노드와 연결된 모든 이웃 노드 탐색
            if neighbor == parent:  # 부모 노드로 되돌아가는 간선은 무시
                continue
            if dfs_num[neighbor] == -1:  # 이웃 노드가 아직 방문되지 않은 경우
                dfs(neighbor, curr)  # 이웃 노드로 DFS 탐색
                low[curr] = min(low[curr], low[neighbor])  # low 값을 업데이트

                if low[neighbor] > dfs_num[curr]:  # 단절선 조건을 만족하는 경우
                    bridges.append(
                        (min(curr, neighbor), max(curr, neighbor))
                    )  # 단절선을 리스트에 추가
            else:  # 이미 방문한 이웃 노드라면
                low[curr] = min(low[curr], dfs_num[neighbor])  # low 값을 업데이트

    for i in range(1, V + 1):  # 모든 노드에 대해 DFS 탐색 수행
        if dfs_num[i] == -1:  # 아직 방문되지 않은 노드에서만 탐색 시작
            dfs(i, -1)  # -1은 부모 노드가 없음을 의미

    bridges.sort()  # 단절선을 사전순으로 정렬
    return bridges  # 정렬된 단절선 리스트 반환


input = sys.stdin.read  # 표준 입력을 읽어들임
data = input().splitlines()  # 입력 데이터를 줄 단위로 분리

V, E = map(int, data[0].split())  # 첫 번째 줄에서 노드와 간선의 개수를 추출
edges = [
    tuple(map(int, line.split())) for line in data[1:]
]  # 간선 정보를 리스트로 저장

bridges = find_bridges(V, edges)  # 단절선을 찾는 함수 호출

print(len(bridges))  # 단절선의 개수 출력
for u, v in bridges:  # 단절선을 하나씩 출력
    print(u, v)
