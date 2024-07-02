from collections import deque, defaultdict
import sys
input = sys.stdin.read

def acm_craft():
    # 표준 입력에서 모든 데이터를 읽어옵니다.
    data = input().strip().split()
    idx = 0
    T = int(data[idx])  # 테스트 케이스의 수
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])  # 건물의 수
        K = int(data[idx + 1])  # 규칙의 수
        idx += 2
        build_times = list(map(int, data[idx:idx + N]))  # 각 건물을 짓는 데 걸리는 시간
        idx += N
        
        rules = []
        for _ in range(K):
            X = int(data[idx])
            Y = int(data[idx + 1])
            rules.append((X, Y))  # 건설 순서 규칙 (X -> Y)
            idx += 2
        
        target = int(data[idx])  # 목표 건물
        idx += 1

        indegree = [0] * (N + 1)  # 각 건물의 진입 차수
        graph = defaultdict(list)  # 그래프 초기화
        time = [0] * (N + 1)  # 각 건물을 짓는 데 걸리는 시간 초기화
        
        # 각 건물의 건설 시간을 설정합니다.
        for i in range(1, N + 1):
            time[i] = build_times[i - 1]
        
        # 그래프를 구성하고 진입 차수를 설정합니다.
        for X, Y in rules:
            graph[X].append(Y)
            indegree[Y] += 1
        
        # Kahn의 알고리즘을 사용한 위상 정렬
        queue = deque()
        dp = [0] * (N + 1)  # 각 건물을 짓는 데 걸리는 최소 시간을 저장할 배열
        
        # 진입 차수가 0인 건물들을 큐에 추가하고, 초기 시간을 설정합니다.
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i]
        
        # 위상 정렬을 수행하면서 각 건물을 짓는 데 걸리는 최소 시간을 계산합니다.
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                dp[neighbor] = max(dp[neighbor], dp[current] + time[neighbor])
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 목표 건물을 짓는 데 걸리는 최소 시간을 결과 리스트에 추가합니다.
        results.append(dp[target])
    
    # 각 테스트 케이스의 결과를 출력합니다.
    for result in results:
        print(result)

if __name__ == "__main__":
    acm_craft()
