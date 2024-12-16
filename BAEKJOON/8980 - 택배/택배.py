def max_boxes_delivered(n, c, box_info):
    # 박스 정보를 받는 마을 번호 기준으로 오름차순 정렬
    box_info.sort(key=lambda x: x[1])

    # 각 마을에 실린 박스 개수를 관리할 배열 초기화
    deliveries = [0] * (n + 1)

    # 최종 배송한 박스의 총 개수를 저장하는 변수
    total_delivered = 0

    # 각 박스 정보를 순회하며 최대한 많은 박스를 배송
    for start, end, boxes in box_info:
        # 현재 구간에서 트럭에 실을 수 있는 최대 박스 수 계산
        max_capacity = min(c - max(deliveries[start:end]), boxes)

        # 구간 내 각 마을에 적재된 박스 개수를 업데이트
        for i in range(start, end):
            deliveries[i] += max_capacity

        # 누적 배송된 박스 수를 갱신
        total_delivered += max_capacity

    # 최종 배송된 박스 수 반환
    return total_delivered


# 입력값으로 마을 수 N과 트럭 용량 C를 읽어옴
n, c = map(int, input().split())

# 박스 정보의 개수 M을 입력받음
m = int(input())

# 박스 정보를 입력받아 리스트로 저장
box_info = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(max_boxes_delivered(n, c, box_info))
