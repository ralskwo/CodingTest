import sys
input = sys.stdin.read  # 입력을 빠르게 처리하기 위해 sys.stdin.read를 사용하여 한 번에 모든 입력을 받음

def bellman_ford(n, edges, start):
    INF = float('inf')  # 무한대를 의미하는 값을 설정
    dist = [INF] * (n + 1)  # 시작 지점에서 다른 지점까지의 최단 거리를 저장하는 배열, 초기에는 모두 무한대 값으로 설정
    dist[start] = 0  # 시작 지점(start)의 거리를 0으로 초기화

    for i in range(n):  # 지점의 개수 n만큼 반복
        updated = False  # 현재 반복에서 거리 갱신이 있었는지 확인하는 변수
        for u, v, w in edges:  # 모든 간선에 대해 반복
            if dist[u] != INF and dist[u] + w < dist[v]:  # 시작 지점까지의 거리가 무한대가 아니고, 갱신 가능할 때
                dist[v] = dist[u] + w  # 현재 간선의 도착 지점까지의 거리 갱신
                updated = True  # 거리 갱신이 있었음을 표시
                if i == n - 1:  # n번째 반복에서 갱신이 발생하면 음수 사이클이 존재
                    return True  # 음수 사이클이 있음을 나타내기 위해 True 반환
        if not updated:  # 거리 갱신이 없으면 더 이상 확인할 필요가 없음
            break  # 반복 종료
    return False  # 음수 사이클이 없음을 나타내기 위해 False 반환

def main():
    data = input().strip().split()  # 입력을 받아 공백을 기준으로 나누고, 리스트로 저장
    idx = 0  # 입력 데이터에서 현재 위치를 가리키는 인덱스
    tc = int(data[idx])  # 테스트 케이스 개수를 첫 번째 값으로 설정
    idx += 1  # 다음 인덱스로 이동
    results = []  # 각 테스트 케이스 결과를 저장할 리스트

    for _ in range(tc):  # 테스트 케이스 개수만큼 반복
        n = int(data[idx])  # 지점의 수
        m = int(data[idx + 1])  # 도로의 개수
        w = int(data[idx + 2])  # 웜홀의 개수
        idx += 3  # 다음 인덱스로 이동
        edges = []  # 도로와 웜홀의 정보를 저장할 리스트

        for __ in range(m):  # 도로의 개수만큼 반복
            s = int(data[idx])  # 도로의 시작 지점
            e = int(data[idx + 1])  # 도로의 끝 지점
            t = int(data[idx + 2])  # 도로의 이동 시간
            edges.append((s, e, t))  # 도로 정보 추가 (양방향)
            edges.append((e, s, t))  # 양방향이므로 역방향도 추가
            idx += 3  # 다음 인덱스로 이동

        for __ in range(w):  # 웜홀의 개수만큼 반복
            s = int(data[idx])  # 웜홀의 시작 지점
            e = int(data[idx + 1])  # 웜홀의 끝 지점
            t = int(data[idx + 2])  # 줄어드는 시간 (음수 가중치)
            edges.append((s, e, -t))  # 웜홀 정보 추가 (단방향)
            idx += 3  # 다음 인덱스로 이동

        has_negative_cycle = False  # 음수 사이클 존재 여부를 확인하는 변수
        for start in range(1, n + 1):  # 모든 지점을 시작점으로 설정하여 음수 사이클 탐지 시도
            if bellman_ford(n, edges, start):  # 음수 사이클이 발견되면
                has_negative_cycle = True  # 음수 사이클 존재를 표시
                break  # 더 이상 탐색할 필요가 없으므로 중단

        if has_negative_cycle:  # 음수 사이클이 발견되었을 경우
            results.append("YES")  # 결과 리스트에 "YES" 추가
        else:  # 음수 사이클이 없을 경우
            results.append("NO")  # 결과 리스트에 "NO" 추가

    print("\n".join(results))  # 모든 테스트 케이스 결과를 출력

if __name__ == "__main__":
    main()  # 프로그램 시작