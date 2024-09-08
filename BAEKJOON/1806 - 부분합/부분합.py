# 첫 번째 줄에서 N(수열의 길이)과 S(부분합의 최소 값)를 입력받아 각각 N과 S에 저장한다.
N, S = map(int, input().split())  

# 두 번째 줄에서 수열의 각 원소를 공백으로 구분하여 입력받고, 이를 리스트로 변환하여 numbers에 저장한다.
numbers = list(map(int, input().split()))  

# 시작 포인터(start)와 끝 포인터(end)를 0으로 초기화한다. 이 포인터들은 슬라이딩 윈도우를 구성하는 데 사용된다.
start, end = 0, 0  

# 현재까지 계산한 부분합을 저장할 변수 current_sum을 0으로 초기화한다.
current_sum = 0  

# 최소 길이를 저장할 변수 min_length를 무한대(inf)로 초기화한다. 나중에 더 작은 값이 나오면 갱신할 것이다.
min_length = float('inf')  

# 종료 조건을 만족할 때까지 반복을 계속한다.
while True:  
    
    # 현재 부분합이 S 이상인 경우, 해당 부분합을 만족하는 구간이므로 처리한다.
    if current_sum >= S:  
        
        # 현재 부분합을 만족하는 구간의 길이와 현재까지의 최소 길이를 비교하여 더 작은 값을 min_length에 저장한다.
        min_length = min(min_length, end - start)  
        
        # 현재 시작점의 값을 부분합에서 제외하여 슬라이딩 윈도우를 줄인다.
        current_sum -= numbers[start]  
        
        # 시작 포인터를 오른쪽으로 한 칸 이동시킨다.
        start += 1  
    
    # 끝 포인터가 수열의 끝에 도달한 경우, 더 이상 확장할 수 없으므로 반복을 종료한다.
    elif end == N:  
        break  
    
    # 현재 부분합이 S보다 작고, 아직 수열의 끝에 도달하지 않은 경우.
    else:  
        
        # 끝 포인터가 가리키는 값을 부분합에 더하여 슬라이딩 윈도우를 확장한다.
        current_sum += numbers[end]  
        
        # 끝 포인터를 오른쪽으로 한 칸 이동시킨다.
        end += 1  

# 만약 최소 길이가 여전히 무한대인 경우, 부분합을 만족하는 구간이 없다는 의미이므로 0을 출력한다.
if min_length == float('inf'):  
    print(0)  
    
# 최소 길이가 갱신되었으면 그 값을 출력한다.
else:  
    print(min_length)
