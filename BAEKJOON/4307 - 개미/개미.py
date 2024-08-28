import sys  # sys 모듈을 가져와 표준 입력 및 출력을 최적화하여 사용하기 위해 import 합니다.
input = sys.stdin.read  # sys.stdin.read를 사용하여 입력을 한 번에 처리할 수 있게 합니다.

def ant_times(l, positions):  # 막대의 길이 l과 개미들의 위치 목록 positions을 받아 최소 시간과 최대 시간을 계산하는 함수입니다.
    min_time = 0  # 개미들이 떨어질 수 있는 최소 시간을 저장할 변수입니다.
    max_time = 0  # 개미들이 떨어질 수 있는 최대 시간을 저장할 변수입니다.
    
    for position in positions:  # 각 개미의 위치를 하나씩 순회하며
        # 개미가 떨어질 최소 시간: 막대의 양 끝 중 가까운 쪽으로 가는 시간을 계산합니다.
        min_time = max(min_time, min(position, l - position))
        
        # 개미가 떨어질 최대 시간: 막대의 양 끝 중 먼 쪽으로 가는 시간을 계산합니다.
        max_time = max(max_time, max(position, l - position))
    
    return min_time, max_time  # 최소 시간과 최대 시간을 반환합니다.

data = input().splitlines()  # 입력을 한 번에 읽어 들이고, 줄 단위로 나누어 리스트로 만듭니다.
test_cases = int(data[0])  # 첫 번째 줄은 테스트 케이스의 수입니다.
index = 1  # 현재 처리할 데이터의 시작 인덱스를 1로 설정합니다.

results = []  # 각 테스트 케이스의 결과를 저장할 리스트를 초기화합니다.
for _ in range(test_cases):  # 테스트 케이스의 수만큼 반복합니다.
    l, n = map(int, data[index].split())  # 막대의 길이 l과 개미의 수 n을 가져옵니다.
    positions = list(map(int, data[index+1:index+1+n]))  # n개의 개미 위치를 리스트로 만듭니다.
    min_time, max_time = ant_times(l, positions)  # ant_times 함수를 호출해 최소 시간과 최대 시간을 계산합니다.
    results.append(f"{min_time} {max_time}")  # 결과를 "최소시간 최대시간" 형식으로 리스트에 추가합니다.
    index += n + 1  # 다음 테스트 케이스로 이동하기 위해 인덱스를 갱신합니다.

sys.stdout.write("\n".join(results) + "\n")  # 결과를 한 번에 출력합니다.
