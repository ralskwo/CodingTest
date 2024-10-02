def find_minimum_unmeasurable_weight():
    N = int(input())  # 첫 번째 줄에서 저울추의 개수 N을 입력받는다.
    weights = list(map(int, input().split()))  # 두 번째 줄에서 저울추의 무게들을 리스트로 입력받는다.
    weights.sort()  # 저울추들을 오름차순으로 정렬한다.

    target = 1  # 만들 수 없는 최소 무게를 추적하기 위한 변수 target을 1로 초기화한다.

    for weight in weights:  # 정렬된 저울추들을 하나씩 순회한다.
        if weight > target:  # 현재 저울추의 무게가 target보다 크다면, target 무게는 만들 수 없는 무게가 된다.
            break  # 더 이상 만들 수 없는 무게가 결정되었으므로 반복문을 종료한다.
        target += weight  # 현재 저울추의 무게를 target에 더해준다.

    print(target)  # 최종적으로 만들 수 없는 최소 무게를 출력한다.

find_minimum_unmeasurable_weight()  # 함수 호출