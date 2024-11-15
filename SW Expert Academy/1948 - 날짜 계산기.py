T = int(input().strip())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    if m1 == m2:
        print(f"#{t} {d2 - d1 + 1}")
    else:
        md1 = sum(month[:m1-1]) + d1
        md2 = sum(month[:m2-1]) + d2

        print(f"#{t} {md2 - md1 + 1}")
