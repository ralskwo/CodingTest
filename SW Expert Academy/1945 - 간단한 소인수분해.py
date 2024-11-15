T = int(input().strip())

primes = [2, 3, 5, 7, 11]

for t in range(1, T + 1):
    N = int(input().strip())

    exp = []

    for p in primes:
        cnt = 0

        while N % p == 0:
            N //= p
            cnt += 1

        exp.append(cnt)

    print(f"#{t} {' '.join(map(str, exp))}")
