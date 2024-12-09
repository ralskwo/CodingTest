using System;
using System.Linq;

class Program
{
    static void Main() {
        // 첫 번째 줄 입력: K와 N
        var input = Console.ReadLine().Split();
        int k = int.Parse(input[0]); // 랜선 개수
        int n = int.Parse(input[1]); // 필요한 랜선 개수

        // 랜선 길이 입력
        long[] lengths = new long[k];
        for (int i = 0; i < k; i++) {
            lengths[i] = long.Parse(Console.ReadLine());
        }

        Console.WriteLine(MaxLanLength(k, n, lengths)); // 최대 랜선 길이 출력
    }

    static long MaxLanLength(int k, int n, long[] lengths) {
        long start = 1; // 이분 탐색의 시작점
        long end = lengths.Max(); // 랜선의 최대 길이
        long result = 0; // 결과를 저장할 변수

        while (start <= end) {
            long mid = (start + end) / 2; // 중간값 계산
            long count = 0; // 현재 중간 길이로 만들 수 있는 랜선 개수

            foreach (var length in lengths) {
                count += length / mid; // 각 랜선을 중간 길이로 잘라 만든 개수 합산
            }

            if (count >= n) {
                result = mid; // 랜선 개수가 N개 이상이면 결과 갱신
                start = mid + 1; // 더 긴 길이를 탐색
            } else {
                end = mid - 1; // 랜선 개수가 N개 미만이면 더 짧은 길이를 탐색
            }
        }

        return result; // 최종적으로 찾은 최대 길이를 반환
    }
}
