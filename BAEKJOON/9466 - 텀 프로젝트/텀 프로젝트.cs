using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static int FindTeams(int n, List<int> choices)
    {
        int[] visited = new int[n + 1]; // 방문 상태를 저장하는 배열 초기화
        int[] team = new int[n + 1]; // 팀에 속한 상태를 저장하는 배열 초기화
        int teamCount = 0; // 팀의 개수 초기화

        for (int student = 1; student <= n; ++student) // 모든 학생에 대해 탐색 시작
        {
            if (visited[student] == 0) // 해당 학생이 방문되지 않은 경우
            {
                Stack<int> stack = new Stack<int>(); // 스택 초기화
                int current = student; // 현재 학생을 현재 위치로 설정

                while (visited[current] == 0) // 현재 학생이 방문되지 않은 경우 반복
                {
                    visited[current] = student; // 현재 학생을 방문 상태로 설정
                    stack.Push(current); // 현재 학생을 스택에 추가
                    current = choices[current]; // 다음 학생으로 이동
                }

                if (visited[current] == student) // 싸이클이 형성된 경우
                {
                    while (stack.Count > 0 && stack.Peek() != current) // 스택에서 싸이클의 시작점까지 팝
                    {
                        team[stack.Pop()] = 1; // 싸이클에 속한 학생을 팀에 속한 것으로 설정
                    }
                    team[stack.Pop()] = 1; // 싸이클의 시작점을 팀에 속한 것으로 설정
                    teamCount += 1; // 팀의 개수 증가
                }

                while (stack.Count > 0) // 남아있는 스택 요소 처리
                {
                    team[stack.Pop()] = 0; // 싸이클에 속하지 않은 학생을 팀에 속하지 않은 것으로 설정
                }
            }
        }

        return n - team.Sum(); // 팀에 속하지 않은 학생의 수 반환
    }

    static void Main()
    {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스의 수

        List<int> results = new List<int>(); // 결과를 저장할 리스트 초기화

        for (int t = 0; t < T; t++)
        {
            int n = int.Parse(Console.ReadLine()); // 학생의 수
            List<int> choices = Console.ReadLine().Split().Select(int.Parse).ToList();
            choices.Insert(0, 0); // 배열의 0번 인덱스를 채우기 위해 앞에 0 추가

            int result = FindTeams(n, choices); // 팀에 속하지 않은 학생의 수 계산
            results.Add(result); // 결과 리스트에 추가
        }

        foreach (int res in results) // 각 테스트 케이스의 결과 출력
        {
            Console.WriteLine(res);
        }
    }
}
