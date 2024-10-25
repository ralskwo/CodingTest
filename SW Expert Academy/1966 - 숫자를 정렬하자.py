T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f"#{t} {' '.join([str(i) for i in sorted(list(map(int, input().strip().split())))])}")