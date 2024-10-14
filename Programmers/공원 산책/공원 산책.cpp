#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    int H = park.size();       // 공원의 세로 길이
    int W = park[0].size();    // 공원의 가로 길이
    int x = 0, y = 0;          // 시작 지점의 좌표를 저장할 변수
    
    // 시작 위치 찾기
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (park[i][j] == 'S') {  // 'S' 위치를 찾으면
                x = i;
                y = j;
            }
        }
    }

    // 방향에 따른 이동 좌표 변화 정의 (북, 남, 서, 동)
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    char directions[] = {'N', 'S', 'W', 'E'};

    // 각 명령어 처리
    for (string route : routes) {
        char dir = route[0];          // 이동할 방향
        int n = stoi(route.substr(2)); // 이동할 거리

        int nx = x, ny = y;           // 임시 좌표 초기화
        bool valid_move = true;       // 이동 가능 여부

        // 주어진 거리만큼 이동 시도
        for (int i = 0; i < 4; i++) {
            if (directions[i] == dir) {
                for (int j = 0; j < n; j++) {
                    nx += dx[i];
                    ny += dy[i];

                    // 공원 경계 밖으로 나가거나 장애물을 만나면 이동 중단
                    if (nx < 0 || nx >= H || ny < 0 || ny >= W || park[nx][ny] == 'X') {
                        valid_move = false;
                        break;
                    }
                }
                break;
            }
        }

        // 유효한 이동이라면 좌표 갱신
        if (valid_move) {
            x = nx;
            y = ny;
        }
    }

    // 최종 위치 반환
    return {x, y};
}

int main() {
    vector<string> park = {"SOO", "OXX", "OOO"};
    vector<string> routes = {"E 2", "S 2", "W 1"};
    vector<int> result = solution(park, routes);

    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
