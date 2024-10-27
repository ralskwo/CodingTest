#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class SegmentTree {
private:
    vector<long long> tree;
    int n;

    long long build(const vector<int>& data, int node, int start, int end) {
        if (start == end) {
            return tree[node] = data[start];
        }
        int mid = (start + end) / 2;
        long long left_sum = build(data, node * 2, start, mid);
        long long right_sum = build(data, node * 2 + 1, mid + 1, end);
        return tree[node] = left_sum + right_sum;
    }

    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l)
            return 0;
        if (l <= start && end <= r)
            return tree[node];
        int mid = (start + end) / 2;
        long long left_sum = query(node * 2, start, mid, l, r);
        long long right_sum = query(node * 2 + 1, mid + 1, end, l, r);
        return left_sum + right_sum;
    }

    void update(int node, int start, int end, int idx, int value) {
        if (start == end) {
            tree[node] = value;
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid)
                update(node * 2, start, mid, idx, value);
            else
                update(node * 2 + 1, mid + 1, end, idx, value);
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }

public:
    SegmentTree(const vector<int>& data) : n(data.size()) {
        tree.resize(4 * n);
        build(data, 1, 0, n - 1);
    }

    long long range_query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }

    void update_value(int idx, int value) {
        update(1, 0, n - 1, idx, value);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> data(n);
    for (int i = 0; i < n; ++i) {
        cin >> data[i];
    }

    SegmentTree seg_tree(data);
    vector<long long> results;

    for (int i = 0; i < q; ++i) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;
        x--; y--; a--;
        if (x > y) swap(x, y);
        results.push_back(seg_tree.range_query(x, y));
        seg_tree.update_value(a, b);
    }

    for (long long result : results) {
        cout << result << '\n';
    }

    return 0;
}