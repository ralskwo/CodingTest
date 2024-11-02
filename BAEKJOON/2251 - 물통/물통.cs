using System;
using System.Collections.Generic;

class Program {
    // 물을 옮기는 함수
    static (int, int) Pour(int x, int y, int max_y) {
        if (x + y > max_y)  // 목표 물통이 가득 차는 경우
            return (x + y - max_y, max_y);  // 넘치는 양만큼 출발 물통에 남기고 목표 물통은 가득 채웁니다.
        else
            return (0, x + y);  // 그렇지 않으면 출발 물통을 비우고 목표 물통을 채웁니다.
    }

    // 가능한 물의 양 계산 함수
    static List<int> PossibleAmounts(int A, int B, int C) {
        var visited = new HashSet<(int, int, int)>();  // 방문한 상태를 저장하는 집합
        var result = new SortedSet<int>();  // 첫 번째 물통이 비어 있을 때 세 번째 물통의 물의 양을 저장하는 집합
        var queue = new Queue<(int, int, int)>();  // BFS 탐색을 위한 큐

        queue.Enqueue((0, 0, C));  // 초기 상태 (0, 0, C)를 큐에 추가합니다.

        while (queue.Count > 0) {
            var (a, b, c) = queue.Dequeue();

            if (a == 0)  // 첫 번째 물통이 비어 있을 때
                result.Add(c);  // 세 번째 물통의 물의 양을 결과에 추가합니다.

            if (visited.Contains((a, b, c)))  // 이미 방문한 상태라면
                continue;  // 다음 상태로 넘어갑니다.
            visited.Add((a, b, c));  // 현재 상태를 방문 처리합니다.

            // 여섯 가지 물 옮기기 경우에 대해 BFS 큐에 추가
            int na, nb, nc;

            (na, nb) = Pour(a, b, B);  // A → B
            queue.Enqueue((na, nb, c));

            (na, nc) = Pour(a, c, C);  // A → C
            queue.Enqueue((na, b, nc));

            (nb, na) = Pour(b, a, A);  // B → A
            queue.Enqueue((na, nb, c));

            (nb, nc) = Pour(b, c, C);  // B → C
            queue.Enqueue((a, nb, nc));

            (nc, na) = Pour(c, a, A);  // C → A
            queue.Enqueue((na, b, nc));

            (nc, nb) = Pour(c, b, B);  // C → B
            queue.Enqueue((a, nb, nc));
        }

        return new List<int>(result);  // 결과를 리스트로 반환
    }

    static void Main() {
        string[] input = Console.ReadLine().Split();  // 입력 받기
        int A = int.Parse(input[0]);
        int B = int.Parse(input[1]);
        int C = int.Parse(input[2]);

        List<int> result = PossibleAmounts(A, B, C);  // 결과 계산

        Console.WriteLine(string.Join(" ", result));  // 결과 출력
    }
}