using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // 입력값 처리
        string[] firstLine = Console.ReadLine().Split();  // 첫 줄 입력
        int N = int.Parse(firstLine[0]);  // 접시 수
        int d = int.Parse(firstLine[1]);  // 초밥 종류 수
        int k = int.Parse(firstLine[2]);  // 연속 접시 수
        int c = int.Parse(firstLine[3]);  // 쿠폰 번호

        int[] sushi = new int[N];  // 초밥 벨트
        for (int i = 0; i < N; i++) {
            sushi[i] = int.Parse(Console.ReadLine());  // 초밥 종류 입력
        }

        // 원형 벨트 처리를 위한 확장
        List<int> extendedSushi = new List<int>(sushi);
        for (int i = 0; i < k - 1; i++) {
            extendedSushi.Add(sushi[i]);  // 처음 k-1개의 초밥을 끝에 추가
        }

        // 슬라이딩 윈도우를 위한 변수 초기화
        Dictionary<int, int> sushiCount = new Dictionary<int, int>();  // 초밥 종류와 개수 저장
        int currentVariety = 0;  // 현재 초밥 종류 수
        int maxVariety = 0;  // 최대 초밥 종류 수

        // 초기 윈도우 설정
        for (int i = 0; i < k; i++) {
            if (!sushiCount.ContainsKey(extendedSushi[i])) {
                sushiCount[extendedSushi[i]] = 0;  // 초밥 초기화
            }
            if (sushiCount[extendedSushi[i]] == 0) {
                currentVariety++;  // 새로운 초밥 종류 발견 시 증가
            }
            sushiCount[extendedSushi[i]]++;
        }

        // 쿠폰 초밥 포함 여부 확인 후 최대값 초기화
        maxVariety = currentVariety + (sushiCount.ContainsKey(c) && sushiCount[c] > 0 ? 0 : 1);

        // 슬라이딩 윈도우 이동
        for (int i = k; i < extendedSushi.Count; i++) {
            // 윈도우에서 빠지는 초밥 처리
            int leavingSushi = extendedSushi[i - k];
            sushiCount[leavingSushi]--;
            if (sushiCount[leavingSushi] == 0) {
                currentVariety--;  // 초밥 종류 감소
            }

            // 윈도우에 새로 추가되는 초밥 처리
            int enteringSushi = extendedSushi[i];
            if (!sushiCount.ContainsKey(enteringSushi)) {
                sushiCount[enteringSushi] = 0;  // 초밥 초기화
            }
            if (sushiCount[enteringSushi] == 0) {
                currentVariety++;  // 새로운 초밥 종류 발견 시 증가
            }
            sushiCount[enteringSushi]++;

            // 쿠폰 초밥 포함하여 최대값 갱신
            maxVariety = Math.Max(maxVariety, currentVariety + (sushiCount.ContainsKey(c) && sushiCount[c] > 0 ? 0 : 1));
        }

        // 결과 출력
        Console.WriteLine(maxVariety);
    }
}
