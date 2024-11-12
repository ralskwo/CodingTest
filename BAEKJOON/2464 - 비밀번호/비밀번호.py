def find_nearest_numbers(A):
    # A보다 큰 수 중에서 1의 개수가 같은 가장 가까운 수를 찾는 함수 정의
    def next_same_bit_count(n):
        # 가장 오른쪽에 위치한 1 비트를 찾음
        smallest = n & -n
        # 가장 오른쪽 0 비트를 1로 변경하여 더 큰 수를 만듦
        ripple = n + smallest
        # 변경된 위치에서 발생한 비트 패턴을 계산
        ones = n ^ ripple
        # 필요한 1의 개수를 유지하며 비트들을 조정
        ones = (ones >> 2) // smallest
        # 새로운 수를 반환
        return ripple | ones

    # A보다 작은 수 중에서 1의 개수가 같은 가장 가까운 수를 찾는 함수 정의
    def prev_same_bit_count(n):
        # 입력된 n을 임시로 저장하여 비트 조작에 사용
        temp = n
        # 오른쪽에서부터 연속된 0과 1의 개수를 세기 위한 변수 초기화
        c0, c1 = 0, 0
        
        # 오른쪽부터 연속된 1의 개수를 셈
        while (temp & 1) == 1:
            c1 += 1
            temp >>= 1
        # 만약 1로만 이루어진 경우, 이전 수를 찾을 수 없으므로 0을 반환
        if temp == 0:
            return 0

        # 1 다음에 나오는 0의 개수를 셈
        while ((temp & 1) == 0) and (temp != 0):
            c0 += 1
            temp >>= 1
        
        # 변경해야 할 비트 위치 계산 (1 다음의 첫 번째 0 위치)
        p = c0 + c1

        # p 이후 모든 비트를 0으로 만듦으로써 1의 개수를 줄임
        n &= ((~0) << (p + 1))
        
        # 필요한 만큼 1 비트를 만든 후 왼쪽으로 이동하여 위치에 맞게 배치
        mask = (1 << (c1 + 1)) - 1
        n |= mask << (c0 - 1)
        
        # 재조정된 값을 반환
        return n

    # A보다 작은 수 중에서 1의 개수가 같은 가장 가까운 수를 찾음
    smaller = prev_same_bit_count(A)
    # A보다 큰 수 중에서 1의 개수가 같은 가장 가까운 수를 찾음
    larger = next_same_bit_count(A)

    # 결과값을 반환
    return smaller, larger

# 사용자로부터 정수 A를 입력받음
A = int(input().strip())
# A에 대해 작은 수와 큰 수를 찾는 함수를 호출하여 결과를 받음
smaller, larger = find_nearest_numbers(A)
# 결과값을 출력
print(smaller, larger)