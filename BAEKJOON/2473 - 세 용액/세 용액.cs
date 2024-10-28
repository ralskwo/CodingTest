using System;
using System.Linq;

class Program
{
    static int[] FindThreeSolutionsClosestToZero(int N, int[] solutions)
    {
        Array.Sort(solutions);
        long closestSum = long.MaxValue;
        int[] answer = new int[3];

        for (int i = 0; i < N - 2; i++)
        {
            int left = i + 1, right = N - 1;

            while (left < right)
            {
                long currentSum = (long)solutions[i] + solutions[left] + solutions[right];

                if (Math.Abs(currentSum) < Math.Abs(closestSum))
                {
                    closestSum = currentSum;
                    answer[0] = solutions[i];
                    answer[1] = solutions[left];
                    answer[2] = solutions[right];
                }

                if (currentSum > 0)
                {
                    right--;
                }
                else if (currentSum < 0)
                {
                    left++;
                }
                else
                {
                    Array.Sort(answer);
                    return answer;
                }
            }
        }

        Array.Sort(answer);
        return answer;
    }

    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] solutions = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int[] result = FindThreeSolutionsClosestToZero(N, solutions);
        Console.WriteLine(string.Join(" ", result));
    }
}