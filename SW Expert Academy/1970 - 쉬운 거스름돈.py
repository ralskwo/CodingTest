# 테스트 케이스 수 입력 받기
T = int(input())

# 화폐 단위 리스트 (큰 순서대로)
currency = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    N = int(input())  # 거스름돈 N 입력 받기
    result = []
    
    # 각 화폐 단위에 대해 필요한 개수 계산
    for c in currency:
        count = N // c  # 해당 화폐 단위의 개수
        result.append(str(count))  # 결과 리스트에 추가
        N %= c  # 남은 금액 갱신
    
    # 출력 형식에 맞게 출력
    print(f"#{t}")
    print(" ".join(result))
