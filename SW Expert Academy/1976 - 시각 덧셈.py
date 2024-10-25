T = int(input().strip())

for t in range(1, T+1):
    hour1, min1, hour2, min2 = map(int, input().strip().split())
    afterRound = 12*60

    time = hour1*60 + min1 +hour2* 60 + min2
    
    if time>afterRound:
        time-=afterRound
    
    curHour = time//60
    curMin = time%60

    print(f"#{t} {curHour} {curMin}")