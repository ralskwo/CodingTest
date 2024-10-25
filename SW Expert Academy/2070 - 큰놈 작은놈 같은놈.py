T = int(input())

for t in range(1, T+1):
    X, Y = map(int, input().split())
    s=''
    if X>Y:
        s = '>'
    elif X<Y:
        s = '<'
    else:
        s= '='

    print(f"#{t} {s}")