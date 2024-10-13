using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main() {
        int n = int.Parse(Console.ReadLine());  // 선수의 수 입력
        Dictionary<char, int> firstLetterCount = new Dictionary<char, int>();  // 성의 첫 글자를 카운트할 딕셔너리

        // 선수들의 성 입력 및 첫 글자 카운트
        for (int i = 0; i < n; i++) {
            string player = Console.ReadLine();  // 선수의 성 입력
            char firstLetter = player[0];  // 성의 첫 글자 추출
            
            // 첫 글자가 딕셔너리에 있는지 확인 후 값 증가
            if (firstLetterCount.ContainsKey(firstLetter)) {
                firstLetterCount[firstLetter]++;
            } else {
                firstLetterCount[firstLetter] = 1;
            }
        }

        List<char> result = new List<char>();  // 5명 이상인 성의 첫 글자를 저장할 리스트

        // 딕셔너리에서 5명 이상인 첫 글자를 추출
        foreach (var entry in firstLetterCount) {
            if (entry.Value >= 5) {  // 출현 횟수가 5 이상인 경우
                result.Add(entry.Key);  // 첫 글자를 결과에 추가
            }
        }

        if (result.Count > 0) {
            result.Sort();  // 결과를 사전순으로 정렬
            foreach (char c in result) {
                Console.Write(c);  // 사전순으로 정렬된 첫 글자를 출력
            }
            Console.WriteLine();
        } else {
            Console.WriteLine("PREDAJA");  // 조건을 만족하는 첫 글자가 없을 경우
        }
    }
}