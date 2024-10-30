using System;
using System.IO;

class SegmentTree {
    private int[] tree, lazy;
    private int n;
    
    public SegmentTree(int n) {
        this.n = n;
        tree = new int[4 * n];
        lazy = new int[4 * n];
    }

    private void UpdateLazy(int node, int start, int end) {
        if (lazy[node] != 0) {
            tree[node] = (end - start + 1) - tree[node];
            
            if (start != end) {
                lazy[node * 2] ^= 1;
                lazy[node * 2 + 1] ^= 1;
            }
            lazy[node] = 0;
        }
    }

    public void UpdateRange(int node, int start, int end, int l, int r) {
        UpdateLazy(node, start, end);
        
        if (start > r || end < l) return;
        
        if (start >= l && end <= r) {
            tree[node] = (end - start + 1) - tree[node];
            if (start != end) {
                lazy[node * 2] ^= 1;
                lazy[node * 2 + 1] ^= 1;
            }
            return;
        }

        int mid = (start + end) / 2;
        UpdateRange(node * 2, start, mid, l, r);
        UpdateRange(node * 2 + 1, mid + 1, end, l, r);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    public int QueryRange(int node, int start, int end, int l, int r) {
        UpdateLazy(node, start, end);
        
        if (start > r || end < l) return 0;
        
        if (start >= l && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        int leftQuery = QueryRange(node * 2, start, mid, l, r);
        int rightQuery = QueryRange(node * 2 + 1, mid + 1, end, l, r);
        return leftQuery + rightQuery;
    }
}

class Program {
    static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };

        var inputs = reader.ReadLine().Split();
        int n = int.Parse(inputs[0]);
        int m = int.Parse(inputs[1]);

        SegmentTree segTree = new SegmentTree(n);

        for (int i = 0; i < m; i++) {
            var line = reader.ReadLine().Split();
            int o = int.Parse(line[0]);
            int si = int.Parse(line[1]);
            int ti = int.Parse(line[2]);

            if (o == 0) {
                segTree.UpdateRange(1, 0, n - 1, si - 1, ti - 1);
            } else if (o == 1) {
                int result = segTree.QueryRange(1, 0, n - 1, si - 1, ti - 1);
                writer.WriteLine(result);
            }
        }
        writer.Flush();
    }
}