T = int(input().strip())

for t in range(1, T + 1):
    N, K = map(int, input().strip().split())
    puzzle = [list(map(int, input().strip().split())) for _ in range(N)]
    
    count = 0

    # 가로 방향 탐색
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    count += 1
                length = 0
        # 줄 끝에 도달했을 때도 길이 체크
        if length == K:
            count += 1

    # 세로 방향 탐색
    for j in range(N):
        length = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    count += 1
                length = 0
        # 줄 끝에 도달했을 때도 길이 체크
        if length == K:
            count += 1

    print(f"#{t} {count}")