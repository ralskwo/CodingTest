import heapq
import sys

input = sys.stdin.read  # 전체 입력을 받아오는 함수로 설정
INF = float('inf')  # 무한대를 나타내기 위한 상수

def main():
    data = input().splitlines()  # 입력 데이터를 줄 단위로 분리하여 리스트로 저장
    first_line = data[0].split()  # 첫 줄에서 역의 수와 도착지 번호를 분리
    N = int(first_line[0])  # 지하철역의 수
    M = int(first_line[1])  # 도착지의 역 번호

    companies = list(map(int, data[1:N+1]))  # 각 역의 소속 회사 정보를 리스트로 변환
    adj_matrix = [list(map(int, line.split())) for line in data[N+1:2*N+1]]  # 역 간 연결 정보를 인접 행렬로 저장
    
    dist = [[(INF, INF) for _ in range(2)] for _ in range(N)]  # 최소 환승 횟수와 이동 시간을 저장할 배열, 각 역에 대해 A/B 두 가지 상태로 초기화
    dist[0][companies[0]] = (0, 0)  # 출발지에서 출발 회사의 환승과 시간 값을 0으로 설정
    
    pq = []  # 다익스트라 알고리즘에 사용할 우선순위 큐를 초기화
    heapq.heappush(pq, (0, 0, 0, companies[0]))  # 출발 역을 우선순위 큐에 추가, (환승, 시간, 역 번호, 회사) 형태로 저장
    
    while pq:  # 우선순위 큐가 빌 때까지 반복
        transfers, time, node, curr_company = heapq.heappop(pq)  # 우선순위 큐에서 가장 작은 값을 꺼냄
        
        # 이미 더 좋은 경로가 있는 경우 현재 경로는 무시
        if (transfers, time) > dist[node][curr_company]:
            continue

        # 현재 역에서 이동 가능한 모든 역을 확인
        for next_node in range(N):
            travel_time = adj_matrix[node][next_node]  # 현재 역에서 다음 역까지의 이동 시간
            if travel_time == 0:
                continue  # 연결되지 않은 경우 스킵
            
            next_company = companies[next_node]  # 다음 역의 소속 회사
            new_transfers = transfers + (1 if curr_company != next_company else 0)  # 회사가 다른 경우 환승 횟수를 증가
            new_time = time + travel_time  # 이동 시간을 추가
            
            # 다음 역으로 가는 새로운 경로가 기존보다 나은 경우 업데이트
            if (new_transfers, new_time) < dist[next_node][next_company]:
                dist[next_node][next_company] = (new_transfers, new_time)  # 최소 환승과 시간으로 업데이트
                heapq.heappush(pq, (new_transfers, new_time, next_node, next_company))  # 업데이트된 경로를 우선순위 큐에 추가

    result = min(dist[M], key=lambda x: (x[0], x[1]))  # 도착지에서 최소 환승과 최소 시간을 찾음
    print(result[0], result[1])  # 환승 횟수와 총 소요 시간을 출력

if __name__ == "__main__":
    main()  # main 함수를 호출하여 프로그램 실행