def count_digits(n):
    # n이 0 이하일 경우 0부터 9까지의 숫자 등장 횟수는 모두 0이므로 [0] * 10 리스트를 반환
    if n <= 0:
        return [0] * 10

    # n을 문자열로 변환하여 자리수를 계산
    str_n = str(n)
    length = len(str_n)
    
    # 각 숫자(0~9)의 등장 횟수를 저장할 리스트를 초기화
    counts = [0] * 10

    # n의 각 자리수에 대해 등장 빈도를 계산
    for i in range(length):
        # 현재 자리의 숫자를 정수형으로 변환하여 저장
        curr = int(str_n[i])
        
        # 현재 자리의 자릿값을 계산 (예: 천의 자리면 1000)
        place_value = 10 ** (length - i - 1)

        # 현재 자릿수보다 앞의 모든 완전한 세트의 숫자 등장 횟수를 계산
        for digit in range(10):
            counts[digit] += (n // (place_value * 10)) * place_value

        # 현재 자리의 숫자보다 작은 숫자들이 해당 자릿수에서 몇 번 등장하는지 계산
        for digit in range(curr):
            counts[digit] += place_value

        # 현재 자릿수의 숫자가 현재 자릿값만큼 등장하는 횟수를 더해줌
        counts[curr] += (n % place_value) + 1

        # 0은 맨 앞자리에 올 수 없기 때문에, 0의 등장 횟수를 보정
        counts[0] -= place_value

    # 0부터 9까지의 숫자가 1부터 n까지 몇 번 등장했는지 리스트로 반환
    return counts

# 사용자로부터 숫자 n을 입력받음
N = int(input())

# 입력받은 n에 대해 0부터 9까지의 숫자 등장 횟수를 계산하여 result에 저장
result = count_digits(N)

# 결과를 공백으로 구분하여 출력
print(*result)