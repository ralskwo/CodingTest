days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

T = int(input())

for t in range(1, T + 1):
    date_str = input().strip()

    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])

    if month in days_in_month and 1 <= day <= days_in_month[month]:
        print(f"#{t} {year:04d}/{month:02d}/{day:02d}")
    else:
        print(f"#{t} -1")
