# 테스트 케이스 수 입력
T = int(input())

for t in range(1, T + 1):
    # 각 테스트 케이스 별로 N과 매매가 리스트 입력
    N = int(input())
    prices = list(map(int, input().split()))
    
    # 뒤에서부터 탐색하면서 현재까지의 최대 매매가 추적
    max_price = 0
    profit = 0
    
    # 뒤에서부터 역순으로 탐색
    for price in reversed(prices):
        # 현재 가격이 최대 매매가보다 작으면 이익을 계산
        if price < max_price:
            profit += max_price - price
        # 그렇지 않으면 현재 가격을 최대 매매가로 갱신
        else:
            max_price = price
    
    # 출력 형식에 맞게 결과 출력
    print(f"#{t} {profit}")
