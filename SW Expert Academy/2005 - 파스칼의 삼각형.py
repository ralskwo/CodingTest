T = int(input().strip())

for t in range(1, T + 1):
    pascal_Triangle = int(input().strip())
    print(f"#{t}")

    bef = []  # 이전 줄 저장 리스트
    for i in range(1, pascal_Triangle + 1):
        tmp = []  # 현재 줄 저장 리스트
        for n in range(0, i):
            # 양 끝값은 1로 설정
            if n == 0 or n == i - 1:
                tmp.append('1')
            else:
                # 내부 값은 이전 줄의 두 값의 합
                tmp.append(str(int(bef[n - 1]) + int(bef[n])))
        # 현재 줄 출력
        print(" ".join(tmp))
        # 현재 줄을 다음 계산을 위해 이전 줄로 저장
        bef = tmp
