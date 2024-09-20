import math  # 수학 관련 함수를 사용하기 위해 math 모듈을 불러옴

def gcd(a, b):  # 두 수의 최대 공약수를 구하는 함수
    while b:  # b가 0이 될 때까지 반복
        a, b = b, a % b  # a에 b를 대입하고 b에 a를 b로 나눈 나머지를 대입
    return a  # b가 0이 되면 a가 최대 공약수이므로 반환

def find_divisors(num):  # num의 약수를 찾는 함수
    divisors = []  # 약수를 저장할 리스트 생성
    for i in range(2, int(math.sqrt(num)) + 1):  # 2부터 num의 제곱근까지 반복
        if num % i == 0:  # i가 num의 약수인지 확인
            divisors.append(i)  # i를 약수 리스트에 추가
            if i != num // i:  # i가 num의 제곱근이 아닌 경우
                divisors.append(num // i)  # num을 i로 나눈 값도 약수 리스트에 추가
    divisors.append(num)  # num 자체도 약수이므로 리스트에 추가
    return sorted(divisors)  # 약수를 오름차순으로 정렬하여 반환

n = int(input())  # 숫자의 개수를 입력받음
numbers = [int(input()) for _ in range(n)]  # 입력된 숫자들을 리스트로 저장

numbers.sort()  # 숫자들을 오름차순으로 정렬

g = numbers[1] - numbers[0]  # 첫 번째와 두 번째 숫자의 차이를 g로 설정
for i in range(2, n):  # 나머지 숫자들에 대해 반복
    g = gcd(g, numbers[i] - numbers[i - 1])  # 이전까지의 차이와 새로운 차이의 최대 공약수를 구함

result = find_divisors(g)  # g의 약수들을 구하여 result에 저장

print(" ".join(map(str, result)))  # 약수들을 공백으로 구분하여 출력
