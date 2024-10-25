def rotate_90(matrix, N):
    return [[matrix[N - j - 1][i] for j in range(N)] for i in range(N)]

def rotate_180(matrix, N):
    return [[matrix[N - i - 1][N - j - 1] for j in range(N)] for i in range(N)]

def rotate_270(matrix, N):
    return [[matrix[j][N - i - 1] for j in range(N)] for i in range(N)]

def solve():
    T = int(input())  # 테스트 케이스의 수
    for t in range(1, T + 1):
        N = int(input())  # 행렬의 크기
        matrix = [list(map(int, input().split())) for _ in range(N)]

        # 각각 90도, 180도, 270도 회전된 행렬 계산
        rotated_90 = rotate_90(matrix, N)
        rotated_180 = rotate_180(matrix, N)
        rotated_270 = rotate_270(matrix, N)

        print(f"#{t}")
        # 출력 형식에 맞추어 회전된 결과 출력
        for i in range(N):
            print("".join(map(str, rotated_90[i])), end=" ")
            print("".join(map(str, rotated_180[i])), end=" ")
            print("".join(map(str, rotated_270[i])))

# 함수를 실행시킵니다.
solve()