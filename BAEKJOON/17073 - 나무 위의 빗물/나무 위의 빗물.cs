using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 첫 번째 입력: 노드 수와 물의 양을 저장할 변수
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]); // 노드 수
        double W = double.Parse(input[1]); // 1번 노드에 고인 물의 양
        
        // 트리의 인접 리스트를 저장할 딕셔너리
        Dictionary<int, List<int>> tree = new Dictionary<int, List<int>>();
        
        // 각 노드에 연결된 간선 입력 받기
        for (int i = 0; i < N - 1; i++)
        {
            input = Console.ReadLine().Split();
            int U = int.Parse(input[0]);
            int V = int.Parse(input[1]);
            
            if (!tree.ContainsKey(U))
                tree[U] = new List<int>(); // U에 리스트 생성
            if (!tree.ContainsKey(V))
                tree[V] = new List<int>(); // V에 리스트 생성
            
            tree[U].Add(V); // U와 V 연결
            tree[V].Add(U); // V와 U 연결
        }
        
        // 리프 노드의 개수를 저장할 변수
        int leafCount = 0;
        
        // 2번 노드부터 N번 노드까지 탐색하여 리프 노드 확인
        for (int node = 2; node <= N; node++)
        {
            if (tree[node].Count == 1) // 연결된 노드가 하나인 경우 리프 노드
                leafCount++;
        }
        
        // 리프 노드에 고인 물의 양 계산
        double result = W / leafCount;
        
        // 결과를 소수점 10자리까지 출력
        Console.WriteLine($"{result:F10}");
    }
}
