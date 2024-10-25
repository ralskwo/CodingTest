using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // 수의 개수 N 입력
        int N = int.Parse(Console.ReadLine());

        // 입력된 수들을 저장할 리스트와 빈도수를 저장할 딕셔너리 선언
        List<int> arr = new List<int>();
        Dictionary<int, int> frequency = new Dictionary<int, int>();

        // 수 입력 및 빈도 계산
        for (int i = 0; i < N; i++)
        {
            // 수 입력받기
            int num = int.Parse(Console.ReadLine());
            arr.Add(num);

            // 빈도수를 딕셔너리에 저장 (기존에 키가 있으면 증가, 없으면 추가)
            if (frequency.ContainsKey(num))
                frequency[num]++;
            else
                frequency[num] = 1;
        }

        // 리스트를 오름차순으로 정렬
        arr.Sort();

        // 산술평균 계산 및 출력
        double sum = arr.Sum(); // 리스트의 합을 구함
        int mean = (int)Math.Round(sum / N); // 평균을 구하고 반올림 후 정수형으로 변환
        Console.WriteLine(mean);

        // 중앙값 계산 (정렬된 리스트의 중앙값)
        int median = arr[N / 2];
        Console.WriteLine(median);

        // 빈도수 딕셔너리를 리스트로 변환하여 빈도수 기준으로 정렬
        var sortedFrequency = frequency.OrderByDescending(x => x.Value).ThenBy(x => x.Key).ToList();

        // 최빈값이 여러 개일 경우 두 번째로 작은 값을 선택
        int mode = (sortedFrequency.Count > 1 && sortedFrequency[0].Value == sortedFrequency[1].Value)
            ? sortedFrequency[1].Key
            : sortedFrequency[0].Key;
        Console.WriteLine(mode);

        // 범위 계산 (정렬된 리스트의 최댓값 - 최솟값)
        int range = arr.Last() - arr.First();
        Console.WriteLine(range);
    }
}