def calculate_gaps(angles):
    # 각도를 정렬하여 시계방향 순서로 정리
    angles.sort()
    # 각도의 개수를 n에 저장
    n = len(angles)
    # 각도 간의 간격을 저장할 리스트 생성
    gaps = []
    # 정렬된 각도 리스트에서 인접한 각도 간의 차이를 계산하여 gaps 리스트에 추가
    for i in range(n - 1):
        gaps.append(angles[i + 1] - angles[i])
    # 마지막 각도와 첫 번째 각도의 차이(원형 구조를 고려한 간격)를 계산하여 gaps에 추가
    gaps.append(360000 - angles[-1] + angles[0])
    # 간격 리스트 반환
    return gaps

def kmp_search(text, pattern):
    # 텍스트와 패턴의 길이를 각각 n, m에 저장
    n, m = len(text), len(pattern)
    # LPS(Longest Prefix Suffix) 배열을 초기화
    lps = [0] * m
    # 패턴 비교 인덱스를 나타내는 j를 0으로 초기화
    j = 0
    # LPS 배열을 채우기 위한 초기 인덱스를 1로 설정
    i = 1
    # LPS 배열을 구축하는 과정
    while i < m:
        # 패턴의 현재 문자와 비교 인덱스가 가리키는 문자가 같을 때
        if pattern[i] == pattern[j]:
            # 접두사와 접미사의 길이를 증가시키고 lps 배열에 기록
            j += 1
            lps[i] = j
            i += 1
        else:
            # 문자가 일치하지 않을 경우
            if j != 0:
                # 이전 접두사 길이로 이동
                j = lps[j - 1]
            else:
                # 초기 접두사 길이로 설정
                lps[i] = 0
                i += 1
    
    # 패턴 검색을 위한 초기 인덱스 설정
    i = 0
    j = 0
    # 텍스트 내에서 패턴을 찾기 위한 탐색 과정
    while i < n:
        # 패턴과 텍스트의 문자가 일치할 경우
        if pattern[j] == text[i]:
            i += 1
            j += 1
        # 패턴 전체를 찾았을 때
        if j == m:
            return True
        # 문자 불일치가 발생할 때
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                # LPS 배열을 참고하여 j의 위치 조정
                j = lps[j - 1]
            else:
                i += 1
    # 패턴이 텍스트에 존재하지 않는 경우 False 반환
    return False

# 입력된 각도 수를 n에 저장
n = int(input())
# 첫 번째 시계의 각도들을 angles1에 저장
angles1 = list(map(int, input().split()))
# 두 번째 시계의 각도들을 angles2에 저장
angles2 = list(map(int, input().split()))

# 첫 번째 시계의 각도 간격 계산
gaps1 = calculate_gaps(angles1)
# 두 번째 시계의 각도 간격 계산
gaps2 = calculate_gaps(angles2)

# 첫 번째 시계의 간격 리스트를 두 배로 확장하여 회전 가능한 모든 경우 고려
doubled_gaps1 = gaps1 + gaps1

# 첫 번째 시계의 확장된 간격 리스트에서 두 번째 시계의 간격 리스트가 발견되면 같은 시각이 가능한 것으로 판단
if kmp_search(doubled_gaps1, gaps2):
    print("possible")
else:
    print("impossible")