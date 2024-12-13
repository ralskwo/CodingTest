from collections import defaultdict


# 최대 초밥 가짓수를 계산하는 함수
def max_sushi_variety():
    import sys

    input = sys.stdin.read  # 표준 입력을 읽는 함수 정의
    data = input().split()  # 입력 데이터를 공백 기준으로 분리하여 리스트로 저장

    # 첫 번째 줄에서 벨트 길이(N), 초밥 가짓수(d), 연속 먹기(k), 쿠폰 번호(c)를 읽음
    N, d, k, c = map(int, data[:4])

    # 벨트 위 초밥 종류를 리스트로 저장
    sushi = list(map(int, data[4:]))

    # 원형 벨트를 처리하기 위해 벨트를 2배로 확장
    sushi += sushi[: k - 1]

    # 현재 윈도우의 초밥 종류를 기록할 딕셔너리 생성
    sushi_count = defaultdict(int)
    current_variety = 0  # 현재 초밥 종류의 수

    # 초기 윈도우 설정: 첫 k개의 접시를 윈도우에 추가
    for i in range(k):
        if sushi_count[sushi[i]] == 0:  # 새로운 종류의 초밥이면
            current_variety += 1  # 종류 개수 증가
        sushi_count[sushi[i]] += 1  # 초밥 개수 증가

    # 쿠폰 초밥을 포함한 최대 종류 계산
    max_variety = current_variety + (1 if sushi_count[c] == 0 else 0)

    # 슬라이딩 윈도우를 이용해 벨트를 순회
    for i in range(k, len(sushi)):
        # 윈도우에서 벗어난 초밥 제거
        leaving_sushi = sushi[i - k]
        sushi_count[leaving_sushi] -= 1  # 초밥 개수 감소
        if sushi_count[leaving_sushi] == 0:  # 초밥 종류가 완전히 사라졌다면
            current_variety -= 1  # 종류 개수 감소

        # 윈도우에 새로 들어온 초밥 추가
        entering_sushi = sushi[i]
        if sushi_count[entering_sushi] == 0:  # 새로운 종류의 초밥이면
            current_variety += 1  # 종류 개수 증가
        sushi_count[entering_sushi] += 1  # 초밥 개수 증가

        # 쿠폰 초밥을 고려하여 최대 종류 갱신
        max_variety = max(
            max_variety, current_variety + (1 if sushi_count[c] == 0 else 0)
        )

    # 최종 계산된 최대 초밥 종류 출력
    print(max_variety)


# 프로그램 시작점 설정
if __name__ == "__main__":
    max_sushi_variety()
