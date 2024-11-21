def generate_expressions(n, current_expr, results):
    # 현재 생성된 수식이 완성되었는지 확인. 숫자와 연산자가 모두 포함된 경우
    if len(current_expr) == 2 * n - 1:
        # 공백을 제거하고 계산 가능한 수식으로 변환
        expr = current_expr.replace(" ", "")
        # 계산 결과가 0인 경우 결과 리스트에 추가
        if eval(expr) == 0:
            results.append(current_expr)
        return

    # 다음에 추가될 숫자를 계산 (현재 길이를 기준으로 계산)
    next_num = len(current_expr) // 2 + 2
    # '+' 연산자를 추가한 수식으로 재귀 호출
    generate_expressions(n, current_expr + "+" + str(next_num), results)
    # '-' 연산자를 추가한 수식으로 재귀 호출
    generate_expressions(n, current_expr + "-" + str(next_num), results)
    # ' '(공백)을 추가한 수식으로 재귀 호출
    generate_expressions(n, current_expr + " " + str(next_num), results)


def solve_zero_sum_expressions():
    # 테스트 케이스의 개수를 입력 받음
    t = int(input().strip())
    # 테스트 케이스에서 주어지는 숫자 N들을 리스트로 저장
    test_cases = [int(input().strip()) for _ in range(t)]

    # 각 테스트 케이스에 대해 반복
    for case_idx, n in enumerate(test_cases):
        # 0이 되는 수식을 저장할 리스트 초기화
        results = []
        # 숫자 1로 시작하는 수식을 생성하는 재귀 호출 시작
        generate_expressions(n, "1", results)
        # 생성된 결과를 ASCII 순서로 정렬
        results.sort()
        # 결과 리스트의 각 수식을 출력
        for result in results:
            print(result)
        # 테스트 케이스 사이에 빈 줄 출력 (마지막 테스트 케이스 제외)
        if case_idx != len(test_cases) - 1:
            print()


# 프로그램 실행
solve_zero_sum_expressions()
