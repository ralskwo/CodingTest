using System;
using System.Collections.Generic;

class Program {
    static int MaxSubstringLength(int n, string s) {
        int left = 0; // 왼쪽 포인터 초기화
        Dictionary<char, int> charCount = new Dictionary<char, int>(); // 각 문자의 개수를 저장할 딕셔너리 초기화
        int maxLen = 0; // 최대 길이 변수 초기화

        // 오른쪽 포인터를 사용하여 문자열 순회
        for (int right = 0; right < s.Length; right++) {
            if (charCount.ContainsKey(s[right])) {
                charCount[s[right]]++; // 이미 있는 문자면 개수 증가
            } else {
                charCount[s[right]] = 1; // 새로운 문자면 개수를 1로 설정
            }

            // 고유 문자 수가 n을 초과하면 윈도우를 축소
            while (charCount.Count > n) {
                charCount[s[left]]--; // 왼쪽 포인터의 문자 개수 감소
                if (charCount[s[left]] == 0) {
                    charCount.Remove(s[left]); // 문자 개수가 0이 되면 딕셔너리에서 삭제
                }
                left++; // 왼쪽 포인터를 오른쪽으로 이동하여 윈도우 축소
            }

            // 최대 길이 갱신
            maxLen = Math.Max(maxLen, right - left + 1);
        }

        return maxLen; // 최종 결과 반환
    }

    static void Main() {
        int n = int.Parse(Console.ReadLine()); // 인식할 문자 종류 수 입력
        string s = Console.ReadLine(); // 문자열 입력

        // 결과 계산 및 출력
        Console.WriteLine(MaxSubstringLength(n, s));
    }
}