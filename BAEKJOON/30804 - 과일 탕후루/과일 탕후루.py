def max_fruit_length(N, fruits):
    from collections import (
        defaultdict,
    )  # 딕셔너리를 기본값으로 초기화하는 defaultdict를 임포트

    fruit_count = defaultdict(int)  # 과일의 종류와 개수를 저장할 딕셔너리 생성
    left = 0  # 슬라이딩 윈도우의 시작 위치를 나타내는 포인터
    max_length = 0  # 최대 과일 길이를 저장할 변수

    for right in range(N):  # 슬라이딩 윈도우의 끝 위치를 나타내는 포인터를 N까지 순회
        fruit_count[fruits[right]] += 1  # 현재 과일을 딕셔너리에 추가하고 개수를 증가

        while len(fruit_count) > 2:  # 윈도우 내 과일 종류가 2개를 초과하면
            fruit_count[fruits[left]] -= 1  # 왼쪽 포인터의 과일 개수를 감소
            if fruit_count[fruits[left]] == 0:  # 과일 개수가 0이 되면 딕셔너리에서 삭제
                del fruit_count[fruits[left]]
            left += 1  # 왼쪽 포인터를 오른쪽으로 이동하여 윈도우 크기를 줄임

        max_length = max(
            max_length, right - left + 1
        )  # 현재 윈도우 길이와 최대 길이를 비교하여 갱신

    return max_length  # 최종적으로 가장 긴 윈도우 길이를 반환


N = int(input())  # 과일 개수를 입력받음
fruits = list(map(int, input().split()))  # 과일 배열을 입력받음
print(max_fruit_length(N, fruits))  # 최대 과일 길이를 출력
