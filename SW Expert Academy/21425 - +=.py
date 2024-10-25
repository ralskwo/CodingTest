T = int(input().strip())

for _ in range(0, T):
    x, y, n = map(int, input().strip().split())
    print(x, y, n)
    cnt = 0
    
    while True:        
        cnt+=1
        if x < y:
            x+=y
        else:
            y+=x
        
        if x>n or y>n:
            break
    
    print(cnt)