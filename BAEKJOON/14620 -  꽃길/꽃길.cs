import sys
input = sys.stdin.read
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def calculate_cost(board, x, y, N):
    cost = board[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        cost += board[nx][ny]
    return cost

def is_valid(x, y, N):
    if x <= 0 or x >= N-1 or y <= 0 or y >= N-1:
        return False
    return True

def check_overlap(visited, x, y):
    if visited[x][y]:
        return False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny]:
            return False
    return True

def place_flower(visited, x, y, place):
    visited[x][y] = place
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        visited[nx][ny] = place

def solve(N, board):
    candidates = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]
    min_cost = float('inf')

    for comb in combinations(candidates, 3):
        visited = [[False] * N for _ in range(N)]
        total_cost = 0
        valid = True

        for x, y in comb:
            if not is_valid(x, y, N) or not check_overlap(visited, x, y):
                valid = False
                break
            total_cost += calculate_cost(board, x, y, N)
            place_flower(visited, x, y, True)
        
        if valid:
            min_cost = min(min_cost, total_cost)

    return min_cost

def main():
    data = input().splitlines()
    N = int(data[0])
    board = [list(map(int, line.split())) for line in data[1:]]
    print(solve(N, board))

main()
