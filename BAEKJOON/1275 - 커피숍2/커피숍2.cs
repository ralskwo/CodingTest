using System;
using System.Text;

class SegmentTree {
    private long[] tree;
    private int n;

    public SegmentTree(int[] data) {
        n = data.Length;
        tree = new long[4 * n];
        Build(data, 1, 0, n - 1);
    }

    private long Build(int[] data, int node, int start, int end) {
        if (start == end) {
            return tree[node] = data[start];
        }
        int mid = (start + end) / 2;
        long left_sum = Build(data, node * 2, start, mid);
        long right_sum = Build(data, node * 2 + 1, mid + 1, end);
        return tree[node] = left_sum + right_sum;
    }

    private long Query(int node, int start, int end, int l, int r) {
        if (r < start || end < l)
            return 0;
        if (l <= start && end <= r)
            return tree[node];
        int mid = (start + end) / 2;
        long left_sum = Query(node * 2, start, mid, l, r);
        long right_sum = Query(node * 2 + 1, mid + 1, end, l, r);
        return left_sum + right_sum;
    }

    private void Update(int node, int start, int end, int idx, int value) {
        if (start == end) {
            tree[node] = value;
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid)
                Update(node * 2, start, mid, idx, value);
            else
                Update(node * 2 + 1, mid + 1, end, idx, value);
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }

    public long RangeQuery(int l, int r) {
        return Query(1, 0, n - 1, l, r);
    }

    public void UpdateValue(int idx, int value) {
        Update(1, 0, n - 1, idx, value);
    }
}

class Program {
    static void Main() {
        string[] inputs = Console.ReadLine().Split();
        int n = int.Parse(inputs[0]);
        int q = int.Parse(inputs[1]);

        int[] data = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        SegmentTree segTree = new SegmentTree(data);

        StringBuilder output = new StringBuilder();  // 출력을 위한 StringBuilder 사용

        for (int i = 0; i < q; i++) {
            inputs = Console.ReadLine().Split();
            int x = int.Parse(inputs[0]) - 1;
            int y = int.Parse(inputs[1]) - 1;
            int a = int.Parse(inputs[2]) - 1;
            int b = int.Parse(inputs[3]);

            if (x > y) {  
                int temp = x;
                x = y;
                y = temp;
            }

            output.AppendLine(segTree.RangeQuery(x, y).ToString());
            segTree.UpdateValue(a, b);
        }

        Console.Write(output.ToString());  // 최종적으로 결과 한 번에 출력
    }
}