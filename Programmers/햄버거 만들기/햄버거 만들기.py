def solution(ingredient):
    stack = []  # 현재 재료들을 쌓아놓을 스택을 초기화
    count = 0   # 완성된 햄버거의 개수를 세기 위한 카운트를 초기화
    
    for item in ingredient:  # 재료 리스트를 순차적으로 처리
        stack.append(item)  # 현재 재료를 스택에 추가
        # 스택의 길이가 4 이상이어야 하며, 마지막 4개의 재료가 [1, 2, 3, 1]인지 확인
        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            count += 1  # 햄버거가 완성되었으므로 카운트를 1 증가
            del stack[-4:]  # 스택에서 완성된 햄버거의 재료 4개를 제거
    
    return count  # 총 완성된 햄버거의 개수를 반환
