import heapq  # 힙큐 모듈을 불러옵니다. 이 모듈을 사용하여 우선순위 큐를 구현합니다.

def solve():
    import sys  # 시스템 모듈을 불러옵니다.
    input = sys.stdin.read  # 표준 입력을 읽는 함수를 설정합니다.
    data = input().split()  # 입력 데이터를 공백으로 분리하여 리스트로 만듭니다.
    
    n = int(data[0])  # 보석의 수 N을 입력 받습니다.
    k = int(data[1])  # 가방의 수 K를 입력 받습니다.
    
    jewels = []  # 보석 정보를 저장할 리스트를 초기화합니다.
    index = 2  # 보석 정보가 시작되는 인덱스를 설정합니다.
    for _ in range(n):
        m = int(data[index])  # 보석의 무게를 입력 받습니다.
        v = int(data[index + 1])  # 보석의 가격을 입력 받습니다.
        jewels.append((m, v))  # 보석의 무게와 가격을 튜플로 저장합니다.
        index += 2  # 다음 보석 정보를 가리키도록 인덱스를 증가시킵니다.
    
    bags = []  # 가방 정보를 저장할 리스트를 초기화합니다.
    for _ in range(k):
        c = int(data[index])  # 가방의 최대 무게를 입력 받습니다.
        bags.append(c)  # 가방의 최대 무게를 리스트에 저장합니다.
        index += 1  # 다음 가방 정보를 가리키도록 인덱스를 증가시킵니다.
    
    # 보석을 무게 오름차순으로 정렬합니다.
    jewels.sort()
    # 가방을 무게 오름차순으로 정렬합니다.
    bags.sort()
    
    max_value = 0  # 챙길 수 있는 보석 가격의 합의 최대값을 저장할 변수를 초기화합니다.
    possible_jewels = []  # 현재 가방에 담을 수 있는 보석들을 저장할 최대 힙을 초기화합니다.
    jewel_index = 0  # 보석 리스트의 현재 인덱스를 초기화합니다.
    
    # 각 가방에 대해 반복합니다.
    for bag in bags:
        # 현재 가방에 담을 수 있는 모든 보석을 힙에 넣습니다.
        while jewel_index < len(jewels) and jewels[jewel_index][0] <= bag:
            # 힙에 넣을 때 가격을 음수로 저장하여 최대 힙을 만듭니다.
            heapq.heappush(possible_jewels, -jewels[jewel_index][1])
            jewel_index += 1  # 다음 보석으로 이동합니다.
        # 가장 비싼 보석을 선택합니다.
        if possible_jewels:
            # 힙에서 가장 큰 값을 꺼내어 max_value에 더합니다.
            max_value += -heapq.heappop(possible_jewels)
    
    print(max_value)  # 최종적으로 챙길 수 있는 보석 가격의 합의 최대값을 출력합니다.

if __name__ == "__main__":
   solve()