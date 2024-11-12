using System;

class Program {
    // A보다 큰 수 중에서 1의 개수가 같은 가장 가까운 수를 찾는 함수
    static long NextSameBitCount(long n) {
        // 가장 오른쪽의 1 비트를 찾음
        long smallest = n & -n;
        // 가장 오른쪽의 0을 1로 바꿈
        long ripple = n + smallest;
        // 변화된 비트의 위치를 계산
        long ones = n ^ ripple;
        // 필요한 만큼의 1 비트를 재배치
        ones = (ones >> 2) / smallest;
        // 큰 수 반환
        return ripple | ones;
    }

    // A보다 작은 수 중에서 1의 개수가 같은 가장 가까운 수를 찾는 함수
    static long PrevSameBitCount(long n) {
        long temp = n;
        int c0 = 0, c1 = 0;

        // 오른쪽에서 연속된 1의 개수를 셈
        while ((temp & 1) == 1) {
            c1++;
            temp >>= 1;
        }
        // n이 모든 비트가 1일 경우, 더 작은 수가 없으므로 0 반환
        if (temp == 0) return 0;

        // 오른쪽에서 연속된 0의 개수를 셈
        while ((temp & 1) == 0 && temp != 0) {
            c0++;
            temp >>= 1;
        }

        int p = c0 + c1; // 비트를 조정할 위치 계산

        // p 이후 모든 비트를 0으로 만듦
        n &= ((~0L) << (p + 1));
        // c1+1 개의 1 비트를 만들어 필요한 위치에 배치
        long mask = (1L << (c1 + 1)) - 1;
        n |= mask << (c0 - 1);

        return n;
    }

    static void Main() {
        // 사용자로부터 수를 입력받음
        long A = long.Parse(Console.ReadLine());

        // A보다 작은 수와 큰 수를 찾음
        long smaller = PrevSameBitCount(A);
        long larger = NextSameBitCount(A);

        // 결과 출력
        Console.WriteLine($"{smaller} {larger}");
    }
}