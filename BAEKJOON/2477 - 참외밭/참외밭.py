K = int(input())  # 1m²당 자라는 참외의 개수를 입력 받음
directions = []  # 변의 방향을 저장할 리스트
lengths = []  # 변의 길이를 저장할 리스트

for _ in range(6):
    direction, length = map(int, input().split())  # 방향과 길이를 입력 받음
    directions.append(direction)  # 방향을 리스트에 추가
    lengths.append(length)  # 길이를 리스트에 추가

max_width = 0  # 가장 긴 가로 길이를 저장할 변수
max_height = 0  # 가장 긴 세로 길이를 저장할 변수
for i in range(6):
    if directions[i] == 1 or directions[i] == 2:  # 동쪽(1) 또는 서쪽(2) 방향
        if lengths[i] > max_width:  # 현재 길이가 기존의 가로 최대값보다 크면
            max_width = lengths[i]  # 가로 최대값을 갱신
    elif directions[i] == 3 or directions[i] == 4:  # 남쪽(3) 또는 북쪽(4) 방향
        if lengths[i] > max_height:  # 현재 길이가 기존의 세로 최대값보다 크면
            max_height = lengths[i]  # 세로 최대값을 갱신

small_width = 0  # 작은 직사각형의 가로 길이를 저장할 변수
small_height = 0  # 작은 직사각형의 세로 길이를 저장할 변수
for i in range(6):
    if directions[i] == 1 or directions[i] == 2:  # 동쪽(1) 또는 서쪽(2) 방향
        if lengths[(i+1) % 6] + lengths[(i-1) % 6] == max_height:  # 양 옆 변의 합이 세로 최대값과 같으면
            small_width = lengths[i]  # 작은 직사각형의 가로 길이로 설정
    elif directions[i] == 3 or directions[i] == 4:  # 남쪽(3) 또는 북쪽(4) 방향
        if lengths[(i+1) % 6] + lengths[(i-1) % 6] == max_width:  # 양 옆 변의 합이 가로 최대값과 같으면
            small_height = lengths[i]  # 작은 직사각형의 세로 길이로 설정

area = (max_width * max_height) - (small_width * small_height)  # 큰 직사각형에서 작은 직사각형의 면적을 빼서 전체 면적 계산

total_melons = area * K  # 전체 면적에 1m²당 참외의 개수를 곱해 총 참외 수 계산

print(total_melons)  # 결과 출력
