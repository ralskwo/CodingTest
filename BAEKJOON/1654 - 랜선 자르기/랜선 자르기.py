def max_lan_length(k, n, lengths):
    # 이분 탐색의 시작점은 1, 최소 길이로 설정
    start = 1
    # 이분 탐색의 끝점은 랜선들 중 가장 긴 길이로 설정
    end = max(lengths)
    # 결과값을 저장할 변수, 초기값은 0
    result = 0

    # 이분 탐색 시작, start가 end보다 작거나 같을 때까지 반복
    while start <= end:
        # 중간값(mid)을 계산
        mid = (start + end) // 2
        # 현재 중간값으로 랜선을 잘랐을 때의 랜선 개수를 계산
        count = sum(l // mid for l in lengths)

        # 랜선 개수가 N개 이상이면
        if count >= n:
            # 결과값에 현재 중간값을 저장
            result = mid
            # 더 긴 길이를 탐색하기 위해 start를 증가
            start = mid + 1
        else:
            # 랜선 개수가 N개 미만이면 더 짧은 길이를 탐색
            end = mid - 1

    # 최종적으로 저장된 최대 길이를 반환
    return result


# 첫 줄에서 K(랜선 개수)와 N(필요한 랜선 개수)를 입력받음
k, n = map(int, input().split())
# K개의 랜선 길이를 입력받아 리스트로 저장
lengths = [int(input()) for _ in range(k)]
# 이분 탐색 결과로 계산된 최대 랜선 길이를 출력
print(max_lan_length(k, n, lengths))
