using System;
using System.Collections.Generic;

class Program
{
    static int Command(int n, char cmd)
    {
        switch (cmd)
        {
            case 'D':
                return (2 * n) % 10000; // D 명령어: 숫자를 두 배로 하고 10000으로 나눈 나머지
            case 'S':
                return (n == 0) ? 9999 : n - 1; // S 명령어: 숫자에서 1을 빼고 음수가 되면 9999로 설정
            case 'L':
                return (n % 1000) * 10 + n / 1000; // L 명령어: 자릿수를 왼쪽으로 한 칸 회전
            case 'R':
                return (n % 10) * 1000 + n / 10; // R 명령어: 자릿수를 오른쪽으로 한 칸 회전
            default:
                return n;
        }
    }

    static string Bfs(int start, int end)
    {
        Queue<Tuple<int, string>> queue = new Queue<Tuple<int, string>>();
        bool[] visited = new bool[10000];
        queue.Enqueue(new Tuple<int, string>(start, ""));
        visited[start] = true;

        while (queue.Count > 0)
        {
            var current = queue.Dequeue();
            int currentNum = current.Item1;
            string path = current.Item2;

            if (currentNum == end)
            {
                return path;
            }

            foreach (char cmd in new char[] { 'D', 'S', 'L', 'R' })
            {
                int nextNum = Command(currentNum, cmd);
                if (!visited[nextNum])
                {
                    visited[nextNum] = true;
                    queue.Enqueue(new Tuple<int, string>(nextNum, path + cmd));
                }
            }
        }

        return "";
    }

    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());
        List<string> results = new List<string>();

        for (int i = 0; i < T; ++i)
        {
            string[] inputs = Console.ReadLine().Split();
            int A = int.Parse(inputs[0]);
            int B = int.Parse(inputs[1]);
            results.Add(Bfs(A, B));
        }

        foreach (string result in results)
        {
            Console.WriteLine(result);
        }
    }
}
