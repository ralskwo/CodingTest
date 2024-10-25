N = int(input())

res = []
for i in range(1, N+1):
    if N % i ==0:
        res.append(i)

print(" ".join(map(str, res)))