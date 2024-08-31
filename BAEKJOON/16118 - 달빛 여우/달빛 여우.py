import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 가져옵니다.
import sys  # 입력 속도를 빠르게 하기 위해 sys 모듈을 가져옵니다.
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
INF = float('inf')  # 무한대를 나타내기 위해 INF를 정의합니다.

def dijkstra_fox(n, adj):
    dist = [INF] * (n + 1)  # 각 그루터기까지의 최단 거리를 저장할 배열을 초기화합니다.
    dist[1] = 0  # 시작점인 1번 그루터기의 거리는 0으로 설정합니다.
    pq = [(0, 1)]  # 우선순위 큐에 (거리, 그루터기 번호) 형식으로 초기 상태를 추가합니다.
    
    while pq:  # 우선순위 큐가 빌 때까지 반복합니다.
        current_dist, u = heapq.heappop(pq)  # 가장 작은 거리를 가진 그루터기를 꺼냅니다.
        if current_dist > dist[u]:  # 이미 처리된 거리보다 크다면 무시합니다.
            continue
        for v, length in adj[u]:  # 현재 그루터기 u와 연결된 모든 인접 그루터기를 탐색합니다.
            new_dist = current_dist + length  # 새로운 경로의 거리를 계산합니다.
            if new_dist < dist[v]:  # 계산된 거리가 기존 거리보다 짧다면 갱신합니다.
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))  # 갱신된 거리를 우선순위 큐에 추가합니다.
    
    return dist  # 모든 그루터기에 대한 최단 거리를 반환합니다.

def dijkstra_wolf(n, adj):
    dist = [[INF, INF] for _ in range(n + 1)]  # 늑대의 두 가지 상태에 따른 최단 거리를 저장할 배열을 초기화합니다.
    dist[1][0] = 0  # 시작점에서 빠르게 출발하는 상태의 거리는 0으로 설정합니다.
    pq = [(0, 1, 0)]  # 우선순위 큐에 (거리, 그루터기 번호, 현재 속도 상태) 형식으로 초기 상태를 추가합니다.
    
    while pq:  # 우선순위 큐가 빌 때까지 반복합니다.
        current_dist, u, speed_state = heapq.heappop(pq)  # 가장 작은 거리를 가진 상태를 꺼냅니다.
        if current_dist > dist[u][speed_state]:  # 이미 처리된 거리보다 크다면 무시합니다.
            continue
        for v, length in adj[u]:  # 현재 그루터기 u와 연결된 모든 인접 그루터기를 탐색합니다.
            if speed_state == 0:  # 현재 상태가 빠르게 이동하는 상태인 경우
                new_dist = current_dist + length / 2  # 새로운 거리를 계산(절반 속도로 이동)
                if new_dist < dist[v][1]:  # 느리게 이동하는 상태에서의 거리와 비교하여 갱신
                    dist[v][1] = new_dist
                    heapq.heappush(pq, (new_dist, v, 1))  # 갱신된 거리를 우선순위 큐에 추가합니다.
            else:  # 현재 상태가 느리게 이동하는 상태인 경우
                new_dist = current_dist + length * 2  # 새로운 거리를 계산(두 배 속도로 이동)
                if new_dist < dist[v][0]:  # 빠르게 이동하는 상태에서의 거리와 비교하여 갱신
                    dist[v][0] = new_dist
                    heapq.heappush(pq, (new_dist, v, 0))  # 갱신된 거리를 우선순위 큐에 추가합니다.
    
    return dist  # 모든 그루터기에 대한 늑대의 두 가지 상태에서의 최단 거리를 반환합니다.

def count_fox_faster(n, dist_fox, dist_wolf):
    count = 0  # 여우가 더 빨리 도착할 수 있는 그루터기의 수를 세기 위한 변수를 초기화합니다.
    for i in range(2, n + 1):  # 2번 그루터기부터 n번 그루터기까지 순회합니다.
        if dist_fox[i] < min(dist_wolf[i][0], dist_wolf[i][1]):  # 여우의 최단 거리가 늑대의 두 상태에서의 최단 거리보다 짧다면
            count += 1  # 해당 그루터기를 카운트합니다.
    return count  # 최종적으로 카운트된 그루터기의 수를 반환합니다.

def main():
    n, m = map(int, input().split())  # 그루터기의 개수와 오솔길의 개수를 입력받습니다.
    adj = [[] for _ in range(n + 1)]  # 인접 리스트를 초기화합니다.
    
    for _ in range(m):
        a, b, d = map(int, input().split())  # 각 오솔길의 정보를 입력받습니다.
        adj[a].append((b, d))  # 그루터기 a에서 b로 가는 오솔길을 추가합니다.
        adj[b].append((a, d))  # 그루터기 b에서 a로 가는 오솔길을 추가합니다 (양방향).

    dist_fox = dijkstra_fox(n, adj)  # 여우의 최단 거리를 계산합니다.
    dist_wolf = dijkstra_wolf(n, adj)  # 늑대의 최단 거리를 계산합니다.
    result = count_fox_faster(n, dist_fox, dist_wolf)  # 여우가 더 빨리 도착할 수 있는 그루터기의 수를 계산합니다.
    
    print(result)  # 계산된 결과를 출력합니다.

if __name__ == "__main__":
    main()  # 메인 함수 호출을 통해 프로그램을 실행합니다.
