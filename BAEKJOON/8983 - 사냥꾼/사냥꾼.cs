using System;      // 기본 입출력 및 시스템 관련 기능을 위한 네임스페이스
using System.Linq; // LINQ 기능 사용을 위한 네임스페이스
using System.Collections.Generic;  // List와 같은 컬렉션을 사용하기 위한 네임스페이스

class Program
{
    static int CountCatchableAnimals(int m, int n, int l, List<int> shootingSpots, List<Tuple<int, int>> animals)
    {
        shootingSpots.Sort();  // 사대 위치를 오름차순으로 정렬
        int catchableCount = 0;  // 잡을 수 있는 동물 수를 저장할 변수

        foreach (var animal in animals)  // 각 동물에 대해 반복
        {
            int x = animal.Item1;  // 동물의 x 좌표
            int y = animal.Item2;  // 동물의 y 좌표

            if (y > l)  // y 좌표가 사정거리보다 크면 사냥 불가능
            {
                continue;  // 이 동물은 건너뜀
            }

            // 이분 탐색으로 사대 위치 중 동물의 x 좌표에 가장 가까운 사대 찾기
            int idx = shootingSpots.BinarySearch(x);  // 이분 탐색
            if (idx < 0) idx = ~idx;  // BinarySearch가 음수 값을 반환할 경우, 올바른 인덱스 구하기

            bool isCatchable = false;  // 해당 동물이 잡힐 수 있는지 여부

            // 찾은 사대의 위치와의 거리 계산
            if (idx < shootingSpots.Count && Math.Abs(shootingSpots[idx] - x) + y <= l)
            {
                isCatchable = true;  // 잡을 수 있는 동물
            }

            // 이전 사대와의 거리도 확인
            if (idx > 0 && Math.Abs(shootingSpots[idx - 1] - x) + y <= l)
            {
                isCatchable = true;  // 잡을 수 있는 동물
            }

            if (isCatchable)
            {
                catchableCount++;  // 잡을 수 있는 동물의 수를 증가
            }
        }

        return catchableCount;  // 결과 반환
    }

    static void Main()
    {
        // 첫 번째 줄 입력 받기
        string[] firstInput = Console.ReadLine().Split();
        int m = int.Parse(firstInput[0]);
        int n = int.Parse(firstInput[1]);
        int l = int.Parse(firstInput[2]);

        // 사대 위치 입력 받기
        List<int> shootingSpots = Console.ReadLine().Split().Select(int.Parse).ToList();

        // 동물 위치 입력 받기
        List<Tuple<int, int>> animals = new List<Tuple<int, int>>();
        for (int i = 0; i < n; i++)
        {
            string[] animalInput = Console.ReadLine().Split();
            int x = int.Parse(animalInput[0]);
            int y = int.Parse(animalInput[1]);
            animals.Add(new Tuple<int, int>(x, y));
        }

        // 결과 계산 및 출력
        int result = CountCatchableAnimals(m, n, l, shootingSpots, animals);
        Console.WriteLine(result);  // 결과 출력
    }
}
