def count_blurays(lectures, size):
    count = 1  # 사용된 블루레이 개수를 세기 위한 변수. 최소 1개의 블루레이는 필요하므로 1로 초기화
    total = 0  # 현재 블루레이에 담긴 강의 길이 합을 저장하는 변수

    for lecture in lectures:  # 강의 목록을 순회하면서 각 강의를 블루레이에 담음
        if (
            total + lecture > size
        ):  # 현재 블루레이에 강의를 추가했을 때 블루레이 크기를 초과하는 경우
            count += 1  # 새로운 블루레이가 필요하므로 개수 증가
            total = lecture  # 새 블루레이에 현재 강의를 담음 (누적 합 초기화)
        else:
            total += lecture  # 크기를 초과하지 않으면 현재 블루레이에 강의를 추가

    return count  # 사용된 블루레이의 총 개수 반환


def find_minimum_bluray_size(n, m, lectures):
    left = max(lectures)  # 블루레이 크기의 최소값은 가장 긴 강의의 길이
    right = sum(
        lectures
    )  # 블루레이 크기의 최대값은 모든 강의를 하나의 블루레이에 담았을 때의 총합
    answer = (
        right  # 가능한 최소 블루레이 크기를 저장하는 변수. 초기값은 최대값으로 설정
    )

    while left <= right:  # 이분 탐색 시작
        mid = (left + right) // 2  # 중간값을 블루레이 크기로 설정
        if (
            count_blurays(lectures, mid) <= m
        ):  # 중간값 크기에서 필요한 블루레이 개수가 M 이하인 경우
            answer = (
                mid  # 가능한 블루레이 크기 중 더 작은 값을 찾기 위해 현재 값을 저장
            )
            right = mid - 1  # 블루레이 크기를 줄이기 위해 탐색 범위를 왼쪽으로 이동
        else:  # 중간값에서 필요한 블루레이 개수가 M보다 큰 경우
            left = mid + 1  # 블루레이 크기를 늘리기 위해 탐색 범위를 오른쪽으로 이동

    return answer  # 최종적으로 찾은 최소 블루레이 크기 반환


n, m = map(int, input().split())  # 강의의 개수 N과 블루레이 개수 M 입력
lectures = list(map(int, input().split()))  # 각 강의의 길이를 입력받아 리스트로 저장

print(find_minimum_bluray_size(n, m, lectures))  # 최소 블루레이 크기를 계산하고 출력
