T = int(input().strip())

for t in range(1, T+1):
    N, M = map(int, input().strip().split())

    A = list(map(int, input().strip().split()))    
    B = list(map(int, input().strip().split()))
    
    gap = abs(len(B)-len(A))
    maxes = []

    for i in range(gap+1):
        sums = 0
        
        if len(A)< len(B):
            for j in range(N):
                sums += A[j] * B[i+j]
        else:
            for j in range(M):
                sums += B[j] * A[i+j]

        maxes.append(sums)

    print(f"#{t} {max(maxes)}")