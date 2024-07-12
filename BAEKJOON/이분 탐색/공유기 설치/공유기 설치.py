# 입력 처리
import sys  # 시스템 관련 모듈을 가져옴
input = sys.stdin.read  # 표준 입력으로부터 모든 데이터를 읽어옴
data = input().split()  # 입력 데이터를 공백을 기준으로 나누어 리스트로 변환

# 집의 개수 N과 공유기의 개수 C를 입력받음
N = int(data[0])  # 첫 번째 값은 집의 개수
C = int(data[1])  # 두 번째 값은 공유기의 개수
# 나머지 값들은 집의 좌표
houses = [int(data[i]) for i in range(2, 2 + N)]  # 각 집의 좌표를 리스트로 저장

# 좌표 정렬
houses.sort()  # 집의 좌표를 오름차순으로 정렬

# 이분 탐색을 위한 초기 값 설정
low = 1  # 가능한 최소 거리
high = houses[-1] - houses[0]  # 가능한 최대 거리 (첫 번째 집과 마지막 집 사이의 거리)

def can_place_routers(distance):
    """
    주어진 거리(distance)로 공유기를 설치할 수 있는지 확인하는 함수
    """
    count = 1  # 첫 번째 집에 공유기를 설치했으므로 설치한 공유기 수는 1
    last_installed = houses[0]  # 첫 번째 집에 공유기를 설치

    for i in range(1, N):
        if houses[i] - last_installed >= distance:  # 현재 집과 마지막 설치한 집의 거리가 주어진 거리 이상이면
            count += 1  # 공유기를 설치하고
            last_installed = houses[i]  # 마지막 설치 위치를 현재 집으로 갱신
            if count == C:  # 만약 설치한 공유기 수가 C와 같아지면
                return True  # 공유기 설치 가능
    return False  # 주어진 거리로는 공유기 설치 불가능

# 이분 탐색
result = 0  # 최적의 거리를 저장할 변수
while low <= high:
    mid = (low + high) // 2  # 중간 값을 계산
    if can_place_routers(mid):  # 중간 값 거리로 공유기 설치가 가능한지 확인
        result = mid  # 가능하면 결과를 갱신
        low = mid + 1  # 최소 거리를 늘려본다
    else:
        high = mid - 1  # 불가능하면 최대 거리를 줄인다

# 결과 출력
print(result)  # 최적의 거리 출력
