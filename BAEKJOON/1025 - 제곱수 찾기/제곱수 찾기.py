import math  # 수학 모듈을 불러옵니다. 이 모듈은 제곱근 계산에 사용됩니다.

N, M = map(int, input().split())  # N과 M을 입력받고 정수로 변환합니다.
table = [input().strip() for _ in range(N)]  # 표의 각 행을 입력받아 리스트로 저장합니다.

def is_perfect_square(num):  # 숫자가 완전 제곱수인지 확인하는 함수입니다.
    if num < 0:  # 음수는 완전 제곱수가 될 수 없으므로 False를 반환합니다.
        return False
    root = int(math.isqrt(num))  # num의 제곱근을 계산한 후 정수로 변환합니다.
    return root * root == num  # 제곱근의 제곱이 num과 같으면 완전 제곱수이므로 True를 반환합니다.

max_square = -1  # 최대 완전 제곱수를 저장할 변수를 초기화합니다.

for i in range(N):  # 모든 행에 대해 반복합니다.
    for j in range(M):  # 모든 열에 대해 반복합니다.
        for di in range(-N, N):  # 행 방향으로 가능한 모든 이동 거리를 설정합니다.
            for dj in range(-M, M):  # 열 방향으로 가능한 모든 이동 거리를 설정합니다.
                if di == 0 and dj == 0:  # 이동 거리가 0,0이면 숫자를 만들 수 없으므로 건너뜁니다.
                    continue
                x, y = i, j  # 시작 위치를 현재 위치로 설정합니다.
                num_str = ""  # 숫자를 이어 붙일 문자열 변수를 초기화합니다.
                while 0 <= x < N and 0 <= y < M:  # 위치가 유효한 범위 내에 있는 동안 반복합니다.
                    num_str += table[x][y]  # 현재 위치의 숫자를 num_str에 추가합니다.
                    num = int(num_str)  # num_str을 정수로 변환합니다.
                    if is_perfect_square(num):  # num이 완전 제곱수인지 확인합니다.
                        max_square = max(max_square, num)  # 현재까지의 최대 완전 제곱수와 비교해 더 큰 값을 저장합니다.
                    x += di  # 행 방향으로 이동합니다.
                    y += dj  # 열 방향으로 이동합니다.

print(max_square)  # 찾은 최대 완전 제곱수를 출력합니다. 만약 완전 제곱수를 찾지 못했다면 -1이 출력됩니다.
