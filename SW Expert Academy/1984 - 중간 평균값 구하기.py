T = int(input().strip())

for t in range(1, T+1):
    arr = sorted(list(map(int, input().strip().split())))
    arr2 = arr[1:len(arr)-1]
    rounded = round(sum(arr2)/len(arr2))

    print(f"#{t} {rounded}")