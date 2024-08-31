using System;            // 표준 입출력 사용
using System.Collections.Generic;  // List 및 Queue 사용

class Program {
    static int MinOperations(int n, int m, List<int> positions) {
        LinkedList<int> dq = new LinkedList<int>();  // 큐를 초기화할 LinkedList 선언
        for (int i = 1; i <= n; i++) {
            dq.AddLast(i);  // 1부터 n까지의 숫자를 큐에 추가
        }

        int operations = 0;  // 연산 횟수를 저장할 변수

        foreach (int position in positions) {
            int idx = 0;
            foreach (var item in dq) {
                if (item == position) break;  // 목표 위치를 찾으면 루프 종료
                idx++;  // 목표 위치까지의 인덱스 계산
            }

            if (idx < dq.Count - idx) {  // 왼쪽으로 회전하는 것이 빠른 경우
                operations += idx;  // 왼쪽으로 회전한 횟수를 누적
                for (int j = 0; j < idx; j++) {
                    dq.AddLast(dq.First.Value);  // 큐의 맨 앞 원소를 맨 뒤로 이동
                    dq.RemoveFirst();  // 맨 앞 원소 제거
                }
            } else {  // 오른쪽으로 회전하는 것이 빠른 경우
                operations += dq.Count - idx;  // 오른쪽으로 회전한 횟수를 누적
                for (int j = 0; j < dq.Count - idx; j++) {
                    dq.AddFirst(dq.Last.Value);  // 큐의 맨 뒤 원소를 맨 앞으로 이동
                    dq.RemoveLast();  // 맨 뒤 원소 제거
                }
            }

            dq.RemoveFirst();  // 목표 위치의 원소를 큐에서 제거
        }

        return operations;  // 총 연산 횟수를 반환
    }

    static void Main() {
        string[] input = Console.ReadLine().Split();  // 큐의 크기 n과 뽑아낼 위치의 수 m 입력받기
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        List<int> positions = new List<int>();  // 뽑아낼 위치를 저장할 List
        string[] posInput = Console.ReadLine().Split();
        for (int i = 0; i < m; i++) {
            positions.Add(int.Parse(posInput[i]));  // 뽑아낼 위치 입력
        }

        Console.WriteLine(MinOperations(n, m, positions));  // 최소 연산 횟수를 계산하고 출력
    }
}
