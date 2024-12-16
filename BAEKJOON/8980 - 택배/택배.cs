using System;
using System.Collections.Generic;

class Program {
    // 박스 정보를 저장하기 위한 클래스 정의
    class Box {
        public int Start { get; set; }
        public int End { get; set; }
        public int Num { get; set; }
    }

    // 트럭 한 대로 배송할 수 있는 최대 박스 수를 계산하는 함수
    static int MaxBoxesDelivered(int n, int c, List<Box> boxes) {
        // 받는 마을 번호를 기준으로 오름차순 정렬
        boxes.Sort((a, b) => a.End.CompareTo(b.End));

        // 각 마을에서 트럭 적재 상태를 저장하는 배열
        int[] deliveries = new int[n + 1];

        int totalDelivered = 0; // 최종 배송된 박스 수

        // 각 박스 정보를 순회
        foreach (var box in boxes) {
            // 현재 구간에서 트럭 적재 가능한 최대 박스 수 계산
            int maxCapacity = c;
            for (int i = box.Start; i < box.End; i++) {
                maxCapacity = Math.Min(maxCapacity, c - deliveries[i]);
            }
            maxCapacity = Math.Min(maxCapacity, box.Num);

            // 구간 내 각 마을에 적재 상황 업데이트
            for (int i = box.Start; i < box.End; i++) {
                deliveries[i] += maxCapacity;
            }

            // 누적 배송된 박스 수 갱신
            totalDelivered += maxCapacity;
        }

        return totalDelivered; // 최종 배송된 박스 수 반환
    }

    static void Main(string[] args) {
        // 입력값 읽기
        string[] firstLine = Console.ReadLine().Split();
        int n = int.Parse(firstLine[0]);
        int c = int.Parse(firstLine[1]);

        int m = int.Parse(Console.ReadLine());

        // 박스 정보를 저장할 리스트
        List<Box> boxes = new List<Box>();
        for (int i = 0; i < m; i++) {
            string[] boxInfo = Console.ReadLine().Split();
            int start = int.Parse(boxInfo[0]);
            int end = int.Parse(boxInfo[1]);
            int num = int.Parse(boxInfo[2]);
            boxes.Add(new Box { Start = start, End = end, Num = num });
        }

        // 결과 출력
        Console.WriteLine(MaxBoxesDelivered(n, c, boxes));
    }
}
