numbers = input().split()

joinNums = ''.join(numbers)

if joinNums == '12345678':
    print('ascending')
elif joinNums == '87654321':
    print('descending')
else:
    print('mixed')