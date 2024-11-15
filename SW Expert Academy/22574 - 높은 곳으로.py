T = int(input().strip())

for t in range(1, T + 1):
    N, P = map(int, input().split())

    floor = 0
    flag = False
    for i in range(1, N + 1):
        if floor + i != P:
            floor += i
        else:
            floor += i
            flag = True

    print(floor if flag == False else floor - 1)
