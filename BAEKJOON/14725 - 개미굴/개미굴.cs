using System;
using System.Collections.Generic;

// 트리 노드를 나타내는 클래스
class TrieNode
{
    public SortedDictionary<string, TrieNode> Children = new SortedDictionary<string, TrieNode>();
}

class Program
{
    // 트리를 깊이 우선 탐색으로 출력하는 함수
    static void PrintTrie(TrieNode node, int depth)
    {
        // 자식 노드를 사전 순서대로 출력하기 위해 SortedDictionary를 순회
        foreach (var key in node.Children.Keys)
        {
            // depth만큼 "--" 출력 후, 현재 노드의 key(먹이 이름) 출력
            Console.WriteLine(new string('-', depth * 2) + key);
            // 자식 노드를 깊이 우선 탐색으로 재귀 호출하여 출력
            PrintTrie(node.Children[key], depth + 1);
        }
    }

    static void Main()
    {
        // 입력 개수 N을 첫 줄에서 읽음
        int N = int.Parse(Console.ReadLine());

        // 트리의 루트 노드 생성
        TrieNode root = new TrieNode();

        // N번 반복하여 각 로봇 개미의 경로 정보를 입력 받음
        for (int i = 0; i < N; i++)
        {
            // 각 입력을 공백으로 분리하여 배열로 저장
            string[] input = Console.ReadLine().Split();
            int K = int.Parse(input[0]);  // 첫 번째 값은 경로에 포함된 방의 개수 K

            TrieNode currentNode = root;  // 루트 노드부터 시작

            // 각 층의 방 정보를 트리에 추가
            for (int j = 1; j <= K; j++)  // input[1]부터 먹이 정보가 시작됨
            {
                string food = input[j];  // 현재 층의 먹이 정보

                // 현재 노드의 자식 중에 해당 먹이 정보가 없으면 새 노드 추가
                if (!currentNode.Children.ContainsKey(food))
                {
                    currentNode.Children[food] = new TrieNode();
                }

                // 해당 자식 노드로 이동
                currentNode = currentNode.Children[food];
            }
        }

        // 트리의 루트 노드부터 깊이 0으로 시작하여 출력
        PrintTrie(root, 0);
    }
}
