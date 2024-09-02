using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 1m²당 자라는 참외의 개수를 입력 받음
        int K = int.Parse(Console.ReadLine());

        // 변의 방향과 길이를 저장할 리스트 선언
        List<(int direction, int length)> edges = new List<(int, int)>();
        for(int i = 0; i < 6; i++)
        {
            string[] input = Console.ReadLine().Split(); // 입력을 공백 기준으로 분리
            int direction = int.Parse(input[0]); // 방향을 정수로 변환
            int length = int.Parse(input[1]);    // 길이를 정수로 변환
            edges.Add((direction, length));      // 리스트에 추가
        }

        // 가장 긴 가로와 세로 길이를 찾기 위한 변수 초기화
        int maxWidth = 0;
        int maxHeight = 0;

        // 각 변을 순회하며 최대 가로와 세로 길이를 찾음
        foreach(var edge in edges)
        {
            if(edge.direction == 1 || edge.direction == 2) // 동쪽(1) 또는 서쪽(2) 방향일 경우
            {
                if(edge.length > maxWidth) // 현재 변의 길이가 최대 가로보다 크면
                {
                    maxWidth = edge.length; // 최대 가로 길이를 갱신
                }
            }
            else if(edge.direction == 3 || edge.direction == 4) // 남쪽(3) 또는 북쪽(4) 방향일 경우
            {
                if(edge.length > maxHeight) // 현재 변의 길이가 최대 세로보다 크면
                {
                    maxHeight = edge.length; // 최대 세로 길이를 갱신
                }
            }
        }

        // 작은 직사각형의 가로와 세로 길이를 찾기 위한 변수 초기화
        int smallWidth = 0;
        int smallHeight = 0;

        // 각 변을 다시 순회하며 작은 직사각형의 길이를 찾음
        for(int i = 0; i < 6; i++)
        {
            var currentEdge = edges[i];
            if(currentEdge.direction == 1 || currentEdge.direction == 2) // 동쪽(1) 또는 서쪽(2) 방향일 경우
            {
                // 다음 변과 이전 변의 길이 합이 최대 세로와 같으면
                int nextIndex = (i + 1) % 6;
                int prevIndex = (i + 5) % 6;
                if(edges[nextIndex].length + edges[prevIndex].length == maxHeight)
                {
                    smallWidth = currentEdge.length; // 작은 직사각형의 가로 길이로 설정
                }
            }
            else if(currentEdge.direction == 3 || currentEdge.direction == 4) // 남쪽(3) 또는 북쪽(4) 방향일 경우
            {
                // 다음 변과 이전 변의 길이 합이 최대 가로와 같으면
                int nextIndex = (i + 1) % 6;
                int prevIndex = (i + 5) % 6;
                if(edges[nextIndex].length + edges[prevIndex].length == maxWidth)
                {
                    smallHeight = currentEdge.length; // 작은 직사각형의 세로 길이로 설정
                }
            }
        }

        // 전체 면적을 계산: 큰 직사각형 면적에서 작은 직사각형 면적을 뺌
        long area = ((long)maxWidth * (long)maxHeight) - ((long)smallWidth * (long)smallHeight);

        // 전체 참외의 개수를 계산
        long totalMelons = area * (long)K;

        // 결과 출력
        Console.WriteLine(totalMelons);
    }
}
