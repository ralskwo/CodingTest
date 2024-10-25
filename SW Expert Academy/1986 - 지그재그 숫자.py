T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    result = 0

    # 1부터 N까지 순회하며 홀수는 더하고, 짝수는 뺀다.
    for i in range(1, N + 1):
        if i % 2 == 1:
            result += i  # 홀수는 더함
        else:
            result -= i  # 짝수는 뺌

    print(f"#{t} {result}")