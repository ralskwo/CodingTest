def count_ways_to_steal():
    import sys  # 표준 입력을 사용하기 위해 sys 모듈을 가져옵니다.

    input = sys.stdin.read  # 표준 입력을 읽기 위한 함수 참조를 가져옵니다.
    data = input().splitlines()  # 입력 데이터를 줄 단위로 분리하여 리스트로 저장합니다.

    T = int(data[0])  # 첫 번째 줄에 주어진 테스트 케이스의 개수를 정수로 변환합니다.
    results = []  # 각 테스트 케이스의 결과를 저장할 리스트를 초기화합니다.

    index = 1  # 입력 데이터를 순회할 때 사용할 인덱스를 초기화합니다.
    for _ in range(T):  # 각 테스트 케이스에 대해 반복합니다.
        # 현재 테스트 케이스의 정보(N, M, K)를 정수로 변환하여 읽어옵니다.
        N, M, K = map(int, data[index].split())
        index += 1  # 다음 줄로 인덱스를 이동합니다.

        # 현재 테스트 케이스에서 각 집의 돈의 양을 리스트로 읽어옵니다.
        money = list(map(int, data[index].split()))
        index += 1  # 다음 줄로 인덱스를 이동합니다.

        # 특수 케이스: 연속된 집의 수 M이 전체 집의 수 N과 같은 경우
        if M == N:
            # 전체 집의 돈의 합이 K보다 작으면 1을 결과에 추가, 아니면 0을 추가합니다.
            if sum(money) < K:
                results.append(1)
            else:
                results.append(0)
            continue  # 다음 테스트 케이스로 넘어갑니다.

        # 초기 슬라이딩 윈도우 합을 계산합니다. 처음 M개의 집의 돈의 합입니다.
        current_sum = sum(money[:M])
        count = 0  # 현재 조건을 만족하는 방법의 수를 초기화합니다.

        # 슬라이딩 윈도우를 이용해 원형 구조에서 모든 연속된 M개의 집을 검사합니다.
        for i in range(N):
            # 현재 슬라이딩 윈도우의 합이 K보다 작으면 방법 수를 증가시킵니다.
            if current_sum < K:
                count += 1

            # 슬라이딩 윈도우를 업데이트합니다.
            # 윈도우에서 빠져나가는 집의 돈을 뺍니다.
            current_sum -= money[i]
            # 윈도우에 새로 추가되는 집의 돈을 더합니다. 원형 구조를 고려하여 % N을 사용합니다.
            current_sum += money[(i + M) % N]

        # 현재 테스트 케이스에서 가능한 방법 수를 결과 리스트에 추가합니다.
        results.append(count)

    # 모든 테스트 케이스의 결과를 출력합니다.
    for result in results:
        print(result)


# 이 코드는 실행 시점에서 실행되며, 메인 프로그램의 시작점을 정의합니다.
if __name__ == "__main__":
    count_ways_to_steal()
