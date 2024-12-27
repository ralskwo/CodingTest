using System;
using System.Collections.Generic;

class Program {
    static void Main() {
        int T = int.Parse(Console.ReadLine());  // 테스트 케이스 개수 입력
        List<string> results = new List<string>();  // 결과를 저장할 리스트

        for (int t = 0; t < T; t++) {
            int N = int.Parse(Console.ReadLine());  // 수첩1의 크기
            HashSet<int> notebook1 = new HashSet<int>();  // 수첩1을 저장할 해시셋

            string[] notebook1Data = Console.ReadLine().Split();  // 수첩1의 정수들
            foreach (string s in notebook1Data) {
                notebook1.Add(int.Parse(s));  // 수첩1에 정수 삽입
            }

            int M = int.Parse(Console.ReadLine());  // 수첩2의 크기
            string[] notebook2Data = Console.ReadLine().Split();  // 수첩2의 정수들

            // 수첩2의 각 정수에 대해 존재 여부 확인
            foreach (string s in notebook2Data) {
                if (notebook1.Contains(int.Parse(s))) {
                    results.Add("1");  // 존재하면 1
                } else {
                    results.Add("0");  // 존재하지 않으면 0
                }
            }
        }

        // 결과 출력
        Console.WriteLine(string.Join("\n", results));
    }
}
