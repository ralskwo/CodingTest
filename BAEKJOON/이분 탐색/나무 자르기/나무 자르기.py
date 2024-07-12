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
