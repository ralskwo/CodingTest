using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 입력을 처리합니다.
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]); // 보석의 수
        int k = int.Parse(input[1]); // 가방의 수

        var jewels = new List<(int weight, int value)>();
        for (int i = 0; i < n; i++)
        {
            string[] jewelInput = Console.ReadLine().Split();
            int weight = int.Parse(jewelInput[0]);
            int value = int.Parse(jewelInput[1]);
            jewels.Add((weight, value));
        }

        var bags = new List<int>();
        for (int i = 0; i < k; i++)
        {
            bags.Add(int.Parse(Console.ReadLine()));
        }

        // 보석을 무게 기준으로 오름차순 정렬합니다.
        jewels.Sort((a, b) => a.weight.CompareTo(b.weight));
        // 가방을 무게 기준으로 오름차순 정렬합니다.
        bags.Sort();

        long maxValue = 0;
        var possibleJewels = new PriorityQueue<int>();
        int jewelIndex = 0;

        // 각 가방에 대해 반복합니다.
        foreach (var bag in bags)
        {
            // 현재 가방에 담을 수 있는 모든 보석을 힙에 넣습니다.
            while (jewelIndex < jewels.Count && jewels[jewelIndex].weight <= bag)
            {
                possibleJewels.Enqueue(jewels[jewelIndex].value);
                jewelIndex++;
            }

            // 가장 비싼 보석을 선택합니다.
            if (possibleJewels.Count > 0)
            {
                maxValue += possibleJewels.Dequeue();
            }
        }

        // 최종 결과를 출력합니다.
        Console.WriteLine(maxValue);
    }
}

// 우선순위 큐 구현
public class PriorityQueue<T> where T : IComparable<T>
{
    private List<T> data;

    public PriorityQueue()
    {
        this.data = new List<T>();
    }

    public void Enqueue(T item)
    {
        data.Add(item);
        int childIndex = data.Count - 1;
        while (childIndex > 0)
        {
            int parentIndex = (childIndex - 1) / 2;
            if (data[childIndex].CompareTo(data[parentIndex]) <= 0) break;

            T tmp = data[childIndex];
            data[childIndex] = data[parentIndex];
            data[parentIndex] = tmp;
            childIndex = parentIndex;
        }
    }

    public T Dequeue()
    {
        if (data.Count == 0) throw new InvalidOperationException("Queue is empty.");

        int lastIndex = data.Count - 1;
        T frontItem = data[0];
        data[0] = data[lastIndex];
        data.RemoveAt(lastIndex);

        int parentIndex = 0;
        while (true)
        {
            int leftChildIndex = parentIndex * 2 + 1;
            if (leftChildIndex >= data.Count) break;

            int rightChildIndex = leftChildIndex + 1;
            int swapIndex = parentIndex;

            if (data[swapIndex].CompareTo(data[leftChildIndex]) < 0)
            {
                swapIndex = leftChildIndex;
            }

            if (rightChildIndex < data.Count && data[swapIndex].CompareTo(data[rightChildIndex]) < 0)
            {
                swapIndex = rightChildIndex;
            }

            if (swapIndex == parentIndex) break;

            T tmp = data[parentIndex];
            data[parentIndex] = data[swapIndex];
            data[swapIndex] = tmp;

            parentIndex = swapIndex;
        }

        return frontItem;
    }

    public int Count
    {
        get { return data.Count; }
    }
}
