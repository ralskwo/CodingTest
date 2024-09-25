using System;

class Program
{
    // 세 점의 좌표를 받아 방향을 계산하는 함수
    static int FindDirection(int x1, int y1, int x2, int y2, int x3, int y3)
    {
        // 벡터 P1P2와 P2P3의 외적을 계산
        int crossProduct = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2);

        // 외적 결과에 따라 방향을 판별
        if (crossProduct > 0)
            return 1;  // 반시계 방향
        else if (crossProduct < 0)
            return -1; // 시계 방향
        else
            return 0;  // 일직선
    }

    static void Main(string[] args)
    {
        // 첫 번째 점의 좌표를 입력받기
        string[] point1 = Console.ReadLine().Split();
        int x1 = int.Parse(point1[0]);
        int y1 = int.Parse(point1[1]);

        // 두 번째 점의 좌표를 입력받기
        string[] point2 = Console.ReadLine().Split();
        int x2 = int.Parse(point2[0]);
        int y2 = int.Parse(point2[1]);

        // 세 번째 점의 좌표를 입력받기
        string[] point3 = Console.ReadLine().Split();
        int x3 = int.Parse(point3[0]);
        int y3 = int.Parse(point3[1]);

        // 방향을 계산하고 결과 출력
        Console.WriteLine(FindDirection(x1, y1, x2, y2, x3, y3));
    }
}
