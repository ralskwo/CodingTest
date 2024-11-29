using System;
using System.Linq; // 배열 작업에 필요한 메서드를 위해 추가

class Program {
    static void Main(string[] args) {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스 개수 읽기
        
        for (int t = 0; t < T; t++) {
            // 각 테스트 케이스의 첫 번째 줄 읽기
            var firstLine = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int N = firstLine[0], M = firstLine[1], K = firstLine[2];
            
            // 각 집의 돈 정보 읽기
            var money = Console.ReadLine().Split().Select(int.Parse).ToArray();

            // 특수 케이스 처리: M == N인 경우
            if (M == N) {
                int totalSum = money.Sum(); // 전체 집의 돈 합계 계산
                Console.WriteLine(totalSum < K ? 1 : 0); // 조건에 따라 결과 출력
                continue; // 다음 테스트 케이스로 넘어감
            }

            // 슬라이딩 윈도우 초기화
            int currentSum = 0;
            for (int i = 0; i < M; i++) {
                currentSum += money[i]; // 처음 M개의 집의 합 계산
            }

            int count = 0; // 조건을 만족하는 경우의 수

            // 슬라이딩 윈도우 실행
            for (int i = 0; i < N; i++) {
                if (currentSum < K) {
                    count++; // 조건을 만족하면 카운트 증가
                }

                // 윈도우 이동: 첫 번째 값 제거, 새로운 값 추가
                currentSum -= money[i];
                currentSum += money[(i + M) % N]; // 원형 배열 처리
            }

            Console.WriteLine(count); // 결과 출력
        }
    }
}
