#include <iostream>
#include <vector>
using namespace std;

class SegmentTree {
    vector<int> tree, lazy;
    int n;

public:
    SegmentTree(int n) : n(n) {
        tree.resize(4 * n, 0);
        lazy.resize(4 * n, 0);
    }

    void updateLazy(int node, int start, int end) {
        if (lazy[node] != 0) {
            tree[node] = (end - start + 1) - tree[node];

            if (start != end) {
                lazy[node * 2] ^= 1;
                lazy[node * 2 + 1] ^= 1;
            }
            lazy[node] = 0;
        }
    }

    void updateRange(int node, int start, int end, int l, int r) {
        updateLazy(node, start, end);

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
        updateRange(node * 2, start, mid, l, r);
        updateRange(node * 2 + 1, mid + 1, end, l, r);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    int queryRange(int node, int start, int end, int l, int r) {
        updateLazy(node, start, end);

        if (start > r || end < l) return 0;

        if (start >= l && end <= r) return tree[node];

        int mid = (start + end) / 2;
        int leftQuery = queryRange(node * 2, start, mid, l, r);
        int rightQuery = queryRange(node * 2 + 1, mid + 1, end, l, r);
        return leftQuery + rightQuery;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;

    SegmentTree segTree(n);

    for (int i = 0; i < m; i++) {
        int o, si, ti;
        cin >> o >> si >> ti;
        if (o == 0) {
            segTree.updateRange(1, 0, n - 1, si - 1, ti - 1);
        } else if (o == 1) {
            int result = segTree.queryRange(1, 0, n - 1, si - 1, ti - 1);
            cout << result << "\n";
        }
    }

    return 0;
}
