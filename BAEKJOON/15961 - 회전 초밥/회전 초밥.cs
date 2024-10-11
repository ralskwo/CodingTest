using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 첫 줄의 입력을 받기 위해 문자열을 읽고 공백으로 분리
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]); // 회전 초밥 벨트에 놓인 접시의 수
        int d = int.Parse(input[1]); // 초밥의 종류 수
        int k = int.Parse(input[2]); // 연속해서 먹는 접시의 수
        int c = int.Parse(input[3]); // 쿠폰 번호

        // 회전 초밥 벨트에 놓인 초밥의 종류를 저장할 배열 생성
        int[] sushi = new int[N];
        for (int i = 0; i < N; i++)
        {
            sushi[i] = int.Parse(Console.ReadLine());
        }

        // 현재 윈도우에 있는 초밥 종류와 개수를 저장할 Dictionary 생성
        Dictionary<int, int> eaten = new Dictionary<int, int>();

        // 초기 윈도우 설정: 처음 k개의 초밥을 윈도우에 추가
        for (int i = 0; i < k; i++)
        {
            if (!eaten.ContainsKey(sushi[i]))
                eaten[sushi[i]] = 0;
            eaten[sushi[i]]++;
        }

        // 쿠폰 초밥을 윈도우에 추가하여 시작 시점에 포함시킴
        if (!eaten.ContainsKey(c))
            eaten[c] = 0;
        eaten[c]++;

        // 현재 윈도우에 포함된 서로 다른 초밥 종류 수를 최대값으로 초기화
        int maxVariety = eaten.Count;

        // 슬라이딩 윈도우를 사용하여 벨트의 모든 위치를 순회
        for (int i = 0; i < N; i++)
        {
            // 윈도우에서 빠지는 초밥 제거
            int removeSushi = sushi[i];
            eaten[removeSushi]--;
            if (eaten[removeSushi] == 0)
                eaten.Remove(removeSushi);

            // 윈도우에 새로운 초밥 추가
            int addSushi = sushi[(i + k) % N];
            if (!eaten.ContainsKey(addSushi))
                eaten[addSushi] = 0;
            eaten[addSushi]++;

            // 최대값 갱신
            maxVariety = Math.Max(maxVariety, eaten.Count);
        }

        // 결과 출력
        Console.WriteLine(maxVariety);
    }
}