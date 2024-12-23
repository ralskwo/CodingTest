using System;
using System.Linq;

class Program
{
    // 블루레이 개수를 계산하는 메서드
    static int CountBlurays(int[] lectures, int size) {
        int count = 1;  // 블루레이 개수 (최소 1부터 시작)
        int total = 0;  // 현재 블루레이에 담긴 강의 길이 합

        foreach (int lecture in lectures) {
            // 현재 블루레이에 강의를 추가했을 때 크기를 초과하는 경우
            if (total + lecture > size) {
                count++;  // 새로운 블루레이 필요
                total = lecture;  // 현재 강의를 새로운 블루레이에 담음
            } else {
                total += lecture;  // 크기를 초과하지 않으면 현재 블루레이에 추가
            }
        }
        return count;  // 사용된 블루레이 개수 반환
    }

    // 최소 블루레이 크기를 찾는 이분 탐색 메서드
    static int FindMinimumBluraySize(int n, int m, int[] lectures) {
        int left = lectures.Max();  // 가장 긴 강의 길이 (최소값)
        int right = lectures.Sum();  // 모든 강의 길이의 합 (최대값)
        int answer = right;  // 정답을 저장할 변수, 초기값은 최대값으로 설정

        // 이분 탐색 수행
        while (left <= right) {
            int mid = (left + right) / 2;  // 블루레이 크기의 중간값 설정
            if (CountBlurays(lectures, mid) <= m) {
                answer = mid;  // 블루레이 개수가 M개 이하이면 정답 갱신
                right = mid - 1;  // 더 작은 크기를 탐색
            } else {
                left = mid + 1;  // 블루레이 개수가 M개 초과하면 더 큰 크기를 탐색
            }
        }
        return answer;  // 최소 블루레이 크기 반환
    }

    static void Main() {
        string[] input = Console.ReadLine().Split(' ');
        int n = int.Parse(input[0]);  // 강의 개수
        int m = int.Parse(input[1]);  // 블루레이 개수
        int[] lectures = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();  // 강의 길이 배열 입력

        Console.WriteLine(FindMinimumBluraySize(n, m, lectures));  // 최소 블루레이 크기 출력
    }
}
