A, B = map(int, input().split())

rsp = {1:2, 2:3, 3:1}
if rsp[A] == B:
    print('B')
else:
    print('A')