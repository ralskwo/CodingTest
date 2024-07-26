def find_closest_to_zero(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장
    left = 0  # 시작 포인터를 배열의 첫 번째 요소로 설정
    right = n - 1  # 끝 포인터를 배열의 마지막 요소로 설정
    closest_sum = float('inf')  # 0에 가장 가까운 합을 저장할 변수, 초기값은 무한대로 설정
    answer = (arr[left], arr[right])  # 가장 가까운 합을 만드는 두 용액의 특성값을 저장할 변수

    while left < right:  # 두 포인터가 교차할 때까지 반복
        current_sum = arr[left] + arr[right]  # 현재 두 포인터가 가리키는 용액의 합 계산
        if abs(current_sum) < abs(closest_sum):  # 현재 합이 0에 더 가까운 경우
            closest_sum = current_sum  # 가장 가까운 합을 갱신
            answer = (arr[left], arr[right])  # 두 용액의 특성값을 갱신
        
        if current_sum < 0:  # 현재 합이 0보다 작은 경우
            left += 1  # 시작 포인터를 오른쪽으로 이동
        else:  # 현재 합이 0보다 크거나 같은 경우
            right -= 1  # 끝 포인터를 왼쪽으로 이동

    return answer  # 0에 가장 가까운 합을 만드는 두 용액의 특성값 반환

# 입력
n = int(input())  # 전체 용액의 수 입력
arr = list(map(int, input().split()))  # 용액의 특성값을 입력받아 리스트로 변환

# 특성값이 0에 가장 가까운 두 용액 찾기
result = find_closest_to_zero(arr)  # find_closest_to_zero 함수 호출
print(result[0], result[1])  # 결과 출력
