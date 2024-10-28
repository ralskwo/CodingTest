def find_three_solutions_closest_to_zero(N, solutions):
    # 용액 리스트를 오름차순으로 정렬하여 두 포인터 접근을 용이하게 만듦
    solutions.sort()
    
    # 0에 가장 가까운 합을 저장할 변수로 초기에는 매우 큰 값으로 설정
    closest_sum = float('inf')
    
    # 조건을 만족하는 세 용액의 값을 저장할 리스트
    answer = []

    # 첫 번째 용액을 고정하여 두 번째와 세 번째 용액을 찾기 위한 반복문
    for i in range(N - 2):
        # 왼쪽 포인터는 고정된 용액 다음 인덱스로 설정
        left = i + 1
        # 오른쪽 포인터는 리스트의 마지막 인덱스로 설정
        right = N - 1

        # 왼쪽 포인터가 오른쪽 포인터보다 작을 때까지 반복
        while left < right:
            # 고정된 용액과 두 포인터가 가리키는 용액들의 합을 계산
            current_sum = solutions[i] + solutions[left] + solutions[right]
            
            # 현재 합이 0에 더 가까운 경우 closest_sum과 answer를 갱신
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                answer = [solutions[i], solutions[left], solutions[right]]
            
            # 합이 양수인 경우 합을 줄이기 위해 오른쪽 포인터를 왼쪽으로 이동
            if current_sum > 0:
                right -= 1
            # 합이 음수인 경우 합을 늘리기 위해 왼쪽 포인터를 오른쪽으로 이동
            elif current_sum < 0:
                left += 1
            # 합이 정확히 0인 경우 최적의 해이므로 바로 결과를 반환
            else:
                return sorted(answer)

    # 모든 경우를 다 확인한 후, 0에 가장 가까운 합을 이루는 세 용액을 오름차순으로 정렬하여 반환
    return sorted(answer)

# 전체 용액의 개수를 입력받음
N = int(input())
# 각 용액의 특성값을 리스트 형태로 입력받음
solutions = list(map(int, input().split()))

# 함수 호출을 통해 0에 가장 가까운 합을 이루는 세 용액의 값을 계산
result = find_three_solutions_closest_to_zero(N, solutions)
# 결과를 공백으로 구분하여 출력
print(" ".join(map(str, result)))