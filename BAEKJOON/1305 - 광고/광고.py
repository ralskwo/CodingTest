def shortest_ad_length(L, ad):
    # 실패 함수 배열 초기화, 길이가 L인 배열을 0으로 채움
    failure = [0] * L
    # 접두사와 접미사가 일치하는 최대 길이를 추적할 인덱스 j 초기화
    j = 0

    # 두 번째 문자부터 마지막 문자까지 반복하여 실패 함수 계산
    for i in range(1, L):
        # j가 0보다 크고 현재 문자가 일치하지 않을 경우, 이전 실패 함수 값을 참고하여 j 갱신
        while j > 0 and ad[i] != ad[j]:
            j = failure[j - 1]
        # 현재 문자가 일치하면, j를 증가시키고 실패 함수 배열에 j 값을 저장
        if ad[i] == ad[j]:
            j += 1
            failure[i] = j

    # 문자열의 길이 L에서 실패 함수의 마지막 값을 빼서 주기성을 나타내는 최소 광고 길이를 반환
    return L - failure[L - 1]

if __name__ == "__main__":
    # 첫 번째 줄에서 광고판 크기 L을 입력받아 정수로 변환
    L = int(input().strip())
    # 두 번째 줄에서 현재 광고판에 보이는 문자열을 입력받음
    ad = input().strip()
    # 계산된 최소 광고 길이를 출력
    print(shortest_ad_length(L, ad))