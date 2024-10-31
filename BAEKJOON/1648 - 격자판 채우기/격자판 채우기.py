MOD = 9901  # 나눌 모듈러 값 설정

def count_ways_to_fill(N, M):
    if (N * M) % 2 != 0:  # 격자판의 칸 수가 홀수일 경우 도미노로 채울 수 없음
        return 0  # 홀수일 경우 0 반환

    # dp 테이블 생성: dp[열][상태 비트마스크]로 설정
    dp = [[0] * (1 << N) for _ in range(M + 1)]
    dp[0][0] = 1  # 초기 상태에서 가능한 배치 수 1로 설정

    # 각 열에 대해 상태를 갱신하며 도미노 배치 계산
    for col in range(M):
        for state in range(1 << N):  # 각 상태 비트마스크에 대해 반복
            if dp[col][state] == 0:  # 해당 상태에서 가능하지 않으면 건너뜀
                continue
            next_states = []  # 다음 열로 전이 가능한 상태 저장할 리스트
            generate_next_states(0, N, state, 0, next_states)  # 현재 상태에서 다음 상태 생성
            for next_state in next_states:
                dp[col + 1][next_state] = (dp[col + 1][next_state] + dp[col][state]) % MOD
                # 모듈러를 사용해 다음 상태에 가능한 배치 수 추가

    return dp[M][0]  # 마지막 열이 모두 채워진 상태에서 가능한 배치 수 반환

def generate_next_states(pos, N, current_state, next_state, next_states):
    if pos == N:  # 현재 위치가 N이라면 전체 열이 채워졌음을 의미
        next_states.append(next_state)  # 완성된 다음 상태를 리스트에 추가
        return
    if (current_state & (1 << pos)) != 0:  # 현재 위치에 도미노가 이미 차있는 경우
        generate_next_states(pos + 1, N, current_state, next_state, next_states)  # 다음 칸으로 이동
    else:
        generate_next_states(pos + 1, N, current_state, next_state | (1 << pos), next_states)  # 2x1 세로 배치
        if pos + 1 < N and (current_state & (1 << (pos + 1))) == 0:  # 1x2 가로 배치가 가능한지 확인
            generate_next_states(pos + 2, N, current_state, next_state, next_states)  # 가로 배치로 전이 가능하면 다음 상태 생성

# 입력 값을 받아 count_ways_to_fill 함수로 가능한 배치 수 계산
N, M = map(int, input().split())
print(count_ways_to_fill(N, M))