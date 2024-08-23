#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();
const vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int dijkstra(const vector<vector<int>>& grid, int N) {
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
    pq.emplace(grid[0][0], 0, 0);
    vector<vector<int>> min_rupee(N, vector<int>(N, INF));
    min_rupee[0][0] = grid[0][0];
    
    while (!pq.empty()) {
        auto [curr_rupee, x, y] = pq.top();
        pq.pop();
        
        if (curr_rupee > min_rupee[x][y]) {
            continue;
        }
        
        for (const auto& [dx, dy] : directions) {
            int nx = x + dx;
            int ny = y + dy;
            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                int new_rupee = curr_rupee + grid[nx][ny];
                if (new_rupee < min_rupee[nx][ny]) {
                    min_rupee[nx][ny] = new_rupee;
                    pq.emplace(new_rupee, nx, ny);
                }
            }
        }
    }
    
    return min_rupee[N - 1][N - 1];
}

vector<string> solve_problems(const vector<pair<int, vector<vector<int>>>>& test_cases) {
    vector<string> results;
    for (size_t idx = 0; idx < test_cases.size(); ++idx) {
        int N = test_cases[idx].first;
        const auto& grid = test_cases[idx].second;
        int min_rupee = dijkstra(grid, N);
        results.push_back("Problem " + to_string(idx + 1) + ": " + to_string(min_rupee));
    }
    return results;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    vector<pair<int, vector<vector<int>>>> test_cases;
    
    while (true) {
        int N;
        cin >> N;
        if (N == 0) {
            break;
        }
        vector<vector<int>> grid(N, vector<int>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> grid[i][j];
            }
        }
        test_cases.emplace_back(N, grid);
    }
    
    vector<string> results = solve_problems(test_cases);
    for (const auto& result : results) {
        cout << result << "\n";
    }
    
    return 0;
}
