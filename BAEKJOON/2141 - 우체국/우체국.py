# 시스템 관련 입력/출력 모듈 가져오기
import sys


# 우체국 최적 위치를 찾는 함수 정의 (마을 개수와 마을 정보를 입력받음)
def find_post_office_location(N, villages):
    # 마을들을 x 좌표 기준으로 정렬
    villages.sort(key=lambda x: x[0])

    # 전체 마을 인구 계산
    total_population = sum(village[1] for village in villages)

    # 현재까지의 누적 인구 초기화
    current_population = 0

    # 정렬된 마을 리스트를 순회
    for i, (x, people) in enumerate(villages):
        # 현재 마을의 인구를 누적 인구에 추가
        current_population += people

        # 누적 인구가 전체 인구의 절반 이상이 되면
        if current_population >= (total_population + 1) // 2:
            # 해당 마을의 x 좌표를 우체국 위치로 반환
            return x

    # 예외적인 경우 첫 번째 마을의 위치 반환
    return villages[0][0]


# 마을의 개수 입력
N = int(sys.stdin.readline().strip())

# 마을 정보를 저장할 리스트 초기화
villages = []

# N개의 마을 정보 입력 받기 (x 좌표와 인구)
for _ in range(N):
    # 한 줄을 입력받아 x 좌표와 인구로 분리
    x, people = map(int, sys.stdin.readline().split())
    # 마을 정보를 리스트에 추가
    villages.append((x, people))

# 우체국 최적 위치 계산 및 출력
print(find_post_office_location(N, villages))
