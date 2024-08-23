def solution(food):
    left_side = []  # 왼쪽 부분에 배치될 음식을 저장할 리스트 생성
    
    # 물(0번 음식)은 고려하지 않기 때문에 food[1]부터 시작
    for i in range(1, len(food)):
        count = food[i] // 2  # 각 음식의 절반을 계산 (대칭 배치를 위해)
        left_side.append(str(i) * count)  # 해당 음식을 '음식 번호 * 절반 개수'로 추가
    
    # right_side는 left_side를 뒤집은 형태로, 오른쪽에 배치될 음식을 저장
    right_side = ''.join(left_side[::-1])
    
    # left_side는 리스트를 문자열로 변환하여 저장
    left_side = ''.join(left_side)
    
    # 최종 결과 문자열을 만들어 반환 (left_side + '0' + right_side)
    # '0'은 물을 의미하며, 중앙에 배치됨
    result = left_side + '0' + right_side
    return result  # 최종 배치 결과를 반환