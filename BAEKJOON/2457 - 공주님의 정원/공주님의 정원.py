import sys
input = sys.stdin.read
data = input().splitlines()  # 입력을 한 번에 받아 각 줄을 리스트로 저장

N = int(data[0])  # 첫 번째 줄에 있는 꽃의 개수 N을 정수로 변환하여 저장
flowers = []  # 꽃의 시작 날짜와 종료 날짜를 저장할 리스트

for i in range(1, N+1):  # 1번 인덱스부터 N번까지의 꽃의 정보들을 처리
    sm, sd, em, ed = map(int, data[i].split())  # 각 꽃의 시작 월, 시작 일, 종료 월, 종료 일을 정수로 변환
    start = sm * 100 + sd  # 시작 날짜를 MMDD 형식으로 변환 (예: 3월 8일 → 308)
    end = em * 100 + ed    # 종료 날짜를 MMDD 형식으로 변환 (예: 7월 31일 → 731)
    flowers.append((start, end))  # 변환된 시작일과 종료일을 flowers 리스트에 추가

flowers.sort(key=lambda x: (x[0], -x[1]))  # 시작 날짜를 기준으로 오름차순 정렬, 같은 시작일이면 종료일을 내림차순 정렬

START = 301  # 꽃이 피어야 하는 기간의 시작일 (3월 1일)을 MMDD 형식으로 설정
END = 1130   # 꽃이 피어야 하는 기간의 종료일 (11월 30일)을 MMDD 형식으로 설정

current_end = START  # 현재 커버할 수 있는 마지막 날짜를 START로 초기화 (처음에는 3월 1일부터 시작)
max_end = 0          # 선택된 꽃들이 커버할 수 있는 최대 종료 날짜
count = 0            # 선택된 꽃의 수
i = 0                # flowers 리스트의 인덱스를 추적할 변수

while i < N and current_end <= END:  # 모든 꽃을 순회하거나, 커버할 수 있는 날짜가 END를 넘어갈 때까지 반복
    while i < N and flowers[i][0] <= current_end:  # 현재 커버할 수 있는 날짜 이하에서 피는 꽃을 찾음
        max_end = max(max_end, flowers[i][1])  # 현재 꽃이 지는 날짜를 기준으로 가장 늦게 지는 꽃을 선택
        i += 1  # 다음 꽃으로 이동

    if max_end <= current_end:  # 만약 더 이상 커버할 수 있는 날짜를 연장할 수 없는 경우 (사각지대 발생)
        break  # 조건을 만족하지 못하므로 반복문 종료

    current_end = max_end  # 현재 커버 가능한 마지막 날짜를 갱신
    count += 1  # 꽃을 하나 선택했으므로 count 증가

if current_end <= END:  # 만약 커버한 마지막 날짜가 END보다 작다면 (즉, 11월 30일까지 도달하지 못하면)
    print(0)  # 두 조건을 만족하지 못하므로 0을 출력
else:
    print(count)  # 11월 30일까지 커버했다면 선택된 꽃의 개수 출력
