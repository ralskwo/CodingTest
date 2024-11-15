T = int(input().strip())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    first = P * W
    second = 0

    if W <= R:
        second = Q
    else:
        diff = W - R
        second = Q + diff * S

    print(f"#{t} {min(first, second)}")
