#include <iostream>  // 입출력을 위한 헤더
#include <vector>    // 동적 배열을 위한 헤더
#include <queue>     // BFS에서 사용할 큐를 위한 헤더

using namespace std;  // 표준 네임스페이스 사용

// BFS 탐색을 수행하는 함수
int bfs(int start, vector<vector<int>>& graph, int n) {
    vector<bool> visited(n + 1, false);  // 방문 여부를 기록할 벡터, 초기값 false
    vector<int> distance(n + 1, -1);     // 상근이로부터의 거리를 기록할 벡터, 초기값 -1
    queue<int> q;                        // BFS 탐색을 위한 큐
    
    q.push(start);              // 시작점(상근이의 학번)을 큐에 삽입
    visited[start] = true;      // 시작점 방문 처리
    distance[start] = 0;        // 시작점의 거리는 0으로 설정
    
    while (!q.empty()) {        // 큐가 빌 때까지 반복
        int current = q.front();  // 큐의 맨 앞 원소를 가져옴
        q.pop();                  // 큐에서 원소 제거
        
        // 현재 노드의 모든 이웃(친구)에 대해 반복
        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {           // 방문하지 않은 이웃이라면
                visited[neighbor] = true;       // 방문 처리
                distance[neighbor] = distance[current] + 1;  // 거리 갱신
                q.push(neighbor);               // 큐에 이웃 추가
            }
        }
    }
    
    int invite_count = 0;  // 초대할 친구 수를 세는 변수
    // 상근이(1번 학번)를 제외한 모든 학생에 대해 반복
    for (int i = 2; i <= n; i++) {
        // 상근이로부터의 거리가 1 또는 2인 경우
        if (0 < distance[i] && distance[i] <= 2) {
            invite_count++;  // 초대할 친구 수 증가
        }
    }
    
    return invite_count;  // 초대할 친구 수 반환
}

int main() {
    int n, m;
    cin >> n >> m;  // 동기의 수(n)와 친구 관계의 수(m) 입력받기
    
    // 그래프를 표현할 2차원 벡터 초기화 (인덱스 1부터 n까지 사용)
    vector<vector<int>> graph(n + 1);
    
    // 친구 관계 입력받기
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;  // 친구 관계 a-b 입력
        graph[a].push_back(b);  // a의 친구 목록에 b 추가
        graph[b].push_back(a);  // b의 친구 목록에 a 추가 (양방향 그래프)
    }
    
    // 상근이(1번 학번)에서 시작하여 BFS 탐색 수행
    int result = bfs(1, graph, n);
    
    cout << result << endl;  // 결과(초대할 친구 수) 출력
    
    return 0;  // 프로그램 정상 종료
}