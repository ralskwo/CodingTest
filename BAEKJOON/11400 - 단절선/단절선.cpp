#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> graph; // 그래프를 저장할 인접 리스트
vector<int> dfs_num;       // 노드의 방문 순서를 저장
vector<int> low;           // 노드의 최소 도달 순서를 저장
vector<pair<int, int>> bridges; // 단절선을 저장할 벡터
int timer = 0;             // DFS 방문 순서를 기록할 타이머 변수

void dfs(int curr, int parent) {
    dfs_num[curr] = low[curr] = timer++; // 현재 노드의 방문 순서와 low 값을 타이머로 초기화

    for (int neighbor : graph[curr]) { // 현재 노드의 이웃 노드 탐색
        if (neighbor == parent) // 부모 노드로 되돌아가는 간선은 무시
            continue;

        if (dfs_num[neighbor] == -1) { // 이웃 노드가 아직 방문되지 않은 경우
            dfs(neighbor, curr); // 이웃 노드로 DFS 탐색
            low[curr] = min(low[curr], low[neighbor]); // low 값을 업데이트

            if (low[neighbor] > dfs_num[curr]) { // 단절선 조건
                bridges.push_back({min(curr, neighbor), max(curr, neighbor)}); // 단절선을 리스트에 추가
            }
        } else { // 이미 방문된 이웃 노드라면
            low[curr] = min(low[curr], dfs_num[neighbor]); // low 값을 업데이트
        }
    }
}

int main() {
    int V, E;
    cin >> V >> E; // 노드 개수와 간선 개수 입력 받기

    graph.resize(V + 1); // 1부터 시작하는 노드 번호에 맞게 크기 설정
    dfs_num.assign(V + 1, -1); // 방문 순서 초기화
    low.assign(V + 1, -1);     // low 값 초기화

    for (int i = 0; i < E; i++) {
        int A, B;
        cin >> A >> B; // 간선 정보 입력 받기
        graph[A].push_back(B); // 무방향 간선이므로 양쪽에 추가
        graph[B].push_back(A);
    }

    for (int i = 1; i <= V; i++) { // 모든 노드를 탐색
        if (dfs_num[i] == -1) { // 방문되지 않은 노드에 대해 DFS 수행
            dfs(i, -1); // 부모 노드가 없는 상태에서 시작
        }
    }

    sort(bridges.begin(), bridges.end()); // 단절선을 사전순으로 정렬

    cout << bridges.size() << "\n"; // 단절선의 개수 출력
    for (auto &bridge : bridges) { // 단절선 출력
        cout << bridge.first << " " << bridge.second << "\n";
    }

    return 0;
}
