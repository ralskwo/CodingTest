def max_profit(n, wages):  # 최대 이익을 계산하는 함수
    left = [0] * n  # 각 일에 대해 왼쪽으로 확장 가능한 최대 범위를 저장하는 배열 초기화
    right = [0] * n  # 각 일에 대해 오른쪽으로 확장 가능한 최대 범위를 저장하는 배열 초기화
    stack = []  # 현재 일급을 기준으로 왼쪽 범위를 찾기 위한 스택

    for i in range(n):  # 0부터 n-1일까지 각 날에 대해 반복
        while stack and wages[stack[-1]] >= wages[i]:  # 스택의 마지막 값보다 현재 일급이 작거나 같으면
            stack.pop()  # 스택에서 제거 (왼쪽 확장 불가능한 범위)
        if stack:  # 스택이 비어있지 않으면
            left[i] = stack[-1] + 1  # 현재 위치에서 왼쪽으로 확장 가능한 범위 설정
        else:  # 스택이 비어있으면
            left[i] = 0  # 현재 위치에서 왼쪽으로 더 이상 확장 불가, 시작 지점이 0
        stack.append(i)  # 현재 위치를 스택에 추가

    stack = []  # 오른쪽 범위를 계산하기 위해 스택 초기화

    for i in range(n - 1, -1, -1):  # n-1부터 0까지 각 날에 대해 반복 (오른쪽 방향으로 탐색)
        while stack and wages[stack[-1]] >= wages[i]:  # 스택의 마지막 값보다 현재 일급이 작거나 같으면
            stack.pop()  # 스택에서 제거 (오른쪽 확장 불가능한 범위)
        if stack:  # 스택이 비어있지 않으면
            right[i] = stack[-1] - 1  # 현재 위치에서 오른쪽으로 확장 가능한 범위 설정
        else:  # 스택이 비어있으면
            right[i] = n - 1  # 현재 위치에서 오른쪽으로 더 이상 확장 불가, 끝 지점이 n-1
        stack.append(i)  # 현재 위치를 스택에 추가

    max_profit = 0  # 최대 이익을 저장할 변수 초기화
    for i in range(n):  # 0부터 n-1까지 각 날에 대해 반복
        current_profit = wages[i] * (right[i] - left[i] + 1)  # 현재 일급을 기준으로 가능한 최대 이익 계산
        max_profit = max(max_profit, current_profit)  # 현재 최대 이익과 비교하여 더 큰 값으로 갱신

    return max_profit  # 최대 이익 반환

n = int(input().strip())  # 일을 할 수 있는 날의 수 입력 받기
wages = list(map(int, input().strip().split()))  # n일 동안의 일급 정보를 리스트로 입력 받기

print(max_profit(n, wages))  # 최대 이익을 계산하여 출력
