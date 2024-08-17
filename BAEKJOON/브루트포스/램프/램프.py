def max_on_rows(N, M, lamp_states, K):  # N, M, 램프 상태와 K를 입력으로 받는 함수 정의
    from collections import Counter  # collections 모듈에서 Counter 클래스를 가져옴
    
    row_count = Counter(lamp_states)  # 각 행의 상태가 몇 번 나타나는지 세어서 row_count에 저장
    max_on = 0  # 최대 켜진 행의 수를 저장할 변수 초기화
    
    for row, count in row_count.items():  # 각 행과 그 행의 개수에 대해 반복
        zero_count = row.count('0')  # 해당 행에서 0의 개수를 셈
        if zero_count <= K and (K - zero_count) % 2 == 0:  # 조건을 만족하는지 확인
            max_on = max(max_on, count)  # 조건을 만족하면 max_on을 갱신
    
    return max_on  # 최대 켜진 행의 수 반환

N, M = map(int, input().split())  # 첫 줄에서 N(행의 수)과 M(열의 수)을 입력받음
lamp_states = [input().strip() for _ in range(N)]  # 다음 N줄에서 램프 상태를 입력받아 리스트로 저장
K = int(input().strip())  # 마지막 줄에서 K를 입력받음

result = max_on_rows(N, M, lamp_states, K)  # 함수 호출하여 결과 계산
print(result)  # 결과 출력
