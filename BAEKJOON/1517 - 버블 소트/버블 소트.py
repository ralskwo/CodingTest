def merge_sort_and_count(arr, temp_arr, left, right):
    if left == right:  # 배열이 하나의 요소만 가지고 있다면, 역전이 발생할 수 없으므로 0을 반환
        return 0
    
    mid = (left + right) // 2  # 배열을 두 부분으로 나누기 위해 중간 인덱스를 계산
    
    inv_count = merge_sort_and_count(arr, temp_arr, left, mid)  # 왼쪽 절반에서 발생하는 역전 횟수를 계산
    inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)  # 오른쪽 절반에서 발생하는 역전 횟수를 계산
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)  # 병합하면서 발생하는 역전 횟수를 계산
    
    return inv_count  # 총 역전 횟수를 반환

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # 왼쪽 서브배열의 시작 인덱스
    j = mid + 1  # 오른쪽 서브배열의 시작 인덱스
    k = left  # 병합된 배열의 시작 인덱스
    inv_count = 0  # 역전 횟수를 저장할 변수
    
    while i <= mid and j <= right:  # 왼쪽과 오른쪽 배열의 요소를 비교하여 병합
        if arr[i] <= arr[j]:  # 왼쪽 배열의 요소가 작거나 같으면 그대로 병합
            temp_arr[k] = arr[i]
            i += 1
        else:  # 오른쪽 배열의 요소가 작다면 역전이 발생한 것
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # 남은 왼쪽 배열의 요소 수만큼 역전 횟수 추가
            j += 1
        k += 1

    while i <= mid:  # 왼쪽 배열에 남은 요소가 있으면 병합
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:  # 오른쪽 배열에 남은 요소가 있으면 병합
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):  # 병합된 결과를 원래 배열에 복사
        arr[i] = temp_arr[i]
    
    return inv_count  # 병합 중 발생한 역전 횟수를 반환

def count_swaps(arr, n):
    temp_arr = [0]*n  # 임시 배열을 생성
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)  # 전체 배열에 대해 역전 횟수를 계산

n = int(input())  # 배열의 크기 입력
arr = list(map(int, input().split()))  # 배열의 요소들을 입력받아 리스트로 변환

print(count_swaps(arr, n))  # 스왑 횟수를 계산하여 출력
