#include <iostream> // 표준 입출력 라이브러리 포함
#include <vector> // 벡터 라이브러리 포함
#include <set> // 셋 라이브러리 포함
#include <iomanip> // 입출력 조작 라이브러리 포함

using namespace std;

// 방향과 확률을 전역 변수로 설정
vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // 동, 서, 남, 북 이동에 따른 좌표 변화
vector<double> probs(4); // 동, 서, 남, 북 이동 확률을 저장할 벡터

// 깊이 우선 탐색(DFS) 함수
double dfs(int x, int y, int n, set<pair<int, int>>& visited) {
    if (n == 0) {
        // n번의 이동이 모두 완료된 경우, 단순 경로 하나를 찾은 것이므로 확률 1을 반환
        return 1.0;
    }
    // 현재 좌표를 방문한 좌표로 추가
    visited.insert({x, y});
    double prob = 0.0; // 단순 경로로 이동할 확률을 저장할 변수
    // 모든 방향에 대해 재귀적으로 이동 시도
    for (int i = 0; i < 4; ++i) {
        int nx = x + directions[i].first; // 새로운 x 좌표
        int ny = y + directions[i].second; // 새로운 y 좌표
        if (visited.find({nx, ny}) == visited.end()) {
            // 다음 좌표가 아직 방문하지 않은 경우에만 이동
            prob += probs[i] * dfs(nx, ny, n - 1, visited);
        }
    }
    // 현재 좌표를 방문한 좌표에서 제거 (백트래킹)
    visited.erase({x, y});
    return prob; // 계산된 확률 반환
}

// 단순 경로로 이동할 확률을 계산하는 함수
double simple_path_probability(int N, double east, double west, double south, double north) {
    // 확률을 소수로 변환
    probs[0] = east / 100.0; // 동쪽으로 이동할 확률
    probs[1] = west / 100.0; // 서쪽으로 이동할 확률
    probs[2] = south / 100.0; // 남쪽으로 이동할 확률
    probs[3] = north / 100.0; // 북쪽으로 이동할 확률

    set<pair<int, int>> visited; // 방문한 좌표를 저장할 세트
    return dfs(0, 0, N, visited); // DFS를 호출하여 단순 경로로 이동할 확률을 계산하여 반환
}

int main() {
    int N; // 이동 횟수
    double east, west, south, north; // 동, 서, 남, 북으로 이동할 확률

    // 입력 처리
    cin >> N >> east >> west >> south >> north; // 표준 입력으로부터 데이터를 읽어옴

    // 결과 계산 및 출력
    double result = simple_path_probability(N, east, west, south, north); // 단순 경로로 이동할 확률을 계산
    cout << fixed << setprecision(10) << result << endl; // 소수점 10자리까지 결과를 출력

    return 0; // 프로그램 종료
}
