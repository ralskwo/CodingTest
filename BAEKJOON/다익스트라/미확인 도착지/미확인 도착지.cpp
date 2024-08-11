#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INF 1e9

using namespace std;

vector<vector<pair<int, int>>> graph;

vector<int> dijkstra(int start, int num_nodes) {
    vector<int> distances(num_nodes + 1, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> priority_queue;

    priority_queue.push({0, start});
    distances[start] = 0;

    while (!priority_queue.empty()) {
        int current_distance = priority_queue.top().first;
        int current_node = priority_queue.top().second;
        priority_queue.pop();

        if (distances[current_node] < current_distance) {
            continue;
        }

        for (auto& edge : graph[current_node]) {
            int adjacent = edge.first;
            int weight = edge.second;
            int distance = current_distance + weight;

            if (distance < distances[adjacent]) {
                distances[adjacent] = distance;
                priority_queue.push({distance, adjacent});
            }
        }
    }

    return distances;
}

int main() {
    int num_test_cases;
    cin >> num_test_cases;

    while (num_test_cases--) {
        int num_nodes, num_edges, num_dest_candidates;
        cin >> num_nodes >> num_edges >> num_dest_candidates;

        int start_node, must_pass1, must_pass2;
        cin >> start_node >> must_pass1 >> must_pass2;

        graph.assign(num_nodes + 1, vector<pair<int, int>>());

        for (int i = 0; i < num_edges; i++) {
            int node1, node2, weight;
            cin >> node1 >> node2 >> weight;
            graph[node1].emplace_back(node2, weight);
            graph[node2].emplace_back(node1, weight);
        }

        vector<int> dest_candidates(num_dest_candidates);
        for (int i = 0; i < num_dest_candidates; i++) {
            cin >> dest_candidates[i];
        }

        vector<int> start_to_all = dijkstra(start_node, num_nodes);
        vector<int> g_to_all = dijkstra(must_pass1, num_nodes);
        vector<int> h_to_all = dijkstra(must_pass2, num_nodes);

        vector<int> result;
        for (int candidate : dest_candidates) {
            if ((start_to_all[must_pass1] + g_to_all[must_pass2] + h_to_all[candidate] == start_to_all[candidate]) ||
                (start_to_all[must_pass2] + h_to_all[must_pass1] + g_to_all[candidate] == start_to_all[candidate])) {
                result.push_back(candidate);
            }
        }

        sort(result.begin(), result.end());
        for (int r : result) {
            cout << r << " ";
        }
        cout << endl;
    }

    return 0;
}
