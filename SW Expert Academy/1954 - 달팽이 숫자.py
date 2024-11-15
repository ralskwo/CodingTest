T = int(input().strip())

for t in range(1, T+1):
    N = int(input().strip())
    snail = [[0] * N for _ in range(N)]
    res = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    dir = 0
    num = 1

    while num <= N * N:
        snail[x][y] = num
        num += 1

        nx, ny = x + dx[dir], y + dy[dir]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            dir = (dir + 1) % 4

            nx = x + dx[dir]
            ny = y + dy[dir]

        x, y = nx, ny

    res.append(f"#{t}")

    for row in snail:
        res.append(" ".join(map(str, row)))

    print("\n".join(res))
