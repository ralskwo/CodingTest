import sys

def tsp(n, W):
    # 상수 정의
    INF = sys.maxsize  # 무한대를 나타내기 위해 최대 정수를 사용
    
    # DP 테이블 초기화
    dp = [[INF] * (1 << n) for _ in range(n)]  # dp[i][mask]는 i번째 도시에 있고, mask 상태일 때의 최소 비용
    
    # 출발지에서 출발하는 비용은 0
    dp[0][1] = 0  # 첫 번째 도시에서 출발하는 비용은 0 (출발지는 항상 0번 도시)
    
    # 모든 도시 순회
    for mask in range(1 << n):  # 모든 가능한 방문 상태를 나타내는 비트마스크
        for i in range(n):  # 현재 도시
            if mask & (1 << i):  # 현재 비트마스크에서 i번째 도시를 방문했는지 확인
                for j in range(n):  # 다음 방문할 도시
                    if not (mask & (1 << j)) and W[i][j] != 0:  # j번째 도시를 방문하지 않았고, i에서 j로 가는 경로가 존재할 때
                        new_mask = mask | (1 << j)  # j번째 도시를 방문하는 새로운 비트마스크
                        # 새로운 상태로 갱신
                        dp[j][new_mask] = min(dp[j][new_mask], dp[i][mask] + W[i][j])  # i에서 j로 가는 비용을 추가하여 최소 비용 갱신
    
    # 모든 도시를 방문하고 출발지로 돌아오는 최소 비용 찾기
    min_cost = INF  # 최소 비용 초기화
    for i in range(1, n):  # 출발지(0번 도시)를 제외한 모든 도시에서 출발
        if W[i][0] != 0:  # i에서 출발지로 돌아오는 경로가 존재할 때
            min_cost = min(min_cost, dp[i][(1 << n) - 1] + W[i][0])  # 모든 도시를 방문하고 출발지로 돌아오는 최소 비용 갱신
    
    return min_cost  # 최종 최소 비용 반환

# 입력 받기
n = int(input())  # 도시의 수 입력
W = [list(map(int, input().split())) for _ in range(n)]  # 비용 행렬 입력

# TSP 문제 해결
result = tsp(n, W)  # 최소 비용 계산

# 결과 출력
print(result)  # 최소 비용 출력
