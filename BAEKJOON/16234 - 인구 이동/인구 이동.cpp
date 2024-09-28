#include <iostream>   // 입출력 처리를 위한 헤더 파일
#include <queue>      // BFS를 위한 큐 자료구조 사용
#include <vector>     // 벡터 자료구조 사용

using namespace std;

int N, L, R;  // 땅의 크기 N, 인구 차이 하한선 L, 상한선 R
vector<vector<int>> population;  // 각 나라의 인구수를 저장하는 2차원 배열
vector<vector<bool>> visited;    // 방문 여부를 체크하는 2차원 배열
int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // 상, 하, 좌, 우 네 방향을 나타내는 배열

// BFS를 통해 연합을 형성하고 인구 이동을 수행하는 함수
bool bfs(int start_row, int start_col) {
    queue<pair<int, int>> q;  // BFS를 위한 큐
    vector<pair<int, int>> union_list;  // 연합에 속한 나라들의 좌표를 저장하는 벡터
    q.push({start_row, start_col});  // 시작 좌표를 큐에 추가
    visited[start_row][start_col] = true;  // 시작 좌표를 방문 처리
    union_list.push_back({start_row, start_col});  // 연합에 시작 좌표 추가

    int total_population = population[start_row][start_col];  // 연합의 총 인구수
    int country_count = 1;  // 연합에 속한 나라의 수

    while (!q.empty()) {  // 큐가 빌 때까지 반복
        int row = q.front().first;
        int col = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {  // 네 방향에 대해 반복
            int new_row = row + directions[i][0];
            int new_col = col + directions[i][1];

            if (new_row >= 0 && new_row < N && new_col >= 0 && new_col < N && !visited[new_row][new_col]) {
                int population_diff = abs(population[row][col] - population[new_row][new_col]);
                
                if (L <= population_diff && population_diff <= R) {  // 인구 차이가 L 이상, R 이하일 때
                    visited[new_row][new_col] = true;  // 새로운 좌표를 방문 처리
                    q.push({new_row, new_col});  // 큐에 새로운 좌표 추가
                    union_list.push_back({new_row, new_col});  // 연합에 새로운 좌표 추가
                    total_population += population[new_row][new_col];  // 연합의 총 인구수 증가
                    country_count++;  // 연합의 나라 수 증가
                }
            }
        }
    }

    if (country_count > 1) {  // 연합이 2개 이상의 나라로 이루어진 경우
        int new_population = total_population / country_count;  // 새로운 인구수 계산

        for (auto country : union_list) {  // 연합에 속한 모든 나라의 인구수 갱신
            population[country.first][country.second] = new_population;
        }
        return true;  // 인구 이동이 발생했음을 반환
    }
    return false;  // 인구 이동이 발생하지 않았음을 반환
}

int main() {
    cin >> N >> L >> R;  // N, L, R 입력
    population = vector<vector<int>>(N, vector<int>(N));  // N x N 크기의 인구수 배열 초기화

    for (int i = 0; i < N; i++) {  // 인구수 입력
        for (int j = 0; j < N; j++) {
            cin >> population[i][j];
        }
    }

    int days = 0;  // 인구 이동이 발생한 일수 초기화

    while (true) {  // 무한 반복
        visited = vector<vector<bool>>(N, vector<bool>(N, false));  // 방문 여부 배열 초기화
        bool movement_occurred = false;  // 인구 이동 발생 여부 초기화

        for (int i = 0; i < N; i++) {  // 모든 나라에 대해 반복
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {  // 방문하지 않은 나라에 대해 BFS 수행
                    if (bfs(i, j)) {
                        movement_occurred = true;  // 인구 이동 발생 표시
                    }
                }
            }
        }

        if (!movement_occurred) break;  // 더 이상 인구 이동이 발생하지 않으면 종료
        days++;  // 인구 이동이 발생한 날 수 증가
    }

    cout << days << endl;  // 결과 출력
    return 0;
}
