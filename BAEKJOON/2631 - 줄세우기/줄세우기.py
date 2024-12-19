import bisect  # bisect 모듈을 불러옵니다. 이진 탐색을 활용해 LIS를 계산할 때 사용됩니다.

# 입력 받기
n = int(input())  # 첫 번째 줄에서 아이들의 수 N을 입력받습니다.
children = [
    int(input()) for _ in range(n)
]  # 두 번째 줄부터 N개의 숫자를 리스트에 저장합니다.

# LIS 계산
lis = []  # LIS를 저장할 리스트를 초기화합니다.
for num in children:  # 모든 아이들의 번호를 순회합니다.
    pos = bisect.bisect_left(
        lis, num
    )  # 현재 번호가 LIS 리스트에 삽입될 위치를 찾습니다.
    if pos == len(lis):  # 위치가 LIS 리스트의 끝이라면
        lis.append(num)  # 현재 번호를 LIS 리스트에 추가합니다.
    else:  # 그렇지 않다면
        lis[pos] = num  # 기존 값을 현재 번호로 업데이트하여 LIS 리스트를 유지합니다.

# 움직여야 하는 최소 아이들의 수 계산
min_moves = n - len(
    lis
)  # 전체 아이들의 수에서 LIS 길이를 빼서 이동해야 하는 최소 아이들의 수를 계산합니다.
print(min_moves)  # 계산된 최소 이동 수를 출력합니다.
