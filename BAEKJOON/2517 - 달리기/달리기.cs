using System;
using System.Collections.Generic;

class FenwickTree
{
    private int[] tree;
    private int size;

    public FenwickTree(int size)
    {
        this.size = size;
        tree = new int[size + 1];
    }

    // 특정 인덱스에 값을 추가하는 함수
    public void Update(int index, int value)
    {
        while (index <= size)
        {
            tree[index] += value;
            index += index & -index;
        }
    }

    // 특정 인덱스까지의 누적 합을 계산하는 함수
    public int Query(int index)
    {
        int result = 0;
        while (index > 0)
        {
            result += tree[index];
            index -= index & -index;
        }
        return result;
    }
}

class Program
{
    static List<int> CoordinateCompress(List<int> values)
    {
        var sortedUnique = new List<int>(values);
        sortedUnique.Sort((a, b) => b.CompareTo(a));
        sortedUnique = new HashSet<int>(sortedUnique).ToList();

        var rank = new Dictionary<int, int>();
        for (int i = 0; i < sortedUnique.Count; i++)
        {
            rank[sortedUnique[i]] = i + 1;
        }

        var compressed = new List<int>();
        foreach (var value in values)
        {
            compressed.Add(rank[value]);
        }

        return compressed;
    }

    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        var abilities = new List<int>();

        for (int i = 0; i < N; i++)
        {
            abilities.Add(int.Parse(Console.ReadLine()));
        }

        // 좌표 압축 수행
        var compressedAbilities = CoordinateCompress(abilities);
        int maxValue = compressedAbilities.Max();
        var fenwickTree = new FenwickTree(maxValue);

        var results = new List<int>();

        // 각 선수의 압축된 실력을 순회하며 등수를 계산
        foreach (var ability in compressedAbilities)
        {
            // 현재 선수보다 앞에 있는 더 높은 실력의 선수 수 쿼리
            int higherCount = fenwickTree.Query(ability - 1);
            results.Add(higherCount + 1);

            // 현재 선수의 능력을 펜윅 트리에 추가
            fenwickTree.Update(ability, 1);
        }

        // 결과 출력
        Console.WriteLine(string.Join("\n", results));
    }
}