using System;  // 기본적인 입출력 및 시스템 기능을 사용하기 위한 네임스페이스
using System.Collections.Generic;  // 리스트를 사용하기 위한 네임스페이스
using System.Linq;  // 정렬 및 기타 LINQ 기능을 사용하기 위한 네임스페이스

class Program {
    // 두 수의 최대 공약수를 구하는 함수
    static int GCD(int a, int b) {
        while (b != 0) {  // b가 0이 될 때까지 반복
            int temp = a % b;  // a를 b로 나눈 나머지를 구함
            a = b;  // a에 b 값을 대입
            b = temp;  // b에 나머지를 대입
        }
        return a;  // 최대 공약수를 반환
    }

    // 주어진 수의 약수를 구하는 함수
    static List<int> FindDivisors(int num) {
        List<int> divisors = new List<int>();  // 약수를 저장할 리스트 생성
        for (int i = 2; i <= Math.Sqrt(num); i++) {  // 2부터 num의 제곱근까지 반복
            if (num % i == 0) {  // i가 num의 약수인지 확인
                divisors.Add(i);  // i를 약수로 추가
                if (i != num / i) {  // i와 num / i가 다르면
                    divisors.Add(num / i);  // num / i도 약수로 추가
                }
            }
        }
        divisors.Add(num);  // num 자신을 약수로 추가
        divisors.Sort();  // 약수들을 오름차순으로 정렬
        return divisors;  // 정렬된 약수 리스트를 반환
    }

    static void Main() {
        int n = int.Parse(Console.ReadLine());  // 첫 번째 줄에서 수의 개수를 입력받음
        int[] numbers = new int[n];  // 입력받을 수들을 저장할 배열
        
        for (int i = 0; i < n; i++) {
            numbers[i] = int.Parse(Console.ReadLine());  // 각각의 수를 입력받음
        }

        Array.Sort(numbers);  // 숫자들을 오름차순으로 정렬

        int g = numbers[1] - numbers[0];  // 첫 번째와 두 번째 수의 차이로 g를 초기화
        for (int i = 2; i < n; i++) {
            g = GCD(g, numbers[i] - numbers[i - 1]);  // 차이들의 최대 공약수를 구함
        }

        List<int> result = FindDivisors(g);  // g의 약수를 구함

        Console.WriteLine(string.Join(" ", result));  // 약수들을 공백으로 구분하여 출력
    }
}
