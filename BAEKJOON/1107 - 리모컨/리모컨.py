def is_possible(channel, broken_buttons):  # 특정 채널을 고장난 버튼을 사용하지 않고 입력할 수 있는지 확인하는 함수
    for ch in str(channel):  # 채널의 각 숫자를 순회
        if int(ch) in broken_buttons:  # 만약 그 숫자가 고장난 버튼 중 하나라면
            return False  # 그 채널은 입력할 수 없으므로 False 반환
    return True  # 고장난 버튼 없이 입력할 수 있으면 True 반환

def min_button_presses(N, broken_buttons):  # 최소 버튼 클릭 수를 계산하는 함수
    min_presses = abs(N - 100)  # 초기값: 100번 채널에서 N번 채널로 이동할 때 +,- 버튼만 사용하는 경우

    for channel in range(1000000):  # 0부터 999,999까지의 채널을 순회
        if is_possible(channel, broken_buttons):  # 해당 채널을 입력할 수 있는지 확인
            presses = len(str(channel)) + abs(N - channel)  # 채널을 입력하는 버튼 수 + 해당 채널에서 N으로 이동하는 +,- 버튼 수
            min_presses = min(min_presses, presses)  # 최소 버튼 수를 갱신

    return min_presses  # 최소 버튼 클릭 수 반환

N = int(input())  # 이동하려는 채널 N 입력
M = int(input())  # 고장난 버튼의 수 M 입력

if M > 0:  # 만약 고장난 버튼이 있으면
    broken_buttons = list(map(int, input().split()))  # 고장난 버튼 리스트 입력
else:  # 고장난 버튼이 없으면
    broken_buttons = []  # 빈 리스트 할당

print(min_button_presses(N, broken_buttons))  # 최소 버튼 클릭 수 출력
