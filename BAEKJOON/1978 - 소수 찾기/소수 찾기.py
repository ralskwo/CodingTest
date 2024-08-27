def sieve_of_eratosthenes(max_num):
    sieve = [True] * (max_num + 1)  # 0부터 max_num까지 True로 초기화된 리스트를 생성 (모든 수를 소수로 가정)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니므로 False로 설정

    for i in range(2, int(max_num ** 0.5) + 1):  # 2부터 max_num의 제곱근까지 반복
        if sieve[i]:  # i가 소수인 경우
            for j in range(i * i, max_num + 1, i):  # i의 배수들을 False로 설정
                sieve[j] = False
    
    return sieve  # 소수 여부를 나타내는 리스트를 반환

def count_primes(numbers, sieve):
    count = 0  # 소수의 개수를 세기 위한 변수
    for num in numbers:  # 입력된 수들을 하나씩 확인
        if sieve[num]:  # 해당 수가 소수인 경우
            count += 1  # 소수 개수 증가
    return count  # 소수의 총 개수를 반환

N = int(input())  # 입력된 수의 개수 N을 입력받음
numbers = list(map(int, input().split()))  # N개의 수를 리스트로 입력받음

max_num = 1000  # 문제에서 주어진 수의 최대값 1000
sieve = sieve_of_eratosthenes(max_num)  # 1000 이하의 소수를 구하기 위해 에라토스테네스의 체를 사용

prime_count = count_primes(numbers, sieve)  # 입력된 수들 중 소수의 개수를 계산

print(prime_count)  # 소수의 개수를 출력
