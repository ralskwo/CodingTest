from itertools import combinations  # itertools의 combinations 함수를 import하여 조합을 생성하는 데 사용

def is_valid(password):
    # 주어진 password 조합이 유효한지 검사하는 함수
    vowels = {'a', 'e', 'i', 'o', 'u'}  # 모음 집합을 정의
    num_vowels = sum(1 for char in password if char in vowels)  # password 내 모음의 개수를 계산
    num_consonants = len(password) - num_vowels  # password 내 자음의 개수를 계산 (전체 길이에서 모음의 개수를 뺌)
    return num_vowels >= 1 and num_consonants >= 2  # 모음이 최소 1개 이상이고 자음이 최소 2개 이상이면 True 반환

def main():
    L, C = map(int, input().split())  # 첫 번째 줄에서 두 정수 L과 C를 입력받음
    chars = input().split()  # 두 번째 줄에서 C개의 문자를 공백으로 구분하여 입력받음
    chars.sort()  # 주어진 문자를 사전식으로 정렬
    
    possible_passwords = combinations(chars, L)  # 길이가 L인 모든 가능한 조합을 생성
    valid_passwords = [''.join(password) for password in possible_passwords if is_valid(password)]  
    # 각 조합에 대해 유효한지 검사하여 유효한 조합만 문자열로 변환하여 리스트에 저장
    
    for password in valid_passwords:  # 유효한 조합을 하나씩 출력
        print(password)

if __name__ == "__main__":
    main()  # main 함수를 호출하여 프로그램 실행
