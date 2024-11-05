dp = {}  # 동적 프로그래밍을 위한 딕셔너리 초기화. 이미 계산한 경우의 수를 저장하여 중복 계산을 방지

def count_ways(whole, half):
    if whole == 0 and half == 0:  # 전체 조각과 반 조각이 모두 0이면, 가능한 문자열 한 가지가 완성된 것이므로 1을 반환
        return 1
    if (whole, half) in dp:  # 현재 (whole, half) 상태가 이미 dp에 저장되어 있다면, 저장된 값을 바로 반환하여 계산을 최적화
        return dp[(whole, half)]
    
    ways = 0  # 가능한 경우의 수를 저장할 변수 초기화
    if whole > 0:  # 전체 조각이 남아 있다면, 새로운 조각을 꺼내 반으로 쪼개서 하나는 먹고 다른 하나는 병에 넣는 경우를 고려
        ways += count_ways(whole - 1, half + 1)  # 전체 조각에서 하나를 줄이고 반 조각을 하나 추가하여 재귀 호출
    if half > 0:  # 반 조각이 남아 있다면, 반 조각을 하나 꺼내 먹는 경우를 고려
        ways += count_ways(whole, half - 1)  # 반 조각을 하나 줄인 상태로 재귀 호출
    
    dp[(whole, half)] = ways  # 현재 상태에서 가능한 경우의 수를 dp 테이블에 저장
    return ways  # 현재 (whole, half) 상태에서 가능한 문자열의 총 경우의 수를 반환

results = []  # 각 테스트 케이스의 결과를 저장할 리스트 초기화
while True:
    N = int(input())  # 약의 개수 N을 입력 받음
    if N == 0:  # 입력이 0이면 종료 조건으로 판단하여 반복문 탈출
        break
    results.append(count_ways(N, 0))  # 가능한 문자열의 개수를 계산하여 results 리스트에 추가

for result in results:  # 저장된 결과를 순서대로 출력
    print(result)