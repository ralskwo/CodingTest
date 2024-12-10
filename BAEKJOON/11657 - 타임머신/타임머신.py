import sys
from collections import defaultdict


# 벨만-포드 알고리즘 구현 함수
def bellman_ford(n, edges, start):
    INF = float("inf")  # 무한대를 나타내는 상수 설정
    distance = [INF] * (n + 1)  # 모든 도시의 최단 거리를 무한대로 초기화
    distance[start] = 0  # 시작 도시의 거리를 0으로 설정

    # 모든 도시를 최대 n-1번 순회하며 거리 갱신
    for i in range(n):
        for u, v, cost in edges:  # 각 간선을 확인
            if distance[u] != INF and distance[u] + cost < distance[v]:
                distance[v] = distance[u] + cost  # 최단 거리 갱신
                if i == n - 1:  # n번째 순회에서 갱신이 발생하면 음수 사이클 존재
                    return -1

    return distance  # 모든 도시로의 최단 거리 배열 반환


# 메인 함수
def main():
    input = sys.stdin.read  # 표준 입력 읽기
    data = input().splitlines()  # 입력 데이터를 줄 단위로 나누기

    n, m = map(int, data[0].split())  # 도시 개수 n과 버스 노선 개수 m 읽기
    edges = []  # 간선 정보를 저장할 리스트

    for i in range(1, m + 1):  # 각 버스 노선의 정보를 읽어들임
        a, b, c = map(int, data[i].split())  # 시작 도시 a, 도착 도시 b, 비용 c
        edges.append((a, b, c))  # 간선 정보를 리스트에 추가

    result = bellman_ford(n, edges, 1)  # 1번 도시에서 출발하여 최단 거리 계산

    if result == -1:  # 음수 사이클이 존재하는 경우
        print(-1)  # -1 출력
    else:
        for dist in result[2:]:  # 2번 도시부터 n번 도시까지 최단 거리 확인
            if dist == float("inf"):  # 도달할 수 없는 경우
                print(-1)  # -1 출력
            else:
                print(dist)  # 최단 거리 출력


# 프로그램의 시작점
if __name__ == "__main__":
    main()
