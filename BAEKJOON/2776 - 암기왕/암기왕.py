import sys

input = sys.stdin.read


def main():
    # 입력을 모두 읽어와서 줄 단위로 나눈다
    data = input().splitlines()
    idx = 0

    # 첫 번째 줄에서 테스트 케이스 개수 T를 가져온다
    T = int(data[idx])
    idx += 1

    # 결과를 저장할 리스트를 초기화한다
    results = []

    # T번 만큼 테스트 케이스를 반복한다
    for _ in range(T):
        # 수첩1에 적힌 정수의 개수 N을 읽는다
        N = int(data[idx])

        # N개의 정수를 공백 기준으로 나누어 집합 notebook1에 저장한다
        notebook1 = set(map(int, data[idx + 1].split()))
        idx += 2

        # 수첩2에 적힌 정수의 개수 M을 읽는다
        M = int(data[idx])

        # M개의 정수를 리스트 notebook2에 저장한다
        notebook2 = list(map(int, data[idx + 1].split()))
        idx += 2

        # notebook2의 각 정수에 대해 notebook1에 존재하는지 확인한다
        for number in notebook2:
            if number in notebook1:
                # 존재하면 결과 리스트에 1을 추가한다
                results.append("1")
            else:
                # 존재하지 않으면 결과 리스트에 0을 추가한다
                results.append("0")

    # 결과 리스트를 개행 문자로 연결하여 한 번에 출력한다
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
