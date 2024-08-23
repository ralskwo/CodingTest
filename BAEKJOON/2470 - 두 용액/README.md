# 두 용액 문제 풀이 및 설명

https://www.acmicpc.net/problem/2470

## 문제 이해

KOI 부설 과학연구소에서는 양성 용액과 알칼리성 용액을 혼합하여 새로운 특성값을 가지는 용액을 만들 수 있습니다. 주어진 특성값 리스트에서 두 개의 용액을 선택하여 그 합이 0에 가장 가까운 용액을 만드는 문제입니다. 산성 용액은 양의 정수, 알칼리성 용액은 음의 정수로 나타내며, 이 둘을 혼합하여 특성값이 0에 가까운 값을 찾아야 합니다.

## 접근 방식
1. **정렬**: 주어진 특성값 리스트를 오름차순으로 정렬합니다. 이렇게 하면 작은 값부터 큰 값까지 순차적으로 비교할 수 있습니다.
2. **투 포인터**: 정렬된 리스트를 양 끝에서부터 하나씩 접근하는 두 개의 포인터를 사용합니다. 왼쪽 포인터는 리스트의 시작에서, 오른쪽 포인터는 리스트의 끝에서 시작합니다.
3. **합 계산**: 두 포인터의 값을 합하여 0에 가까운지를 확인합니다. 현재 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동시키고, 0보다 크면 오른쪽 포인터를 왼쪽으로 이동시킵니다. 합이 정확히 0이면 가장 가까운 값을 찾은 것이므로 반복을 종료합니다.
4. **최적의 쌍 저장**: 현재까지 발견된 가장 0에 가까운 합을 저장하고, 포인터가 이동할 때마다 업데이트합니다.

## 풀이 과정
1. 입력을 받아 리스트로 변환하고 정렬합니다.
2. 투 포인터를 초기화하고, 리스트를 순회하면서 두 용액의 합이 0에 가장 가까운 값을 찾습니다.
3. 최적의 쌍을 발견하면 그 값을 저장하고, 반복이 끝난 후 출력합니다.

## 코드
```python
def find_closest_to_zero_pair(N, properties):
    # 리스트를 정렬합니다.
    properties.sort()
    left, right = 0, N - 1  # 왼쪽 포인터와 오른쪽 포인터 초기화
    closest_pair = (properties[left], properties[right])
    closest_sum = abs(properties[left] + properties[right])
    
    # 투 포인터를 사용하여 합이 0에 가장 가까운 두 용액을 찾습니다.
    while left < right:
        current_sum = properties[left] + properties[right]
        
        # 현재 합이 더 0에 가까운 경우 업데이트합니다.
        if abs(current_sum) < closest_sum:
            closest_sum = abs(current_sum)
            closest_pair = (properties[left], properties[right])
        
        # 현재 합이 0보다 작으면 left 포인터를 오른쪽으로 이동
        if current_sum < 0:
            left += 1
        # 현재 합이 0보다 크면 right 포인터를 왼쪽으로 이동
        elif current_sum > 0:
            right -= 1
        # 현재 합이 0이면 가장 가까운 값을 찾은 것이므로 반복을 종료
        else:
            break
    
    return closest_pair

N = int(input().strip())
properties = list(map(int, input().strip().split()))

# 가장 가까운 두 용액의 특성값을 찾습니다.
result = find_closest_to_zero_pair(N, properties)

# 결과를 출력합니다.
print(result[0], result[1])