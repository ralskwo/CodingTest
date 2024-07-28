#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<int> dijkstra(const vector<vector<pair<int, int>>>& graph, int start, int n) {
    vector<int> distances(n, INF);
    distances[start] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.emplace(0, start);

    while (!pq.empty()) {
        int current_distance = pq.top().first;
        int current_node = pq.top().second;
        pq.pop();

        if (current_distance > distances[current_node]) continue;

        for (const auto& [adjacent, weight] : graph[current_node]) {
            int distance = current_distance + weight;
            if (distance < distances[adjacent]) {
                distances[adjacent] = distance;
                pq.emplace(distance, adjacent);
            }
        }
    }
    return distances;
}

void remove_shortest_paths(vector<vector<pair<int, int>>>& graph, const vector<vector<pair<int, int>>>& reverse_graph, const vector<int>& shortest_distances, int D) {
    queue<int> q;
    q.push(D);
    vector<vector<bool>> removed(graph.size(), vector<bool>(graph.size(), false));

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (const auto& [prev, weight] : reverse_graph[node]) {
            if (shortest_distances[prev] + weight == shortest_distances[node]) {
                if (!removed[prev][node]) {
                    auto it = find_if(graph[prev].begin(), graph[prev].end(), [&](const pair<int, int>& edge) {
                        return edge.first == node && edge.second == weight;
                    });
                    if (it != graph[prev].end()) {
                        graph[prev].erase(it);
                        removed[prev][node] = true;
                        q.push(prev);
                    }
                }
            }
        }
    }
}

void almost_shortest_path() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    while (true) {
        int N, M;
        cin >> N >> M;

        if (N == 0 && M == 0) break;

        int S, D;
        cin >> S >> D;

        vector<vector<pair<int, int>>> graph(N), reverse_graph(N);
        
        for (int i = 0; i < M; ++i) {
            int U, V, P;
            cin >> U >> V >> P;
            graph[U].emplace_back(V, P);
            reverse_graph[V].emplace_back(U, P);
        }

        vector<int> shortest_distances = dijkstra(graph, S, N);
        int shortest_distance = shortest_distances[D];

        if (shortest_distance == INF) {
            cout << -1 << "\n";
            continue;
        }

        remove_shortest_paths(graph, reverse_graph, shortest_distances, D);
        vector<int> new_distances = dijkstra(graph, S, N);
        int new_distance = new_distances[D];

        if (new_distance == INF) {
            cout << -1 << "\n";
        } else {
            cout << new_distance << "\n";
        }
    }
}

int main() {
    almost_shortest_path();
    return 0;
}
