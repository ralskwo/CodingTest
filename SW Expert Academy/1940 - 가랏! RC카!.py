T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())

    curSpeed = 0
    total_distance = 0

    for _ in range(N):
        commands = list(map(int, input().split()))

        if commands[0] == 1:
            curSpeed += commands[1]
        elif commands[0] == 2:
            curSpeed -= commands[1]

        if curSpeed < 0:
            curSpeed = 0

        total_distance += curSpeed

    print(f"#{t} {total_distance}")
