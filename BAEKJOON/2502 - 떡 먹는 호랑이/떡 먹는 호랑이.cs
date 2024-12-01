using System;

class Program {
    static (int, int) FindAandB(int D, int K) {
        // 계수를 저장할 배열 초기화
        int[,] coeff = new int[D + 1, 2];
        coeff[1, 0] = 1; // 첫째 날: A의 계수
        coeff[1, 1] = 0;
        coeff[2, 0] = 0; // 둘째 날: B의 계수
        coeff[2, 1] = 1;

        // 점화식을 통해 D일까지의 계수를 계산
        for (int i = 3; i <= D; i++) {
            coeff[i, 0] = coeff[i - 2, 0] + coeff[i - 1, 0]; // A의 계수
            coeff[i, 1] = coeff[i - 2, 1] + coeff[i - 1, 1]; // B의 계수
        }

        // A를 1부터 탐색하며 조건을 만족하는 A와 B를 찾음
        for (int A = 1; A <= K / coeff[D, 0]; A++) {
            if ((K - A * coeff[D, 0]) % coeff[D, 1] == 0) {
                int B = (K - A * coeff[D, 0]) / coeff[D, 1]; // B 계산
                return (A, B); // A와 B 반환
            }
        }

        return (-1, -1); // 문제 조건에서 항상 답이 존재한다고 보장
    }

    static void Main(string[] args) {
        string[] input = Console.ReadLine().Split(); // 입력값 받기
        int D = int.Parse(input[0]);
        int K = int.Parse(input[1]);

        var result = FindAandB(D, K); // A와 B 계산
        Console.WriteLine(result.Item1); // 첫째 날 떡 개수 출력
        Console.WriteLine(result.Item2); // 둘째 날 떡 개수 출력
    }
}
