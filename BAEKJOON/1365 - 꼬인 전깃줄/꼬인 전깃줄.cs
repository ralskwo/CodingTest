using System;
using System.Collections.Generic;

class Program {
    // 가장 긴 증가하는 부분 수열(LIS)을 구하는 함수
    static int MinimumCutWires(int N, int[] poles) {
        List<int> lis = new List<int>();  // LIS를 저장하는 리스트

        for (int i = 0; i < N; i++) {
            int pos = lis.BinarySearch(poles[i]);  // 이분 탐색으로 위치 찾기

            if (pos < 0) {
                // BinarySearch는 음수 인덱스를 반환할 경우 삽입 위치를 나타냄
                pos = ~pos;  // 비트 NOT 연산으로 삽입 위치 변환
            }

            if (pos == lis.Count) {
                // 새로운 전봇대를 LIS 끝에 추가
                lis.Add(poles[i]);
            } else {
                // 이미 LIS에 포함된 경우 해당 위치 값을 갱신
                lis[pos] = poles[i];
            }
        }

        // 전체 전봇대에서 LIS 길이를 뺀 값이 잘라야 할 전선 개수
        return N - lis.Count;
    }

    static void Main() {
        int N = int.Parse(Console.ReadLine());  // 전봇대 개수 입력
        string[] input = Console.ReadLine().Split(' ');  // 전봇대 연결 상태 입력
        int[] poles = Array.ConvertAll(input, int.Parse);  // 문자열을 정수 배열로 변환

        Console.WriteLine(MinimumCutWires(N, poles));  // 결과 출력
    }
}
