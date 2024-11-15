using System;
using System.Linq;

class Program
{
    static int CalculateTrappedRainwater(int H, int W, int[] heights)
    {
        // 왼쪽과 오른쪽 최대 높이를 저장할 배열을 생성하고 0으로 초기화
        int[] leftMax = new int[W];
        int[] rightMax = new int[W];
        
        // 첫 번째 위치의 왼쪽 최대 높이는 그 위치의 높이로 설정
        leftMax[0] = heights[0];
        // 각 위치에 대해 왼쪽 최대 높이를 계산
        for (int i = 1; i < W; i++)
        {
            leftMax[i] = Math.Max(leftMax[i - 1], heights[i]);
        }
        
        // 마지막 위치의 오른쪽 최대 높이는 그 위치의 높이로 설정
        rightMax[W - 1] = heights[W - 1];
        // 각 위치에 대해 오른쪽 최대 높이를 계산
        for (int i = W - 2; i >= 0; i--)
        {
            rightMax[i] = Math.Max(rightMax[i + 1], heights[i]);
        }
        
        // 총 고일 수 있는 빗물의 양을 저장할 변수
        int totalWater = 0;
        // 각 위치에 대해 고일 수 있는 빗물의 양을 계산
        for (int i = 0; i < W; i++)
        {
            // 현재 위치에서 고일 수 있는 물의 양을 계산
            int water = Math.Min(leftMax[i], rightMax[i]) - heights[i];
            // 양수인 경우에만 총 빗물 양에 더해줌
            if (water > 0)
            {
                totalWater += water;
            }
        }
        
        return totalWater;
    }

    static void Main()
    {
        // 세로 길이(H)와 가로 길이(W) 입력 받기
        var inputs = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int H = inputs[0];
        int W = inputs[1];
        
        // 각 위치의 높이 입력 받기
        int[] heights = Console.ReadLine().Split().Select(int.Parse).ToArray();
        
        // 함수 호출 및 결과 출력
        Console.WriteLine(CalculateTrappedRainwater(H, W, heights));
    }
}