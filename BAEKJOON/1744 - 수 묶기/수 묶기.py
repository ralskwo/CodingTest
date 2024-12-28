def max_sequence_sum(nums):
    positive = []  # 양수를 저장할 리스트
    negative = []  # 음수와 0을 저장할 리스트
    result = 0  # 최종 결과를 저장할 변수

    for num in nums:  # 입력 받은 숫자들을 하나씩 확인
        if num > 1:  # 1보다 큰 양수는 positive 리스트에 추가
            positive.append(num)
        elif num == 1:  # 1은 묶지 않고 결과에 바로 더함
            result += 1
        else:  # 0과 음수는 negative 리스트에 추가
            negative.append(num)

    positive.sort(reverse=True)  # 양수는 큰 것부터 곱하기 위해 내림차순 정렬
    negative.sort()  # 음수는 작은 것부터 곱하기 위해 오름차순 정렬

    i = 0  # 양수 리스트의 인덱스를 관리할 변수
    while i < len(positive) - 1:  # 두 개씩 묶어서 곱하기
        result += (
            positive[i] * positive[i + 1]
        )  # 양수 두 개를 묶어 곱한 값을 결과에 추가
        i += 2  # 두 개씩 묶었으므로 인덱스를 2 증가시킴
    if i < len(positive):  # 묶지 못하고 남은 양수가 있으면 그대로 더하기
        result += positive[i]

    i = 0  # 음수 리스트의 인덱스를 관리할 변수
    while i < len(negative) - 1:  # 두 개씩 묶어서 곱하기
        result += (
            negative[i] * negative[i + 1]
        )  # 음수 두 개를 묶어 곱한 값을 결과에 추가
        i += 2  # 두 개씩 묶었으므로 인덱스를 2 증가시킴
    if i < len(negative):  # 묶지 못하고 남은 음수가 있으면
        if 0 in nums:  # 0이 있을 경우, 음수와 0을 묶어 결과에 0을 더함 (음수 상쇄)
            result += 0
        else:  # 0이 없으면 남은 음수를 결과에 그대로 더함
            result += negative[i]

    return result  # 최종 결과 반환


n = int(input())  # 수열의 크기 입력
nums = [int(input()) for _ in range(n)]  # 수열의 각 수를 입력 받아 리스트에 저장
print(max_sequence_sum(nums))  # 최종 결과 출력
