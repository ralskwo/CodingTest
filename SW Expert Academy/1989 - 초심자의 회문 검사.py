T = int(input().strip())

for t in range(1, T+1):
    string = input()
    x, y = '', ''
    if len(string)%2 ==0:
        mid = len(string)//2    
        x, y = string[:mid], "".join(reversed(string[mid:]))
    else:
        mid = len(string)//2+1
        x, y = string[:mid], "".join(reversed(string[mid-1:]))

    answer = 0
    if x == y: 
        answer = 1
    print(f"#{t} {answer}")