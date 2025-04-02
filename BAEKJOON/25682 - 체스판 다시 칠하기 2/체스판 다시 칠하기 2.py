import sys  # sys 모듈을 불러와 시스템 입력 및 출력을 사용

def main():
    input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 함수를 사용
    N, M, K = map(int, input().split())  # 보드의 행(N), 열(M), 체스판 크기(K)를 입력받아 정수로 변환
    board = [input().strip() for _ in range(N)]  # 보드의 각 행을 입력받아 양쪽 공백 제거 후 리스트에 저장

    p1 = [[0] * (M + 1) for _ in range(N + 1)]  # 패턴 1(맨 왼쪽이 'W')에 대한 2차원 누적합 배열을 (N+1)x(M+1) 크기로 0으로 초기화
    p2 = [[0] * (M + 1) for _ in range(N + 1)]  # 패턴 2(맨 왼쪽이 'B')에 대한 2차원 누적합 배열을 (N+1)x(M+1) 크기로 0으로 초기화

    for i in range(N):  # 보드의 각 행에 대해 순회
        row = board[i]  # 현재 행의 문자열을 row 변수에 저장
        for j in range(M):  # 현재 행의 각 열에 대해 순회
            if ((i + j) & 1) == 0:  # 행 인덱스와 열 인덱스의 합이 짝수이면
                expected1 = 'W'  # 패턴 1에서는 예상 색이 'W'
                expected2 = 'B'  # 패턴 2에서는 예상 색이 'B'
            else:  # 행 인덱스와 열 인덱스의 합이 홀수이면
                expected1 = 'B'  # 패턴 1에서는 예상 색이 'B'
                expected2 = 'W'  # 패턴 2에서는 예상 색이 'W'
            v1 = 1 if row[j] != expected1 else 0  # 현재 칸의 색이 패턴 1의 예상 색과 다르면 1, 같으면 0 저장
            v2 = 1 if row[j] != expected2 else 0  # 현재 칸의 색이 패턴 2의 예상 색과 다르면 1, 같으면 0 저장

            p1[i+1][j+1] = v1 + p1[i][j+1] + p1[i+1][j] - p1[i][j]  # 현재 칸을 포함한 패턴 1의 누적합 갱신 (현재 값 + 위쪽 + 왼쪽 - 대각선 위쪽)
            p2[i+1][j+1] = v2 + p2[i][j+1] + p2[i+1][j] - p2[i][j]  # 현재 칸을 포함한 패턴 2의 누적합 갱신 (현재 값 + 위쪽 + 왼쪽 - 대각선 위쪽)

    ans = float('inf')  # 최소 재칠 횟수를 저장할 변수 ans를 무한대로 초기화

    for i in range(0, N - K + 1):  # K×K 부분 보드의 시작 행 인덱스를 순회 (i는 시작 행)
        for j in range(0, M - K + 1):  # K×K 부분 보드의 시작 열 인덱스를 순회 (j는 시작 열)
            mismatches1 = p1[i+K][j+K] - p1[i][j+K] - p1[i+K][j] + p1[i][j]  # (i,j) 시작하는 영역의 패턴 1에 대한 재칠해야 하는 칸의 수 계산
            mismatches2 = p2[i+K][j+K] - p2[i][j+K] - p2[i+K][j] + p2[i][j]  # (i,j) 시작하는 영역의 패턴 2에 대한 재칠해야 하는 칸의 수 계산
            if mismatches1 < ans:  # 패턴 1의 재칠 횟수가 현재 최소값보다 작으면
                ans = mismatches1  # 최소값 갱신
            if mismatches2 < ans:  # 패턴 2의 재칠 횟수가 현재 최소값보다 작으면
                ans = mismatches2  # 최소값 갱신

    sys.stdout.write(str(ans))  # 최종 최소 재칠 횟수를 문자열로 변환하여 출력

if __name__ == '__main__':  # 해당 스크립트가 메인 프로그램으로 실행될 때
    main()  # main 함수를 호출하여 프로그램 실행
