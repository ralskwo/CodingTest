#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

// BFS 함수 정의
int optimized_bfs(int h, int w, const vector<string>& building, const string& initial_keys) {
    // 4방향 이동을 위한 배열 (상, 우, 하, 좌)
    const int dx[] = {-1, 0, 1, 0};
    const int dy[] = {0, 1, 0, -1};
    
    // 빌딩 주변에 패딩 추가
    vector<string> extended_building(h + 2, string(w + 2, '.'));
    for (int i = 0; i < h; ++i) {
        extended_building[i + 1] = "." + building[i] + ".";
    }
    
    // 초기 열쇠 설정
    unordered_set<char> keys;
    for (char k : initial_keys) {
        if (k != '0') keys.insert(toupper(k));
    }
    
    // BFS를 위한 큐와 방문 배열 초기화
    queue<pair<int, int>> q;
    vector<vector<bool>> visited(h + 2, vector<bool>(w + 2, false));
    q.push({0, 0});
    visited[0][0] = true;
    
    // 접근 불가능한 문들을 저장할 맵
    unordered_map<char, vector<pair<int, int>>> inaccessible_doors;
    int documents_collected = 0;
    
    // BFS 시작
    while (!q.empty()) {
        int x = q.front().first, y = q.front().second;
        q.pop();
        
        // 4방향 탐색
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i], ny = y + dy[i];
            
            // 범위 체크 및 방문 여부 확인
            if (nx >= 0 && nx < h + 2 && ny >= 0 && ny < w + 2 && !visited[nx][ny]) {
                char cell = extended_building[nx][ny];
                
                // 벽인 경우 스킵
                if (cell == '*') continue;
                
                visited[nx][ny] = true;
                
                // 문서 발견
                if (cell == '$') {
                    documents_collected++;
                }
                // 열쇠 발견
                else if (islower(cell)) {
                    char key = toupper(cell);
                    if (keys.find(key) == keys.end()) {
                        keys.insert(key);
                        // 해당 열쇠로 열 수 있는 문들 처리
                        if (inaccessible_doors.find(key) != inaccessible_doors.end()) {
                            for (const auto& door : inaccessible_doors[key]) {
                                q.push(door);
                            }
                            inaccessible_doors.erase(key);
                        }
                    }
                }
                // 문 발견
                else if (isupper(cell)) {
                    if (keys.find(cell) == keys.end()) {
                        inaccessible_doors[cell].push_back({nx, ny});
                        continue;
                    }
                }
                
                // 다음 위치 큐에 추가
                q.push({nx, ny});
            }
        }
    }
    
    return documents_collected;
}

// 각 테스트 케이스 해결 함수
int solve() {
    int h, w;
    cin >> h >> w;
    
    vector<string> building(h);
    for (int i = 0; i < h; ++i) {
        cin >> building[i];
    }
    
    string initial_keys;
    cin >> initial_keys;
    
    return optimized_bfs(h, w, building, initial_keys);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    // 각 테스트 케이스에 대해 solve 함수 호출
    for (int i = 0; i < T; ++i) {
        cout << solve() << '\n';
    }
    
    return 0;
}