T = int(input().strip())

for t in range(1, T + 1):
    N, M = map(int, input().strip().split())
    board = []
    for _ in range(N):
        tmp = list(map(int, input().strip().split()))
        board.append(tmp)
    
    maxFly = 0

    # 파리채의 시작점을 모든 가능한 위치에서 시도
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            stamp = 0
            # M x M 영역의 파리 수를 합산
            for i in range(M):
                for j in range(M):
                    stamp += board[x + i][y + j]
            # 최댓값 갱신
            maxFly = max(maxFly, stamp)

    print(f"#{t} {maxFly}")
