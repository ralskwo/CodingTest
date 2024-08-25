#include <iostream>                  // 표준 입출력을 위한 헤더 파일
#include <vector>                    // 벡터를 사용하기 위한 헤더 파일
#include <deque>                     // 덱(Deque)을 사용하기 위한 헤더 파일
#include <algorithm>                 // min 함수를 사용하기 위한 헤더 파일
#include <tuple>                     // tie 함수를 사용하기 위한 헤더 파일
#include <limits>                    // numeric_limits를 사용하기 위한 헤더 파일

using namespace std;                 // 표준 네임스페이스를 사용

// BFS 함수 정의
vector<vector<int>> bfs(pair<int, int> start, const vector<string>& prison_map, int h, int w) {
    vector<vector<int>> dist(h + 2, vector<int>(w + 2, numeric_limits<int>::max())); // 거리 배열을 무한대로 초기화
    deque<pair<int, int>> queue;    // BFS 탐색을 위한 덱(Deque) 선언
    queue.push_back(start);         // 시작 위치를 덱에 추가
    dist[start.first][start.second] = 0; // 시작 위치의 거리를 0으로 설정

    int dx[] = {-1, 1, 0, 0};       // 상, 하, 좌, 우로 이동하기 위한 배열
    int dy[] = {0, 0, -1, 1};

    while (!queue.empty()) {        // 덱이 빌 때까지 BFS 탐색을 수행
        int x, y;
        tie(x, y) = queue.front();  // 덱의 첫 번째 원소를 가져옴
        queue.pop_front();          // 덱의 첫 번째 원소를 제거

        for (int i = 0; i < 4; ++i) { // 네 방향으로 이동을 시도
            int nx = x + dx[i];     // 새로운 x 좌표
            int ny = y + dy[i];     // 새로운 y 좌표

            if (nx >= 0 && nx < h + 2 && ny >= 0 && ny < w + 2) { // 새로운 좌표가 맵의 범위 내에 있는지 확인
                if (prison_map[nx][ny] != '*' && dist[nx][ny] == numeric_limits<int>::max()) {
                    // 벽이 아니고 아직 방문하지 않은 경우
                    if (prison_map[nx][ny] == '#') {  // 만약 문을 만났다면
                        dist[nx][ny] = dist[x][y] + 1; // 거리를 1 증가시키고
                        queue.push_back({nx, ny});    // 덱의 뒤에 추가
                    } else {                          // 빈 공간이라면
                        dist[nx][ny] = dist[x][y];    // 거리를 그대로 유지하고
                        queue.push_front({nx, ny});   // 덱의 앞에 추가 (우선적으로 처리)
                    }
                }
            }
        }
    }

    return dist;                   // 시작점으로부터 각 위치까지의 최소 거리를 반환
}

// solve 함수 정의
int solve(const vector<string>& prison_map, int h, int w) {
    vector<pair<int, int>> prisoners; // 죄수들의 위치를 저장할 벡터

    for (int i = 0; i < h + 2; ++i) { // 맵 전체를 탐색하며 죄수들의 위치를 찾음
        for (int j = 0; j < w + 2; ++j) {
            if (prison_map[i][j] == '$') {
                prisoners.push_back({i, j}); // 죄수의 위치를 벡터에 추가
            }
        }
    }

    auto dist1 = bfs({0, 0}, prison_map, h, w);       // 외부에서 시작하는 BFS
    auto dist2 = bfs(prisoners[0], prison_map, h, w); // 첫 번째 죄수 위치에서 BFS
    auto dist3 = bfs(prisoners[1], prison_map, h, w); // 두 번째 죄수 위치에서 BFS

    int result = numeric_limits<int>::max(); // 최솟값을 저장하기 위한 변수 초기화

    for (int i = 0; i < h + 2; ++i) { // 맵 전체를 탐색하면서 최소 문의 개수를 계산
        for (int j = 0; j < w + 2; ++j) {
            if (prison_map[i][j] != '*') { // 벽이 아닌 경우
                int total_cost = dist1[i][j] + dist2[i][j] + dist3[i][j]; // 세 경로의 거리 합산
                if (prison_map[i][j] == '#') { // 만약 위치가 문이라면
                    total_cost -= 2; // 중복된 문의 개수를 제거
                }
                result = min(result, total_cost); // 현재까지의 최소값과 비교하여 업데이트
            }
        }
    }

    return result; // 최종 계산된 최소 문의 개수를 반환
}

// main 함수 정의
int main() {
    int T;                             // 테스트 케이스 개수
    cin >> T;                          // 테스트 케이스 개수 입력
    vector<int> results;               // 결과를 저장할 벡터

    while (T--) {                      // 테스트 케이스마다 반복
        int h, w;
        cin >> h >> w;                 // 감옥의 높이와 너비 입력
        vector<string> prison_map(h + 2, string(w + 2, '.')); // 맵을 확장하여 초기화

        for (int i = 1; i <= h; ++i) {
            string line;
            cin >> line;               // 감옥의 각 줄을 입력받음
            prison_map[i] = '.' + line + '.'; // 입력받은 줄을 확장하여 맵에 저장
        }

        results.push_back(solve(prison_map, h, w)); // 각 테스트 케이스의 결과를 벡터에 저장
    }

    for (int result : results) {       // 모든 결과를 출력
        cout << result << endl;
    }

    return 0;
}
