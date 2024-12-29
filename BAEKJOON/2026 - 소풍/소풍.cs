using System;
using System.Collections.Generic;

class Program
{
    // 전역 변수 선언
    static int K, N, F;
    static List<HashSet<int>> friends = new List<HashSet<int>>();
    static List<int> selected = new List<int>();

    // 백트래킹 함수
    static void Backtrack(int start)
    {
        // 학생을 K명 선택한 경우 결과 출력
        if (selected.Count == K)
        {
            selected.Sort(); // 학생 번호를 오름차순으로 정렬
            foreach (var s in selected)
            {
                Console.WriteLine(s); // 한 줄씩 학생 번호 출력
            }
            Environment.Exit(0); // 프로그램 종료 (가장 먼저 찾은 경우)
        }

        // start부터 N까지 학생을 확인하며 선발
        for (int i = start; i <= N; i++)
        {
            bool canSelect = true;

            // 현재 학생 i가 이미 선택된 모든 학생과 친구 관계인지 확인
            foreach (var s in selected)
            {
                if (!friends[i].Contains(s))
                {
                    canSelect = false;
                    break;
                }
            }

            // 선택이 가능한 경우 학생 i를 추가하고 재귀 호출
            if (canSelect)
            {
                selected.Add(i);
                Backtrack(i + 1);  // 다음 학생을 탐색
                selected.RemoveAt(selected.Count - 1); // 탐색이 끝난 후 되돌리기 (백트래킹)
            }
        }
    }

    static void Main(string[] args)
    {
        // 입력 처리
        var inputs = Console.ReadLine().Split();
        K = int.Parse(inputs[0]);
        N = int.Parse(inputs[1]);
        F = int.Parse(inputs[2]);

        // 인접 리스트 초기화 (학생 번호 1부터 사용)
        for (int i = 0; i <= N; i++)
        {
            friends.Add(new HashSet<int>());
        }

        // 친구 관계 입력
        for (int i = 0; i < F; i++)
        {
            var friendInput = Console.ReadLine().Split();
            int a = int.Parse(friendInput[0]);
            int b = int.Parse(friendInput[1]);

            friends[a].Add(b);
            friends[b].Add(a); // 양방향 친구 관계 설정
        }

        // 백트래킹 탐색 시작
        Backtrack(1);

        // 조건을 만족하는 조합이 없는 경우
        Console.WriteLine("-1");
    }
}
