def find_direction(x1, y1, x2, y2, x3, y3):  # 세 점의 좌표를 받아 방향을 계산하는 함수 정의
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)  # 벡터 P1P2와 P2P3의 외적을 계산

    if cross_product > 0:  # 외적 값이 양수면 반시계 방향
        return 1  # 반시계 방향인 경우 1을 반환
    elif cross_product < 0:  # 외적 값이 음수면 시계 방향
        return -1  # 시계 방향인 경우 -1을 반환
    else:  # 외적 값이 0이면 일직선 상에 있는 경우
        return 0  # 일직선인 경우 0을 반환

x1, y1 = map(int, input().split())  # 첫 번째 점 P1의 좌표를 입력받아 x1, y1에 저장
x2, y2 = map(int, input().split())  # 두 번째 점 P2의 좌표를 입력받아 x2, y2에 저장
x3, y3 = map(int, input().split())  # 세 번째 점 P3의 좌표를 입력받아 x3, y3에 저장

print(find_direction(x1, y1, x2, y2, x3, y3))  # 세 점의 방향을 계산한 결과를 출력