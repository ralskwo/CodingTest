#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n, m; // 가수의 수 n과 보조 PD의 수 m
    cin >> n >> m;

    vector<vector<int>> graph(n + 1); // 그래프를 인접 리스트로 표현
    vector<int> indegree(n + 1, 0);  // 각 노드의 진입 차수를 저장할 배열

    // 보조 PD가 제시한 순서를 그래프로 구성
    for (int i = 0; i < m; i++) {
        int k; // 현재 보조 PD가 담당하는 가수의 수
        cin >> k;
        vector<int> sequence(k); // 보조 PD가 정한 가수 순서
        for (int j = 0; j < k; j++) {
            cin >> sequence[j];
        }
        for (int j = 0; j < k - 1; j++) {
            // 간선 추가 및 진입 차수 증가
            graph[sequence[j]].push_back(sequence[j + 1]);
            indegree[sequence[j + 1]]++;
        }
    }

    // 위상 정렬 수행
    queue<int> q; // 진입 차수가 0인 노드를 처리할 큐
    vector<int> result; // 정렬된 결과를 저장할 배열

    // 초기 진입 차수가 0인 노드를 큐에 추가
    for (int i = 1; i <= n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        result.push_back(current); // 현재 노드를 결과에 추가

        for (int neighbor : graph[current]) {
            indegree[neighbor]--; // 연결된 노드의 진입 차수를 감소
            if (indegree[neighbor] == 0) {
                q.push(neighbor); // 진입 차수가 0이 된 노드를 큐에 추가
            }
        }
    }

    // 결과 검증
    if (result.size() != n) {
        cout << 0 << endl; // 사이클이 발생한 경우 0 출력
    } else {
        for (int node : result) {
            cout << node << endl; // 정렬된 결과 출력
        }
    }

    return 0;
}
