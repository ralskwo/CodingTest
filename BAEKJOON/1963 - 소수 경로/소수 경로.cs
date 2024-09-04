using System;
using System.Collections.Generic;

class Program
{
    // 1000 이상 9999 이하의 소수를 판별하기 위한 배열
    static bool[] is_prime = new bool[10000];

    // 에라토스테네스의 체를 사용하여 소수를 구하는 함수
    static void SieveOfEratosthenes() {
        for (int i = 0; i < 10000; i++) is_prime[i] = true; // 배열을 true로 초기화
        is_prime[0] = is_prime[1] = false; // 0과 1은 소수가 아님

        for (int i = 2; i <= Math.Sqrt(9999); i++) { // 2부터 9999의 제곱근까지 반복
            if (is_prime[i]) { // i가 소수인 경우
                for (int j = i * i; j < 10000; j += i) { // i의 배수를 모두 소수가 아님으로 설정
                    is_prime[j] = false;
                }
            }
        }
    }

    // 한 자리만 바꿔서 나올 수 있는 이웃 소수들을 반환하는 함수
    static List<int> GetNeighbors(int num) {
        List<int> neighbors = new List<int>();
        char[] numArray = num.ToString().ToCharArray(); // 숫자를 문자열로 변환

        for (int i = 0; i < 4; i++) { // 각 자리수에 대해
            char original = numArray[i]; // 원래 숫자를 저장

            for (char d = '0'; d <= '9'; d++) { // 각 자리수를 0부터 9로 바꾸어 봄
                if (numArray[i] != d) { // 다른 숫자로 변경 시도
                    numArray[i] = d; // 해당 자리수를 변경
                    int new_num = int.Parse(new string(numArray)); // 새로운 숫자를 정수로 변환

                    // 1000 이상이고 소수인 경우만 이웃으로 추가
                    if (new_num >= 1000 && is_prime[new_num]) {
                        neighbors.Add(new_num);
                    }
                }
            }

            numArray[i] = original; // 원래 자리수로 복원
        }

        return neighbors; // 가능한 이웃 소수들을 반환
    }

    // BFS를 사용하여 최소 변환 횟수를 계산하는 함수
    static int BFS(int start, int end) {
        if (start == end) return 0; // 시작과 목표가 같으면 0을 반환

        Queue<Tuple<int, int>> q = new Queue<Tuple<int, int>>(); // 큐에는 현재 소수와 그 소수까지의 변환 횟수를 저장
        bool[] visited = new bool[10000]; // 각 숫자에 대해 방문 여부를 저장

        q.Enqueue(new Tuple<int, int>(start, 0)); // 시작 소수와 0번째 변환 횟수를 큐에 추가
        visited[start] = true; // 시작 소수 방문 처리

        while (q.Count > 0) {
            var current = q.Dequeue(); // 현재 소수와 변환 횟수를 큐에서 꺼냄
            int currentNum = current.Item1;
            int steps = current.Item2;

            List<int> neighbors = GetNeighbors(currentNum); // 이웃 소수들을 구함

            foreach (int neighbor in neighbors) { // 이웃 소수들을 하나씩 확인
                if (!visited[neighbor]) { // 방문하지 않은 소수인 경우
                    if (neighbor == end) return steps + 1; // 목표 소수에 도달한 경우 변환 횟수 반환
                    visited[neighbor] = true; // 방문 처리
                    q.Enqueue(new Tuple<int, int>(neighbor, steps + 1)); // 이웃 소수를 큐에 추가
                }
            }
        }

        return -1; // 목표 소수에 도달할 수 없는 경우 -1 반환
    }

    static void Main() {
        int T = int.Parse(Console.ReadLine()); // 테스트 케이스 수 입력

        SieveOfEratosthenes(); // 소수를 미리 계산

        while (T-- > 0) {
            string[] input = Console.ReadLine().Split(); // 시작 소수와 목표 소수를 입력받음
            int start = int.Parse(input[0]);
            int end = int.Parse(input[1]);

            int result = BFS(start, end); // BFS를 통해 변환 횟수 계산

            if (result == -1)
                Console.WriteLine("Impossible"); // 변환이 불가능한 경우
            else
                Console.WriteLine(result); // 변환이 가능한 경우 최소 횟수 출력
        }
    }
}
