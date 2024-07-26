#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

set<int> bfs(const vector<vector<int>>& graph, int start) {
    set<int> visited;
    queue<int> q;
    q.push(start);
    visited.insert(start);
    
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int neighbor : graph[v]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
    return visited;
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> graph(n + 1); // 컴퓨터 번호가 1부터 시작하므로 n+1 크기
    
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    set<int> infected_computers = bfs(graph, 1);
    
    // 1번 컴퓨터를 제외
    infected_computers.erase(1);
    
    // 결과 출력
    cout << infected_computers.size() << endl;
    
    return 0;
}
