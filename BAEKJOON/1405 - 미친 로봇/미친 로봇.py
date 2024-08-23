def simple_path_probability(N, east, west, south, north):
    # 동, 서, 남, 북으로의 이동 확률을 각각 백분율에서 소수로 변환
    prob_east = east / 100
    prob_west = west / 100
    prob_south = south / 100
    prob_north = north / 100
    
    # 이동할 방향에 따른 좌표 변화 (동, 서, 남, 북)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    probs = [prob_east, prob_west, prob_south, prob_north]
    
    # 방문한 좌표를 추적하기 위한 세트
    visited = set()
    
    def dfs(x, y, n):
        # n번의 이동이 모두 완료된 경우, 단순 경로 하나를 찾은 것이므로 확률 1을 반환
        if n == 0:
            return 1.0
        # 현재 좌표를 방문한 좌표로 추가
        visited.add((x, y))
        prob = 0.0
        # 모든 방향에 대해 재귀적으로 이동 시도
        for (dx, dy), p in zip(directions, probs):
            nx, ny = x + dx, y + dy
            # 다음 좌표가 아직 방문하지 않은 경우에만 이동
            if (nx, ny) not in visited:
                prob += p * dfs(nx, ny, n - 1)
        # 현재 좌표를 방문한 좌표에서 제거 (백트래킹)
        visited.remove((x, y))
        return prob
    
    return dfs(0, 0, N)

# 입력 처리
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    east = int(data[1])
    west = int(data[2])
    south = int(data[3])
    north = int(data[4])
    
    # 결과 계산 및 출력
    result = simple_path_probability(N, east, west, south, north)
    print(f"{result:.10f}")
