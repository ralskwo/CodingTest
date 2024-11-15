T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    tmp = []
    for _ in range(N):
        test_case = input().split()

        tmp.append(test_case[0] * int(test_case[1]))

    res = "".join(tmp)

    print(f"#{t}")

    split = len(res) // 10
    for i in range(split):
        print(res[10 * i : 10 * (i + 1)])

    if len(res) % 10 > 0:
        print(res[10 * split :])
