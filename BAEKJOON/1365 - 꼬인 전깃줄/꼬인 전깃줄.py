from bisect import bisect_left  # 이분 탐색을 위한 bisect_left 함수 임포트


def minimum_cut_wires(N, poles):
    lis = []  # 가장 긴 증가하는 부분 수열(LIS)을 저장할 리스트 초기화

    for pole in poles:  # 전봇대 연결 상태를 하나씩 순회
        pos = bisect_left(lis, pole)  # pole이 들어갈 위치를 이분 탐색으로 찾음
        if pos == len(lis):  # 찾은 위치가 현재 LIS의 길이와 같다면
            lis.append(pole)  # 새로운 값을 LIS 끝에 추가
        else:  # pole이 LIS의 중간에 들어갈 경우
            lis[pos] = pole  # LIS에서 해당 위치의 값을 pole로 교체

    return N - len(
        lis
    )  # 전체 전봇대 수에서 LIS의 길이를 뺀 값이 잘라야 할 최소 전선 개수


if __name__ == "__main__":
    N = int(input().strip())  # 전봇대의 개수 N을 입력받음
    poles = list(
        map(int, input().split())
    )  # N개의 전봇대 연결 상태를 리스트로 입력받음
    print(minimum_cut_wires(N, poles))  # 잘라야 할 전선의 최소 개수를 출력
