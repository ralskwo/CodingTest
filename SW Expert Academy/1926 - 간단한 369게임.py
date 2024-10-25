def play_369_game(N):
    result = []
    for num in range(1, N + 1):
        num_str = str(num)
        clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')
        if clap_count > 0:
            result.append('-' * clap_count)
        else:
            result.append(num_str)
    # 출력 형식에 맞게 결과를 공백으로 구분하여 출력
    print(" ".join(result))

# 예시 입력
N = int(input())
play_369_game(N)