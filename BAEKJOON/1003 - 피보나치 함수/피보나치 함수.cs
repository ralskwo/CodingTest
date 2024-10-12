using System;
using System.Collections.Generic;

class Program
{
    static (int, int) Fibonacci(int n, Dictionary<int, (int, int)> memo)
    {
        if (n == 0) return (1, 0);
        if (n == 1) return (0, 1);
        
        if (memo.ContainsKey(n)) return memo[n];
        
        var (zeros1, ones1) = Fibonacci(n - 1, memo);
        var (zeros2, ones2) = Fibonacci(n - 2, memo);
        
        var result = (zeros1 + zeros2, ones1 + ones2);
        memo[n] = result;
        return result;
    }

    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());
        
        for (int i = 0; i < T; i++)
        {
            int N = int.Parse(Console.ReadLine());
            var memo = new Dictionary<int, (int, int)>();
            var (zeros, ones) = Fibonacci(N, memo);
            Console.WriteLine($"{zeros} {ones}");
        }
    }
}