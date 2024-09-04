from collections import deque  # deque를 사용하여 BFS(너비 우선 탐색)를 구현하기 위해 collections 모듈에서 deque를 가져옴

def sieve_of_eratosthenes():  # 에라토스테네스의 체 알고리즘을 사용하여 1000부터 9999까지의 소수를 미리 구하는 함수
    is_prime = [True] * 10000  # 숫자 0부터 9999까지 소수 여부를 저장하는 배열, 처음엔 모두 소수라고 가정
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False로 설정
    
    for i in range(2, int(10000**0.5) + 1):  # 2부터 10000의 제곱근까지 반복, 소수 여부를 판단
        if is_prime[i]:  # i가 소수인 경우
            for j in range(i * i, 10000, i):  # i의 배수들을 소수가 아니라고 표시
                is_prime[j] = False  # i의 배수들은 소수가 아니므로 False로 설정
                
    primes = [i for i in range(1000, 10000) if is_prime[i]]  # 1000 이상 9999 이하의 소수 리스트 생성
    return is_prime  # 소수 여부를 나타내는 배열 반환

def get_neighbors(num, is_prime):  # 주어진 숫자에서 한 자리만 바꿔서 나오는 네 자리 소수를 찾는 함수
    neighbors = []  # 이웃 소수를 저장할 리스트
    num_str = str(num)  # 숫자를 문자열로 변환하여 각 자리 수에 접근
    
    for i in range(4):  # 네 자리 수의 각 자리마다 반복
        for d in '0123456789':  # 각 자리 숫자를 0부터 9까지 대입
            if num_str[i] != d:  # 현재 자리 숫자와 다른 숫자로만 변경
                new_num = int(num_str[:i] + d + num_str[i+1:])  # 해당 자리를 새로운 숫자로 변경한 새로운 숫자 생성
                if new_num >= 1000 and is_prime[new_num]:  # 1000 이상이며 소수인 경우
                    neighbors.append(new_num)  # 이웃 소수 리스트에 추가
                    
    return neighbors  # 가능한 이웃 소수 리스트 반환

def bfs(start, end, is_prime):  # BFS를 사용해 최소 변환 횟수를 찾는 함수
    if start == end:  # 시작 소수와 끝 소수가 같으면 0 반환
        return 0
    
    queue = deque([(start, 0)])  # 큐에 시작 소수와 변환 횟수 0을 넣음
    visited = [False] * 10000  # 각 숫자가 방문되었는지 여부를 저장할 배열
    visited[start] = True  # 시작 소수는 방문했으므로 True로 설정
    
    while queue:  # 큐가 빌 때까지 반복
        current, steps = queue.popleft()  # 큐에서 현재 소수와 변환 횟수를 꺼냄
        
        for neighbor in get_neighbors(current, is_prime):  # 현재 소수에서 한 자리만 바꾼 소수들을 반복
            if not visited[neighbor]:  # 아직 방문하지 않은 소수에 대해
                if neighbor == end:  # 이웃 소수가 목표 소수와 같으면
                    return steps + 1  # 변환 횟수를 반환
                visited[neighbor] = True  # 방문 처리
                queue.append((neighbor, steps + 1))  # 이웃 소수와 변환 횟수를 큐에 추가
    
    return "Impossible"  # 목표 소수에 도달하지 못하면 "Impossible" 반환

def main():  # 메인 함수
    T = int(input())  # 테스트 케이스의 수 입력
    is_prime = sieve_of_eratosthenes()  # 미리 1000부터 9999까지의 소수를 구함
    
    for _ in range(T):  # 각 테스트 케이스에 대해
        start, end = map(int, input().split())  # 시작 소수와 목표 소수 입력
        result = bfs(start, end, is_prime)  # BFS로 최소 변환 횟수를 계산
        print(result)  # 결과 출력

if __name__ == "__main__":  # 프로그램의 시작점
    main()  # 메인 함수 호출
