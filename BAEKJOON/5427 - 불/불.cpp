#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

// 방향 벡터 (동, 서, 남, 북)
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

// 빌딩 탈출 함수
string escape_building(int w, int h, vector<string>& building) {
    queue<pair<int, int>> fire_queue; // 불의 위치를 저장할 큐
    queue<pair<int, int>> person_queue; // 상근이의 위치를 저장할 큐
    vector<vector<int>> fire_times(h, vector<int>(w, -1)); // 불이 각 위치에 도달하는 시간을 저장하는 배열
    vector<vector<int>> person_times(h, vector<int>(w, -1)); // 상근이가 각 위치에 도달하는 시간을 저장하는 배열

    // 초기 위치 설정
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            if (building[y][x] == '*') {
                fire_queue.push({x, y}); // 불의 위치를 큐에 추가
                fire_times[y][x] = 0; // 불이 시작한 위치의 시간을 0으로 설정
            }
            if (building[y][x] == '@') {
                person_queue.push({x, y}); // 상근이의 시작 위치를 큐에 추가
                person_times[y][x] = 0; // 상근이가 시작한 위치의 시간을 0으로 설정
            }
        }
    }

    // 불의 확산 BFS
    while (!fire_queue.empty()) {
        int x = fire_queue.front().first;
        int y = fire_queue.front().second;
        fire_queue.pop();
        
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 지도 범위 내에 있고, 아직 불이 도달하지 않은 빈 공간일 때
            if (nx >= 0 && nx < w && ny >= 0 && ny < h && fire_times[ny][nx] == -1 && building[ny][nx] == '.') {
                fire_times[ny][nx] = fire_times[y][x] + 1; // 현재 시간에서 1초 뒤에 불이 도달
                fire_queue.push({nx, ny}); // 새로운 불의 위치를 큐에 추가
            }
        }
    }

    // 상근이의 이동 BFS
    while (!person_queue.empty()) {
        int x = person_queue.front().first;
        int y = person_queue.front().second;
        person_queue.pop();
        
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 상근이가 지도 밖으로 나가면 탈출 성공
            if (nx < 0 || nx >= w || ny < 0 || ny >= h) {
                return to_string(person_times[y][x] + 1); // 탈출하는데 걸린 시간 반환
            }
            
            // 이동할 수 있는 빈 공간이며, 아직 방문하지 않은 경우
            if (nx >= 0 && nx < w && ny >= 0 && ny < h && person_times[ny][nx] == -1 && building[ny][nx] == '.') {
                // 불이 도달하지 않았거나 상근이가 먼저 도착할 수 있는 경우에만 이동
                if (fire_times[ny][nx] == -1 || fire_times[ny][nx] > person_times[y][x] + 1) {
                    person_times[ny][nx] = person_times[y][x] + 1; // 이동 시간을 기록
                    person_queue.push({nx, ny}); // 새로운 위치를 큐에 추가
                }
            }
        }
    }

    return "IMPOSSIBLE"; // 탈출할 수 없는 경우
}

int main() {
    int t;
    cin >> t; // 테스트 케이스의 개수 입력

    while (t--) {
        int w, h;
        cin >> w >> h; // 빌딩의 너비와 높이 입력
        vector<string> building(h);
        
        for (int i = 0; i < h; ++i) {
            cin >> building[i]; // 빌딩의 지도 입력
        }

        cout << escape_building(w, h, building) << endl; // 각 테스트 케이스의 결과 출력
    }

    return 0;
}