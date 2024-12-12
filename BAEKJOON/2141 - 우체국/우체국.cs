using System;
using System.Collections.Generic;
using System.Linq;

class Program {
    // 우체국 최적 위치를 찾는 함수 정의 (마을 개수와 마을 정보를 입력받음)
    static int FindPostOfficeLocation(int N, List<(int x, int people)> villages) {
        // 마을들을 x 좌표 기준으로 정렬
        villages.Sort((a, b) => a.x.CompareTo(b.x));

        // 전체 마을 인구 계산 (long 자료형으로 변경)
        long totalPopulation = villages.Sum(v => (long)v.people);

        // 현재까지의 누적 인구 초기화
        long currentPopulation = 0;

        // 정렬된 마을 리스트를 순회
        foreach (var village in villages) {
            // 현재 마을의 인구를 누적 인구에 추가
            currentPopulation += village.people;

            // 누적 인구가 전체 인구의 절반 이상이 되면
            if (currentPopulation >= (totalPopulation + 1) / 2) {
                // 해당 마을의 x 좌표를 우체국 위치로 반환
                return village.x;
            }
        }

        // 예외적인 경우 첫 번째 마을의 위치 반환
        return villages[0].x;
    }

    static void Main(string[] args) {
        // 마을의 개수 입력
        int N = int.Parse(Console.ReadLine());

        // 마을 정보를 저장할 리스트 초기화
        var villages = new List<(int x, int people)>();

        // N개의 마을 정보 입력 받기 (x 좌표와 인구)
        for (int i = 0; i < N; i++) {
            var input = Console.ReadLine().Split(' ');
            int x = int.Parse(input[0]);
            int people = int.Parse(input[1]);
            villages.Add((x, people));
        }

        // 우체국 최적 위치 계산 및 출력
        Console.WriteLine(FindPostOfficeLocation(N, villages));
    }
}
