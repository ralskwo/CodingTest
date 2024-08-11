from collections import deque  # BFS 구현을 위해 deque를 import
import sys  # 빠른 입력 처리를 위해 sys 모듈을 import

def find_cities_at_distance_k(N, M, K, X, roads):
    graph = [[] for _ in range(N + 1)]  # 각 도시별로 연결된 도로를 저장할 리스트를 생성
    for a, b in roads:  # 모든 도로 정보를 처리하여 그래프에 저장
        graph[a].append(b)  # 도로가 연결된 도시를 그래프에 추가

    distance = [-1] * (N + 1)  # 모든 도시의 최단 거리를 저장할 리스트, 처음에는 모두 -1로 설정
    distance[X] = 0  # 출발 도시는 자기 자신이므로 거리를 0으로 설정

    queue = deque([X])  # BFS를 위한 큐를 생성하고 출발 도시를 큐에 삽입

    while queue:  # 큐가 빌 때까지 BFS를 수행
        current_city = queue.popleft()  # 큐에서 현재 도시를 꺼냄

        for next_city in graph[current_city]:  # 현재 도시와 연결된 모든 도시에 대해 반복
            if distance[next_city] == -1:  # 해당 도시가 아직 방문되지 않았다면
                distance[next_city] = distance[current_city] + 1  # 현재 도시까지의 거리 + 1을 다음 도시의 거리로 설정
                queue.append(next_city)  # 다음 도시를 큐에 삽입하여 BFS를 이어나감

    result = []  # 최단 거리가 K인 도시들을 저장할 리스트 생성
    for i in range(1, N + 1):  # 모든 도시를 탐색
        if distance[i] == K:  # 만약 도시 i까지의 거리가 K라면
            result.append(i)  # 결과 리스트에 해당 도시 번호를 추가

    if not result:  # 만약 최단 거리가 K인 도시가 없다면
        print(-1)  # -1을 출력
    else:
        result.sort()  # 도시 번호를 오름차순으로 정렬
        for city in result:  # 결과 리스트에 있는 각 도시 번호를 출력
            print(city)

# 입력 처리
if __name__ == "__main__":  # 메인 함수로서 실행될 때만 실행되는 코드 블록
    N, M, K, X = map(int, input().split())  # 첫 줄에서 도시 수, 도로 수, 목표 거리, 출발 도시 번호를 입력받음
    roads = [tuple(map(int, input().split())) for _ in range(M)]  # 다음 M개의 줄에서 도로 정보를 입력받아 리스트로 저장
    
    # 함수 호출
    find_cities_at_distance_k(N, M, K, X, roads)  # 입력받은 데이터를 기반으로 도시들을 탐색하여 결과 출력