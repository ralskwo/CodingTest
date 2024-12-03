#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

// 5x5 격자를 저장할 변수
vector<string> grid(5);

// 방향 벡터 (상하좌우 이동)
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

// 주어진 좌표들이 서로 인접한지 확인하는 함수
bool isAdjacent(const vector<pair<int, int>>& selected) {
    // BFS 탐색을 위한 큐
    queue<pair<int, int>> q;
    // 방문 여부를 저장할 집합
    set<pair<int, int>> visited;
    // 초기화: 첫 번째 좌표를 큐와 방문 집합에 추가
    q.push(selected[0]);
    visited.insert(selected[0]);
    int count = 1; // 연결된 좌표 수를 저장

    // BFS 탐색
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        // 상하좌우로 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            pair<int, int> neighbor = {nx, ny};

            // 선택된 좌표에 포함되며 아직 방문하지 않은 좌표라면
            if (find(selected.begin(), selected.end(), neighbor) != selected.end() && visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
                count++;
            }
        }
    }

    // 연결된 좌표 수가 7개라면 true 반환
    return count == 7;
}

// 선택된 좌표들 중 'S' 학생의 수를 세는 함수
int countS(const vector<pair<int, int>>& selected) {
    int count = 0;
    for (auto [x, y] : selected) {
        if (grid[x][y] == 'S') count++;
    }
    return count;
}

int main() {
    // 격자 입력 받기
    for (int i = 0; i < 5; i++) {
        cin >> grid[i];
    }

    // 가능한 모든 좌표를 저장할 벡터
    vector<pair<int, int>> positions;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            positions.push_back({i, j});
        }
    }

    int result = 0;

    // 25개의 좌표 중 7개를 선택하는 모든 조합 생성
    vector<bool> comb(25, false);
    fill(comb.end() - 7, comb.end(), true);
    do {
        vector<pair<int, int>> selected;
        for (int i = 0; i < 25; i++) {
            if (comb[i]) selected.push_back(positions[i]);
        }

        // 조건 확인: 'S' 학생이 4명 이상이고, 좌표들이 인접한 경우
        if (countS(selected) >= 4 && isAdjacent(selected)) {
            result++;
        }
    } while (next_permutation(comb.begin(), comb.end()));

    // 결과 출력
    cout << result << endl;

    return 0;
}
