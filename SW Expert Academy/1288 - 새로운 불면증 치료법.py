T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())

    checkSet = {str(i): 0 for i in range(10)}
    checkNum = 0

    multiCnt = 1
    while checkNum < 10:
        strNums = list(str(N * multiCnt))

        for i in strNums:
            if checkSet[i] == 0:
                checkSet[i] = 1
                checkNum += 1

        multiCnt += 1

    print(f"#{t} {N * (multiCnt-1)}")
