using System;

class Program {
    // 가능한 광고 길이를 찾는 함수
    static int ShortestAdLength(int L, string ad) {
        // KMP 실패 함수 배열 초기화
        int[] failure = new int[L];
        int j = 0; // 접두사와 접미사의 일치 길이 추적

        // KMP 실패 함수 계산
        for (int i = 1; i < L; i++) {
            // j가 0보다 크고 현재 문자와 일치하지 않을 경우, 이전 실패 함수 값으로 j 갱신
            while (j > 0 && ad[i] != ad[j]) {
                j = failure[j - 1];
            }
            // 현재 문자가 일치하는 경우, j를 증가시키고 failure 배열에 j 값을 저장
            if (ad[i] == ad[j]) {
                j++;
                failure[i] = j;
            }
        }

        // 반복되는 최소 광고 길이 계산 후 반환
        return L - failure[L - 1];
    }

    static void Main(string[] args) {
        // 광고판의 크기 입력받기
        int L = int.Parse(Console.ReadLine());
        // 광고판에 보이는 문자열 입력받기
        string ad = Console.ReadLine();

        // 가능한 가장 짧은 광고 길이 출력
        Console.WriteLine(ShortestAdLength(L, ad));
    }
}