#include <iostream>
#include <deque>
#include <vector>
using namespace std;

class ConvexHullTrick {
public:
    deque<pair<long long, long long>> hull;

    bool is_redundant(pair<long long, long long> l1, pair<long long, long long> l2, pair<long long, long long> l3) {
        // (c3 - c1) / (m1 - m3) >= (c2 - c1) / (m1 - m2)
        return (l3.second - l1.second) * (l1.first - l2.first) <= (l2.second - l1.second) * (l1.first - l3.first);
    }

    void add_line(long long m, long long c) {
        while (hull.size() >= 2 && is_redundant(hull[hull.size()-2], hull.back(), {m, c})) {
            hull.pop_back();
        }
        hull.emplace_back(m, c);
    }

    long long evaluate(pair<long long, long long> line, long long x) {
        return line.first * x + line.second;
    }

    long long get_max(long long x) {
        while (hull.size() >= 2 && evaluate(hull[0], x) <= evaluate(hull[1], x)) {
            hull.pop_front();
        }
        return evaluate(hull[0], x);
    }
};

long long max_adjusted_combat_power(int n, long long a, long long b, long long c, const vector<int>& x) {
    long long dp_prev = 0;
    long long prefix_sum = 0;

    ConvexHullTrick cht;
    cht.add_line(0, 0);

    for (int j = 1; j <= n; ++j) {
        prefix_sum += x[j - 1];
        long long S = prefix_sum;
        long long dp_curr = a * S * S + b * S + c + cht.get_max(S);
        cht.add_line(-2 * a * S, dp_curr + a * S * S - b * S);
        dp_prev = dp_curr;
    }

    return dp_prev;
}

int main() {
    int n;
    long long a, b, c;
    cin >> n >> a >> b >> c;
    vector<int> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }

    cout << max_adjusted_combat_power(n, a, b, c, x) << endl;

    return 0;
}
