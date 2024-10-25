T = int(input())

for t in range(1, T+1):
    str30 = input()
    slen = 1

    while True:
        if str30[0:slen] == str30[slen:slen*2]:
            print(f"#{t} {slen}")
            break
        else:
            slen+=1