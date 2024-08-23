#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();

// 플로이드-워셜 알고리즘을 수행하는 함수
void floyd_warshall(int n, vector<vector<int>>& dist, vector<vector<int>>& next) {
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    next[i][j] = next[i][k];
                }
            }
        }
    }
}

// 경로를 재구성하는 함수
vector<int> construct_path(int start, int end, vector<vector<int>>& next) {
    if (next[start][end] == -1) {
        return {}; // 경로가 존재하지 않음
    }
    vector<int> path = {start};
    while (start != end) {
        start = next[start][end];
        path.push_back(start);
    }
    return path;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> dist(n, vector<int>(n, INF));
    vector<vector<int>> next(n, vector<int>(n, -1));

    // 자기 자신으로의 경로는 0으로 초기화
    for (int i = 0; i < n; ++i) {
        dist[i][i] = 0;
    }

    // 버스 정보 입력받기
    for (int i = 0; i < m; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        a--; b--; // 0-index로 변환
        if (c < dist[a][b]) {
            dist[a][b] = c;
            next[a][b] = b;
        }
    }

    // 플로이드-워셜 알고리즘 수행
    floyd_warshall(n, dist, next);

    // 모든 쌍에 대한 최단 거리 출력
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] == INF) {
                cout << 0 << " ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }

    // 경로 재구성 및 출력
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] == INF) {
                cout << 0 << endl;
            } else {
                vector<int> path = construct_path(i, j, next);
                cout << path.size() << " ";
                for (int v : path) {
                    cout << (v + 1) << " "; // 1-index로 변환하여 출력
                }
                cout << endl;
            }
        }
    }

    return 0;
}
