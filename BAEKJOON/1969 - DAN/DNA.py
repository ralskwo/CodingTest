def find_min_hamming_dna(N, M, dna_list):
    # 문자열 빈도 계산을 위해 Counter 모듈을 가져온다
    from collections import Counter

    # 최소 거리 DNA를 저장할 변수
    min_distance_dna = ""
    # Hamming Distance 총합을 저장할 변수
    total_hamming_distance = 0

    # 각 열(column)마다 반복
    for col in range(M):
        # 현재 열에서 모든 DNA 문자열의 해당 위치 문자들을 추출
        column_nucleotides = [dna[col] for dna in dna_list]

        # 현재 열에서 문자의 빈도를 계산
        freq = Counter(column_nucleotides)

        # 빈도가 가장 높은 문자를 선택하며, 빈도가 같다면 사전순으로 가장 앞선 문자를 선택
        most_common = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[0][0]

        # 최소 거리 DNA에 가장 빈번한 문자를 추가
        min_distance_dna += most_common

        # 현재 열에서 Hamming Distance에 해당하는 문자 수를 계산
        # 전체 문자의 개수에서 가장 빈번한 문자의 개수를 뺀 값을 더함
        total_hamming_distance += sum(freq.values()) - freq[most_common]

    # 최소 거리 DNA와 총 Hamming Distance를 반환
    return min_distance_dna, total_hamming_distance


# DNA의 개수와 문자열의 길이를 입력받음
N, M = map(int, input().split())

# 각 DNA 문자열을 입력받아 리스트에 저장
dna_list = [input().strip() for _ in range(N)]

# 최소 거리 DNA와 Hamming Distance 총합을 계산
result_dna, hamming_distance = find_min_hamming_dna(N, M, dna_list)

# 최소 거리 DNA를 출력
print(result_dna)

# Hamming Distance의 총합을 출력
print(hamming_distance)
