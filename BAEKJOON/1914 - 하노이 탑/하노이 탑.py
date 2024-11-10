def hanoi(n, start, end, auxiliary, moves):
    # 원판이 1개일 때, 바로 시작 장대에서 끝 장대로 이동
    if n == 1:
        moves.append((start, end))  # 이동 기록을 moves 리스트에 추가
        return  # 재귀 호출 종료

    # n-1개의 원판을 시작 장대에서 보조 장대로 이동
    hanoi(n - 1, start, auxiliary, end, moves)

    # n번째 원판을 시작 장대에서 끝 장대로 이동
    moves.append((start, end))

    # n-1개의 원판을 보조 장대에서 끝 장대로 이동
    hanoi(n - 1, auxiliary, end, start, moves)

def solve_hanoi(n):
    # 총 이동 횟수를 계산 (2의 n승 - 1)
    total_moves = (2 ** n) - 1
    print(total_moves)  # 첫 번째 줄에 이동 횟수 출력

    # 원판의 개수가 20 이하일 때만 이동 과정을 출력
    if n <= 20:
        moves = []  # 이동 경로를 저장할 리스트 생성
        hanoi(n, 1, 3, 2, moves)  # 하노이 함수를 호출하여 이동 과정 저장

        # 이동 과정을 차례로 출력
        for move in moves:
            print(move[0], move[1])  # 각 이동을 시작 장대와 끝 장대로 출력

# 첫 번째 장대에 쌓인 원판의 개수를 입력받고 정수형으로 변환
n = int(input().strip())

# 하노이 탑 문제 해결 함수 호출
solve_hanoi(n)