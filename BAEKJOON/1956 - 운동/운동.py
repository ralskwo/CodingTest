import sys  # 표준 입력을 사용하기 위해 sys 모듈을 임포트

def floyd_warshall_min_cycle(V, edges):
    inf = float('inf')  # 무한대를 나타내기 위해 inf 변수에 float('inf') 할당
    dist = [[inf] * V for _ in range(V)]  # V x V 크기의 2차원 리스트를 생성하고 모든 값을 inf로 초기화

    # 간선 정보를 바탕으로 dist 배열 초기화
    for a, b, c in edges:
        dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)  # a에서 b로 가는 거리를 c로 설정 (1-based index를 0-based로 변환)

    # 플로이드-워셜 알고리즘 수행
    for k in range(V):  # 중간에 거쳐가는 정점 k에 대해 반복
        for i in range(V):  # 출발 정점 i에 대해 반복
            for j in range(V):  # 도착 정점 j에 대해 반복
                # dist[i][j]를 경유하는 경우와 비교하여 더 짧은 거리로 갱신
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_cycle = inf  # 최소 사이클의 길이를 저장할 변수 초기화
    for i in range(V):  # 각 정점 i에 대해 반복
        if dist[i][i] < min_cycle:  # 정점 i에서 다시 i로 돌아오는 경로의 길이가 최소값보다 작으면 갱신
            min_cycle = dist[i][i]

    # 가능한 최소 사이클이 존재하지 않으면 -1 반환, 그렇지 않으면 최소 사이클의 길이를 반환
    return min_cycle if min_cycle != inf else -1

# 입력 처리: 정점의 수 V와 간선의 수 E를 입력받음
V, E = map(int, sys.stdin.readline().split())
# 간선 정보를 E개의 줄에 걸쳐 입력받아 리스트로 저장
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

# 최소 사이클 길이를 계산하고 결과 출력
result = floyd_warshall_min_cycle(V, edges)
print(result)