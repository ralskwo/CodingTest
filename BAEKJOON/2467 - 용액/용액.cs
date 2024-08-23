using System;

class Program
{
    static void Main()
    {
        // 총 요소의 개수를 입력 받음
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse); // 요소들을 배열에 저장

        // 0에 가장 가까운 합을 만드는 두 요소를 찾음
        var result = FindClosestToZero(arr);
        Console.WriteLine($"{result.Item1} {result.Item2}"); // 결과 출력
    }

    static Tuple<int, int> FindClosestToZero(int[] arr)
    {
        int n = arr.Length; // 배열의 크기를 변수 n에 저장
        int left = 0; // 시작 포인터를 배열의 첫 번째 요소에 설정
        int right = n - 1; // 끝 포인터를 배열의 마지막 요소에 설정
        int closestSum = int.MaxValue; // 0에 가장 가까운 합을 저장할 변수, 초기값은 무한대
        Tuple<int, int> answer = new Tuple<int, int>(arr[left], arr[right]); // 가장 가까운 합을 만드는 두 요소의 값을 저장할 변수

        while (left < right) // 두 포인터가 교차할 때까지 반복
        {
            int currentSum = arr[left] + arr[right]; // 현재 두 포인터가 가리키는 요소의 합을 계산
            if (Math.Abs(currentSum) < Math.Abs(closestSum)) // 현재 합이 0에 더 가까운 경우
            {
                closestSum = currentSum; // 가장 가까운 합을 업데이트
                answer = new Tuple<int, int>(arr[left], arr[right]); // 두 요소의 값을 업데이트
            }

            if (currentSum < 0) // 현재 합이 0보다 작은 경우
            {
                left++; // 시작 포인터를 오른쪽으로 이동
            }
            else // 현재 합이 0보다 크거나 같은 경우
            {
                right--; // 끝 포인터를 왼쪽으로 이동
            }
        }

        return answer; // 0에 가장 가까운 합을 만드는 두 요소의 값을 반환
    }
}
