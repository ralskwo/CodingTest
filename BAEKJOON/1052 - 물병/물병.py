def min_bottle_purchase(N, K):
    # 이진수로 변환된 숫자에서 1의 개수를 세는 함수
    def count_set_bits(x):
        return bin(x).count('1')
    
    # 추가로 구매할 물병의 수 초기화
    purchase_count = 0
    
    # N의 물병 개수에서 1의 개수가 K 이하가 될 때까지 반복
    while count_set_bits(N) > K:
        # 물병을 하나 추가 구매하여 N을 1 증가
        N += 1
        # 구매한 물병의 수를 증가
        purchase_count += 1
    
    # 필요한 최소 추가 물병의 수를 반환
    return purchase_count

# 입력 값을 받아 N과 K로 분리
N, K = map(int, input().split())

# 결과를 계산하여 출력
result = min_bottle_purchase(N, K)
print(result)
