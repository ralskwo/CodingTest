#include <iostream>
#include <vector>

using namespace std;

pair<int, int> fibonacci(int n, vector<pair<int, int>>& memo) {
    if (n == 0) return {1, 0};
    if (n == 1) return {0, 1};
    
    if (memo[n].first != -1) return memo[n];
    
    auto p1 = fibonacci(n-1, memo);
    auto p2 = fibonacci(n-2, memo);
    
    memo[n] = {p1.first + p2.first, p1.second + p2.second};
    return memo[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    
    while (T--) {
        int N;
        cin >> N;
        
        vector<pair<int, int>> memo(N+1, {-1, -1});
        auto result = fibonacci(N, memo);
        
        cout << result.first << " " << result.second << "\n";
    }
    
    return 0;
}