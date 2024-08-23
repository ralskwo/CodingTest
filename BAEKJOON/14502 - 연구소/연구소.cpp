#include <iostream>  // 표준 입출력을 사용하기 위한 헤더 파일
#include <vector>    // 벡터 자료형을 사용하기 위한 헤더 파일
#include <queue>     // 큐 자료형을 사용하기 위한 헤더 파일
#include <algorithm> // next_permutation과 같은 알고리즘 함수를 사용하기 위한 헤더 파일
#include <tuple>     // tie와 tuple을 사용하기 위한 헤더 파일

using namespace std;

int n, m;  // 연구소의 세로 크기 n과 가로 크기 m
vector<vector<int>> lab;  // 연구소의 상태를 저장하는 2차원 벡터
vector<pair<int, int>> empty_spaces;  // 빈 칸의 위치를 저장하는 벡터
vector<pair<int, int>> viruses;  // 바이러스의 위치를 저장하는 벡터
int dx[4] = {-1, 1, 0, 0};  // 상하좌우 이동을 위한 x축 방향 벡터
int dy[4] = {0, 0, -1, 1};  // 상하좌우 이동을 위한 y축 방향 벡터

// 바이러스 확산을 시뮬레이션하는 함수
void spread_virus(vector<vector<int>>& temp_lab) {
    queue<pair<int, int>> q;  // 바이러스 위치를 저장할 큐 생성
    for (auto v : viruses) {  // 모든 바이러스 위치를 큐에 추가
        q.push(v);
    }

    while (!q.empty()) {  // 큐가 빌 때까지 반복
        int x, y;  // 현재 위치의 x, y 좌표
        tie(x, y) = q.front();  // 큐에서 좌표를 꺼내옴
        q.pop();  // 큐에서 제거

        for (int i = 0; i < 4; i++) {  // 상하좌우 4방향에 대해 반복
            int nx = x + dx[i];  // 새로운 x 좌표 계산
            int ny = y + dy[i];  // 새로운 y 좌표 계산

            // 새로운 좌표가 연구소 범위 내에 있고, 빈 칸(0)인 경우
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && temp_lab[nx][ny] == 0) {
                temp_lab[nx][ny] = 2;  // 바이러스를 퍼뜨림
                q.push({nx, ny});  // 새로 바이러스가 퍼진 위치를 큐에 추가
            }
        }
    }
}

// 안전 영역의 크기를 계산하는 함수
int get_safe_area(vector<vector<int>>& temp_lab) {
    int safe_area = 0;  // 안전 영역 크기를 저장할 변수
    for (int i = 0; i < n; i++) {  // 연구소의 모든 칸을 확인
        for (int j = 0; j < m; j++) {
            if (temp_lab[i][j] == 0) {  // 빈 칸(0)이면
                safe_area++;  // 안전 영역 크기 증가
            }
        }
    }
    return safe_area;  // 안전 영역 크기 반환
}

// 최대 안전 영역을 찾는 함수
int find_max_safe_area() {
    int max_safe_area = 0;  // 최대 안전 영역 크기를 저장할 변수

    vector<int> wall_select(empty_spaces.size(), 0);  // 벽을 세울 위치를 결정하는 벡터 초기화 (0으로 초기화)
    fill(wall_select.end() - 3, wall_select.end(), 1);  // 벡터의 마지막 3개 요소를 1로 설정 (벽 세우기)

    do {
        vector<vector<int>> temp_lab = lab;  // 연구소 상태를 깊은 복사

        for (int i = 0; i < empty_spaces.size(); i++) {  // 빈 칸 중에서
            if (wall_select[i] == 1) {  // 벽을 세우기로 선택된 위치에 대해
                int x, y;  // 빈 칸의 x, y 좌표
                tie(x, y) = empty_spaces[i];  // 해당 위치의 좌표를 가져옴
                temp_lab[x][y] = 1;  // 벽을 세움
            }
        }

        spread_virus(temp_lab);  // 바이러스를 확산시킴

        int safe_area = get_safe_area(temp_lab);  // 안전 영역 크기를 계산
        max_safe_area = max(max_safe_area, safe_area);  // 최대 안전 영역 크기를 갱신

    } while (next_permutation(wall_select.begin(), wall_select.end()));  // 가능한 모든 벽의 조합을 시도

    return max_safe_area;  // 최대 안전 영역 크기 반환
}

int main() {
    cin >> n >> m;  // 연구소의 세로 크기 n과 가로 크기 m을 입력받음
    lab = vector<vector<int>>(n, vector<int>(m));  // 연구소의 상태를 저장할 2차원 벡터 초기화

    for (int i = 0; i < n; i++) {  // 연구소의 상태를 입력받음
        for (int j = 0; j < m; j++) {
            cin >> lab[i][j];
            if (lab[i][j] == 0) {  // 빈 칸(0)일 경우
                empty_spaces.push_back({i, j});  // 빈 칸의 위치를 저장
            } else if (lab[i][j] == 2) {  // 바이러스(2)일 경우
                viruses.push_back({i, j});  // 바이러스의 위치를 저장
            }
        }
    }

    cout << find_max_safe_area() << endl;  // 최대 안전 영역 크기를 계산하고 출력

    return 0;  // 프로그램 종료
}
