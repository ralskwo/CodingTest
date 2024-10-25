T = int(input().strip())

# 학점 목록을 준비합니다.
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T + 1):
    N, K = map(int, input().strip().split())

    # K번째 학생의 점수와 다른 학생들의 점수를 함께 저장합니다.
    scores = []
    for i in range(1, N + 1):
        mid, fin, ap = map(int, input().strip().split())
        total = mid * 0.35 + fin * 0.45 + ap * 0.2
        scores.append(total)

    # K번째 학생의 점수를 미리 저장
    target_score = scores[K - 1]

    # 점수를 내림차순으로 정렬하여 K번째 학생의 위치를 계산
    scores.sort(reverse=True)

    # K번째 학생의 위치를 찾아 학점을 할당
    rank = scores.index(target_score)
    grade_index = rank // (N // 10)

    print(f"#{t} {grade[grade_index]}")