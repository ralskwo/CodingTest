import heapq  # 우선순위 큐 구현을 위해 heapq 모듈을 import
import sys
input = sys.stdin.read  # 표준 입력을 받아올 함수를 input으로 사용

def dijkstra(grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 이동을 위한 방향 설정
    pq = []  # 우선순위 큐를 위한 리스트 초기화
    heapq.heappush(pq, (grid[0][0], 0, 0))  # 시작점 (0, 0)의 루피 값을 큐에 삽입
    min_rupee = [[float('inf')] * N for _ in range(N)]  # 최소 루피 합 배열을 무한대로 초기화
    min_rupee[0][0] = grid[0][0]  # 시작점의 최소 루피 합은 해당 칸의 루피 값으로 설정
    
    while pq:
        curr_rupee, x, y = heapq.heappop(pq)  # 현재 위치와 루피 값을 큐에서 꺼냄
        
        # 현재 위치의 최소 루피 합이 큐에서 꺼낸 루피 값보다 크면 무시
        if curr_rupee > min_rupee[x][y]:
            continue
        
        # 상, 하, 좌, 우 방향으로 인접한 칸들을 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:  # 인접한 칸이 격자 내에 있는지 확인
                new_rupee = curr_rupee + grid[nx][ny]  # 새로운 루피 합 계산
                if new_rupee < min_rupee[nx][ny]:  # 새로운 루피 합이 기존 루피 합보다 작으면
                    min_rupee[nx][ny] = new_rupee  # 최소 루피 합 갱신
                    heapq.heappush(pq, (new_rupee, nx, ny))  # 큐에 새로운 상태 삽입
    
    return min_rupee[N-1][N-1]  # 도착점 (N-1, N-1)의 최소 루피 합 반환

def solve_problems(test_cases):
    results = []  # 결과를 저장할 리스트 초기화
    for idx, (N, grid) in enumerate(test_cases):  # 각 테스트 케이스를 순회
        min_rupee = dijkstra(grid, N)  # 다익스트라 알고리즘으로 최소 루피 합 계산
        results.append(f"Problem {idx + 1}: {min_rupee}")  # 결과를 포맷에 맞게 저장
    return results  # 모든 결과 반환

def main():
    data = input().split()  # 표준 입력을 공백으로 구분하여 읽어옴
    
    index = 0  # 데이터 인덱스 초기화
    test_cases = []  # 테스트 케이스를 저장할 리스트 초기화
    
    while True:
        N = int(data[index])  # 격자 크기 N 읽어오기
        index += 1  # 인덱스 증가
        if N == 0:  # N이 0이면 종료
            break
        grid = []  # 격자를 저장할 리스트 초기화
        for _ in range(N):
            row = list(map(int, data[index:index+N]))  # 격자의 한 행 읽어오기
            index += N  # 인덱스 증가
            grid.append(row)  # 격자의 한 행을 리스트에 추가
        test_cases.append((N, grid))  # 하나의 테스트 케이스를 리스트에 추가
    
    results = solve_problems(test_cases)  # 모든 테스트 케이스 해결
    for result in results:  # 각 테스트 케이스 결과 출력
        print(result)

if __name__ == "__main__":
    main()  # main 함수 실행
