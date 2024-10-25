N = int(input())

numbers = sorted(list(map(int, input().split())))
print(numbers[N//2])