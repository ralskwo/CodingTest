import sys
input = sys.stdin.read
INF = float('inf')

# 플로이드-워셜 알고리즘을 구현하는 함수
def floyd_warshall(n, bus_info):
    # 초기 거리를 무한대로 설정한 n x n 크기의 2차원 배열 생성
    dist = [[INF] * n for _ in range(n)]
    # 경로를 추적하기 위한 n x n 크기의 2차원 배열 생성
    next_city = [[-1] * n for _ in range(n)]
    
    # 모든 도시에서 자기 자신으로 가는 비용은 0으로 설정
    for i in range(n):
        dist[i][i] = 0
    
    # 주어진 버스 정보로 dist와 next_city 초기화
    for a, b, c in bus_info:
        # 시작 도시 a에서 도착 도시 b로 가는 비용이 더 적으면 업데이트
        if c < dist[a-1][b-1]:
            dist[a-1][b-1] = c
            next_city[a-1][b-1] = b-1
    
    # 플로이드-워셜 알고리즘 수행: 모든 도시 쌍 간의 최단 경로 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i에서 j로 바로 가는 경로보다 i를 거쳐 k를 통해 j로 가는 경로가 더 짧으면 갱신
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    # 경로를 갱신할 때 next_city 배열도 함께 갱신
                    next_city[i][j] = next_city[i][k]
    
    # 최종적으로 모든 도시 쌍 간의 최단 경로 비용(dist)과 경로(next_city)를 반환
    return dist, next_city

# 경로를 재구성하는 함수
def construct_path(next_city, start, end):
    # start에서 end로 가는 경로가 없으면 빈 리스트 반환
    if next_city[start][end] == -1:
        return []
    # 경로를 저장할 리스트 생성
    path = [start]
    # 다음 도시가 끝 도시와 같아질 때까지 경로를 따라감
    while start != end:
        start = next_city[start][end]
        path.append(start)
    # 완성된 경로 리스트 반환
    return path

# 메인 함수
def main():
    # 입력 데이터를 모두 읽어옴
    data = input().strip().split('\n')
    # 첫 번째 줄에서 도시의 개수 n을 읽어옴
    n = int(data[0])
    # 두 번째 줄에서 버스의 개수 m을 읽어옴
    m = int(data[1])
    # 버스 정보를 저장할 리스트 생성
    bus_info = []
    
    # 세 번째 줄부터 m개의 버스 정보를 읽어옴
    for i in range(2, 2 + m):
        a, b, c = map(int, data[i].split())
        bus_info.append((a, b, c))
    
    # 플로이드-워셜 알고리즘을 통해 최단 경로와 경로를 계산
    dist, next_city = floyd_warshall(n, bus_info)
    
    # 모든 도시 쌍 간의 최단 경로 비용을 출력
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print(0, end=" ")  # 경로가 없는 경우 0 출력
            else:
                print(dist[i][j], end=" ")  # 최단 경로 비용 출력
        print()
    
    # 모든 도시 쌍 간의 최단 경로를 출력
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print(0)  # 경로가 없는 경우 0 출력
            else:
                path = construct_path(next_city, i, j)
                print(len(path), ' '.join(map(lambda x: str(x + 1), path)))  # 경로의 도시 개수와 경로 출력

# 프로그램의 시작점
if __name__ == "__main__":
    main()
