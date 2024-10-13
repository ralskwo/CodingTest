def main():
    n = int(input())  # 먼저, 선수의 수를 입력받아 정수로 변환한다.
    players = [input().strip() for _ in range(n)]  # n명의 선수 성을 입력받고, 공백을 제거한 후 리스트로 저장한다.
    
    first_letter_count = {}  # 각 성의 첫 글자를 카운트할 딕셔너리를 초기화한다.
    
    # 각 선수의 성에서 첫 글자를 추출하고 해당 글자의 출현 횟수를 기록한다.
    for player in players:
        first_letter = player[0]  # 선수 성의 첫 글자를 가져온다.
        if first_letter in first_letter_count:  # 이미 해당 글자가 딕셔너리에 있는지 확인한다.
            first_letter_count[first_letter] += 1  # 있다면, 출현 횟수를 1 증가시킨다.
        else:
            first_letter_count[first_letter] = 1  # 없다면, 새로 추가하고 출현 횟수를 1로 설정한다.
    
    result = []  # 5명 이상인 첫 글자를 저장할 리스트를 초기화한다.
    
    # 딕셔너리에서 출현 횟수가 5 이상인 첫 글자를 결과 리스트에 추가한다.
    for letter, count in first_letter_count.items():
        if count >= 5:
            result.append(letter)
    
    # 5명 이상인 첫 글자가 있는 경우, 이를 사전순으로 정렬하여 출력한다.
    if result:
        print(''.join(sorted(result)))  # 사전순으로 정렬된 결과 리스트를 공백 없이 출력한다.
    else:
        print("PREDAJA")  # 5명 이상인 첫 글자가 없으면 "PREDAJA"를 출력한다.

# 해당 파일이 메인으로 실행될 때만 main() 함수를 호출한다.
if __name__ == "__main__":
    main()