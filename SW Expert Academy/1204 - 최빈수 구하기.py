from collections import Counter

T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    scores = Counter(list(map(int, input().split())))
    max_scores = max(scores.values())
    max_score = max([k for k, v in scores.items() if v == max_scores])

    print(f"#{t} {max_score}")
