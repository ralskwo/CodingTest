using System;

class Program {
    static void Main() {
        // 첫 번째 줄 입력: N과 K를 읽음
        string[] firstLine = Console.ReadLine().Split();
        int N = int.Parse(firstLine[0]);
        int K = int.Parse(firstLine[1]);

        // 두 번째 줄 입력: 온도를 배열로 저장
        int[] temperatures = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        // 초기 K일의 합을 계산
        int currentSum = 0;
        for (int i = 0; i < K; i++) {
            currentSum += temperatures[i];
        }

        // 최대값을 현재 합으로 초기화
        int maxSum = currentSum;

        // 슬라이딩 윈도우를 사용하여 최대값 계산
        for (int i = K; i < N; i++) {
            // 현재 합에서 맨 앞 값을 빼고 새 값을 더함
            currentSum = currentSum - temperatures[i - K] + temperatures[i];
            // 최대값 갱신
            maxSum = Math.Max(maxSum, currentSum);
        }

        // 최대값 출력
        Console.WriteLine(maxSum);
    }
}