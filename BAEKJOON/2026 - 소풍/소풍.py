import sys  # 표준 라이브러리 sys 불러오기 (입출력 및 재귀 한도 설정을 위해 사용)

input = sys.stdin.read  # 표준 입력을 한 번에 읽어오는 함수 설정
sys.setrecursionlimit(
    10000
)  # 재귀 호출 제한을 10000으로 설정 (백트래킹 중 깊은 재귀를 허용하기 위함)


def picnic(
    K, N, F, friendships
):  # 소풍에 참가할 학생을 선발하는 함수 정의 (K: 선발할 학생 수, N: 전체 학생 수, F: 친구 관계 수, friendships: 친구 관계 리스트)
    friends = [
        set() for _ in range(N + 1)
    ]  # 학생 번호를 인덱스로 하여 각 학생의 친구를 저장할 집합 리스트 초기화 (1번 학생부터 사용하기 때문에 N+1 크기로 설정)

    for a, b in friendships:  # 모든 친구 관계에 대해 반복
        friends[a].add(b)  # a 학생의 친구 목록에 b 추가
        friends[b].add(
            a
        )  # b 학생의 친구 목록에 a 추가 (친구 관계는 양방향이므로 반대로도 추가)

    def backtrack(
        selected,
    ):  # 백트래킹을 수행하는 재귀 함수 (selected: 현재까지 선택된 학생 목록)
        if len(selected) == K:  # 선택된 학생 수가 K명과 같으면 조건 충족
            for s in sorted(selected):  # 학생 번호를 오름차순으로 정렬하여 출력
                print(s)  # 학생 번호 출력
            exit(0)  # 프로그램 종료 (첫 번째로 찾은 경우 바로 종료)

        start = (
            selected[-1] + 1 if selected else 1
        )  # 다음 학생 선택 범위 설정 (선택된 학생이 없으면 1번부터 시작, 선택된 학생이 있으면 가장 큰 번호 + 1부터 시작)

        for i in range(start, N + 1):  # start부터 N까지 학생을 순차적으로 확인
            if all(
                i in friends[s] for s in selected
            ):  # 현재 학생 i가 이미 선택된 모든 학생과 친구 관계인지 확인
                backtrack(
                    selected + [i]
                )  # 조건을 만족하면 학생 i를 선택에 추가하고 재귀 호출

    backtrack([])  # 백트래킹 탐색 시작 (초기에는 빈 리스트로 시작)
    print(-1)  # 조건을 만족하는 학생 조합을 찾지 못한 경우 -1 출력


if (
    __name__ == "__main__"
):  # 프로그램이 직접 실행될 경우에만 아래 코드 실행 (모듈로 임포트될 경우 실행되지 않음)
    data = (
        input().splitlines()
    )  # 표준 입력으로 받은 데이터를 줄 단위로 분리하여 리스트로 저장
    K, N, F = map(int, data[0].split())  # 첫 줄에서 K, N, F 값을 정수로 변환하여 할당
    friendships = [
        tuple(map(int, line.split())) for line in data[1:]
    ]  # 두 번째 줄부터 친구 관계를 튜플 형태로 변환하여 리스트로 저장

    picnic(K, N, F, friendships)  # picnic 함수 호출하여 프로그램 실행
