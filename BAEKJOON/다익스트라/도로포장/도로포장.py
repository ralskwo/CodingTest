import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 임포트합니다.
import sys  # 표준 입력을 읽기 위해 sys 모듈을 임포트합니다.

# 최소 여행 시간을 계산하는 함수 정의
def minimum_travel_time(N, M, K, roads):
    # 그래프를 인접 리스트로 표현하기 위해 초기화합니다.
    graph = [[] for _ in range(N + 1)]
    
    # 주어진 도로 정보를 기반으로 그래프를 구성합니다.
    for u, v, w in roads:
        graph[u].append((v, w))  # 도시 u에서 v로 가는 도로와 시간을 추가합니다.
        graph[v].append((u, w))  # 도시 v에서 u로 가는 반대 방향 도로도 추가합니다.
    
    # 우선순위 큐를 사용하여 최단 경로를 계산합니다.
    # (시간, 현재 도시, 사용한 패치 수) 형태의 튜플을 저장합니다.
    pq = [(0, 1, 0)]  # 시작점 설정: (시간 0, 도시 1, 패치 수 0)
    
    # DP 테이블을 초기화합니다.
    # dp[u][k]는 도시 u까지 k개의 패치를 사용했을 때의 최소 시간을 의미합니다.
    dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    dp[1][0] = 0  # 출발지인 도시 1의 초기값을 0으로 설정합니다.
    
    # 우선순위 큐가 빌 때까지 반복합니다.
    while pq:
        time, u, k = heapq.heappop(pq)  # 우선순위 큐에서 현재 가장 짧은 시간의 요소를 추출합니다.
        
        # 현재 시간이 이미 기록된 시간보다 크면 무시합니다.
        if dp[u][k] < time:
            continue
        
        # 현재 도시 u와 연결된 모든 도시 v에 대해
        for v, w in graph[u]:
            # 도로를 패치할 경우
            if k < K and time < dp[v][k + 1]:
                dp[v][k + 1] = time  # 패치 후의 시간을 갱신합니다.
                heapq.heappush(pq, (time, v, k + 1))  # 우선순위 큐에 추가합니다.
            
            # 도로를 패치하지 않을 경우
            if time + w < dp[v][k]:
                dp[v][k] = time + w  # 시간을 갱신합니다.
                heapq.heappush(pq, (time + w, v, k))  # 우선순위 큐에 추가합니다.
    
    # 도시 N에 도달하는 최소 시간을 반환합니다.
    return min(dp[N])

# 입력을 읽습니다.
input = sys.stdin.read
data = input().split()  # 입력 데이터를 공백으로 분리합니다.
N = int(data[0])  # 첫 번째 값은 도시의 수입니다.
M = int(data[1])  # 두 번째 값은 도로의 수입니다.
K = int(data[2])  # 세 번째 값은 패치할 수 있는 최대 도로 수입니다.

# 도로 정보를 읽습니다.
roads = []
index = 3  # 도로 정보는 네 번째 요소부터 시작합니다.
for _ in range(M):
    u = int(data[index])  # 도로의 시작 도시를 읽습니다.
    v = int(data[index+1])  # 도로의 도착 도시를 읽습니다.
    w = int(data[index+2])  # 도로의 시간을 읽습니다.
    roads.append((u, v, w))  # 도로 정보를 리스트에 추가합니다.
    index += 3  # 다음 도로 정보를 가리킵니다.

# 최소 여행 시간을 계산합니다.
result = minimum_travel_time(N, M, K, roads)
# 결과를 출력합니다.
print(result)
