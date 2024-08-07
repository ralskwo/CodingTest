# 나무 자르기 문제 풀이 및 설명

https://www.acmicpc.net/problem/2805

## 문제 이해

상근이는 나무를 필요로 합니다. 하지만 근처의 모든 나무를 무작정 자를 수 없기 때문에 절단기에 특정 높이 \( H \)를 설정해서 그 높이 이상인 부분만 잘라야 합니다. 나무를 잘랐을 때, 잘린 나무의 총 길이가 적어도 \( M \) 미터가 되어야 합니다. 상근이는 절단기에 설정할 수 있는 최대 높이 \( H \)를 찾아야 합니다.

입력으로는 나무의 수 \( N \)과 필요한 나무의 길이 \( M \)이 주어집니다. 또한 각 나무의 높이가 주어지며, 나무의 높이는 1부터 1,000,000,000 사이의 값입니다. 나무의 수는 최대 1,000,000개, 필요한 나무의 길이는 최대 2,000,000,000입니다.

출력은 나무의 길이 합이 적어도 \( M \) 미터가 되도록 절단기에 설정할 수 있는 높이의 최댓값을 구하는 것입니다.

## 접근 방식

이 문제는 이진 탐색(Binary Search) 알고리즘을 사용하여 해결할 수 있습니다. 이진 탐색은 정렬된 배열에서 효율적으로 원하는 값을 찾을 수 있는 알고리즘입니다. 이 문제에서는 절단기의 높이 \( H \)를 이진 탐색을 통해 찾아야 합니다.

1. **이진 탐색 초기 설정**:
   - `start`를 0으로, `end`를 가장 높은 나무의 높이로 설정합니다.
   - 절단기 높이 \( H \)를 `start`와 `end`의 중간값으로 설정합니다.

2. **탐색 과정**:
   - 중간값 `mid`를 계산합니다.
   - 모든 나무를 순회하며 `mid` 높이로 잘랐을 때 얻을 수 있는 나무의 총 길이를 계산합니다.
   - 만약 총 길이가 \( M \) 이상이면, `mid`를 결과값으로 설정하고, `start`를 `mid + 1`로 변경하여 더 큰 값의 `H`를 탐색합니다.
   - 총 길이가 \( M \) 미만이면, `end`를 `mid - 1`로 변경하여 더 작은 값의 `H`를 탐색합니다.

3. **탐색 종료**:
   - `start`가 `end`보다 커질 때 탐색을 종료합니다.
   - 최종적으로 저장된 `result` 값이 절단기에 설정할 수 있는 높이의 최댓값이 됩니다.

## 풀이 과정

1. **이진 탐색 초기 설정**:
   - 이진 탐색을 위해 `start`를 0으로 설정하고, `end`를 가장 높은 나무의 높이로 설정합니다. 이 변수들은 이진 탐색의 범위를 나타냅니다. `result`는 최종적으로 절단기의 높이를 저장할 변수입니다.

2. **탐색 과정**:
   - `start`가 `end`보다 작거나 같을 때까지 이진 탐색을 반복합니다. 
   - `mid`를 `start`와 `end`의 중간값으로 설정합니다.
   - 나무의 높이가 `mid`보다 큰 경우, `mid` 높이로 잘랐을 때의 나무 길이를 `total`에 더합니다.
   - 만약 `total`이 \( M \) 이상이면, `mid`가 충분한 높이이므로 `result`를 `mid`로 업데이트하고, 더 큰 값을 찾기 위해 `start`를 `mid + 1`로 설정합니다.
   - 만약 `total`이 \( M \) 미만이면, `mid`가 충분한 높이가 아니므로 더 작은 값을 찾기 위해 `end`를 `mid - 1`로 설정합니다.

3. **탐색 종료 및 결과 출력**:
   - `start`가 `end`보다 커지면 탐색을 종료합니다. 이 때, `result`에는 절단기에 설정할 수 있는 높이의 최댓값이 저장되어 있습니다.
   - 최종적으로 `result` 값을 출력합니다.

## 코드
```python
def find_max_height(trees, N, M):
    # 이진 탐색을 위한 초기 시작점과 끝점 설정
    start, end = 0, max(trees)
    result = 0

    # 이진 탐색 시작
    while start <= end:
        # 중간값 계산
        mid = (start + end) // 2
        total = 0
        
        # 현재 중간값(mid) 높이로 나무를 잘라 얻을 수 있는 총 나무 길이 계산
        for tree in trees:
            if tree > mid:
                total += tree - mid

        # 얻은 총 나무 길이가 필요한 길이 M 이상인지 확인
        if total >= M:
            # 현재 중간값(mid) 높이로도 충분한 나무 길이를 얻을 수 있으므로, 결과값 업데이트
            result = mid
            # 더 큰 높이에서 잘라도 충분한지 확인하기 위해 시작점을 중간값+1로 설정
            start = mid + 1
        else:
            # 현재 중간값(mid) 높이로는 충분한 나무 길이를 얻을 수 없으므로, 끝점을 중간값-1로 설정
            end = mid - 1

    return result

# 입력 처리
N, M = map(int, input().split())  # 나무의 수 N과 필요한 나무 길이 M 입력
trees = list(map(int, input().split()))  # 나무의 높이들을 리스트로 입력

# 최대 높이 출력
print(find_max_height(trees, N, M))
