import bisect  # bisect 모듈을 사용하여 이분 탐색 기능을 제공

def count_catchable_animals(m, n, l, shooting_spots, animals):
    shooting_spots.sort()  # 사대 위치를 오름차순으로 정렬
    catchable_count = 0  # 잡을 수 있는 동물의 수를 저장할 변수 초기화
    
    for x, y in animals:  # 각 동물에 대해 반복
        if y > l:  # 동물의 y 좌표가 사정거리 L보다 크면 사냥 불가능
            continue  # 해당 동물은 건너뛰기
        
        idx = bisect.bisect_left(shooting_spots, x)  # 이분 탐색으로 동물의 x 좌표에 가장 가까운 사대를 찾음
        
        is_catchable = False  # 해당 동물이 잡힐 수 있는지 여부를 저장할 변수 초기화
        
        if idx < len(shooting_spots):  # 찾은 사대의 인덱스가 유효한지 확인
            if abs(shooting_spots[idx] - x) + y <= l:  # 해당 사대와의 거리 계산 후 사정거리 내에 있으면
                is_catchable = True  # 잡을 수 있는 동물로 표시
        
        if idx > 0:  # 사대의 이전 위치도 확인 (가장 가까운 사대가 이전 사대일 수 있음)
            if abs(shooting_spots[idx - 1] - x) + y <= l:  # 이전 사대와의 거리 계산 후 사정거리 내에 있으면
                is_catchable = True  # 잡을 수 있는 동물로 표시
        
        if is_catchable:  # 동물이 잡을 수 있는 상태이면
            catchable_count += 1  # 잡을 수 있는 동물의 수를 증가시킴
    
    return catchable_count  # 최종적으로 잡을 수 있는 동물의 수 반환

m, n, l = map(int, input().split())  # 사대의 수, 동물의 수, 사정거리 L 입력 받기
shooting_spots = list(map(int, input().split()))  # 사대의 위치를 리스트로 입력 받기
animals = [tuple(map(int, input().split())) for _ in range(n)]  # 각 동물의 위치를 리스트로 입력 받기

result = count_catchable_animals(m, n, l, shooting_spots, animals)  # 동물들을 잡을 수 있는지 계산
print(result)  # 결과 출력
