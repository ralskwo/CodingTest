def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    # 첫 번째 입력값을 정수로 변환하여 추의 개수를 저장
    n = int(data[0])

    # 두 번째부터 n개의 값을 정수로 변환하여 추의 무게 리스트로 저장
    weights = list(map(int, data[1 : n + 1]))

    # 추 뒤에 오는 값을 정수로 변환하여 구슬의 개수를 저장
    m = int(data[n + 1])

    # 구슬의 무게들을 정수로 변환하여 리스트로 저장
    marbles = list(map(int, data[n + 2 :]))

    # 추의 무게 총합을 계산하여 가능한 무게의 최대치를 구함
    max_weight = sum(weights)

    # 0부터 max_weight까지의 무게를 체크하기 위한 DP 테이블 생성
    dp = [False] * (max_weight + 1)

    # 무게 0은 항상 만들 수 있으므로 True로 설정
    dp[0] = True

    # 각 추에 대해 DP 테이블을 갱신
    for weight in weights:
        # 기존 DP 테이블 값을 복사하여 현재 추를 추가한 후 결과를 저장할 테이블 생성
        current = dp[:]

        # 모든 무게를 확인하며 가능한 새로운 무게를 DP 테이블에 추가
        for w in range(max_weight + 1):
            if dp[w]:  # 현재 무게가 True일 때만 처리
                # 추를 왼쪽에 올렸을 때의 무게를 갱신
                if w + weight <= max_weight:
                    current[w + weight] = True
                # 추를 오른쪽에 올렸을 때의 무게를 갱신
                if abs(w - weight) <= max_weight:
                    current[abs(w - weight)] = True

        # DP 테이블을 현재 상태로 갱신
        dp = current

    # 구슬 무게 확인 결과를 저장할 리스트 생성
    result = []

    # 각 구슬의 무게를 DP 테이블에서 확인
    for marble in marbles:
        # 구슬의 무게가 DP 테이블에서 가능한 무게로 표시되어 있으면 Y 추가
        if marble <= max_weight and dp[marble]:
            result.append("Y")
        else:  # 그렇지 않으면 N 추가
            result.append("N")

    # 결과 리스트를 공백으로 구분하여 출력
    print(" ".join(result))


if __name__ == "__main__":
    # 메인 함수로 실행될 때 solve 함수 호출
    solve()
