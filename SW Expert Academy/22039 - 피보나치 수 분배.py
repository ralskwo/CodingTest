def generate_fibonacci(n):
    # 피보나치 수열 생성 함수
    # n개까지의 피보나치 수열 값을 계산하여 리스트로 반환
    fib = [1, 1]  # 초기 두 값 설정
    while len(fib) < n:  # n개가 될 때까지 반복
        fib.append(fib[-1] + fib[-2])  # 직전 두 값을 더하여 추가
    return fib  # 피보나치 수열 리스트 반환


def solve_partition_problem(n, fib):
    # 주어진 n에 대해 피보나치 수를 두 집합으로 나누는 문제를 해결
    total_sum = sum(fib[:n])  # n개의 피보나치 수의 총합 계산
    if total_sum % 2 != 0:  # 총합이 홀수이면 분할이 불가능
        return "impossible"  # "impossible" 반환

    target = total_sum // 2  # 두 집합의 목표 합 계산
    subset_sum = 0  # 집합 A의 현재 합 초기화
    partition = ["B"] * n  # 모든 요소를 집합 B로 초기화

    for i in range(n - 1, -1, -1):  # 피보나치 수열을 역순으로 확인
        if (
            subset_sum + fib[i] <= target
        ):  # 현재 합에 피보나치 값을 더해도 목표를 초과하지 않으면
            subset_sum += fib[i]  # 집합 A에 추가
            partition[i] = "A"  # i번째 요소를 집합 A로 변경
        if subset_sum == target:  # 목표 합에 도달하면 중단
            break

    if subset_sum != target:  # 목표 합에 도달하지 못하면
        return "impossible"  # "impossible" 반환
    return "".join(partition)  # 분할 결과 문자열 반환


def main():
    # 메인 함수: 입력을 처리하고 결과를 출력
    t = int(input())  # 테스트 케이스 개수 입력
    test_cases = [int(input()) for _ in range(t)]  # 각 테스트 케이스 입력
    max_n = max(test_cases)  # 테스트 케이스 중 가장 큰 N 값을 확인

    fib = generate_fibonacci(max_n)  # 가장 큰 N에 대한 피보나치 수열 생성

    results = [
        solve_partition_problem(n, fib) for n in test_cases
    ]  # 각 테스트 케이스에 대해 문제 해결
    print("\n".join(results))  # 결과를 출력


if __name__ == "__main__":
    # 프로그램 시작점
    main()  # 메인 함수 호출
