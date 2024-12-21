using System;
using System.Linq;

class Program
{
    // 두 빌딩이 서로 보이는지 여부를 판단하는 함수
    static bool IsVisible(int[] heights, int i, int j)
    {
        // 두 빌딩 간의 기울기 계산
        double slope = (double)(heights[j] - heights[i]) / (j - i);
        
        // i와 j 사이의 빌딩을 확인
        for (int k = i + 1; k < j; k++)
        {
            // k번 빌딩이 i와 j를 잇는 직선 위에 있거나 직선보다 높으면 false 반환
            if (heights[k] >= heights[i] + slope * (k - i))
            {
                return false;
            }
        }
        // 가려지지 않으면 true 반환
        return true;
    }

    // 가장 많은 빌딩이 보이는 수를 계산하는 함수
    static int CountVisibleBuildings(int N, int[] heights)
    {
        int maxCount = 0;

        // 각 빌딩을 기준으로 보이는 빌딩 수 계산
        for (int i = 0; i < N; i++)
        {
            int visibleCount = 0;

            // 왼쪽 빌딩 확인
            for (int j = i - 1; j >= 0; j--)
            {
                if (IsVisible(heights, j, i))
                {
                    visibleCount++;
                }
            }

            // 오른쪽 빌딩 확인
            for (int j = i + 1; j < N; j++)
            {
                if (IsVisible(heights, i, j))
                {
                    visibleCount++;
                }
            }

            // 최대 보이는 빌딩 수 갱신
            maxCount = Math.Max(maxCount, visibleCount);
        }

        return maxCount;
    }

    static void Main()
    {
        // 빌딩 개수 입력
        int N = int.Parse(Console.ReadLine());
        
        // 빌딩 높이 입력
        int[] heights = Console.ReadLine().Split().Select(int.Parse).ToArray();

        // 결과 출력
        Console.WriteLine(CountVisibleBuildings(N, heights));
    }
}
