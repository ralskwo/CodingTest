using System;

class Program
{
    static long MergeSortAndCount(int[] arr, int[] temp_arr, int left, int right)
    {
        if (left == right) // 배열이 하나의 요소만 남았을 때
            return 0;

        int mid = (left + right) / 2; // 중간 인덱스 계산

        // 왼쪽과 오른쪽 부분 배열에서의 역전 횟수를 재귀적으로 계산
        long inv_count = MergeSortAndCount(arr, temp_arr, left, mid);
        inv_count += MergeSortAndCount(arr, temp_arr, mid + 1, right);

        // 병합 과정에서 발생하는 역전 횟수 계산
        inv_count += MergeAndCount(arr, temp_arr, left, mid, right);

        return inv_count;
    }

    static long MergeAndCount(int[] arr, int[] temp_arr, int left, int mid, int right)
    {
        int i = left;   // 왼쪽 배열의 시작 인덱스
        int j = mid + 1; // 오른쪽 배열의 시작 인덱스
        int k = left;    // 임시 배열의 시작 인덱스
        long inv_count = 0;

        // 두 배열을 병합하면서 역전 횟수 계산
        while (i <= mid && j <= right)
        {
            if (arr[i] <= arr[j])
            {
                temp_arr[k++] = arr[i++];
            }
            else
            {
                temp_arr[k++] = arr[j++];
                inv_count += (mid - i + 1); // 역전 횟수는 왼쪽 배열의 남은 요소 수만큼 증가
            }
        }

        // 남아 있는 요소들을 임시 배열에 복사
        while (i <= mid)
            temp_arr[k++] = arr[i++];

        while (j <= right)
            temp_arr[k++] = arr[j++];

        // 병합된 결과를 원래 배열로 복사
        for (int l = left; l <= right; l++)
            arr[l] = temp_arr[l];

        return inv_count;
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine()); // 배열의 크기 입력
        int[] arr = new int[n];
        int[] temp_arr = new int[n];

        string[] inputs = Console.ReadLine().Split(); // 배열의 요소 입력
        for (int i = 0; i < n; i++)
            arr[i] = int.Parse(inputs[i]);

        // 총 스왑 횟수 출력
        Console.WriteLine(MergeSortAndCount(arr, temp_arr, 0, n - 1));
    }
}
