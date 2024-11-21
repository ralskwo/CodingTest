using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // 모든 가능한 수식을 생성하는 재귀 함수
    static void GenerateExpressions(int n, string currentExpr, List<string> results, int currentNum)
    {
        // 수식이 완성된 경우
        if (currentNum > n)
        {
            string evalExpr = currentExpr.Replace(" ", ""); // 공백 제거
            int result = EvaluateExpression(evalExpr); // 수식 계산
            if (result == 0) results.Add(currentExpr); // 결과가 0이면 추가
            return;
        }

        // '+' 연산 추가
        GenerateExpressions(n, currentExpr + "+" + currentNum, results, currentNum + 1);
        // '-' 연산 추가
        GenerateExpressions(n, currentExpr + "-" + currentNum, results, currentNum + 1);
        // 공백 추가
        GenerateExpressions(n, currentExpr + " " + currentNum, results, currentNum + 1);
    }

    // 수식을 계산하는 함수
    static int EvaluateExpression(string expr)
    {
        int result = 0, term = 0, sign = 1;
        foreach (char c in expr)
        {
            if (char.IsDigit(c))
            {
                term = term * 10 + (c - '0'); // 숫자 처리
            }
            else
            {
                result += sign * term; // 연산 처리
                term = 0;
                sign = (c == '+' ? 1 : -1);
            }
        }
        result += sign * term; // 마지막 숫자 추가
        return result;
    }

    // 메인 함수
    static void Main(string[] args)
    {
        int t = int.Parse(Console.ReadLine()); // 테스트 케이스 개수 입력
        while (t-- > 0)
        {
            int n = int.Parse(Console.ReadLine()); // 테스트 케이스의 N 입력
            var results = new List<string>();
            GenerateExpressions(n, "1", results, 2); // 숫자 1로 시작하는 수식 생성
            results.Sort(); // 결과를 ASCII 순서로 정렬
            foreach (var expr in results)
            {
                Console.WriteLine(expr); // 결과 출력
            }
            if (t > 0) Console.WriteLine(); // 테스트 케이스 사이에 빈 줄 추가
        }
    }
}
